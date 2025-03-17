use pyo3::prelude::*;
use hex::encode as hex_encode;
use pyo3::exceptions::PyValueError;
use pyo3::wrap_pyfunction;
use std::io::BufRead;
use std::usize;

const CLASS_SHIFT: u8 = 6;
const TWO_BIT_MASK: u8 = 3;
const ENCODE_SHIFT: u8 = 5;
const MODULO_2: u8 = 1;
const CLASSNUM_MASK: u8 = 31;
const MASK_BIT7: u8 = 127;
const SHIFT_7: u8 = 7;
// const HIGH_CLASS_NUM: u8 = 31;
// const MASK_BIT8: u8 = 128;
const SHIFT_8: u8 = 8;


// #[pyclass]
// pub struct BerClass {
//     #[pyo3(get)]
//     pub UNIVERSAL: u8, 
//     #[pyo3(get)]
//     pub APPLICATION: u8,
//     #[pyo3(get)]
//     pub CONTEXT: u8,
//     #[pyo3(get)]
//     pub PRIVATE: u8
// }


// pub const BERCLASS: BerClass = BerClass {
//     UNIVERSAL: 0,
//     APPLICATION: 1,
//     CONTEXT: 2,
//     PRIVATE: 3,
// };

const EOC: &[(u8, bool, u8, i32)] = &[
    (0, false, 0, 0),
    (2, true, 1, 0),
];

#[derive(Clone)]
#[pyclass]
pub struct BerTag {
    #[pyo3(get)]
    pub name: String, 
    #[pyo3(get)]
    pub tag_class: u8,
    #[pyo3(get)]
    pub constructed: bool,
    #[pyo3(get)]
    pub number: u8,
}

#[derive(Clone)]
#[pyclass]
pub struct TlvObject {
    #[pyo3(get)]
    pub tag: BerTag, 
    #[pyo3(get)]
    pub length: u32,
    #[pyo3(get)]
    pub value: Vec<u8>,
    #[pyo3(get)]
    pub offset: u32,
    #[pyo3(get)]
    pub children: Vec<TlvObject>,
}


#[pyfunction]
pub fn decode_tag(tag_bytes: &[u8]) -> PyResult<BerTag> {
    if tag_bytes.is_empty() {
        return Err(PyValueError::new_err("Empty tag bytes"));
    }
    
    let first_byte = tag_bytes[0];
    let name = hex_encode(&tag_bytes[..1]);
    let tag_class = (first_byte >> CLASS_SHIFT) & TWO_BIT_MASK;
    let constructed = ((first_byte >> ENCODE_SHIFT) & MODULO_2) != 0;
    let mut number: u8 = first_byte & CLASSNUM_MASK;

    if number == CLASSNUM_MASK {
        number = 0;
        for &b in &tag_bytes[1..] {
            number = (number << SHIFT_7) | (b & MASK_BIT7);
        }
    }

    Ok(BerTag {
        name: name,
        tag_class: tag_class,
        constructed: constructed,
        number: number,
    })
}

#[pyfunction]
pub fn _reach_eoc(tag: &BerTag, length: i32) -> bool {
    EOC.iter().any(|&(class, constructed, number, len)| 
        (class, constructed, number, len) == (tag.tag_class, tag.constructed, tag.number, length)
    )
}


pub fn _length_size<R: BufRead>(stream: &mut R) -> usize {
    let mut buffer = [0u8; 1];
    match stream.read_exact(&mut buffer) {
        Ok(()) => {
            if buffer[0] >> SHIFT_7 == 0 {
                // Short form
                return 1;
            } else {
                // Long form length size (lower 7 bits)
                let length_size = (buffer[0] & MASK_BIT7) as usize;
                return length_size;
            }
        }
        Err(_) => 0,
    }
}

pub fn _read_length<R: BufRead>(stream: &mut R) -> (usize, usize) {
    let mut first_byte_buf = [0u8; 1];
    stream.read_exact(&mut first_byte_buf).expect("Failed to read first byte");
    let first_byte = first_byte_buf[0];

    // Check short form
    if first_byte >> SHIFT_7 == 0 {
        return (first_byte as usize, 1);
    }

    // Long form
    let length_size = (first_byte & MASK_BIT7) as usize;

    // Indefinite form
    if length_size == 0 {
        return (0, 1);
    }
    let mut buffer = vec![0u8; length_size];
    stream.read_exact(&mut buffer).expect("Unexpected end of length");

    let mut length: usize = 0;
    for &b in buffer.iter() {
        length = (length << SHIFT_8) | (b as usize);
    }
    (length, length_size + 1) // Include the first byte
}




#[pymodule]
fn rust_bindings(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<BerTag>()?; 
    m.add_function(wrap_pyfunction!(decode_tag, m)?)?;
    m.add_function(wrap_pyfunction!(_reach_eoc, m)?)?;
    Ok(())
}
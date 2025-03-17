use pyo3::prelude::*;
use hex::encode as hex_encode;
use pyo3::exceptions::PyValueError;
use pyo3::wrap_pyfunction;

const CLASS_SHIFT: u8 = 6;
const TWO_BIT_MASK: u8 = 3;
const ENCODE_SHIFT: u8 = 5;
const MODULO_2: u8 = 1;
const CLASSNUM_MASK: u8 = 31;
const MASK_BIT7: u8 = 127;
const SHIFT_7: u8 = 7;
// const HIGH_CLASS_NUM: u8 = 31;
// const MASK_BIT8: u8 = 128;
// const SHIFT_8: u8 = 8;

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

#[pyclass]
pub struct TlvObject {
    #[pyo3(get)]
    pub tag: String, 
    #[pyo3(get)]
    pub lenght: u8,
    #[pyo3(get)]
    pub value: Vec<u8>,
    #[pyo3(get)]
    pub start_offset: u8,
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


#[pymodule]
fn rust_bindings(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<BerTag>()?; 
    m.add_function(wrap_pyfunction!(decode_tag, m)?)?;
    Ok(())
}
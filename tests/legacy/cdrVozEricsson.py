import os, gzip, binascii, time, datetime, shutil, glob, tarfile, sys
from datetime import datetime


buffer_size = 50000
ia6 = 10
ia7 = 0

process_number = sys.argv[1]
validation_mode = sys.argv[2]
output_path = sys.argv[3]
base_path = sys.argv[4]
cdr_database = sys.argv[5]
raw_cdr_path = sys.argv[6]
queue_position = sys.argv[7]
active_sessions = sys.argv[8]
record_type = sys.argv[9]

error_log_file = open("Erro" + process_number + ".txt", "w")
process_id = str(os.getpid())
current_directory = os.getcwd()


timestamp = time.asctime().replace(":", "").replace(" ", "")
oper = {
    "VI": "VIVO",
    "TI": "TIM",
    "OI": "OI",
    "CL": "CLARO",
    "NE": "NEXTEL",
    "AL": "ALGAR",
}


res = "ResDados" + "&" + process_id + "&" + cdr_database + "-" + process_number


opid = {
    "0": "sID",
    "02": "TIM",
    "03": "TIM",
    "04": "TIM",
    "05": "CLARO",
    "06": "VIVO",
    "08": "CLARO",
    "12": "CLARO",
    "14": "CLARO",
    "16": "OI",
    "31": "OI",
    "24": "OI",
    "23": "VIVO",
    "13": "VIVO",
    "19": "VIVO",
    "21": "VIVO",
    "10": "VIVO",
    "11": "VIVO",
    "15": "SERCOMTEL",
    "34": "CTBC",
    "39": "NEXTEL",
    "32": "CTBC",
    "33": "CTBC",
}
dictb = {}
dicterro = {}
diax = {}
dicnb = {}
dicna = {}
lb = []
la = []
la1 = []
la2 = set()
la3 = []
la4 = []
dicna1 = {}
dicna2 = {}
dicha = {}
dicha2 = {}
dicnb = {}
lb1 = []
lb2 = set()
lb3 = []
lb4 = []
dicnb1 = {}
dicnb2 = {}
dichb = {}
dichb2 = {}
lac = set()
dilac = {}
m4 = set()
m8 = set()
he = 0


tcar = 1000000
orig = glob.glob(raw_cdr_path)

process_counter = 0
file_counter = 0
total_counter = 0
a17 = -1

ana = ["a0", "a1", "a2", "a3", "a4"]
hor1 = ["10", "11", "12"]
hor2 = ["18", "19", "20"]


for i in orig:
    file_processed_flag = 0
    current_file = i
    process_counter = process_counter + 1

    total_counter = total_counter + 1

    file_counter = file_counter + 1
    iarq = str(file_counter)

    if process_counter > int(queue_position):
        process_counter = 1
    try:
        if validation_mode == "a":
            csa = glob.glob(base_path + "f*")
            while len(csa) > int(active_sessions) + int(process_number):
                csa = glob.glob(base_path + "f*")

        if process_counter == int(process_number):
            processing_status = str(file_counter)
            file_processed_flag = 1
            file_content = gzip.open(i, "rb")

            if validation_mode == "a":
                g = open(base_path + cdr_database + ";" + str(file_counter) + ".txt", "w")
            else:
                iii = i.split("\\")

                g = open(
                    base_path
                    + output_path
                    + cdr_database
                    + "\\"
                    + iii[len(iii) - 2]
                    + "\\"
                    + iii[len(iii) - 1].replace("gz", "txt"),
                    "w",
                )
                g.write(
                    "Tipo_de_chamada;Bilhetador;Referencia;Data;Hora;IMSI;1stCelA;Outgoing_route;Origem;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto"
                    + "\n"
                )
                ali = (
                    base_path
                    + output_path
                    + cdr_database
                    + "\\"
                    + iii[len(iii) - 2]
                    + "\\"
                    + iii[len(iii) - 1].replace(".gz", "")
                )
            processing_status = "-2"

            raw_binary_data = file_content.read(buffer_size)

            hex_data = str(binascii.b2a_hex(raw_binary_data))

            current_position = 2

            parsed_records = []
            try:
                while hex_data[current_position] != "'":
                    if 4 > 3:
                        if hex_data[current_position] == "'":
                            break
                        current_tag = hex_data[current_position : current_position + 2]

                        if current_tag != "00":
                            h = 1
                            if int(current_tag[1], 16) == 15 and int(current_tag[0], 16) % 2 != 0:
                                current_position = current_position + 2
                                a12 = hex_data[current_position : current_position + 2]
                                h = h + 1
                                while int(a12[0:2], 16) > 127:
                                    current_position = current_position + 2
                                    a12 = hex_data[current_position : current_position + 2]
                                    h = h + 1
                            record_tag = hex_data[(current_position - (h * 2)) + 2 : current_position + 2]

                            mta = current_position - (h * 2) + 2

                            current_position = current_position + 2
                            a3 = hex_data[current_position : current_position + 2]
                            field_length = int(a3[0:2], 16)
                            if field_length > 127:
                                c = field_length - 128
                                if c == 0:
                                    field_length = 0
                                else:
                                    current_position = current_position + 2
                                    c2 = hex_data[current_position : current_position + c * 2]
                                    field_length = int(c2, 16)
                                    current_position = (current_position - 2) + c * 2

                            timestamp = -2
                            if 2 * buffer_size - current_position < 10000:
                                timestamp = len(hex_data[mta:].replace("'", ""))

                            if timestamp != -2 and timestamp < field_length * 2 + 30:
                                fr = hex_data[mta:].replace("'", "")

                                raw_binary_data = file_content.read(buffer_size)
                                fn = str(binascii.b2a_hex(raw_binary_data))[2:]

                                hex_data = fr + fn

                                current_position = 0
                                for xx in parsed_records:
                                    g.write(xx + "\n")
                                parsed_records = []
                            else:
                                current_position = current_position + 2
                                if record_tag == "a0":
                                    ab = hex_data[current_position : current_position + field_length * 2]
                                    current_position = current_position + field_length * 2

                                    if 4 > 3:
                                        if ab[0:2] in ana:
                                            ca = int(ab[2:4], 16)
                                            if ca > 127:
                                                ca1 = ca - 128
                                            else:
                                                ca1 = 0
                                            x = ab[2 + ca1 * 2 + 2 : (field_length * 2 + 2)] + "."

                                            record_type = ""
                                            carrier_code = ""
                                            origin_number = ""
                                            destination_number = ""
                                            reference_id = ""
                                            date = ""
                                            time = ""
                                            billing_id = ""
                                            duration = ""
                                            fault_code = ""
                                            eos_info = ""
                                            internal_cause = ""
                                            call_type = ""
                                            ty2 = ""
                                            route = ""
                                            cs = ""
                                            cst = ""
                                            location_info = ""
                                            call_position = ""
                                            cco = ""
                                            imsi = ""
                                            disconnecting_party = ""
                                            tn = ""
                                            imei = ""
                                            trssc = ""
                                            intt = ""

                                            if ab[0:2] == "a0":
                                                record_type = "TRA"

                                                i1 = 0

                                                while x[i1] != ".":
                                                    h = i1
                                                    if (
                                                        int(x[i1 + 1], 16) == 15
                                                        and int(x[i1], 16) % 2 != 0
                                                    ):
                                                        i1 = i1 + 2
                                                        while (
                                                            int(x[i1 : i1 + 2], 16)
                                                            > 127
                                                        ):
                                                            i1 = i1 + 2
                                                    t = x[h : i1 + 2]
                                                    i1 = i1 + 2
                                                    field_length = int(x[i1 : i1 + 2], 16)
                                                    if field_length > 127:
                                                        c = field_length - 128
                                                        if c == 0:
                                                            field_length = 0
                                                        else:
                                                            i1 = i1 + 2
                                                            field_length = int(
                                                                x[i1 : i1 + c * 2], 16
                                                            )

                                                    if t == "84":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        origin_number = ""
                                                        for i in range(2, len(field_data), 2):
                                                            origin_number = (
                                                                origin_number + field_data[i + 1] + field_data[i]
                                                            )
                                                    if t == "96":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        rou1 = str.encode(field_data)
                                                        carrier_code = str(binascii.a2b_hex(rou1))
                                                        carrier_code = carrier_code[2:].replace("'", "")

                                                    if t == "86":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]

                                                        imsi = ""
                                                        for i in range(0, len(field_data), 2):
                                                            imsi = (
                                                                imsi
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if t == "9f2e":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        reference_id = field_data
                                                    if t == "85":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        destination_number = ""
                                                        for i in range(2, len(field_data), 2):
                                                            destination_number = (
                                                                destination_number + field_data[i + 1] + field_data[i]
                                                            )
                                                    if t == "88":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        date = (
                                                            str(int(field_data[4:6], 16))
                                                            + "/"
                                                            + str(int(field_data[2:4], 16))
                                                            + "/"
                                                            + str(int(field_data[0:2], 16))
                                                        )
                                                    if t == "89":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        time = (
                                                            str(int(field_data[0:2], 16))
                                                            + ":"
                                                            + str(int(field_data[2:4], 16))
                                                            + ":"
                                                            + str(int(field_data[4:6], 16))
                                                        )
                                                    if t == "93":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        bi2 = str.encode(field_data)
                                                        billing_id = str(binascii.a2b_hex(bi2))
                                                    if t == "8b":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        duration = (
                                                            str(int(field_data[0:2], 16))
                                                            + ":"
                                                            + str(int(field_data[2:4], 16))
                                                            + ":"
                                                            + str(int(field_data[4:6], 16))
                                                        )
                                                    if t == "9f29":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        fault_code = str(int(field_data, 16))
                                                    if t == "9b":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        eos_info = str(int(field_data, 16))
                                                    if t == "9c":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        internal_cause = str(int(field_data, 16))
                                                    if t == "83":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        call_type = str(int(field_data, 16))

                                                    if t == "9a":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        call_position = str(int(field_data, 16))
                                                    if t == "95":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        rou1 = str.encode(field_data)
                                                        route = str(
                                                            binascii.a2b_hex(rou1)
                                                        )

                                                    if t == "87":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        disconnecting_party = str(int(field_data, 16))
                                                    if t == "8d":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        trssc = (
                                                            str(int(field_data[0:2], 16))
                                                            + ":"
                                                            + str(int(field_data[2:4], 16))
                                                            + ":"
                                                            + str(int(field_data[4:6], 16))
                                                        )
                                                    i1 = i1 + 2 + field_length * 2

                                            if ab[0:2] == "a1":
                                                record_type = "ORI"
                                                i1 = 0
                                                try:
                                                    while x[i1] != ".":
                                                        h = i1
                                                        if (
                                                            int(x[i1 + 1], 16) == 15
                                                            and int(x[i1], 16) % 2 != 0
                                                        ):
                                                            i1 = i1 + 2
                                                            while (
                                                                int(x[i1 : i1 + 2], 16)
                                                                > 127
                                                            ):
                                                                i1 = i1 + 2
                                                        t = x[h : i1 + 2]
                                                        i1 = i1 + 2
                                                        field_length = int(x[i1 : i1 + 2], 16)
                                                        if field_length > 127:
                                                            c = field_length - 128
                                                            if c == 0:
                                                                field_length = 0
                                                            else:
                                                                i1 = i1 + 2
                                                                field_length = int(
                                                                    x[i1 : i1 + c * 2],
                                                                    16,
                                                                )

                                                        if t == "84":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            origin_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                origin_number = (
                                                                    origin_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )

                                                        if t == "97":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            carrier_code = str(
                                                                binascii.a2b_hex(rou1)
                                                            )
                                                            carrier_code = carrier_code[2:].replace("'", "")

                                                        if t == "86":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]

                                                            imei = ""
                                                            for i in range(
                                                                0, len(field_data), 2
                                                            ):
                                                                imei = (
                                                                    imei
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "85":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]

                                                            imsi = ""
                                                            for i in range(
                                                                0, len(field_data), 2
                                                            ):
                                                                imsi = (
                                                                    imsi
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "9f44":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            reference_id = field_data
                                                        if t == "87":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            destination_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                destination_number = (
                                                                    destination_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "9f4a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            tn = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                tn = (
                                                                    tn
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "89":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            date = (
                                                                str(int(field_data[4:6], 16))
                                                                + "/"
                                                                + str(int(field_data[2:4], 16))
                                                                + "/"
                                                                + str(int(field_data[0:2], 16))
                                                            )
                                                        if t == "8a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            time = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "94":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            bi2 = str.encode(field_data)
                                                            billing_id = str(
                                                                binascii.a2b_hex(bi2)
                                                            )
                                                        if t == "8c":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            duration = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "8d":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            intt = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "9f3b":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            fault_code = str(int(field_data, 16))
                                                        if t == "9f22":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            eos_info = str(int(field_data, 16))
                                                        if t == "9f23":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            internal_cause = str(int(field_data, 16))
                                                        if t == "83":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_type = str(int(field_data, 16))
                                                        if t == "9f21":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_position = str(int(field_data, 16))
                                                        if t == "96":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            route = str(
                                                                binascii.a2b_hex(rou1)
                                                            )

                                                        if t == "88":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            disconnecting_party = str(int(field_data, 16))
                                                        if t == "9a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            cs = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "9f62":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            cco = str(int(field_data, 16))
                                                        if t == "9b":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            location_info = (
                                                                str(int(field_data[1], 16))
                                                                + str(int(field_data[0], 16))
                                                                + str(int(field_data[3], 16))
                                                                + "-"
                                                                + str(int(field_data[5], 16))
                                                                + str(int(field_data[4], 16))
                                                                + str(int(field_data[2], 16))
                                                                + "-"
                                                                + str(
                                                                    int(field_data[6:10], 16)
                                                                )
                                                                + "-"
                                                                + str(
                                                                    int(field_data[10:14], 16)
                                                                )
                                                                + "|"
                                                                + field_data
                                                            )
                                                        if t == "8e":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            trssc = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        i1 = i1 + 2 + field_length * 2
                                                except IndexError:
                                                    print(current_position)
                                                    print(i)
                                                    pass
                                            if ab[0:2] == "a2":
                                                record_type = "ROA"
                                                i1 = 0
                                                try:
                                                    while x[i1] != ".":
                                                        h = i1
                                                        if (
                                                            int(x[i1 + 1], 16) == 15
                                                            and int(x[i1], 16) % 2 != 0
                                                        ):
                                                            i1 = i1 + 2
                                                            while (
                                                                int(x[i1 : i1 + 2], 16)
                                                                > 127
                                                            ):
                                                                i1 = i1 + 2
                                                        t = x[h : i1 + 2]
                                                        i1 = i1 + 2
                                                        field_length = int(x[i1 : i1 + 2], 16)
                                                        if field_length > 127:
                                                            c = field_length - 128
                                                            if c == 0:
                                                                field_length = 0
                                                            else:
                                                                i1 = i1 + 2
                                                                field_length = int(
                                                                    x[i1 : i1 + c * 2],
                                                                    16,
                                                                )

                                                        if t == "84":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            origin_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                origin_number = (
                                                                    origin_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )

                                                        if t == "96":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            carrier_code = str(
                                                                binascii.a2b_hex(rou1)
                                                            )
                                                            carrier_code = carrier_code[2:].replace("'", "")

                                                        if t == "86":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]

                                                            imsi = ""
                                                            for i in range(
                                                                0, len(field_data), 2
                                                            ):
                                                                imsi = (
                                                                    imsi
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "9f31":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            reference_id = field_data
                                                        if t == "85":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            destination_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                destination_number = (
                                                                    destination_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "89":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            date = (
                                                                str(int(field_data[4:6], 16))
                                                                + "/"
                                                                + str(int(field_data[2:4], 16))
                                                                + "/"
                                                                + str(int(field_data[0:2], 16))
                                                            )
                                                        if t == "8a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            time = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "93":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            bi2 = str.encode(field_data)
                                                            billing_id = str(
                                                                binascii.a2b_hex(bi2)
                                                            )
                                                        if t == "8c":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            duration = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "9f2d":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            fault_code = str(int(field_data, 16))
                                                        if t == "9a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            eos_info = str(int(field_data, 16))
                                                        if t == "9b":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            internal_cause = str(int(field_data, 16))
                                                        if t == "83":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_type = str(int(field_data, 16))
                                                        if t == "99":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_position = str(int(field_data, 16))
                                                        if t == "95":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            route = str(
                                                                binascii.a2b_hex(rou1)
                                                            )
                                                        if t == "88":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            disconnecting_party = str(int(field_data, 16))
                                                        if t == "8e":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            trssc = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        i1 = i1 + 2 + field_length * 2
                                                except IndexError:
                                                    print(current_position)
                                                    print(i)
                                                    pass
                                            if ab[0:2] == "a5":
                                                record_type = "SMSo"
                                                i1 = 0

                                                while x[i1] != ".":
                                                    h = i1
                                                    if (
                                                        int(x[i1 + 1], 16) == 15
                                                        and int(x[i1], 16) % 2 != 0
                                                    ):
                                                        i1 = i1 + 2
                                                        while (
                                                            int(x[i1 : i1 + 2], 16)
                                                            > 127
                                                        ):
                                                            i1 = i1 + 2
                                                    t = x[h : i1 + 2]
                                                    i1 = i1 + 2
                                                    field_length = int(x[i1 : i1 + 2], 16)
                                                    if field_length > 127:
                                                        c = field_length - 128
                                                        if c == 0:
                                                            field_length = 0
                                                        else:
                                                            i1 = i1 + 2
                                                            field_length = int(
                                                                x[i1 : i1 + c * 2], 16
                                                            )

                                                    if t == "8e":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        location_info = (
                                                            str(int(field_data[1], 16))
                                                            + str(int(field_data[0], 16))
                                                            + str(int(field_data[3], 16))
                                                            + "-"
                                                            + str(int(field_data[5], 16))
                                                            + str(int(field_data[4], 16))
                                                            + str(int(field_data[2], 16))
                                                            + "-"
                                                            + str(int(field_data[6:10], 16))
                                                            + "-"
                                                            + str(int(field_data[10:14], 16))
                                                        )
                                                    if t == "84":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        origin_number = ""
                                                        for i in range(2, len(field_data), 2):
                                                            origin_number = (
                                                                origin_number + field_data[i + 1] + field_data[i]
                                                            )
                                                    if t == "81":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        carrier_code = str(int(field_data, 16))
                                                    if t == "9f2a":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        imei = str(int(field_data, 16))
                                                    if t == "9f2b":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        reference_id = field_data

                                                    if t == "87":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        date = (
                                                            str(int(field_data[4:6], 16))
                                                            + "/"
                                                            + str(int(field_data[2:4], 16))
                                                            + "/"
                                                            + str(int(field_data[0:2], 16))
                                                        )
                                                    if t == "88":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        time = (
                                                            str(int(field_data[0:2], 16))
                                                            + ":"
                                                            + str(int(field_data[2:4], 16))
                                                            + ":"
                                                            + str(int(field_data[4:6], 16))
                                                        )
                                                    if t == "8b":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        bi2 = str.encode(field_data)
                                                        billing_id = str(binascii.a2b_hex(bi2))

                                                    if t == "83":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        call_type = str(int(field_data, 16))
                                                    if t == "9f2a":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        call_position = str(int(field_data, 16))

                                                    i1 = i1 + 2 + field_length * 2
                                            if ab[0:2] == "a7":
                                                record_type = "SMSt"
                                                i1 = 0

                                                while x[i1] != ".":
                                                    h = i1
                                                    if (
                                                        int(x[i1 + 1], 16) == 15
                                                        and int(x[i1], 16) % 2 != 0
                                                    ):
                                                        i1 = i1 + 2
                                                        while (
                                                            int(x[i1 : i1 + 2], 16)
                                                            > 127
                                                        ):
                                                            i1 = i1 + 2
                                                    t = x[h : i1 + 2]
                                                    i1 = i1 + 2
                                                    field_length = int(x[i1 : i1 + 2], 16)
                                                    if field_length > 127:
                                                        c = field_length - 128
                                                        if c == 0:
                                                            field_length = 0
                                                        else:
                                                            i1 = i1 + 2
                                                            field_length = int(
                                                                x[i1 : i1 + c * 2], 16
                                                            )

                                                    if t == "81":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        carrier_code = str(int(field_data, 16))

                                                    if t == "83":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        destination_number = ""
                                                        for i in range(2, len(field_data), 2):
                                                            destination_number = (
                                                                destination_number + field_data[i + 1] + field_data[i]
                                                            )
                                                    if t == "86":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        date = (
                                                            str(int(field_data[4:6], 16))
                                                            + "/"
                                                            + str(int(field_data[2:4], 16))
                                                            + "/"
                                                            + str(int(field_data[0:2], 16))
                                                        )
                                                    if t == "87":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        time = (
                                                            str(int(field_data[0:2], 16))
                                                            + ":"
                                                            + str(int(field_data[2:4], 16))
                                                            + ":"
                                                            + str(int(field_data[4:6], 16))
                                                        )
                                                    if t == "8a":
                                                        field_data = x[
                                                            i1 + 2 : i1 + field_length * 2 + 2
                                                        ]
                                                        bi2 = str.encode(field_data)
                                                        billing_id = str(binascii.a2b_hex(bi2))

                                                    i1 = i1 + 2 + field_length * 2
                                            if ab[0:2] == "a3":
                                                record_type = "FOR"
                                                i1 = 0
                                                try:
                                                    while x[i1] != ".":
                                                        h = i1
                                                        if (
                                                            int(x[i1 + 1], 16) == 15
                                                            and int(x[i1], 16) % 2 != 0
                                                        ):
                                                            i1 = i1 + 2
                                                            while (
                                                                int(x[i1 : i1 + 2], 16)
                                                                > 127
                                                            ):
                                                                i1 = i1 + 2
                                                        t = x[h : i1 + 2]
                                                        i1 = i1 + 2
                                                        field_length = int(x[i1 : i1 + 2], 16)
                                                        if field_length > 127:
                                                            c = field_length - 128
                                                            if c == 0:
                                                                field_length = 0
                                                            else:
                                                                i1 = i1 + 2
                                                                field_length = int(
                                                                    x[i1 : i1 + c * 2],
                                                                    16,
                                                                )

                                                        if t == "84":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            origin_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                origin_number = (
                                                                    origin_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )

                                                        if t == "9a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            carrier_code = str(
                                                                binascii.a2b_hex(rou1)
                                                            )
                                                            carrier_code = carrier_code[2:].replace("'", "")

                                                        if t == "8a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]

                                                            imsi = ""
                                                            for i in range(
                                                                0, len(field_data), 2
                                                            ):
                                                                imsi = (
                                                                    imsi
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "9f39":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            reference_id = field_data
                                                        if t == "85":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            destination_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                destination_number = (
                                                                    destination_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "8d":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            date = (
                                                                str(int(field_data[4:6], 16))
                                                                + "/"
                                                                + str(int(field_data[2:4], 16))
                                                                + "/"
                                                                + str(int(field_data[0:2], 16))
                                                            )
                                                        if t == "8e":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            time = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "97":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            bi2 = str.encode(field_data)
                                                            billing_id = str(
                                                                binascii.a2b_hex(bi2)
                                                            )
                                                        if t == "90":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            duration = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "9f33":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            fault_code = str(int(field_data, 16))
                                                        if t == "9e":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            eos_info = str(int(field_data, 16))
                                                        if t == "9f1f":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            internal_cause = str(int(field_data, 16))
                                                        if t == "83":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_type = str(int(field_data, 16))
                                                        if t == "9d":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_position = str(int(field_data, 16))
                                                        if t == "99":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            route = str(
                                                                binascii.a2b_hex(rou1)
                                                            )
                                                        if t == "8c":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            disconnecting_party = str(int(field_data, 16))
                                                        if t == "92":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            trssc = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        i1 = i1 + 2 + field_length * 2
                                                except IndexError:
                                                    print(current_position)
                                                    print(i)
                                                    pass

                                            if ab[0:2] == "a4":
                                                record_type = "TER"
                                                i1 = 0
                                                try:
                                                    while x[i1] != ".":
                                                        h = i1
                                                        if (
                                                            int(x[i1 + 1], 16) == 15
                                                            and int(x[i1], 16) % 2 != 0
                                                        ):
                                                            i1 = i1 + 2
                                                            while (
                                                                int(x[i1 : i1 + 2], 16)
                                                                > 127
                                                            ):
                                                                i1 = i1 + 2
                                                        t = x[h : i1 + 2]
                                                        i1 = i1 + 2
                                                        field_length = int(x[i1 : i1 + 2], 16)
                                                        if field_length > 127:
                                                            c = field_length - 128
                                                            if c == 0:
                                                                field_length = 0
                                                            else:
                                                                i1 = i1 + 2
                                                                field_length = int(
                                                                    x[i1 : i1 + c * 2],
                                                                    16,
                                                                )

                                                        if t == "84":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            origin_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                origin_number = (
                                                                    origin_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )

                                                        if t == "97":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            carrier_code = str(int(field_data, 16))

                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            carrier_code = str(
                                                                binascii.a2b_hex(rou1)
                                                            )
                                                            carrier_code = carrier_code[2:].replace("'", "")

                                                        if t == "87":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]

                                                            imei = ""
                                                            for i in range(
                                                                0, len(field_data), 2
                                                            ):
                                                                imei = (
                                                                    imei
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "86":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]

                                                            imsi = ""
                                                            for i in range(
                                                                0, len(field_data), 2
                                                            ):
                                                                imsi = (
                                                                    imsi
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "9f43":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            reference_id = field_data
                                                        if t == "85":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            destination_number = ""
                                                            for i in range(
                                                                2, len(field_data), 2
                                                            ):
                                                                destination_number = (
                                                                    destination_number
                                                                    + field_data[i + 1]
                                                                    + field_data[i]
                                                                )
                                                        if t == "8a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            date = (
                                                                str(int(field_data[4:6], 16))
                                                                + "/"
                                                                + str(int(field_data[2:4], 16))
                                                                + "/"
                                                                + str(int(field_data[0:2], 16))
                                                            )
                                                        if t == "8b":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            time = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "94":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            bi2 = str.encode(field_data)
                                                            billing_id = str(
                                                                binascii.a2b_hex(bi2)
                                                            )

                                                        if t == "8d":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            duration = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "9f3b":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            fault_code = str(int(field_data, 16))
                                                        if t == "9f22":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            eos_info = str(int(field_data, 16))
                                                        if t == "9f23":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            internal_cause = str(int(field_data, 16))
                                                        if t == "83":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_type = str(int(field_data, 16))
                                                        if t == "9f21":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            call_position = str(int(field_data, 16))
                                                        if t == "96":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            rou1 = str.encode(field_data)
                                                            route = str(
                                                                binascii.a2b_hex(rou1)
                                                            )
                                                        if t == "89":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            disconnecting_party = str(int(field_data, 16))
                                                        if t == "9a":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            cst = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        if t == "9f55":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            cco = str(int(field_data, 16))
                                                        if t == "9b":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            location_info = (
                                                                str(int(field_data[1], 16))
                                                                + str(int(field_data[0], 16))
                                                                + str(int(field_data[3], 16))
                                                                + "-"
                                                                + str(int(field_data[5], 16))
                                                                + str(int(field_data[4], 16))
                                                                + str(int(field_data[2], 16))
                                                                + "-"
                                                                + str(
                                                                    int(field_data[6:10], 16)
                                                                )
                                                                + "-"
                                                                + str(
                                                                    int(field_data[10:14], 16)
                                                                )
                                                            )
                                                        if t == "8f":
                                                            field_data = x[
                                                                i1 + 2 : i1 + field_length * 2 + 2
                                                            ]
                                                            trssc = (
                                                                str(int(field_data[0:2], 16))
                                                                + ":"
                                                                + str(int(field_data[2:4], 16))
                                                                + ":"
                                                                + str(int(field_data[4:6], 16))
                                                            )
                                                        i1 = i1 + 2 + field_length * 2
                                                except IndexError:
                                                    print(current_position)
                                                    print(i)
                                                    pass

                                            dt2 = date.split("/")
                                            dt3 = (
                                                dt2[2].zfill(2)
                                                + "/"
                                                + dt2[1].zfill(2)
                                                + "/"
                                                + dt2[0].zfill(2)
                                            )
                                            hr2 = time.split(":")
                                            hr3 = (
                                                hr2[0].zfill(2)
                                                + ":"
                                                + hr2[1].zfill(2)
                                                + ":"
                                                + hr2[2].zfill(2)
                                            )

                                            li8 = location_info.split("-")
                                            if len(li8) == 4:
                                                location_info = (
                                                    li8[0]
                                                    + "-"
                                                    + li8[1][0:2]
                                                    + "-"
                                                    + li8[2]
                                                    + "-"
                                                    + li8[3]
                                                )

                                            parsed_records.append(
                                                record_type
                                                + ";"
                                                + billing_id[2:].replace("'", "")
                                                + ";"
                                                + reference_id
                                                + ";"
                                                + dt3
                                                + ";"
                                                + hr3
                                                + ";"
                                                + imsi.replace("f", "")
                                                + ";"
                                                + location_info
                                                + ";"
                                                + route[2:].replace("'", "")
                                                + ";"
                                                + origin_number
                                                + ";"
                                                + destination_number.replace("f", "")
                                                + ";"
                                                + call_type
                                                + ";"
                                                + duration
                                                + ";"
                                                + call_position
                                                + ";"
                                                + fault_code
                                                + ";"
                                                + eos_info
                                                + ";"
                                                + internal_cause
                                                + ";"
                                                + disconnecting_party
                                                + ";"
                                                + cco
                                                + ";"
                                                + cs
                                                + ";"
                                                + cst
                                                + ";"
                                                + carrier_code
                                                + ";"
                                                + tn
                                                + ";"
                                                + imei.replace("f", "")
                                                + ";"
                                                + trssc
                                                + ";"
                                                + intt
                                                + ";"
                                                + iarq
                                            )

                                else:
                                    if record_type != "8":
                                        current_position = current_position + field_length * 2

                        else:
                            current_position = current_position + 2

            except IndexError:
                print(current_file)
            for xx in parsed_records:
                g.write(xx + "\n")
            g.close()
            file_content.close()
            processing_status = "-3"
            if validation_mode == "a":
                os.rename(
                    base_path + cdr_database + ";" + str(file_counter) + ".txt",
                    base_path + "f" + cdr_database + ";" + str(file_counter) + ".txt",
                )
            else:
                os.rename(ali + ".txt", ali + "f.txt")

    except Exception as eru:
        print(eru)
        print(current_file)
        error_log_file.write(str(eru) + ";" + current_file + "\n")
    if file_processed_flag == 1 and processing_status != "-3":
        if processing_status == "-2":
            if validation_mode == "a":
                g.close()

                os.rename(
                    base_path + cdr_database + ";" + str(file_counter) + ".txt",
                    base_path + "f" + cdr_database + ";" + str(file_counter) + "N.txt",
                )
            else:
                g.close()

                os.rename(ali + ".txt", ali + "fN.txt")
            file_content.close()


error_log_file.close()

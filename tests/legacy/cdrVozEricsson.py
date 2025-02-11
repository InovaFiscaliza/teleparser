import binascii
import glob
import gzip
import os
import sys
from time import asctime


def process_cdr_voz_ericsson(
    process_number,
    validation_mode,
    output_path,
    base_path,
    cdr_database,
    raw_cdr_path,
    queue_position,
    active_sessions,
    record_type,
):
    buffer_size = 50000
    input_attempt_count = 10
    input_retry_count = 0

    error_log_file = open("Erro" + process_number + ".txt", "w")
    process_id = str(os.getpid())
    current_directory = os.getcwd()

    timestamp = asctime().replace(":", "").replace(" ", "")
    carrier_names = {
        "VI": "VIVO",
        "TI": "TIM",
        "OI": "OI",
        "CL": "CLARO",
        "NE": "NEXTEL",
        "AL": "ALGAR",
    }

    res = "ResDados" + "&" + process_id + "&" + cdr_database + "-" + process_number

    operator_ids = {
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
    billing_dict = {}
    error_dict = {}
    date_dict = {}
    destination_numbers_dict = {}
    origin_numbers_dict = {}
    billing_list = []
    numbers_list = []
    filtered_numbers = []
    unique_numbers = set()
    processed_numbers = []
    result_numbers = []
    dicna1 = {}
    dicna2 = {}
    cell_a_dict = {}
    dicha2 = {}
    destination_numbers_dict = {}
    billing_filtered = []
    unique_billing = set()
    processed_billing = []
    result_billing = []
    dicnb1 = {}
    dicnb2 = {}
    cell_b_dict = {}
    dichb2 = {}
    location_areas = set()
    location_area_dict = {}
    processed_records = set()
    failed_records = set()
    header_flag = 0

    max_records = 1000000
    orig = glob.glob(raw_cdr_path)

    process_counter = 0
    file_counter = 0
    total_counter = 0
    archive_counter = -1

    record_types = ["a0", "a1", "a2", "a3", "a4"]
    morning_hours = ["10", "11", "12"]
    evening_hours = ["18", "19", "20"]

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
                    output_file = open(
                        base_path + cdr_database + ";" + str(file_counter) + ".txt", "w"
                    )
                else:
                    file_path_parts = i.split("\\")

                    output_file = open(
                        base_path
                        + output_path
                        + cdr_database
                        + "\\"
                        + file_path_parts[len(file_path_parts) - 2]
                        + "\\"
                        + file_path_parts[len(file_path_parts) - 1].replace(
                            "gz", "txt"
                        ),
                        "w",
                    )
                    output_file.write(
                        "Tipo_de_chamada;Bilhetador;Referencia;Data;Hora;IMSI;1stCelA;Outgoing_route;Origem;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto"
                        + "\n"
                    )
                    output_file_path = (
                        base_path
                        + output_path
                        + cdr_database
                        + "\\"
                        + file_path_parts[len(file_path_parts) - 2]
                        + "\\"
                        + file_path_parts[len(file_path_parts) - 1].replace(".gz", "")
                    )
                processing_status = "-2"

                raw_binary_data = file_content.read(buffer_size)

                hex_data = str(binascii.b2a_hex(raw_binary_data))

                current_position = 2

                parsed_records = []
                try:
                    while hex_data[current_position] != "'":
                        current_tag = hex_data[current_position : current_position + 2]

                        if current_tag != "00":
                            tag_length = 1
                            if (
                                int(current_tag[1], 16) == 15
                                and int(current_tag[0], 16) % 2 != 0
                            ):
                                current_position += 2
                                a12 = hex_data[current_position : current_position + 2]
                                tag_length = tag_length + 1
                                while int(a12[0:2], 16) > 127:
                                    current_position += 2
                                    a12 = hex_data[
                                        current_position : current_position + 2
                                    ]
                                    tag_length += 1
                            record_tag = hex_data[
                                (current_position - (tag_length * 2))
                                + 2 : current_position + 2
                            ]

                            tag_start_position = current_position - (tag_length * 2) + 2

                            current_position += 2
                            a3 = hex_data[current_position : current_position + 2]
                            field_length = int(a3[0:2], 16)
                            if field_length > 127:
                                length_indicator = field_length - 128
                                if length_indicator == 0:
                                    field_length = 0
                                else:
                                    current_position += 2
                                    actual_length = hex_data[
                                        current_position : current_position
                                        + length_indicator * 2
                                    ]
                                    field_length = int(actual_length, 16)
                                    current_position = (
                                        current_position - 2
                                    ) + length_indicator * 2

                            timestamp = -2
                            if 2 * buffer_size - current_position < 10000:
                                timestamp = len(
                                    hex_data[tag_start_position:].replace("'", "")
                                )

                            if timestamp != -2 and timestamp < field_length * 2 + 30:
                                remaining_hex_data = hex_data[
                                    tag_start_position:
                                ].replace("'", "")

                                raw_binary_data = file_content.read(buffer_size)
                                next_hex_block = str(binascii.b2a_hex(raw_binary_data))[
                                    2:
                                ]

                                hex_data = remaining_hex_data + next_hex_block

                                current_position = 0
                                for record_line in parsed_records:
                                    output_file.write(record_line + "\n")
                                parsed_records = []
                            else:
                                current_position += 2
                                if record_tag == "a0":
                                    record_block = hex_data[
                                        current_position : current_position
                                        + field_length * 2
                                    ]
                                    current_position = (
                                        current_position + field_length * 2
                                    )

                                    if record_block[0:2] in record_types:
                                        content_length = int(record_block[2:4], 16)
                                        if content_length > 127:
                                            adjusted_length = content_length - 128
                                        else:
                                            adjusted_length = 0
                                        record_data = (
                                            record_block[
                                                2 + adjusted_length * 2 + 2 : (
                                                    field_length * 2 + 2
                                                )
                                            ]
                                            + "."
                                        )

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
                                        channel_seizure_time = ""
                                        called_party_seizure_time = ""
                                        location_info = ""
                                        call_position = ""
                                        bssmap_cause_code = ""
                                        imsi = ""
                                        disconnecting_party = ""
                                        translated_number = ""
                                        imei = ""
                                        trssc = ""
                                        intt = ""

                                        if record_block[0:2] == "a0":
                                            record_type = "TRA"

                                            field_position = 0

                                            while record_data[field_position] != ".":
                                                tag_length = field_position
                                                if (
                                                    int(
                                                        record_data[field_position + 1],
                                                        16,
                                                    )
                                                    == 15
                                                    and int(
                                                        record_data[field_position],
                                                        16,
                                                    )
                                                    % 2
                                                    != 0
                                                ):
                                                    field_position = field_position + 2
                                                    while (
                                                        int(
                                                            record_data[
                                                                field_position : field_position
                                                                + 2
                                                            ],
                                                            16,
                                                        )
                                                        > 127
                                                    ):
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                field_tag = record_data[
                                                    tag_length : field_position + 2
                                                ]
                                                field_position = field_position + 2
                                                field_length = int(
                                                    record_data[
                                                        field_position : field_position
                                                        + 2
                                                    ],
                                                    16,
                                                )
                                                if field_length > 127:
                                                    length_indicator = (
                                                        field_length - 128
                                                    )
                                                    if length_indicator == 0:
                                                        field_length = 0
                                                    else:
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                        field_length = int(
                                                            record_data[
                                                                field_position : field_position
                                                                + length_indicator * 2
                                                            ],
                                                            16,
                                                        )

                                                if field_tag == "84":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
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
                                                if field_tag == "96":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    route_bytes = str.encode(field_data)
                                                    carrier_code = str(
                                                        binascii.a2b_hex(route_bytes)
                                                    )
                                                    carrier_code = carrier_code[
                                                        2:
                                                    ].replace("'", "")

                                                if field_tag == "86":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
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
                                                if field_tag == "9f2e":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    reference_id = field_data
                                                if field_tag == "85":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
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
                                                if field_tag == "88":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    date = (
                                                        str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                        + "/"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + "/"
                                                        + str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "89":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    time = (
                                                        str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "93":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    billing_bytes = str.encode(
                                                        field_data
                                                    )
                                                    billing_id = str(
                                                        binascii.a2b_hex(billing_bytes)
                                                    )
                                                if field_tag == "8b":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    duration = (
                                                        str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "9f29":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    fault_code = str(
                                                        int(field_data, 16)
                                                    )
                                                if field_tag == "9b":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    eos_info = str(int(field_data, 16))
                                                if field_tag == "9c":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    internal_cause = str(
                                                        int(field_data, 16)
                                                    )
                                                if field_tag == "83":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    call_type = str(int(field_data, 16))

                                                if field_tag == "9a":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    call_position = str(
                                                        int(field_data, 16)
                                                    )
                                                if field_tag == "95":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    route_bytes = str.encode(field_data)
                                                    route = str(
                                                        binascii.a2b_hex(route_bytes)
                                                    )

                                                if field_tag == "87":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    disconnecting_party = str(
                                                        int(field_data, 16)
                                                    )
                                                if field_tag == "8d":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    trssc = (
                                                        str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                field_position = (
                                                    field_position
                                                    + 2
                                                    + field_length * 2
                                                )

                                        if record_block[0:2] == "a1":
                                            record_type = "ORI"
                                            field_position = 0
                                            try:
                                                while (
                                                    record_data[field_position] != "."
                                                ):
                                                    tag_length = field_position
                                                    if (
                                                        int(
                                                            record_data[
                                                                field_position + 1
                                                            ],
                                                            16,
                                                        )
                                                        == 15
                                                        and int(
                                                            record_data[field_position],
                                                            16,
                                                        )
                                                        % 2
                                                        != 0
                                                    ):
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                        while (
                                                            int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + 2
                                                                ],
                                                                16,
                                                            )
                                                            > 127
                                                        ):
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                    field_tag = record_data[
                                                        tag_length : field_position + 2
                                                    ]
                                                    field_position = field_position + 2
                                                    field_length = int(
                                                        record_data[
                                                            field_position : field_position
                                                            + 2
                                                        ],
                                                        16,
                                                    )
                                                    if field_length > 127:
                                                        length_indicator = (
                                                            field_length - 128
                                                        )
                                                        if length_indicator == 0:
                                                            field_length = 0
                                                        else:
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                            field_length = int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + length_indicator
                                                                    * 2
                                                                ],
                                                                16,
                                                            )

                                                    if field_tag == "84":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        origin_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            origin_number = (
                                                                origin_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )

                                                    if field_tag == "97":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        carrier_code = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )
                                                        carrier_code = carrier_code[
                                                            2:
                                                        ].replace("'", "")

                                                    if field_tag == "86":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]

                                                        imei = ""
                                                        for i in range(
                                                            0,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            imei = (
                                                                imei
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "85":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]

                                                        imsi = ""
                                                        for i in range(
                                                            0,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            imsi = (
                                                                imsi
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "9f44":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        reference_id = field_data
                                                    if field_tag == "87":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        destination_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            destination_number = (
                                                                destination_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "9f4a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        translated_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            translated_number = (
                                                                translated_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "89":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        date = (
                                                            str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "8a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        time = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "94":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        billing_bytes = str.encode(
                                                            field_data
                                                        )
                                                        billing_id = str(
                                                            binascii.a2b_hex(
                                                                billing_bytes
                                                            )
                                                        )
                                                    if field_tag == "8c":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        duration = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "8d":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        intt = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "9f3b":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        fault_code = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9f22":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        eos_info = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9f23":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        internal_cause = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "83":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_type = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9f21":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_position = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "96":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        route = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )

                                                    if field_tag == "88":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        disconnecting_party = str(
                                                            int(
                                                                field_data,
                                                                16,
                                                            )
                                                        )
                                                    if field_tag == "9a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        channel_seizure_time = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "9f62":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        bssmap_cause_code = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9b":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        location_info = (
                                                            str(
                                                                int(
                                                                    field_data[1],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[0],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[3],
                                                                    16,
                                                                )
                                                            )
                                                            + "-"
                                                            + str(
                                                                int(
                                                                    field_data[5],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[4],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[2],
                                                                    16,
                                                                )
                                                            )
                                                            + "-"
                                                            + str(
                                                                int(
                                                                    field_data[6:10],
                                                                    16,
                                                                )
                                                            )
                                                            + "-"
                                                            + str(
                                                                int(
                                                                    field_data[10:14],
                                                                    16,
                                                                )
                                                            )
                                                            + "|"
                                                            + field_data
                                                        )
                                                    if field_tag == "8e":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        trssc = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    field_position = (
                                                        field_position
                                                        + 2
                                                        + field_length * 2
                                                    )
                                            except IndexError:
                                                print(current_position)
                                                print(i)
                                                pass
                                        if record_block[0:2] == "a2":
                                            record_type = "ROA"
                                            field_position = 0
                                            try:
                                                while (
                                                    record_data[field_position] != "."
                                                ):
                                                    tag_length = field_position
                                                    if (
                                                        int(
                                                            record_data[
                                                                field_position + 1
                                                            ],
                                                            16,
                                                        )
                                                        == 15
                                                        and int(
                                                            record_data[field_position],
                                                            16,
                                                        )
                                                        % 2
                                                        != 0
                                                    ):
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                        while (
                                                            int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + 2
                                                                ],
                                                                16,
                                                            )
                                                            > 127
                                                        ):
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                    field_tag = record_data[
                                                        tag_length : field_position + 2
                                                    ]
                                                    field_position = field_position + 2
                                                    field_length = int(
                                                        record_data[
                                                            field_position : field_position
                                                            + 2
                                                        ],
                                                        16,
                                                    )
                                                    if field_length > 127:
                                                        length_indicator = (
                                                            field_length - 128
                                                        )
                                                        if length_indicator == 0:
                                                            field_length = 0
                                                        else:
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                            field_length = int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + length_indicator
                                                                    * 2
                                                                ],
                                                                16,
                                                            )

                                                    if field_tag == "84":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        origin_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            origin_number = (
                                                                origin_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )

                                                    if field_tag == "96":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        carrier_code = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )
                                                        carrier_code = carrier_code[
                                                            2:
                                                        ].replace("'", "")

                                                    if field_tag == "86":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]

                                                        imsi = ""
                                                        for i in range(
                                                            0,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            imsi = (
                                                                imsi
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "9f31":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        reference_id = field_data
                                                    if field_tag == "85":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        destination_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            destination_number = (
                                                                destination_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "89":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        date = (
                                                            str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "8a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        time = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "93":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        billing_bytes = str.encode(
                                                            field_data
                                                        )
                                                        billing_id = str(
                                                            binascii.a2b_hex(
                                                                billing_bytes
                                                            )
                                                        )
                                                    if field_tag == "8c":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        duration = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "9f2d":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        fault_code = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        eos_info = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9b":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        internal_cause = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "83":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_type = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "99":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_position = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "95":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        route = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )
                                                    if field_tag == "88":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        disconnecting_party = str(
                                                            int(
                                                                field_data,
                                                                16,
                                                            )
                                                        )
                                                    if field_tag == "8e":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        trssc = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    field_position = (
                                                        field_position
                                                        + 2
                                                        + field_length * 2
                                                    )
                                            except IndexError:
                                                print(current_position)
                                                print(i)
                                                pass
                                        if record_block[0:2] == "a5":
                                            record_type = "SMSo"
                                            field_position = 0

                                            while record_data[field_position] != ".":
                                                tag_length = field_position
                                                if (
                                                    int(
                                                        record_data[field_position + 1],
                                                        16,
                                                    )
                                                    == 15
                                                    and int(
                                                        record_data[field_position],
                                                        16,
                                                    )
                                                    % 2
                                                    != 0
                                                ):
                                                    field_position = field_position + 2
                                                    while (
                                                        int(
                                                            record_data[
                                                                field_position : field_position
                                                                + 2
                                                            ],
                                                            16,
                                                        )
                                                        > 127
                                                    ):
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                field_tag = record_data[
                                                    tag_length : field_position + 2
                                                ]
                                                field_position = field_position + 2
                                                field_length = int(
                                                    record_data[
                                                        field_position : field_position
                                                        + 2
                                                    ],
                                                    16,
                                                )
                                                if field_length > 127:
                                                    length_indicator = (
                                                        field_length - 128
                                                    )
                                                    if length_indicator == 0:
                                                        field_length = 0
                                                    else:
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                        field_length = int(
                                                            record_data[
                                                                field_position : field_position
                                                                + length_indicator * 2
                                                            ],
                                                            16,
                                                        )

                                                if field_tag == "8e":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    location_info = (
                                                        str(
                                                            int(
                                                                field_data[1],
                                                                16,
                                                            )
                                                        )
                                                        + str(
                                                            int(
                                                                field_data[0],
                                                                16,
                                                            )
                                                        )
                                                        + str(
                                                            int(
                                                                field_data[3],
                                                                16,
                                                            )
                                                        )
                                                        + "-"
                                                        + str(
                                                            int(
                                                                field_data[5],
                                                                16,
                                                            )
                                                        )
                                                        + str(
                                                            int(
                                                                field_data[4],
                                                                16,
                                                            )
                                                        )
                                                        + str(
                                                            int(
                                                                field_data[2],
                                                                16,
                                                            )
                                                        )
                                                        + "-"
                                                        + str(
                                                            int(
                                                                field_data[6:10],
                                                                16,
                                                            )
                                                        )
                                                        + "-"
                                                        + str(
                                                            int(
                                                                field_data[10:14],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "84":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
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
                                                if field_tag == "81":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    carrier_code = str(
                                                        int(field_data, 16)
                                                    )
                                                if field_tag == "9f2a":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    imei = str(int(field_data, 16))
                                                if field_tag == "9f2b":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    reference_id = field_data

                                                if field_tag == "87":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    date = (
                                                        str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                        + "/"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + "/"
                                                        + str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "88":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    time = (
                                                        str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "8b":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    billing_bytes = str.encode(
                                                        field_data
                                                    )
                                                    billing_id = str(
                                                        binascii.a2b_hex(billing_bytes)
                                                    )

                                                if field_tag == "83":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    call_type = str(int(field_data, 16))
                                                if field_tag == "9f2a":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    call_position = str(
                                                        int(field_data, 16)
                                                    )

                                                field_position = (
                                                    field_position
                                                    + 2
                                                    + field_length * 2
                                                )
                                        if record_block[0:2] == "a7":
                                            record_type = "SMSt"
                                            field_position = 0

                                            while record_data[field_position] != ".":
                                                tag_length = field_position
                                                if (
                                                    int(
                                                        record_data[field_position + 1],
                                                        16,
                                                    )
                                                    == 15
                                                    and int(
                                                        record_data[field_position],
                                                        16,
                                                    )
                                                    % 2
                                                    != 0
                                                ):
                                                    field_position = field_position + 2
                                                    while (
                                                        int(
                                                            record_data[
                                                                field_position : field_position
                                                                + 2
                                                            ],
                                                            16,
                                                        )
                                                        > 127
                                                    ):
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                field_tag = record_data[
                                                    tag_length : field_position + 2
                                                ]
                                                field_position = field_position + 2
                                                field_length = int(
                                                    record_data[
                                                        field_position : field_position
                                                        + 2
                                                    ],
                                                    16,
                                                )
                                                if field_length > 127:
                                                    length_indicator = (
                                                        field_length - 128
                                                    )
                                                    if length_indicator == 0:
                                                        field_length = 0
                                                    else:
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                        field_length = int(
                                                            record_data[
                                                                field_position : field_position
                                                                + length_indicator * 2
                                                            ],
                                                            16,
                                                        )

                                                if field_tag == "81":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    carrier_code = str(
                                                        int(field_data, 16)
                                                    )

                                                if field_tag == "83":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
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
                                                if field_tag == "86":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    date = (
                                                        str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                        + "/"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + "/"
                                                        + str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "87":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    time = (
                                                        str(
                                                            int(
                                                                field_data[0:2],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[2:4],
                                                                16,
                                                            )
                                                        )
                                                        + ":"
                                                        + str(
                                                            int(
                                                                field_data[4:6],
                                                                16,
                                                            )
                                                        )
                                                    )
                                                if field_tag == "8a":
                                                    field_data = record_data[
                                                        field_position
                                                        + 2 : field_position
                                                        + field_length * 2
                                                        + 2
                                                    ]
                                                    billing_bytes = str.encode(
                                                        field_data
                                                    )
                                                    billing_id = str(
                                                        binascii.a2b_hex(billing_bytes)
                                                    )

                                                field_position = (
                                                    field_position
                                                    + 2
                                                    + field_length * 2
                                                )
                                        if record_block[0:2] == "a3":
                                            record_type = "FOR"
                                            field_position = 0
                                            try:
                                                while (
                                                    record_data[field_position] != "."
                                                ):
                                                    tag_length = field_position
                                                    if (
                                                        int(
                                                            record_data[
                                                                field_position + 1
                                                            ],
                                                            16,
                                                        )
                                                        == 15
                                                        and int(
                                                            record_data[field_position],
                                                            16,
                                                        )
                                                        % 2
                                                        != 0
                                                    ):
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                        while (
                                                            int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + 2
                                                                ],
                                                                16,
                                                            )
                                                            > 127
                                                        ):
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                    field_tag = record_data[
                                                        tag_length : field_position + 2
                                                    ]
                                                    field_position = field_position + 2
                                                    field_length = int(
                                                        record_data[
                                                            field_position : field_position
                                                            + 2
                                                        ],
                                                        16,
                                                    )
                                                    if field_length > 127:
                                                        length_indicator = (
                                                            field_length - 128
                                                        )
                                                        if length_indicator == 0:
                                                            field_length = 0
                                                        else:
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                            field_length = int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + length_indicator
                                                                    * 2
                                                                ],
                                                                16,
                                                            )

                                                    if field_tag == "84":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        origin_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            origin_number = (
                                                                origin_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )

                                                    if field_tag == "9a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        carrier_code = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )
                                                        carrier_code = carrier_code[
                                                            2:
                                                        ].replace("'", "")

                                                    if field_tag == "8a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]

                                                        imsi = ""
                                                        for i in range(
                                                            0,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            imsi = (
                                                                imsi
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "9f39":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        reference_id = field_data
                                                    if field_tag == "85":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        destination_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            destination_number = (
                                                                destination_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "8d":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        date = (
                                                            str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "8e":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        time = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "97":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        billing_bytes = str.encode(
                                                            field_data
                                                        )
                                                        billing_id = str(
                                                            binascii.a2b_hex(
                                                                billing_bytes
                                                            )
                                                        )
                                                    if field_tag == "90":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        duration = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "9f33":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        fault_code = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9e":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        eos_info = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9f1f":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        internal_cause = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "83":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_type = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9d":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_position = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "99":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        route = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )
                                                    if field_tag == "8c":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        disconnecting_party = str(
                                                            int(
                                                                field_data,
                                                                16,
                                                            )
                                                        )
                                                    if field_tag == "92":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        trssc = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    field_position = (
                                                        field_position
                                                        + 2
                                                        + field_length * 2
                                                    )
                                            except IndexError:
                                                print(current_position)
                                                print(i)
                                                pass

                                        if record_block[0:2] == "a4":
                                            record_type = "TER"
                                            field_position = 0
                                            try:
                                                while (
                                                    record_data[field_position] != "."
                                                ):
                                                    tag_length = field_position
                                                    if (
                                                        int(
                                                            record_data[
                                                                field_position + 1
                                                            ],
                                                            16,
                                                        )
                                                        == 15
                                                        and int(
                                                            record_data[field_position],
                                                            16,
                                                        )
                                                        % 2
                                                        != 0
                                                    ):
                                                        field_position = (
                                                            field_position + 2
                                                        )
                                                        while (
                                                            int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + 2
                                                                ],
                                                                16,
                                                            )
                                                            > 127
                                                        ):
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                    field_tag = record_data[
                                                        tag_length : field_position + 2
                                                    ]
                                                    field_position = field_position + 2
                                                    field_length = int(
                                                        record_data[
                                                            field_position : field_position
                                                            + 2
                                                        ],
                                                        16,
                                                    )
                                                    if field_length > 127:
                                                        length_indicator = (
                                                            field_length - 128
                                                        )
                                                        if length_indicator == 0:
                                                            field_length = 0
                                                        else:
                                                            field_position = (
                                                                field_position + 2
                                                            )
                                                            field_length = int(
                                                                record_data[
                                                                    field_position : field_position
                                                                    + length_indicator
                                                                    * 2
                                                                ],
                                                                16,
                                                            )

                                                    if field_tag == "84":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        origin_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            origin_number = (
                                                                origin_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )

                                                    if field_tag == "97":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        carrier_code = str(
                                                            int(field_data, 16)
                                                        )

                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        carrier_code = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )
                                                        carrier_code = carrier_code[
                                                            2:
                                                        ].replace("'", "")

                                                    if field_tag == "87":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]

                                                        imei = ""
                                                        for i in range(
                                                            0,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            imei = (
                                                                imei
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "86":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]

                                                        imsi = ""
                                                        for i in range(
                                                            0,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            imsi = (
                                                                imsi
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "9f43":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        reference_id = field_data
                                                    if field_tag == "85":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        destination_number = ""
                                                        for i in range(
                                                            2,
                                                            len(field_data),
                                                            2,
                                                        ):
                                                            destination_number = (
                                                                destination_number
                                                                + field_data[i + 1]
                                                                + field_data[i]
                                                            )
                                                    if field_tag == "8a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        date = (
                                                            str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + "/"
                                                            + str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "8b":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        time = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "94":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        billing_bytes = str.encode(
                                                            field_data
                                                        )
                                                        billing_id = str(
                                                            binascii.a2b_hex(
                                                                billing_bytes
                                                            )
                                                        )

                                                    if field_tag == "8d":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        duration = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "9f3b":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        fault_code = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9f22":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        eos_info = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9f23":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        internal_cause = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "83":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_type = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9f21":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        call_position = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "96":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        route_bytes = str.encode(
                                                            field_data
                                                        )
                                                        route = str(
                                                            binascii.a2b_hex(
                                                                route_bytes
                                                            )
                                                        )
                                                    if field_tag == "89":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        disconnecting_party = str(
                                                            int(
                                                                field_data,
                                                                16,
                                                            )
                                                        )
                                                    if field_tag == "9a":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        called_party_seizure_time = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "9f55":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        bssmap_cause_code = str(
                                                            int(field_data, 16)
                                                        )
                                                    if field_tag == "9b":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        location_info = (
                                                            str(
                                                                int(
                                                                    field_data[1],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[0],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[3],
                                                                    16,
                                                                )
                                                            )
                                                            + "-"
                                                            + str(
                                                                int(
                                                                    field_data[5],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[4],
                                                                    16,
                                                                )
                                                            )
                                                            + str(
                                                                int(
                                                                    field_data[2],
                                                                    16,
                                                                )
                                                            )
                                                            + "-"
                                                            + str(
                                                                int(
                                                                    field_data[6:10],
                                                                    16,
                                                                )
                                                            )
                                                            + "-"
                                                            + str(
                                                                int(
                                                                    field_data[10:14],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    if field_tag == "8f":
                                                        field_data = record_data[
                                                            field_position
                                                            + 2 : field_position
                                                            + field_length * 2
                                                            + 2
                                                        ]
                                                        trssc = (
                                                            str(
                                                                int(
                                                                    field_data[0:2],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[2:4],
                                                                    16,
                                                                )
                                                            )
                                                            + ":"
                                                            + str(
                                                                int(
                                                                    field_data[4:6],
                                                                    16,
                                                                )
                                                            )
                                                        )
                                                    field_position = (
                                                        field_position
                                                        + 2
                                                        + field_length * 2
                                                    )
                                            except IndexError:
                                                print(current_position)
                                                print(i)
                                                pass

                                        date_parts = date.split("/")
                                        formatted_date = (
                                            date_parts[2].zfill(2)
                                            + "/"
                                            + date_parts[1].zfill(2)
                                            + "/"
                                            + date_parts[0].zfill(2)
                                        )
                                        time_parts = time.split(":")
                                        formatted_time = (
                                            time_parts[0].zfill(2)
                                            + ":"
                                            + time_parts[1].zfill(2)
                                            + ":"
                                            + time_parts[2].zfill(2)
                                        )

                                        location_parts = location_info.split("-")
                                        if len(location_parts) == 4:
                                            location_info = (
                                                location_parts[0]
                                                + "-"
                                                + location_parts[1][0:2]
                                                + "-"
                                                + location_parts[2]
                                                + "-"
                                                + location_parts[3]
                                            )

                                        parsed_records.append(
                                            record_type
                                            + ";"
                                            + billing_id[2:].replace("'", "")
                                            + ";"
                                            + reference_id
                                            + ";"
                                            + formatted_date
                                            + ";"
                                            + formatted_time
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
                                            + bssmap_cause_code
                                            + ";"
                                            + channel_seizure_time
                                            + ";"
                                            + called_party_seizure_time
                                            + ";"
                                            + carrier_code
                                            + ";"
                                            + translated_number
                                            + ";"
                                            + imei.replace("f", "")
                                            + ";"
                                            + trssc
                                            + ";"
                                            + intt
                                            + ";"
                                            + iarq
                                        )

                                elif record_type != "8":
                                    current_position = (
                                        current_position + field_length * 2
                                    )

                        else:
                            current_position += 2

                except IndexError:
                    print(current_file)
                for record_line in parsed_records:
                    output_file.write(record_line + "\n")
                output_file.close()
                file_content.close()
                processing_status = "-3"
                if validation_mode == "a":
                    os.rename(
                        base_path + cdr_database + ";" + str(file_counter) + ".txt",
                        base_path
                        + "f"
                        + cdr_database
                        + ";"
                        + str(file_counter)
                        + ".txt",
                    )
                else:
                    os.rename(output_file_path + ".txt", output_file_path + "f.txt")

        except Exception as error_details:
            print(error_details)
            print(current_file)
            error_log_file.write(str(error_details) + ";" + current_file + "\n")
        if file_processed_flag == 1 and processing_status != "-3":
            if processing_status == "-2":
                if validation_mode == "a":
                    output_file.close()

                    os.rename(
                        base_path + cdr_database + ";" + str(file_counter) + ".txt",
                        base_path
                        + "f"
                        + cdr_database
                        + ";"
                        + str(file_counter)
                        + "N.txt",
                    )
                else:
                    output_file.close()

                    os.rename(output_file_path + ".txt", output_file_path + "fN.txt")
                file_content.close()

    error_log_file.close()

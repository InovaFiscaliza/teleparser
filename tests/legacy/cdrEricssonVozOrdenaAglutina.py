import glob
import os
import shutil
import sys
from time import asctime
from datetime import datetime
from operator import itemgetter
from dividearq import split_records_by_prefix

def cdr_ericsson_sort_merge(base_path, cdr_database, operator_code, input_file_path):
    diret = os.getcwd() + "\\"
    max_memory_sort_size = 6000000  # tamanho máximo a ordenar na memória (trecho: ordenar)
    max_file_sort_size = 5000000  # tamanho máximo de arquivo a ser ordenado de uma vez na memória (trecho: ordenar)
    original_input_file = input_file_path
    prefix_length = 15

    timestamp = asctime().replace(":", "").replace(" ", "")
    start_time = datetime.now()
    consolidation_flag = "s"
    opid = {
        "0": "sID",
        "02": "TIM",
        "03": "TIM",
        "04": "TIM",
        "05": "CLARO",
        "06": "CLARO",
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
    }

    if len(glob.glob(base_path + "Arqparciais" + cdr_database)) != 0:  # Ordenar - início - versão 07/2018
        shutil.rmtree(base_path + "Arqparciais" + cdr_database)
    os.mkdir(base_path + "Arqparciais" + cdr_database)

    sorted_files = []
    record_count = 0
    prefixes_set = set()
    prefix_counts = {}
    sorted_prefix_counts = []
    prefix_mapping = {}
    large_prefix_set = set()


    read_attempts = 0
    d = open(input_file_path)

    unique_records_file = open(base_path + cdr_database + "unico.txt", "w")
    voice_record_flag = 0
    for current_record in d:
        if current_record[0:3] == "ORI" or current_record[0:3] == "TER":
            voice_record_flag = 1
            record_count = record_count + 1
            if current_record[0:prefix_length] in prefix_counts:
                prefix_counts[current_record[0:prefix_length]] = prefix_counts[current_record[0:prefix_length]] + 1
            else:
                prefix_counts[current_record[0:prefix_length]] = 1
        else:
            record_fields = current_record.split(";")
            duration_parts = record_fields[11].split(":")
            try:
                duration_seconds = int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + int(duration_parts[2])
            except ValueError:
                if record_fields[11] == "":
                    duration_seconds = 0

            full_date = "20" + record_fields[3].replace("/", "-")
            datetime_string = full_date + ";" + record_fields[4]
            unique_records_file.write(
                record_fields[2]
                + ";"
                + record_fields[8]
                + ";"
                + datetime_string
                + ";"
                + record_fields[0]
                + ";"
                + record_fields[1]
                + ";"
                + record_fields[5]
                + ";"
                + record_fields[6]
                + ";"
                + record_fields[7]
                + ";"
                + record_fields[9]
                + ";"
                + record_fields[10]
                + ";"
                + str(duration_seconds)
                + ";"
                + record_fields[12]
                + ";"
                + record_fields[13]
                + ";"
                + record_fields[14]
                + ";"
                + record_fields[15]
                + ";"
                + record_fields[16]
                + ";"
                + record_fields[17]
                + ";"
                + record_fields[18]
                + ";"
                + record_fields[19]
                + ";"
                + record_fields[20]
                + ";"
                + record_fields[21]
                + ";"
                + record_fields[22]
                + ";"
                + record_fields[23]
                + ";"
                + record_fields[24]
                + ";"
                + record_fields[25]
            )


    d.close()
    unique_records_file.close()

    if len(prefix_counts) != 0:
        sorted_prefix_counts = sorted(prefix_counts.items(), key=itemgetter(0))

        so = 0
        ie = sorted_prefix_counts[0][0]
        for current_record in sorted_prefix_counts:
            if current_record[1] > max_memory_sort_size:
                large_prefix_set.add(current_record[0])
            so = so + current_record[1]
            if so > max_file_sort_size:
                ie = current_record[0]
                so = current_record[1]
            prefix_mapping[current_record[0]] = ie
            prefixes_set.add(ie)

        if len(glob.glob(base_path + "Auxiliar" + cdr_database)) != 0:
            shutil.rmtree(base_path + "Auxiliar" + cdr_database)
        os.mkdir(base_path + "Auxiliar" + cdr_database)

        pra = open(base_path + "Auxiliar" + cdr_database + "\\pr", "w")
        for current_record in prefixes_set:
            pra.write(current_record + "\n")
        pra.close()
        aaea = open(base_path + "Auxiliar" + cdr_database + "\\aae", "w")
        for current_record in prefix_mapping:
            aaea.write(current_record + "|" + prefix_mapping[current_record] + "\n")
        aaea.close()

        split_records_by_prefix(prefix_length, base_path, cdr_database, input_file_path)

        partial_files = glob.glob(base_path + "Arqparciais" + cdr_database + "\\*.txt")
        partial_files.sort()
        os.remove(input_file_path)
        sorted_output_file = open(base_path + cdr_database + "ord3.txt", "w")
        temp_records = []
        for t in partial_files:
            file_prefix = t.split("\\")
            file_prefix = file_prefix[len(file_prefix) - 1].replace(".txt", "")
            if file_prefix in large_prefix_set:
                prefix_length = prefix_length + 1
                prefix_counts = {}  # ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
                prefixes_set = set()
                prefix_list = []
                prefix_chunks = {}
                sorted_chunk = []
                import os

                d = open(t)
                for current_record in d:
                    prefixes_set.add(current_record[0:prefix_length])
                    if current_record[0:prefix_length] in prefix_counts:
                        prefix_counts[current_record[0:prefix_length]] = prefix_counts[current_record[0:prefix_length]] + 1
                    else:
                        prefix_counts[current_record[0:prefix_length]] = 1
                d.close()
                for current_record in prefixes_set:
                    prefix_list.append(current_record)
                prefix_list.sort()
                chunk_size = 0
                chunk_number = 1
                for current_record in prefix_list:
                    chunk_size = prefix_counts[current_record] + chunk_size
                    if chunk_size <= max_memory_sort_size:
                        prefix_chunks[current_record] = chunk_number
                    else:
                        chunk_number = chunk_number + 1
                        chunk_size = prefix_counts[current_record]
                        prefix_chunks[current_record] = chunk_number
                for current_record in range(prefix_chunks[prefix_list[0]], prefix_chunks[prefix_list[len(prefix_list) - 1]] + 1):
                    d = open(t)
                    for chunk_record in d:
                        if prefix_chunks[chunk_record[0:prefix_length]] == current_record:
                            sorted_chunk.append(chunk_record)
                    d.close()
                    sorted_chunk.sort()
                    for sorted_record in sorted_chunk:
                        sorted_output_file.write(sorted_record)
                    sorted_chunk = []
                os.remove(t)
                prefixes_set = set()
                prefix_list = []
                prefix_chunks = {}
                prefix_counts = {}
            else:
                d = open(t)
                for temp_record in d:
                    temp_records.append(temp_record)
                d.close()
                temp_records.sort()
                for temp_record in temp_records:
                    sorted_output_file.write(temp_record)
                temp_records = []
                os.remove(t)
        sorted_output_file.close()  # ordenar - fim

        re4 = open(base_path + cdr_database + "ord3.txt")
        r = open(base_path + cdr_database + "unico.txt", "a")
        consolidated_output_file = open(base_path + cdr_database + "consolidado.txt", "w")
        j = re4.readline()
        record_fields = j.split(";")

        duration_parts = record_fields[11].split(":")
        try:
            duration_seconds = int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + int(duration_parts[2])
        except ValueError:
            if record_fields[11] == "":
                duration_seconds = 0

        full_date = "20" + record_fields[3].replace("/", "-")
        datetime_string = full_date + ";" + record_fields[4]
        current_reference = record_fields[2]
        current_origin = record_fields[8]
        current_destination = record_fields[9]

        for current_record in re4:
            record_found_flag = 1
            record_parts = current_record.split(";")

            sorted_record = record_parts[11].split(":")
            if record_parts[2] != "":
                if record_parts[2] == current_reference and (record_parts[0] == "ORI" or record_parts[0] == "TER") and record_parts[8] == current_origin:
                    consolidated_output_file.write(j)
                    while record_parts[2] == current_reference and record_parts[8] == current_origin:
                        consolidated_output_file.write(current_record)
                        try:
                            duration_seconds = duration_seconds + int(sorted_record[0]) * 3600 + int(sorted_record[1]) * 60 + int(sorted_record[2])

                        except ValueError:
                            duration_seconds = record_parts[11]
                        except TypeError:
                            duration_seconds = record_parts[11]

                        current_reference = record_parts[2]
                        current_origin = record_fields[8]
                        current_destination = record_fields[9]
                        last_record = current_record.split(";")
                        current_record = re4.readline()
                        if current_record == "":
                            break
                        record_parts = current_record.split(";")
                        sorted_record = record_parts[11].split(":")
                    consolidated_output_file.write(
                        last_record[2]
                        + ";"
                        + last_record[8]
                        + ";"
                        + datetime_string
                        + ";"
                        + last_record[0]
                        + ";"
                        + last_record[1]
                        + ";"
                        + last_record[5]
                        + ";"
                        + last_record[6]
                        + ";"
                        + last_record[7]
                        + ";"
                        + last_record[9]
                        + ";"
                        + last_record[10]
                        + ";"
                        + str(duration_seconds)
                        + ";"
                        + last_record[12]
                        + ";"
                        + last_record[13]
                        + ";"
                        + last_record[14]
                        + ";"
                        + last_record[15]
                        + ";"
                        + last_record[16]
                        + ";"
                        + last_record[17]
                        + ";"
                        + last_record[18]
                        + ";"
                        + last_record[19]
                        + ";"
                        + last_record[20]
                        + ";"
                        + last_record[21]
                        + ";"
                        + last_record[22]
                        + ";"
                        + last_record[23]
                        + ";"
                        + last_record[24]
                        + ";"
                        + last_record[25]
                    )
                    r.write(
                        last_record[2]
                        + ";"
                        + last_record[8]
                        + ";"
                        + datetime_string
                        + ";"
                        + last_record[0]
                        + ";"
                        + last_record[1]
                        + ";"
                        + last_record[5]
                        + ";"
                        + last_record[6]
                        + ";"
                        + last_record[7]
                        + ";"
                        + last_record[9]
                        + ";"
                        + last_record[10]
                        + ";"
                        + str(duration_seconds)
                        + ";"
                        + last_record[12]
                        + ";"
                        + last_record[13]
                        + ";"
                        + last_record[14]
                        + ";"
                        + last_record[15]
                        + ";"
                        + last_record[16]
                        + ";"
                        + last_record[17]
                        + ";"
                        + last_record[18]
                        + ";"
                        + last_record[19]
                        + ";"
                        + last_record[20]
                        + ";"
                        + last_record[21]
                        + ";"
                        + last_record[22]
                        + ";"
                        + last_record[23]
                        + ";"
                        + last_record[24]
                        + ";"
                        + last_record[25]
                    )
                    record_found_flag = 0
                    j = current_record
                    if j == "":
                        break
                    record_fields = current_record.split(";")
                    duration_parts = record_fields[11].split(":")
                    try:
                        duration_seconds = int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + int(duration_parts[2])

                    except ValueError:
                        if record_fields[11] == "":
                            duration_seconds = 0
                        else:
                            duration_seconds = record_fields[11]
                    full_date = "20" + record_fields[3].replace("/", "-")
                    datetime_string = full_date + ";" + record_fields[4]
                    current_reference = record_fields[2]
                    current_origin = record_fields[8]
                    current_destination = record_fields[9]
                else:
                    r.write(
                        record_fields[2]
                        + ";"
                        + record_fields[8]
                        + ";"
                        + datetime_string
                        + ";"
                        + record_fields[0]
                        + ";"
                        + record_fields[1]
                        + ";"
                        + record_fields[5]
                        + ";"
                        + record_fields[6]
                        + ";"
                        + record_fields[7]
                        + ";"
                        + record_fields[9]
                        + ";"
                        + record_fields[10]
                        + ";"
                        + str(duration_seconds)
                        + ";"
                        + record_fields[12]
                        + ";"
                        + record_fields[13]
                        + ";"
                        + record_fields[14]
                        + ";"
                        + record_fields[15]
                        + ";"
                        + record_fields[16]
                        + ";"
                        + record_fields[17]
                        + ";"
                        + record_fields[18]
                        + ";"
                        + record_fields[19]
                        + ";"
                        + record_fields[20]
                        + ";"
                        + record_fields[21]
                        + ";"
                        + record_fields[22]
                        + ";"
                        + record_fields[23]
                        + ";"
                        + record_fields[24]
                        + ";"
                        + record_fields[25]
                    )
                    j = current_record
                    if j == "":
                        break
                    record_fields = current_record.split(";")
                    duration_parts = record_fields[11].split(":")
                    try:
                        duration_seconds = int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + int(duration_parts[2])
                    except ValueError:
                        if record_fields[11] == "":
                            duration_seconds = 0
                        else:
                            duration_seconds = record_fields[11]
                    full_date = "20" + record_fields[3].replace("/", "-")
                    datetime_string = full_date + ";" + record_fields[4]
                    current_reference = record_fields[2]
                    current_origin = record_fields[8]
                    current_destination = record_fields[9]
        if record_found_flag == 1:
            r.write(
                record_fields[2]
                + ";"
                + record_fields[8]
                + ";"
                + datetime_string
                + ";"
                + record_fields[0]
                + ";"
                + record_fields[1]
                + ";"
                + record_fields[5]
                + ";"
                + record_fields[6]
                + ";"
                + record_fields[7]
                + ";"
                + record_fields[9]
                + ";"
                + record_fields[10]
                + ";"
                + str(duration_seconds)
                + ";"
                + record_fields[12]
                + ";"
                + record_fields[13]
                + ";"
                + record_fields[14]
                + ";"
                + record_fields[15]
                + ";"
                + record_fields[16]
                + ";"
                + record_fields[17]
                + ";"
                + record_fields[18]
                + ";"
                + record_fields[19]
                + ";"
                + record_fields[20]
                + ";"
                + record_fields[21]
                + ";"
                + record_fields[22]
                + ";"
                + record_fields[23]
                + ";"
                + record_fields[24]
                + ";"
                + record_fields[25]
            )
        re4.close()
        r.close()
        consolidated_output_file.close()

        os.remove(base_path + cdr_database + "ord3.txt")

    if voice_record_flag == 0:
        os.remove(original_input_file)
    input_file_path = base_path + cdr_database + "unico.txt"
    prefix_length = 2

    if len(glob.glob(base_path + "Arqparciais" + cdr_database)) == 1:  # Ordenar - início - versão 07/2018
        shutil.rmtree(base_path + "Arqparciais" + cdr_database)
    partial_dir_check = glob.glob(base_path + "Arqparciais" + cdr_database)
    while len(partial_dir_check) == 1:  # teste
        partial_dir_check = glob.glob(base_path + "Arqparciais" + cdr_database)  # teste
    os.mkdir(base_path + "Arqparciais" + cdr_database)
    for retry_count in range(10000000):  # teste
        retry_flag = 1  # teste
    sorted_files = []
    record_count = 0
    prefixes_set = set()
    prefix_counts = {}
    sorted_prefix_counts = []
    prefix_mapping = {}
    large_prefix_set = set()
    d = open(input_file_path)


    for current_record in d:
        record_count = record_count + 1
        if current_record[0:prefix_length] in prefix_counts:
            prefix_counts[current_record[0:prefix_length]] = prefix_counts[current_record[0:prefix_length]] + 1
        else:
            prefix_counts[current_record[0:prefix_length]] = 1
    d.close()

    sorted_prefix_counts = sorted(prefix_counts.items(), key=itemgetter(0))
    so = 0
    ie = sorted_prefix_counts[0][0]
    for current_record in sorted_prefix_counts:
        if current_record[1] > max_memory_sort_size:
            large_prefix_set.add(current_record[0])
        so = so + current_record[1]
        if so > max_file_sort_size:
            ie = current_record[0]
            so = current_record[1]
        prefix_mapping[current_record[0]] = ie
        prefixes_set.add(ie)


    if len(glob.glob(base_path + "Auxiliar" + cdr_database)) == 1:
        shutil.rmtree(base_path + "Auxiliar" + cdr_database)
    os.mkdir(base_path + "Auxiliar" + cdr_database)

    pra = open(base_path + "Auxiliar" + cdr_database + "\\pr", "w")
    for current_record in prefixes_set:
        pra.write(current_record + "\n")
    pra.close()
    aaea = open(base_path + "Auxiliar" + cdr_database + "\\aae", "w")
    for current_record in prefix_mapping:
        aaea.write(current_record + "|" + prefix_mapping[current_record] + "\n")
    aaea.close()



    split_records_by_prefix(prefix_length, base_path, cdr_database, input_file_path)


    partial_files = glob.glob(base_path + "Arqparciais" + cdr_database + "\\*.txt")
    partial_files.sort()
    sorted_output_file = open(base_path + cdr_database + "ord4.txt", "w")
    os.remove(input_file_path)
    sorted_output_file.write(
        "Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;IMSI;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto"
        + "\n"
    )
    temp_records = []
    for t in partial_files:
        file_prefix = t.split("\\")
        file_prefix = file_prefix[len(file_prefix) - 1].replace(".txt", "")
        if file_prefix in large_prefix_set:
            prefix_length = prefix_length + 1
            prefix_counts = {}  # ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
            prefixes_set = set()
            prefix_list = []
            prefix_chunks = {}
            sorted_chunk = []
            import os

            d = open(t)
            for current_record in d:
                prefixes_set.add(current_record[0:prefix_length])
                if current_record[0:prefix_length] in prefix_counts:
                    prefix_counts[current_record[0:prefix_length]] = prefix_counts[current_record[0:prefix_length]] + 1
                else:
                    prefix_counts[current_record[0:prefix_length]] = 1
            d.close()
            for current_record in prefixes_set:
                prefix_list.append(current_record)
            prefix_list.sort()
            chunk_size = 0
            chunk_number = 1
            for current_record in prefix_list:
                chunk_size = prefix_counts[current_record] + chunk_size
                if chunk_size <= max_memory_sort_size:
                    prefix_chunks[current_record] = chunk_number
                else:
                    chunk_number = chunk_number + 1
                    chunk_size = prefix_counts[current_record]
                    prefix_chunks[current_record] = chunk_number
            for current_record in range(prefix_chunks[prefix_list[0]], prefix_chunks[prefix_list[len(prefix_list) - 1]] + 1):
                d = open(t)
                for chunk_record in d:
                    if prefix_chunks[chunk_record[0:prefix_length]] == current_record:
                        sorted_chunk.append(chunk_record)
                d.close()
                sorted_chunk.sort()
                for sorted_record in sorted_chunk:
                    sorted_output_file.write(sorted_record)
                sorted_chunk = []
            os.remove(t)
            prefixes_set = set()
            prefix_list = []
            prefix_chunks = {}
            prefix_counts = {}
        else:
            d = open(t)
            for temp_record in d:
                temp_records.append(temp_record)
            d.close()
            temp_records.sort()
            for temp_record in temp_records:
                sorted_output_file.write(temp_record)
            temp_records = []
            os.remove(t)
    sorted_output_file.close()  # ordenar - fim
    g = open(base_path + cdr_database + "ord4.txt", "r")
    month = ""
    year = ""
    operator_id  = "0"
    for current_record in g:
        record_parts = current_record.split(";")
        if (record_parts[4] == "ORI" or record_parts[4] == "TER") and record_parts[7] != "":
            ii21 = record_parts[2].split("-")
            ii61 = record_parts[7].split("-")
            month = ii21[1]
            year = ii21[0]
            operator_id  = ii61[1][0:2]
            break
    g.close()
    if voice_record_flag == 0:
        resolved_operator = operator_code
    else:
        resolved_operator = opid[operator_id ]
    os.rename(
        base_path + cdr_database + "ord4.txt",
        base_path + "VozEricsson" + "-" + cdr_database + "-" + resolved_operator + "-" + month + year + ".txt",
    )

    if len(glob.glob(base_path + "Arqparciais" + cdr_database)) == 1:
        shutil.rmtree(base_path + "Arqparciais" + cdr_database)
    if len(glob.glob(base_path + "Auxiliar" + cdr_database)) == 1:
        shutil.rmtree(base_path + "Auxiliar" + cdr_database)

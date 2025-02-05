import glob
import os
import shutil
import subprocess
import sys
import time
import zipfile
from datetime import datetime

current_directory = os.getcwd()


lim1 = glob.glob(current_directory + "/arqli*")
for i in lim1:
    os.remove(i)

selection_option = "5"
print("Tipos de CDRs que podem ser lidos:")
print()
print("1 - Voz (Vivo ou Tim ou Claro-Ericsson)")
print("2 - Voz (Claro-Nokia)")
print("3 - Voz - Oi")
print("4 - Voz (Nextel ou Sercomtel) (Huawei)")
print("5 - Voz - Algar")
print("6 - Dados - qualquer operadora")
print("7 - Volte 3gpp")
print("8 - Volte não 3gpp (Tim)")
print("9 - Volte não 3gpp (Claro)")
print("10 - Stir (Tim)")
print()
output_format_option = ""
cdr_type_selection = ""
attempt_counter = 0
retry_counter = 0

file_format_type = "nada"
valid_cdr_types = [
    "1",
    "2",
    "3",
    "4",
    "1i",
    "5",
    "5i",
    "6",
    "7",
    "8",
    "9",
    "10",
    "10i",
    "21",
]
telecom_operators = [
    "vivo",
    "claro",
    "tim",
    "oi",
    "nextel",
    "sercomtel",
    "algar",
    "ctbc",
]

while len(cdr_type_selection) != 2 and attempt_counter < 4:
    print(
        "Informe um número entre 1 e 9 para indicar o tipo de CDR a ser lido, acompanhado por uma letra conforme abaixo."
    )
    print("      - 'u' para apresentação do resultado em arquivo único (ex.: 2u)")
    print(
        "      - 'i' para resultado em arquivos individuais (um arquivo para cada arquivo bruto; ex.: 4i)"
    )
    print(
        "      - 'n' para arquivos separados por faixas de numeração dos acessos originadores (ex.: 3n)"
    )
    print("      - 'd' para arquivos separados por data-hora (ex.: 5d)")
    print("AGUARDANDO...:", end="")
    cdr_type_selection = input()

    attempt_counter = attempt_counter + 1
    file_format_type = cdr_type_selection[-1:]
    if file_format_type != "i":
        output_format_option = "a"

    if cdr_type_selection[0:2] == "10" and len(cdr_type_selection) == 3:
        break
cdr_type_selection = cdr_type_selection[:-1]

if cdr_type_selection in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
    print()

    print(
        "Informe o caminho para leitura dos CDRs brutos (para a leitura de todos os arquivos, finalize com /*.gz). Caso os arquivos .gz estejam compactados em pastas .zip, finalize com /*.zip ao invés de /*.gz. "
    )
    print("AGUARDANDO...:", end="")
    raw_cdr_path = input()
    raw_cdr_path = raw_cdr_path.replace("'", "").replace('"', "").replace("/", "\\")
    input_files = glob.glob(raw_cdr_path)
    gz_file_found = zip_file_found = 0
    if raw_cdr_path[-3:] == "zip":
        zip_error_flag = 0
        for tu in input_files:
            try:
                zip_archive_handle = zipfile.ZipFile(tu)
            except Exception:
                print("Falha pasta", tu)
                zip_error_flag = 1

            zip_archive_handle.close()

        if zip_error_flag == 1:
            print()
            b80 = input('Para interromper, tecle "p" e depois "Enter" ')
            if b80 == "p":
                sys.exit()

        print(raw_cdr_path)
        zip_file_found = 1

    for vz1 in input_files:
        if vz1[-2:] == "gz":
            gz_file_found = 1
            break

    print()

    while gz_file_found == 0 and zip_file_found == 0 and retry_counter < 3:
        print()
        print("Não foram localizados arquivos para leitura.")
        print("Reveja o caminho informado.")
        raw_cdr_path = input(
            "Informe o caminho para leitura dos CDRs brutos. AGUARDANDO...:"
        )

        raw_cdr_path = raw_cdr_path.replace("'", "").replace('"', "").replace("/", "\\")
        input_files = glob.glob(raw_cdr_path)
        gz_file_found = zip_file_found = 0
        if raw_cdr_path[-3:] == "zip":
            zip_file_found = 1

        for vz1 in input_files:
            if vz1[-2:] == "gz":
                gz_file_found = 1
                break

        print()
        retry_counter = retry_counter + 1

    operator_name = ""
    eb = raw_cdr_path.lower()
    for tu in telecom_operators:
        if eb.find(tu + "\\") != -1:
            operator_name = tu
            break
    if operator_name == "":
        print("- Informe o nome da operadora da qual os CDRs brutos serão lidos.")
        print("AGUARDANDO...:", end="")
        operator_name = input()
    operator_name = operator_name.upper()

    if len(input_files) != 0:
        total_input_files = str(len(input_files))
        print()
        print("Quantidade de arquivos para leitura:", len(input_files))
        print()
        print(
            "Estimativa para conclusão da leitura:",
            len(input_files) * 0.3 / 1000,
            "horas",
        )
        print()

        timestamp = time.asctime().replace(":", "").replace(" ", "")
        print("Caminho para salvar o arquivo resultado (CDRs lidos):")
        print(
            'Tecle "Enter" para salvar o resultado nesta máquina ('
            + current_directory
            + "\\Resultados\\), ou indique o caminho desejado."
        )
        print("AGUARDANDO...:", end="")
        output_directory = input()
        output_directory = (
            output_directory.replace("'", "").replace('"', "").replace("/", "\\")
        )
        execution_timestamp = (
            str(datetime.now())
            .replace("\n", "")
            .replace(".", "")
            .replace(":", "")
            .replace(" ", "")
            .replace("-", "")
        )
        if output_directory == "":
            output_directory = current_directory + "\\Resultados\\"
        else:
            if output_directory[-1:] != "\\":
                output_directory = output_directory + "\\"
        print("Resultado em:", output_directory)

        if zip_file_found == 1:
            print("DESCOMPACTANDO...")

            input_path_components = raw_cdr_path.split("\\")
            zip_filename = input_path_components[len(input_path_components) - 1]
            cdr_extract_base_path = raw_cdr_path.replace(zip_filename, "")

            os.mkdir(cdr_extract_base_path + "descomp")

            zip_entry_counter = 0
            entry_processed_flag = 0
            total_zip_entries = 0
            zip_file_counter = 0
            print(len(input_files))
            extracted_paths_set = set()
            extracted_paths_list = []
            for z2 in input_files:
                zip_file_counter = zip_file_counter + 1

                try:
                    zip_archive_handle = zipfile.ZipFile(z2)
                except Exception:
                    print("falha pasta", z2)

                total_zip_entries = (
                    total_zip_entries + len(zip_archive_handle.namelist()) - 1
                )

                zip_entry_path = (zip_archive_handle.namelist()[0]).replace("../", "")
                path_components = (zip_entry_path).split("/")
                extracted_paths_list.append(zip_entry_path)

                extracted_path = ""
                for zd in range(len(path_components) - 1):
                    extracted_path = extracted_path + "\\*"
                extracted_paths_set.add(extracted_path)

                for zip_entry_name in zip_archive_handle.namelist():
                    zip_entry_counter = zip_entry_counter + 1
                    if zip_entry_counter > 1:
                        entry_processed_flag = 1

                    if entry_processed_flag == 1:
                        entry_components = zip_entry_name.split("/")

                        try:
                            zip_archive_handle.extract(
                                zip_entry_name, cdr_extract_base_path + "descomp"
                            )
                        except Exception:
                            print("falha arquivo", zip_entry_name)

            if len(extracted_paths_set) == 1:
                raw_cdr_path = (
                    cdr_extract_base_path + "descomp" + extracted_path + "\\*.gz"
                )
            else:
                for zu in extracted_paths_list:
                    current_range = zu.split("/")
                    if len(current_range) > 2:
                        zu3 = zu[:-1].replace("/", "\\")
                        shutil.move(
                            cdr_extract_base_path + "descomp\\" + zu3,
                            cdr_extract_base_path
                            + "descomp\\"
                            + current_range[len(current_range) - 1],
                        )

                raw_cdr_path = cdr_extract_base_path + "descomp\\*\\*.gz"


print()
print()

if file_format_type == "i":
    print(
        "=/= Os arquivos individuais estarão na pasta:",
        operator_name + execution_timestamp,
    )


print()
print("O percentual de execução pode ser acompanhado conforme a seguir:.......")
print()


current_directory = os.getcwd()

start_time = datetime.now()
print()
print("Início de leitura...", start_time)
print()
process_count = 2
accumulated_count = 0
duration_counter = 0

cdr_type = cdr_type_selection

volte_cdr_type = ""
if cdr_type_selection == "8":
    volte_cdr_type = cdr_type_selection
    cdr_type = "1"

parallel_processes = 5
progress_percentage = 5
print(output_format_option, operator_name)

processed_files_log = open("arquivosparaleitura.txt", "w")
failed_files_log = open("arquivosnaolidos.txt", "w")
processed_files_set = set()
failed_files_set = set()
cdr_type_name = ""
voice_cdr_types = ["1", "2", "3", "4", "5"]


vac1 = output_format_option
zip_directories = set()
input_file_list = glob.glob(raw_cdr_path)


vendor_name = ""
if cdr_type == "1":
    vendor_name = "Ericsson"
if cdr_type == "2":
    vendor_name = "Nokia"


if cdr_type in voice_cdr_types:
    cdr_type_name = "Voz" + vendor_name
if cdr_type == "6":
    cdr_type_name = "Dados"
if volte_cdr_type == "8" or cdr_type == "9" or cdr_type == "7":
    cdr_type_name = "Volte"
if cdr_type == "10":
    cdr_type_name = "Stir"
if output_format_option == "a":
    consolidated_output_path = (
        output_directory
        + operator_name
        + "-"
        + cdr_type_name
        + execution_timestamp[0:12]
        + ".txt"
    )

    if cdr_type in voice_cdr_types or file_format_type == "u":
        consolidated_output_file = open(consolidated_output_path, "w")
    if cdr_type == "6":
        if file_format_type == "u":
            consolidated_output_file.write(
                "Tipo de CDR"
                + ";"
                + "listOfTrafficVolumes"
                + ";"
                + "Location"
                + ";"
                + "servedMSISDN"
                + ";"
                + "listOfServiceData"
                + ";"
                + "recordSequenceNumber"
                + ";"
                + "CauseforRecClosing"
                + ";"
                + "ChargingID"
                + ";"
                + "duration"
                + ";"
                + "ggsnAddress"
                + ";"
                + "OpenningTime;StartTime;Diagnostics;Radio;ServedIMSI;;IMEI;Arquivo"
                + "\n"
            )
        else:
            os.mkdir(
                output_directory + operator_name + execution_timestamp + cdr_type_name
            )
    if cdr_type == "7":
        if file_format_type == "u":
            consolidated_output_file.write(
                "Originador(list-Of-Calling-Party-Address);Data(recordOpeningTime);Hora;TipodeCDR(role-of-Node);called-Party-Address(NúmeroChamado);dialled-Party-Address(NúmeroTeclado);List-Of-Called-Asserted-Identity;Duration;Célula(accessNetworkInformation);IMSI(List-of-Subscription-ID);IMEI(private-User-Equipment-Info);MSC-Number;network-Call-Reference;causeForRecordClosing;interOperatorIdentifiers;sIP-Method\n"
            )
        else:
            os.mkdir(
                output_directory + operator_name + execution_timestamp + cdr_type_name
            )

    if cdr_type == "10":
        if file_format_type == "u":
            consolidated_output_file.write(
                "Originador(list-Of-Calling-Party-Address);Data(recordOpeningTime);Hora;TipodeCDR(role-of-Node);called-Party-Address(NúmeroChamado);dialled-Party-Address(NúmeroTeclado);List-Of-Called-Asserted-Identity;Duration;Célula(accessNetworkInformation);IMSI(List-of-Subscription-ID);IMEI(private-User-Equipment-Info);MSC-Number;network-Call-Reference;causeForRecordClosing;interOperatorIdentifiers;sIP-Method\n"
            )
        else:
            os.mkdir(
                output_directory + operator_name + execution_timestamp + cdr_type_name
            )

    if cdr_type == "9":
        if file_format_type == "u":
            consolidated_output_file.write(
                "Data;Hora;Originador;TipoCDR;NúmeroChamado;Duração;Célula\n"
            )
        else:
            os.mkdir(
                output_directory + operator_name + execution_timestamp + cdr_type_name
            )

    if cdr_type in voice_cdr_types and file_format_type != "u":
        os.mkdir(output_directory + operator_name + execution_timestamp + cdr_type_name)
else:
    os.mkdir(output_directory + operator_name + execution_timestamp)
    for i in input_file_list:
        ii = i.split("\\")
        zip_directories.add(ii[len(ii) - 2])
    for i in zip_directories:
        os.mkdir(output_directory + operator_name + execution_timestamp + "\\" + i)


for i15 in range(1, parallel_processes + 1):
    npc = str(i15)

    pp = "pp" + npc

    if cdr_type == "7":
        pp = subprocess.Popen(
            [
                "python",
                current_directory + "\\Volte3gpp.py",
                npc,
                output_format_option,
                operator_name,
                output_directory,
                execution_timestamp,
                raw_cdr_path,
                str(parallel_processes),
                selection_option,
            ]
        )

    if cdr_type == "10":
        pp = subprocess.Popen(
            [
                "python",
                current_directory + "\\stirtim.py",
                npc,
                output_format_option,
                operator_name,
                output_directory,
                execution_timestamp,
                raw_cdr_path,
                str(parallel_processes),
                selection_option,
            ]
        )

    if cdr_type == "9":
        pp = subprocess.Popen(
            [
                "python",
                current_directory + "\\VolteClaro.py",
                npc,
                output_format_option,
                operator_name,
                output_directory,
                execution_timestamp,
                raw_cdr_path,
                str(parallel_processes),
                selection_option,
            ]
        )

    if cdr_type == "6":
        pp = subprocess.Popen(
            [
                "python",
                current_directory + "\\cdrDados.py",
                npc,
                output_format_option,
                operator_name,
                output_directory,
                execution_timestamp,
                raw_cdr_path,
                str(parallel_processes),
                selection_option,
            ]
        )

    if cdr_type == "1":
        pp = subprocess.Popen(
            [
                "python",
                current_directory + "\\cdrVozEricsson.py",
                npc,
                output_format_option,
                operator_name,
                output_directory,
                execution_timestamp,
                raw_cdr_path,
                str(parallel_processes),
                selection_option,
                volte_cdr_type,
            ]
        )
    if cdr_type == "4":
        pp = subprocess.Popen(
            [
                "python",
                current_directory + "\\rodahuawei.py",
                npc,
                output_format_option,
                operator_name,
                output_directory,
                execution_timestamp,
                raw_cdr_path,
                str(parallel_processes),
                selection_option,
            ]
        )
    if cdr_type == "2" or cdr_type == "3" or cdr_type == "5":
        pp = subprocess.Popen(
            [
                "python",
                current_directory + "\\cdrVozNokia.py",
                npc,
                output_format_option,
                operator_name,
                output_directory,
                execution_timestamp,
                raw_cdr_path,
                str(parallel_processes),
                selection_option,
                cdr_type,
            ]
        )

opera = ""

breakpoint()

processed_count = 0
file_count = 0
processed_list = []
not_processed_list = []


total_files_processed = 0
current_files_processed = 0


checkpoint_counter = 0

processed_ranges = set()
range_files_dict = {}
range_counter = 0

print(len(input_file_list))
progress_checkpoint = int(len(input_file_list) * progress_percentage / 100)
next_checkpoint = progress_checkpoint

if output_format_option == "a":
    range_batch_number = 0
    number_ranges_set = set()
    nr11 = ""
    range_file_counter = 0
    while current_files_processed != len(input_file_list):
        consolidated_output_files = glob.glob(
            output_directory + "f" + execution_timestamp + "*"
        )
        try:
            for z2 in consolidated_output_files:
                input_file_handle = open(z2)

                if file_format_type == "u" or cdr_type in voice_cdr_types:
                    for y2 in input_file_handle:
                        consolidated_output_file.write(y2)

                    input_file_handle.close()

                if cdr_type == "6" and (
                    file_format_type == "n"
                    or file_format_type == "d"
                    or file_format_type == "nada"
                ):
                    range_counter = 0

                    for y2 in input_file_handle:
                        cdr_fields = y2.split(";")
                        if file_format_type == "d":
                            range_identifier = (
                                cdr_fields[11][0:13].replace("/", "-").replace(" ", "-")
                            )
                            if cdr_fields[11] == "":
                                if cdr_fields[10] == "":
                                    range_identifier = "semdata"
                                else:
                                    range_identifier = (
                                        cdr_fields[10][0:13]
                                        .replace("/", "-")
                                        .replace(" ", "-")
                                    )
                        else:
                            range_identifier = (cdr_fields[3].replace("f", ""))[-11:][
                                0:4
                            ]

                            if cdr_fields[3] == "":
                                range_identifier = "semnumero"

                        if range_identifier + nr11 not in processed_ranges:
                            range_counter = range_counter + 1
                            range_output_file = str(range_counter)
                            range_output_file = open(
                                output_directory
                                + operator_name
                                + execution_timestamp
                                + cdr_type_name
                                + "\\"
                                + range_identifier
                                + nr11
                                + ".txt",
                                "w",
                            )
                            range_output_file.write(
                                "TipodeCDR"
                                + ";"
                                + "listOfTrafficVolumes"
                                + ";"
                                + "Location"
                                + ";"
                                + "servedMSISDN"
                                + ";"
                                + "listOfServiceData"
                                + ";"
                                + "recordSequenceNumber"
                                + ";"
                                + "CauseforRecClosing"
                                + ";"
                                + "ChargingID"
                                + ";"
                                + "duration"
                                + ";"
                                + "ggsnAddress"
                                + ";"
                                + "OpenningTime;StartTime;Diagnostics;Radio;ServedIMSI;;IMEI;Arquivo"
                                + "\n"
                            )
                            processed_ranges.add(range_identifier + nr11)
                            range_files_dict[range_identifier + nr11] = (
                                range_output_file
                            )

                            number_ranges_set.add(range_identifier)

                        if range_identifier + nr11 in processed_ranges:
                            if 4 > 3:
                                try:
                                    range_files_dict[range_identifier + nr11].write(y2)
                                except OSError:
                                    range_files_dict[range_identifier + nr11].write(y2)

                    input_file_handle.close()
                    if len(range_files_dict) > 7999:
                        range_batch_number = range_batch_number + 1
                        nr11 = "-" + str(range_batch_number)
                        for current_range in range_files_dict:
                            range_files_dict[current_range].close()

                if (cdr_type == "9") and (
                    file_format_type == "n"
                    or file_format_type == "d"
                    or file_format_type == "nada"
                ):
                    range_counter = 0

                    for y2 in input_file_handle:
                        cdr_fields = y2.split(";")
                        if file_format_type == "d":
                            range_identifier = cdr_fields[0] + "-" + cdr_fields[1][0:2]
                            if cdr_fields[0] == "":
                                if cdr_fields[7] == "":
                                    range_identifier = "semdata"
                                else:
                                    range_identifier == cdr_fields[
                                        7
                                    ] + "-" + cdr_fields[8][0:2]
                        else:
                            if len(cdr_fields[2]) > 9:
                                if cdr_fields[2][0:2] == "55" and (
                                    len(cdr_fields[2].replace("f", "")) == 12
                                    or len(cdr_fields[2].replace("f", "")) == 13
                                ):
                                    range_identifier = cdr_fields[2][2:6]
                                else:
                                    if len(cdr_fields[2].replace("f", "")) == 10:
                                        range_identifier = cdr_fields[2][0:4]
                                    else:
                                        range_identifier = (
                                            cdr_fields[2].replace("f", "")
                                        )[-11:][0:4]

                            if cdr_fields[2] == "":
                                range_identifier = "semnumero"

                        if range_identifier + nr11 not in processed_ranges:
                            range_counter = range_counter + 1
                            range_output_file = str(range_counter)
                            range_output_file = open(
                                output_directory
                                + operator_name
                                + execution_timestamp
                                + cdr_type_name
                                + "\\"
                                + range_identifier
                                + nr11
                                + ".txt",
                                "w",
                            )
                            range_output_file.write(
                                "Data;Hora;Originador;TipoCDR;NúmeroChamado;Duração;Célula\n"
                            )
                            processed_ranges.add(range_identifier + nr11)
                            range_files_dict[range_identifier + nr11] = (
                                range_output_file
                            )

                            number_ranges_set.add(range_identifier)

                        if range_identifier + nr11 in processed_ranges:
                            if 4 > 3:
                                range_files_dict[range_identifier + nr11].write(y2)

                    input_file_handle.close()
                    if len(range_files_dict) > 7999:
                        range_batch_number = range_batch_number + 1
                        nr11 = "-" + str(range_batch_number)
                        for current_range in range_files_dict:
                            range_files_dict[current_range].close()

                if (cdr_type == "7" or cdr_type == "10") and (
                    file_format_type == "n"
                    or file_format_type == "d"
                    or file_format_type == "nada"
                ):
                    range_counter = 0

                    for y2 in input_file_handle:
                        cdr_fields = y2.split(";")
                        if file_format_type == "d":
                            range_identifier = cdr_fields[1] + "-" + cdr_fields[2][0:2]
                            if cdr_fields[1] == "":
                                range_identifier = "semdata"

                        else:
                            if len(cdr_fields[0]) > 9:
                                if cdr_fields[0][0:2] == "55" and (
                                    len(cdr_fields[0].replace("F", "")) == 12
                                    or len(cdr_fields[0].replace("F", "")) == 13
                                ):
                                    range_identifier = cdr_fields[0][2:6]
                                else:
                                    if len(cdr_fields[0].replace("F", "")) == 10:
                                        range_identifier = cdr_fields[0][0:4]

                                    else:
                                        range_identifier = (
                                            cdr_fields[0].replace("F", "")
                                        )[-11:][0:4]

                            else:
                                if cdr_fields[0] == "":
                                    range_identifier = "semnumero"
                                else:
                                    range_identifier = "poucosdigitos"

                        if range_identifier + nr11 not in processed_ranges:
                            range_counter = range_counter + 1
                            range_output_file = str(range_counter)

                            range_output_file = open(
                                output_directory
                                + operator_name
                                + execution_timestamp
                                + cdr_type_name
                                + "\\"
                                + range_identifier
                                + nr11
                                + ".txt",
                                "w",
                            )
                            range_output_file.write(
                                "Originador(list-Of-Calling-Party-Address);Data(recordOpeningTime);Hora;TipodeCDR(role-of-Node);called-Party-Address(NúmeroChamado);dialled-Party-Address(NúmeroTeclado);List-Of-Called-Asserted-Identity;Duration;Célula(accessNetworkInformation);IMSI(List-of-Subscription-ID);IMEI(private-User-Equipment-Info);MSC-Number;network-Call-Reference;causeForRecordClosing;interOperatorIdentifiers;sIP-Method\n"
                            )
                            processed_ranges.add(range_identifier + nr11)
                            range_files_dict[range_identifier + nr11] = (
                                range_output_file
                            )

                            number_ranges_set.add(range_identifier)

                        if range_identifier + nr11 in processed_ranges:
                            if 4 > 3:
                                range_files_dict[range_identifier + nr11].write(y2)

                    input_file_handle.close()
                    if len(range_files_dict) > 7999:
                        range_batch_number = range_batch_number + 1
                        nr11 = "-" + str(range_batch_number)

                        for current_range in range_files_dict:
                            range_files_dict[current_range].close()

                not_processed_marker = z2.find("N.txt")
                if not_processed_marker != -1:
                    not_processed_list.append(z2)

                os.remove(z2)
                current_files_processed = current_files_processed + 1
                checkpoint_counter = checkpoint_counter + 1

                if checkpoint_counter == progress_checkpoint:
                    print(
                        str(int(current_files_processed * 100 / len(input_file_list)))
                        + "%"
                    )
                    checkpoint_counter = 0

        except PermissionError:
            pass
        except FileNotFoundError:
            pass

    for zu in range_files_dict:
        range_files_dict[zu].close()

    if nr11 != "":
        for z11 in number_ranges_set:
            t53 = glob.glob(
                output_directory
                + operator_name
                + execution_timestamp
                + cdr_type_name
                + "\\"
                + z11
                + "*"
            )

            ve15 = 0
            for z12 in t53:
                ve15 = ve15 + 1
                if ve15 == 1:
                    main_range_file = open(z12, "a")
                    range_file_path = z12
                else:
                    temp_range_file = open(z12)
                    temp_range_file.readline()
                    for z13 in temp_range_file:
                        main_range_file.write(z13)
                    temp_range_file.close()
                    os.remove(z12)
            main_range_file.close()
            file_parts = range_file_path.split("-")

            range_number = file_parts[len(file_parts) - 1].replace(".txt", "")

            base_filename = range_file_path.replace("-" + range_number, "")
            os.rename(range_file_path, base_filename)

    if cdr_type in voice_cdr_types or file_format_type == "u":
        consolidated_output_file.close()
    for failed_file_path in not_processed_list:
        failed_file_path = (failed_file_path.split(";"))[1].replace("N.txt", "")
        failed_files_log.write(failed_file_path + "\n")
        print()
        print()
        print(
            'Não lido ou lido parcialmente (veja arquivos "arquivosnaolidos" e "arquivosparaleitura"):'
        )
        print(failed_file_path)
else:
    individual_output_files = glob.glob(
        output_directory + operator_name + execution_timestamp + "\\*\\*f*.txt"
    )
    aca3 = len(individual_output_files)
    while len(individual_output_files) != len(input_file_list):
        individual_output_files = glob.glob(
            output_directory + operator_name + execution_timestamp + "\\*\\*f*.txt"
        )

        if len(individual_output_files) > aca3:
            if len(individual_output_files) > next_checkpoint:
                print(
                    str(int(len(individual_output_files) * 100 / len(input_file_list)))
                    + "%",
                    end=" ",
                )
                next_checkpoint = len(individual_output_files) + progress_checkpoint
        aca3 = len(individual_output_files)
    for pj in individual_output_files:
        pj1 = pj.find("N.txt")
        if pj1 != -1:
            failed_files_log.write(pj)
            print()
            print()
            print(
                'Não lido ou lido parcialmente (veja arquivos "arquivosnaolidos" e "arquivosparaleitura"):'
            )
            print(pj)
file_sequence = 0
for pz in input_file_list:
    file_sequence = file_sequence + 1
    processed_files_log.write(str(file_sequence) + ";" + pz + "\n")
processed_files_log.close()
failed_files_log.close()
print()
print("Duração da leitura: ", datetime.now() - start_time)
print()
consolidation_start_time = datetime.now()
if vac1 == "a" and cdr_type in voice_cdr_types:
    print("Início de consolidação e ordenação...", consolidation_start_time)
    print()
    if cdr_type == "1":
        p = subprocess.call(
            [
                "python",
                "cdrEricssonVozOrdenaAglutina.py",
                output_directory,
                execution_timestamp,
                operator_name,
                consolidated_output_path,
            ]
        )

    if cdr_type == "2" or cdr_type == "3" or cdr_type == "5":
        p = subprocess.call(
            [
                "python",
                current_directory + "\\cdrNokiaVozOrdenaAglutina.py",
                output_directory,
                execution_timestamp,
                operator_name,
                consolidated_output_path,
            ]
        )
    if cdr_type == "4":
        p = subprocess.call(
            [
                "python",
                "cdrHuaweiVozOrdenaAglutina.py",
                output_directory,
                execution_timestamp,
                operator_name,
                consolidated_output_path,
            ]
        )


if (
    output_format_option == "a"
    and cdr_type in voice_cdr_types
    and file_format_type == "u"
):
    print(
        "Duração da consolidação e ordenação: ",
        datetime.now() - consolidation_start_time,
    )
    print()
    print("Duração total: ", datetime.now() - start_time)


if (
    cdr_type in voice_cdr_types
    and (
        file_format_type == "n" or file_format_type == "d" or file_format_type == "nada"
    )
    and output_format_option == "a"
):
    print(
        "Duração da consolidação e ordenação: ",
        datetime.now() - consolidation_start_time,
    )
    print()
    print("Início da redistribuição de CDRs nos tipos escolhidos de arquivos de saída")

    consolidated_output_files = glob.glob(
        output_directory + "Voz*" + execution_timestamp + "*"
    )
    if len(consolidated_output_files) == 1:
        range_identifier = ""
        processed_ranges = set()
        range_files_dict = {}
        range_counter = 0
        processing_batch_counter = 0
        number_ranges_set = set()
        processing_complete_flag = 1
        processed_ranges_set = set()
        processed_ranges_counter = 0
        while processing_complete_flag == 1:
            input_file_handle = open(consolidated_output_files[0])

            input_file_handle.readline()
            processed_ranges = set()
            range_files_dict = {}
            range_counter = 0
            range_identifier = ""
            msisdn_field = ""
            for y2 in input_file_handle:
                cdr_fields = y2.split(";")
                if file_format_type == "d":
                    if cdr_type == "2" or cdr_type == "3" or cdr_type == "5":
                        range_identifier = (
                            cdr_fields[3][0:13].replace("/", "-").replace(" ", "-")
                        )
                        if cdr_fields[3] == "":
                            range_identifier = "semdata"
                    if cdr_type == "1":
                        range_identifier = (
                            cdr_fields[2].replace("/", "-").replace(" ", "-")
                            + "-"
                            + cdr_fields[3][0:2]
                        )
                        if cdr_fields[2] == "":
                            range_identifier = "semdata"
                    if cdr_type == "4":
                        range_identifier = (
                            cdr_fields[2][0:13].replace("/", "-").replace(" ", "-")
                        )
                        if cdr_fields[2] == "":
                            range_identifier = "semdata"
                else:
                    if cdr_type == "2" or cdr_type == "3" or cdr_type == "5":
                        msisdn_field = cdr_fields[7].replace("f", "")
                        if len(msisdn_field) > 9:
                            if msisdn_field[0:2] == "55" and (
                                len(msisdn_field) == 12 or len(msisdn_field) == 13
                            ):
                                range_identifier = msisdn_field[2:6]
                            else:
                                if len(msisdn_field) == 10:
                                    range_identifier = msisdn_field[0:4]
                                else:
                                    range_identifier = (msisdn_field)[-11:][0:4]

                        else:
                            if msisdn_field == "":
                                range_identifier = "semnumero"
                            else:
                                range_identifier = "poucosdigitos"

                    if cdr_type == "1":
                        msisdn_field = cdr_fields[1].replace("f", "")
                        if len(msisdn_field) > 9:
                            if msisdn_field[0:2] == "55" and (
                                len(msisdn_field) == 12 or len(msisdn_field) == 13
                            ):
                                range_identifier = msisdn_field[2:6]
                            else:
                                if len(msisdn_field) == 10:
                                    range_identifier = msisdn_field[0:4]
                                else:
                                    range_identifier = (msisdn_field)[-11:][0:4]

                        else:
                            if msisdn_field == "":
                                range_identifier = "semnumero"
                            else:
                                range_identifier = "poucosdigitos"

                    if cdr_type == "4":
                        msisdn_field = cdr_fields[3].replace("f", "")
                        if len(msisdn_field) > 9:
                            if msisdn_field[0:4] == "1955" and (
                                len(msisdn_field) == 14 or len(msisdn_field) == 15
                            ):
                                range_identifier = msisdn_field[4:8]
                            else:
                                if len(msisdn_field) == 10:
                                    range_identifier = msisdn_field[0:4]
                                else:
                                    range_identifier = (msisdn_field)[-11:][0:4]

                        else:
                            if msisdn_field == "":
                                range_identifier = "semnumero"
                            else:
                                range_identifier = "poucosdigitos"

                if (
                    len(processed_ranges) < 8000
                    and range_identifier not in processed_ranges_set
                ):
                    if range_identifier not in processed_ranges:
                        range_counter = range_counter + 1
                        range_output_file = str(range_counter)
                        range_output_file = open(
                            output_directory
                            + operator_name
                            + execution_timestamp
                            + cdr_type_name
                            + "\\"
                            + range_identifier
                            + ".txt",
                            "w",
                        )
                        if cdr_type == "1":
                            range_output_file.write(
                                "Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;IMSI;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto"
                                + "\n"
                            )
                        if cdr_type == "2" or cdr_type == "3" or cdr_type == "5":
                            range_output_file.write(
                                "TipodeCDR"
                                + ";"
                                + "Exch_id"
                                + ";"
                                + "Referencia"
                                + ";"
                                + "DataAloc.Canal"
                                + ";"
                                + "TecnologiaCelula-MCC-MNC"
                                + ";"
                                + "LAC"
                                + ";"
                                + "1stCellA"
                                + ";"
                                + "Origem"
                                + ";"
                                + "Destino"
                                + ";"
                                + "PMM"
                                + ";"
                                + "Inter_Charg_Ind"
                                + ";"
                                + "IMSI"
                                + ";"
                                + "NumeroDig."
                                + ";"
                                + "NumeroConec."
                                + ";"
                                + "CausaTerm."
                                + ";"
                                + "TTC"
                                + ";"
                                + "DataCharg"
                                + ";"
                                + "DataReferencia"
                                + ";"
                                + "IMEI"
                                + ";"
                                + "TAT"
                                + ";"
                                + "ChrgType"
                                + ";"
                                + "Routing_Category"
                                + ";"
                                + "Cause_for_Forwarding"
                                + ";"
                                + "Arquivo"
                                + "\n"
                            )
                        if cdr_type == "4":
                            range_output_file.write(
                                "TipodeCDR;ReferenciadeRede;DataHora;Origem;Destino;Duracao;Causefortermination;Diagnóstico;Célula;ReferenciaCentral;Atendimento;Ocupaçãocanaltráfego;Arquivo"
                                + "\n"
                            )
                        processed_ranges.add(range_identifier)
                        range_files_dict[range_identifier] = range_output_file

                        processed_ranges_set.add(range_identifier)

                if range_identifier in range_files_dict:
                    range_files_dict[range_identifier].write(y2)

                if processing_batch_counter == 0:
                    number_ranges_set.add(range_identifier)

            input_file_handle.close()
            processing_batch_counter = processing_batch_counter + 1

            for z in range_files_dict:
                range_files_dict[z].close()
                processed_ranges_counter = processed_ranges_counter + 1

            if len(number_ranges_set) == processed_ranges_counter:
                processing_complete_flag = 0

        range_identifier = ""
        processed_ranges = set()
        range_files_dict = {}
        range_counter = 0
        processing_batch_counter = 0
        number_ranges_set = set()
        processing_complete_flag = 1
        processed_ranges_set = set()
        processed_ranges_counter = 0

        os.remove(consolidated_output_files[0])

    else:
        print("Não foi identificado arquivo para separação")
        print()
if zip_file_found == 1:
    print("Excluindo descompactação...")
    shutil.rmtree(cdr_extract_base_path + "descomp")

print("Processamento encerrado.")
if cdr_type in voice_cdr_types and (file_format_type == "n" or file_format_type == "d"):
    print()
    print("Duração total:", datetime.now() - start_time)
    print()

completion_marker_file = open(
    output_directory + operator_name + execution_timestamp + cdr_type_name + "FIM.txt",
    "w",
)
completion_marker_file.close()

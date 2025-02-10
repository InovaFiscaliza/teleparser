import glob
import os
import shutil
import sys
import time
from datetime import datetime
from operator import itemgetter

diret = os.getcwd() + "\\"
max_memory_sort_size = 6000000  # tamanho máximo a ordenar na memória (trecho: ordenar)
max_file_sort_size = 5000000  # tamanho máximo de arquivo a ser ordenado de uma vez na memória (trecho: ordenar)
base_path = sys.argv[1]
cdr_database = sys.argv[2]
operator_code = sys.argv[3]
input_file_path = sys.argv[4]
original_input_file = input_file_path
prefix_length = 15

timestamp = time.asctime().replace(":", "").replace(" ", "")
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
for i in d:
    if i[0:3] == "ORI" or i[0:3] == "TER":
        voice_record_flag = 1
        record_count = record_count + 1
        if i[0:prefix_length] in prefix_counts:
            prefix_counts[i[0:prefix_length]] = prefix_counts[i[0:prefix_length]] + 1
        else:
            prefix_counts[i[0:prefix_length]] = 1
    else:
        jj = i.split(";")
        j2 = jj[11].split(":")
        try:
            duration_seconds = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])
        except ValueError:
            if jj[11] == "":
                duration_seconds = 0

        da2 = "20" + jj[3].replace("/", "-")
        datetime_string = da2 + ";" + jj[4]
        unique_records_file.write(
            jj[2]
            + ";"
            + jj[8]
            + ";"
            + datetime_string
            + ";"
            + jj[0]
            + ";"
            + jj[1]
            + ";"
            + jj[5]
            + ";"
            + jj[6]
            + ";"
            + jj[7]
            + ";"
            + jj[9]
            + ";"
            + jj[10]
            + ";"
            + str(duration_seconds)
            + ";"
            + jj[12]
            + ";"
            + jj[13]
            + ";"
            + jj[14]
            + ";"
            + jj[15]
            + ";"
            + jj[16]
            + ";"
            + jj[17]
            + ";"
            + jj[18]
            + ";"
            + jj[19]
            + ";"
            + jj[20]
            + ";"
            + jj[21]
            + ";"
            + jj[22]
            + ";"
            + jj[23]
            + ";"
            + jj[24]
            + ";"
            + jj[25]
        )


d.close()
unique_records_file.close()

if len(prefix_counts) != 0:
    sorted_prefix_counts = sorted(prefix_counts.items(), key=itemgetter(0))

    so = 0
    ie = sorted_prefix_counts[0][0]
    for i in sorted_prefix_counts:
        if i[1] > max_memory_sort_size:
            large_prefix_set.add(i[0])
        so = so + i[1]
        if so > max_file_sort_size:
            ie = i[0]
            so = i[1]
        prefix_mapping[i[0]] = ie
        prefixes_set.add(ie)

    if len(glob.glob(base_path + "Auxiliar" + cdr_database)) != 0:
        shutil.rmtree(base_path + "Auxiliar" + cdr_database)
    os.mkdir(base_path + "Auxiliar" + cdr_database)

    pra = open(base_path + "Auxiliar" + cdr_database + "\\pr", "w")
    for i in prefixes_set:
        pra.write(i + "\n")
    pra.close()
    aaea = open(base_path + "Auxiliar" + cdr_database + "\\aae", "w")
    for i in prefix_mapping:
        aaea.write(i + "|" + prefix_mapping[i] + "\n")
    aaea.close()

    import dividearq

    dividearq.div(prefix_length, base_path, cdr_database, input_file_path)

    ad = glob.glob(base_path + "Arqparciais" + cdr_database + "\\*.txt")
    ad.sort()
    os.remove(input_file_path)
    sorted_output_file = open(base_path + cdr_database + "ord3.txt", "w")
    ppp = []
    for t in ad:
        zi = t.split("\\")
        zi = zi[len(zi) - 1].replace(".txt", "")
        if zi in large_prefix_set:
            prefix_length = prefix_length + 1
            prefix_counts = {}  # ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
            prefixes_set = set()
            pr1 = []
            pr2 = {}
            pp = []
            import os

            d = open(t)
            for i in d:
                prefixes_set.add(i[0:prefix_length])
                if i[0:prefix_length] in prefix_counts:
                    prefix_counts[i[0:prefix_length]] = prefix_counts[i[0:prefix_length]] + 1
                else:
                    prefix_counts[i[0:prefix_length]] = 1
            d.close()
            for i in prefixes_set:
                pr1.append(i)
            pr1.sort()
            tso = 0
            nn = 1
            for i in pr1:
                tso = prefix_counts[i] + tso
                if tso <= max_memory_sort_size:
                    pr2[i] = nn
                else:
                    nn = nn + 1
                    tso = prefix_counts[i]
                    pr2[i] = nn
            for i in range(pr2[pr1[0]], pr2[pr1[len(pr1) - 1]] + 1):
                d = open(t)
                for i1 in d:
                    if pr2[i1[0:prefix_length]] == i:
                        pp.append(i1)
                d.close()
                pp.sort()
                for i2 in pp:
                    sorted_output_file.write(i2)
                pp = []
            os.remove(t)
            prefixes_set = set()
            pr1 = []
            pr2 = {}
            prefix_counts = {}
        else:
            d = open(t)
            for i3 in d:
                ppp.append(i3)
            d.close()
            ppp.sort()
            for i3 in ppp:
                sorted_output_file.write(i3)
            ppp = []
            os.remove(t)
    sorted_output_file.close()  # ordenar - fim

    re4 = open(base_path + cdr_database + "ord3.txt")
    r = open(base_path + cdr_database + "unico.txt", "a")
    consolidated_output_file = open(base_path + cdr_database + "consolidado.txt", "w")
    j = re4.readline()
    jj = j.split(";")

    j2 = jj[11].split(":")
    try:
        duration_seconds = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])
    except ValueError:
        if jj[11] == "":
            duration_seconds = 0

    da2 = "20" + jj[3].replace("/", "-")
    datetime_string = da2 + ";" + jj[4]
    current_reference = jj[2]
    current_origin = jj[8]
    current_destination = jj[9]

    for i in re4:
        record_found_flag = 1
        ii = i.split(";")

        i2 = ii[11].split(":")
        if ii[2] != "":
            if ii[2] == current_reference and (ii[0] == "ORI" or ii[0] == "TER") and ii[8] == current_origin:
                consolidated_output_file.write(j)
                while ii[2] == current_reference and ii[8] == current_origin:
                    consolidated_output_file.write(i)
                    try:
                        duration_seconds = duration_seconds + int(i2[0]) * 3600 + int(i2[1]) * 60 + int(i2[2])

                    except ValueError:
                        duration_seconds = ii[11]
                    except TypeError:
                        duration_seconds = ii[11]

                    current_reference = ii[2]
                    current_origin = jj[8]
                    current_destination = jj[9]
                    ju = i.split(";")
                    i = re4.readline()
                    if i == "":
                        break
                    ii = i.split(";")
                    i2 = ii[11].split(":")
                consolidated_output_file.write(
                    ju[2]
                    + ";"
                    + ju[8]
                    + ";"
                    + datetime_string
                    + ";"
                    + ju[0]
                    + ";"
                    + ju[1]
                    + ";"
                    + ju[5]
                    + ";"
                    + ju[6]
                    + ";"
                    + ju[7]
                    + ";"
                    + ju[9]
                    + ";"
                    + ju[10]
                    + ";"
                    + str(duration_seconds)
                    + ";"
                    + ju[12]
                    + ";"
                    + ju[13]
                    + ";"
                    + ju[14]
                    + ";"
                    + ju[15]
                    + ";"
                    + ju[16]
                    + ";"
                    + ju[17]
                    + ";"
                    + ju[18]
                    + ";"
                    + ju[19]
                    + ";"
                    + ju[20]
                    + ";"
                    + ju[21]
                    + ";"
                    + ju[22]
                    + ";"
                    + ju[23]
                    + ";"
                    + ju[24]
                    + ";"
                    + ju[25]
                )
                r.write(
                    ju[2]
                    + ";"
                    + ju[8]
                    + ";"
                    + datetime_string
                    + ";"
                    + ju[0]
                    + ";"
                    + ju[1]
                    + ";"
                    + ju[5]
                    + ";"
                    + ju[6]
                    + ";"
                    + ju[7]
                    + ";"
                    + ju[9]
                    + ";"
                    + ju[10]
                    + ";"
                    + str(duration_seconds)
                    + ";"
                    + ju[12]
                    + ";"
                    + ju[13]
                    + ";"
                    + ju[14]
                    + ";"
                    + ju[15]
                    + ";"
                    + ju[16]
                    + ";"
                    + ju[17]
                    + ";"
                    + ju[18]
                    + ";"
                    + ju[19]
                    + ";"
                    + ju[20]
                    + ";"
                    + ju[21]
                    + ";"
                    + ju[22]
                    + ";"
                    + ju[23]
                    + ";"
                    + ju[24]
                    + ";"
                    + ju[25]
                )
                record_found_flag = 0
                j = i
                if j == "":
                    break
                jj = i.split(";")
                j2 = jj[11].split(":")
                try:
                    duration_seconds = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])

                except ValueError:
                    if jj[11] == "":
                        duration_seconds = 0
                    else:
                        duration_seconds = jj[11]
                da2 = "20" + jj[3].replace("/", "-")
                datetime_string = da2 + ";" + jj[4]
                current_reference = jj[2]
                current_origin = jj[8]
                current_destination = jj[9]
            else:
                r.write(
                    jj[2]
                    + ";"
                    + jj[8]
                    + ";"
                    + datetime_string
                    + ";"
                    + jj[0]
                    + ";"
                    + jj[1]
                    + ";"
                    + jj[5]
                    + ";"
                    + jj[6]
                    + ";"
                    + jj[7]
                    + ";"
                    + jj[9]
                    + ";"
                    + jj[10]
                    + ";"
                    + str(duration_seconds)
                    + ";"
                    + jj[12]
                    + ";"
                    + jj[13]
                    + ";"
                    + jj[14]
                    + ";"
                    + jj[15]
                    + ";"
                    + jj[16]
                    + ";"
                    + jj[17]
                    + ";"
                    + jj[18]
                    + ";"
                    + jj[19]
                    + ";"
                    + jj[20]
                    + ";"
                    + jj[21]
                    + ";"
                    + jj[22]
                    + ";"
                    + jj[23]
                    + ";"
                    + jj[24]
                    + ";"
                    + jj[25]
                )
                j = i
                if j == "":
                    break
                jj = i.split(";")
                j2 = jj[11].split(":")
                try:
                    duration_seconds = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])
                except ValueError:
                    if jj[11] == "":
                        duration_seconds = 0
                    else:
                        duration_seconds = jj[11]
                da2 = "20" + jj[3].replace("/", "-")
                datetime_string = da2 + ";" + jj[4]
                current_reference = jj[2]
                current_origin = jj[8]
                current_destination = jj[9]
    if record_found_flag == 1:
        r.write(
            jj[2]
            + ";"
            + jj[8]
            + ";"
            + datetime_string
            + ";"
            + jj[0]
            + ";"
            + jj[1]
            + ";"
            + jj[5]
            + ";"
            + jj[6]
            + ";"
            + jj[7]
            + ";"
            + jj[9]
            + ";"
            + jj[10]
            + ";"
            + str(duration_seconds)
            + ";"
            + jj[12]
            + ";"
            + jj[13]
            + ";"
            + jj[14]
            + ";"
            + jj[15]
            + ";"
            + jj[16]
            + ";"
            + jj[17]
            + ";"
            + jj[18]
            + ";"
            + jj[19]
            + ";"
            + jj[20]
            + ";"
            + jj[21]
            + ";"
            + jj[22]
            + ";"
            + jj[23]
            + ";"
            + jj[24]
            + ";"
            + jj[25]
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
ap3 = glob.glob(base_path + "Arqparciais" + cdr_database)
while len(ap3) == 1:  # teste
    ap3 = glob.glob(base_path + "Arqparciais" + cdr_database)  # teste
os.mkdir(base_path + "Arqparciais" + cdr_database)
for ap8 in range(10000000):  # teste
    ap10 = 1  # teste
sorted_files = []
record_count = 0
prefixes_set = set()
prefix_counts = {}
sorted_prefix_counts = []
prefix_mapping = {}
large_prefix_set = set()
d = open(input_file_path)


for i in d:
    record_count = record_count + 1
    if i[0:prefix_length] in prefix_counts:
        prefix_counts[i[0:prefix_length]] = prefix_counts[i[0:prefix_length]] + 1
    else:
        prefix_counts[i[0:prefix_length]] = 1
d.close()

sorted_prefix_counts = sorted(prefix_counts.items(), key=itemgetter(0))
so = 0
ie = sorted_prefix_counts[0][0]
for i in sorted_prefix_counts:
    if i[1] > max_memory_sort_size:
        large_prefix_set.add(i[0])
    so = so + i[1]
    if so > max_file_sort_size:
        ie = i[0]
        so = i[1]
    prefix_mapping[i[0]] = ie
    prefixes_set.add(ie)


if len(glob.glob(base_path + "Auxiliar" + cdr_database)) == 1:
    shutil.rmtree(base_path + "Auxiliar" + cdr_database)
os.mkdir(base_path + "Auxiliar" + cdr_database)

pra = open(base_path + "Auxiliar" + cdr_database + "\\pr", "w")
for i in prefixes_set:
    pra.write(i + "\n")
pra.close()
aaea = open(base_path + "Auxiliar" + cdr_database + "\\aae", "w")
for i in prefix_mapping:
    aaea.write(i + "|" + prefix_mapping[i] + "\n")
aaea.close()


import dividearq

dividearq.div(prefix_length, base_path, cdr_database, input_file_path)


ad = glob.glob(base_path + "Arqparciais" + cdr_database + "\\*.txt")
ad.sort()
sorted_output_file = open(base_path + cdr_database + "ord4.txt", "w")
os.remove(input_file_path)
sorted_output_file.write(
    "Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;IMSI;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto"
    + "\n"
)
ppp = []
for t in ad:
    zi = t.split("\\")
    zi = zi[len(zi) - 1].replace(".txt", "")
    if zi in large_prefix_set:
        prefix_length = prefix_length + 1
        prefix_counts = {}  # ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
        prefixes_set = set()
        pr1 = []
        pr2 = {}
        pp = []
        import os

        d = open(t)
        for i in d:
            prefixes_set.add(i[0:prefix_length])
            if i[0:prefix_length] in prefix_counts:
                prefix_counts[i[0:prefix_length]] = prefix_counts[i[0:prefix_length]] + 1
            else:
                prefix_counts[i[0:prefix_length]] = 1
        d.close()
        for i in prefixes_set:
            pr1.append(i)
        pr1.sort()
        tso = 0
        nn = 1
        for i in pr1:
            tso = prefix_counts[i] + tso
            if tso <= max_memory_sort_size:
                pr2[i] = nn
            else:
                nn = nn + 1
                tso = prefix_counts[i]
                pr2[i] = nn
        for i in range(pr2[pr1[0]], pr2[pr1[len(pr1) - 1]] + 1):
            d = open(t)
            for i1 in d:
                if pr2[i1[0:prefix_length]] == i:
                    pp.append(i1)
            d.close()
            pp.sort()
            for i2 in pp:
                sorted_output_file.write(i2)
            pp = []
        os.remove(t)
        prefixes_set = set()
        pr1 = []
        pr2 = {}
        prefix_counts = {}
    else:
        d = open(t)
        for i3 in d:
            ppp.append(i3)
        d.close()
        ppp.sort()
        for i3 in ppp:
            sorted_output_file.write(i3)
        ppp = []
        os.remove(t)
sorted_output_file.close()  # ordenar - fim
g = open(base_path + cdr_database + "ord4.txt", "r")
me = ""
an = ""
op = "0"
for i in g:
    ii = i.split(";")
    if (ii[4] == "ORI" or ii[4] == "TER") and ii[7] != "":
        ii21 = ii[2].split("-")
        ii61 = ii[7].split("-")
        me = ii21[1]
        an = ii21[0]
        op = ii61[1][0:2]
        break
g.close()
if voice_record_flag == 0:
    rop = operator_code
else:
    rop = opid[op]
os.rename(
    base_path + cdr_database + "ord4.txt",
    base_path + "VozEricsson" + "-" + cdr_database + "-" + rop + "-" + me + an + ".txt",
)

if len(glob.glob(base_path + "Arqparciais" + cdr_database)) == 1:
    shutil.rmtree(base_path + "Arqparciais" + cdr_database)
if len(glob.glob(base_path + "Auxiliar" + cdr_database)) == 1:
    shutil.rmtree(base_path + "Auxiliar" + cdr_database)

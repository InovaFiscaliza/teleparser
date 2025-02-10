import glob
import os
import shutil
import sys
import time
from datetime import datetime
from operator import itemgetter

diret = os.getcwd() + "\\"
tord = 6000000  # tamanho máximo a ordenar na memória (trecho: ordenar)
tma = 5000000  # tamanho máximo de arquivo a ser ordenado de uma vez na memória (trecho: ordenar)
car = sys.argv[1]
cdb = sys.argv[2]
oe = sys.argv[3]
da = sys.argv[4]
da9 = da
xx = 15

tm = time.asctime().replace(":", "").replace(" ", "")
tr = datetime.now()
icn = "s"
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

if len(glob.glob(car + "Arqparciais" + cdb)) != 0:  # Ordenar - início - versão 07/2018
    shutil.rmtree(car + "Arqparciais" + cdb)
os.mkdir(car + "Arqparciais" + cdb)

aaq = []
cc = 0
pr = set()
tam = {}
tamo = []
aae = {}
soa = set()


rea = 0
d = open(da)

d6 = open(car + cdb + "unico.txt", "w")
ve9 = 0
for i in d:
    if i[0:3] == "ORI" or i[0:3] == "TER":
        ve9 = 1
        cc = cc + 1
        if i[0:xx] in tam:
            tam[i[0:xx]] = tam[i[0:xx]] + 1
        else:
            tam[i[0:xx]] = 1
    else:
        jj = i.split(";")
        j2 = jj[11].split(":")
        try:
            du = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])
        except ValueError:
            if jj[11] == "":
                du = 0

        da2 = "20" + jj[3].replace("/", "-")
        dah = da2 + ";" + jj[4]
        d6.write(
            jj[2]
            + ";"
            + jj[8]
            + ";"
            + dah
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
            + str(du)
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
d6.close()

if len(tam) != 0:
    tamo = sorted(tam.items(), key=itemgetter(0))

    so = 0
    ie = tamo[0][0]
    for i in tamo:
        if i[1] > tord:
            soa.add(i[0])
        so = so + i[1]
        if so > tma:
            ie = i[0]
            so = i[1]
        aae[i[0]] = ie
        pr.add(ie)

    if len(glob.glob(car + "Auxiliar" + cdb)) != 0:
        shutil.rmtree(car + "Auxiliar" + cdb)
    os.mkdir(car + "Auxiliar" + cdb)

    pra = open(car + "Auxiliar" + cdb + "\\pr", "w")
    for i in pr:
        pra.write(i + "\n")
    pra.close()
    aaea = open(car + "Auxiliar" + cdb + "\\aae", "w")
    for i in aae:
        aaea.write(i + "|" + aae[i] + "\n")
    aaea.close()

    import dividearq

    dividearq.div(xx, car, cdb, da)

    ad = glob.glob(car + "Arqparciais" + cdb + "\\*.txt")
    ad.sort()
    os.remove(da)
    re = open(car + cdb + "ord3.txt", "w")
    ppp = []
    for t in ad:
        zi = t.split("\\")
        zi = zi[len(zi) - 1].replace(".txt", "")
        if zi in soa:
            xx = xx + 1
            tam = {}  # ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
            pr = set()
            pr1 = []
            pr2 = {}
            pp = []
            import os

            d = open(t)
            for i in d:
                pr.add(i[0:xx])
                if i[0:xx] in tam:
                    tam[i[0:xx]] = tam[i[0:xx]] + 1
                else:
                    tam[i[0:xx]] = 1
            d.close()
            for i in pr:
                pr1.append(i)
            pr1.sort()
            tso = 0
            nn = 1
            for i in pr1:
                tso = tam[i] + tso
                if tso <= tord:
                    pr2[i] = nn
                else:
                    nn = nn + 1
                    tso = tam[i]
                    pr2[i] = nn
            for i in range(pr2[pr1[0]], pr2[pr1[len(pr1) - 1]] + 1):
                d = open(t)
                for i1 in d:
                    if pr2[i1[0:xx]] == i:
                        pp.append(i1)
                d.close()
                pp.sort()
                for i2 in pp:
                    re.write(i2)
                pp = []
            os.remove(t)
            pr = set()
            pr1 = []
            pr2 = {}
            tam = {}
        else:
            d = open(t)
            for i3 in d:
                ppp.append(i3)
            d.close()
            ppp.sort()
            for i3 in ppp:
                re.write(i3)
            ppp = []
            os.remove(t)
    re.close()  # ordenar - fim

    re4 = open(car + cdb + "ord3.txt")
    r = open(car + cdb + "unico.txt", "a")
    con = open(car + cdb + "consolidado.txt", "w")
    j = re4.readline()
    jj = j.split(";")

    j2 = jj[11].split(":")
    try:
        du = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])
    except ValueError:
        if jj[11] == "":
            du = 0

    da2 = "20" + jj[3].replace("/", "-")
    dah = da2 + ";" + jj[4]
    ref = jj[2]
    ref2 = jj[8]
    ref3 = jj[9]

    for i in re4:
        tf = 1
        ii = i.split(";")

        i2 = ii[11].split(":")
        if ii[2] != "":
            if ii[2] == ref and (ii[0] == "ORI" or ii[0] == "TER") and ii[8] == ref2:
                con.write(j)
                while ii[2] == ref and ii[8] == ref2:
                    con.write(i)
                    try:
                        du = du + int(i2[0]) * 3600 + int(i2[1]) * 60 + int(i2[2])

                    except ValueError:
                        du = ii[11]
                    except TypeError:
                        du = ii[11]

                    ref = ii[2]
                    ref2 = jj[8]
                    ref3 = jj[9]
                    ju = i.split(";")
                    i = re4.readline()
                    if i == "":
                        break
                    ii = i.split(";")
                    i2 = ii[11].split(":")
                con.write(
                    ju[2]
                    + ";"
                    + ju[8]
                    + ";"
                    + dah
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
                    + str(du)
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
                    + dah
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
                    + str(du)
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
                tf = 0
                j = i
                if j == "":
                    break
                jj = i.split(";")
                j2 = jj[11].split(":")
                try:
                    du = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])

                except ValueError:
                    if jj[11] == "":
                        du = 0
                    else:
                        du = jj[11]
                da2 = "20" + jj[3].replace("/", "-")
                dah = da2 + ";" + jj[4]
                ref = jj[2]
                ref2 = jj[8]
                ref3 = jj[9]
            else:
                r.write(
                    jj[2]
                    + ";"
                    + jj[8]
                    + ";"
                    + dah
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
                    + str(du)
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
                    du = int(j2[0]) * 3600 + int(j2[1]) * 60 + int(j2[2])
                except ValueError:
                    if jj[11] == "":
                        du = 0
                    else:
                        du = jj[11]
                da2 = "20" + jj[3].replace("/", "-")
                dah = da2 + ";" + jj[4]
                ref = jj[2]
                ref2 = jj[8]
                ref3 = jj[9]
    if tf == 1:
        r.write(
            jj[2]
            + ";"
            + jj[8]
            + ";"
            + dah
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
            + str(du)
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
    con.close()

    os.remove(car + cdb + "ord3.txt")

if ve9 == 0:
    os.remove(da9)
da = car + cdb + "unico.txt"
xx = 2

if len(glob.glob(car + "Arqparciais" + cdb)) == 1:  # Ordenar - início - versão 07/2018
    shutil.rmtree(car + "Arqparciais" + cdb)
ap3 = glob.glob(car + "Arqparciais" + cdb)
while len(ap3) == 1:  # teste
    ap3 = glob.glob(car + "Arqparciais" + cdb)  # teste
os.mkdir(car + "Arqparciais" + cdb)
for ap8 in range(10000000):  # teste
    ap10 = 1  # teste
aaq = []
cc = 0
pr = set()
tam = {}
tamo = []
aae = {}
soa = set()
d = open(da)


for i in d:
    cc = cc + 1
    if i[0:xx] in tam:
        tam[i[0:xx]] = tam[i[0:xx]] + 1
    else:
        tam[i[0:xx]] = 1
d.close()

tamo = sorted(tam.items(), key=itemgetter(0))
so = 0
ie = tamo[0][0]
for i in tamo:
    if i[1] > tord:
        soa.add(i[0])
    so = so + i[1]
    if so > tma:
        ie = i[0]
        so = i[1]
    aae[i[0]] = ie
    pr.add(ie)


if len(glob.glob(car + "Auxiliar" + cdb)) == 1:
    shutil.rmtree(car + "Auxiliar" + cdb)
os.mkdir(car + "Auxiliar" + cdb)

pra = open(car + "Auxiliar" + cdb + "\\pr", "w")
for i in pr:
    pra.write(i + "\n")
pra.close()
aaea = open(car + "Auxiliar" + cdb + "\\aae", "w")
for i in aae:
    aaea.write(i + "|" + aae[i] + "\n")
aaea.close()


import dividearq

dividearq.div(xx, car, cdb, da)


ad = glob.glob(car + "Arqparciais" + cdb + "\\*.txt")
ad.sort()
re = open(car + cdb + "ord4.txt", "w")
os.remove(da)
re.write(
    "Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;IMSI;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto"
    + "\n"
)
ppp = []
for t in ad:
    zi = t.split("\\")
    zi = zi[len(zi) - 1].replace(".txt", "")
    if zi in soa:
        xx = xx + 1
        tam = {}  # ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
        pr = set()
        pr1 = []
        pr2 = {}
        pp = []
        import os

        d = open(t)
        for i in d:
            pr.add(i[0:xx])
            if i[0:xx] in tam:
                tam[i[0:xx]] = tam[i[0:xx]] + 1
            else:
                tam[i[0:xx]] = 1
        d.close()
        for i in pr:
            pr1.append(i)
        pr1.sort()
        tso = 0
        nn = 1
        for i in pr1:
            tso = tam[i] + tso
            if tso <= tord:
                pr2[i] = nn
            else:
                nn = nn + 1
                tso = tam[i]
                pr2[i] = nn
        for i in range(pr2[pr1[0]], pr2[pr1[len(pr1) - 1]] + 1):
            d = open(t)
            for i1 in d:
                if pr2[i1[0:xx]] == i:
                    pp.append(i1)
            d.close()
            pp.sort()
            for i2 in pp:
                re.write(i2)
            pp = []
        os.remove(t)
        pr = set()
        pr1 = []
        pr2 = {}
        tam = {}
    else:
        d = open(t)
        for i3 in d:
            ppp.append(i3)
        d.close()
        ppp.sort()
        for i3 in ppp:
            re.write(i3)
        ppp = []
        os.remove(t)
re.close()  # ordenar - fim
g = open(car + cdb + "ord4.txt", "r")
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
if ve9 == 0:
    rop = oe
else:
    rop = opid[op]
os.rename(
    car + cdb + "ord4.txt",
    car + "VozEricsson" + "-" + cdb + "-" + rop + "-" + me + an + ".txt",
)

if len(glob.glob(car + "Arqparciais" + cdb)) == 1:
    shutil.rmtree(car + "Arqparciais" + cdb)
if len(glob.glob(car + "Auxiliar" + cdb)) == 1:
    shutil.rmtree(car + "Auxiliar" + cdb)

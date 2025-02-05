import os
import time
import datetime
import shutil
import glob
import subprocess
import zipfile
import sys
from datetime import datetime

# from termcolor import *
# import colorama
# colorama.init()
diret = os.getcwd()


lim1 = glob.glob(diret + "/arqli*")
for i in lim1:
    os.remove(i)

sa = "5"
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
vac = ""
op3 = ""
c11 = 0
c12 = 0

vam = "nada"
cpar = ["1", "2", "3", "4", "1i", "5", "5i", "6", "7", "8", "9", "10", "10i", "21"]
emp = ["vivo", "claro", "tim", "oi", "nextel", "sercomtel", "algar", "ctbc"]
# while op3 not in ('1','1i','2','3','4','5','5i','6','7','8','9','10','10i','21') and c11<4:
while len(op3) != 2 and c11 < 4:
    # while op3 not in ('1','2','3','4','5') and c11<4:
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
    op3 = input()

    c11 = c11 + 1
    vam = op3[-1:]
    if vam != "i":
        vac = "a"
    #            if op3=='5':
    #                print()
    #                print('Informe uma das opções abaixo:')
    #                print('    - "u" (Resultado em um único arquivo)')
    #                print('    - "n" ou "Enter" (Em arquivos separados por faixa de numeração de usuário)')
    #                print('    - "d" (Em arquivos separados para cada hora)')
    #                print(''('AGUARDANDO...:','green'),end='')
    #                ag=input()
    #                print()
    if op3[0:2] == "10" and len(op3) == 3:
        break
op3 = op3[:-1]

if op3 in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
    print()

    print(
        "Informe o caminho para leitura dos CDRs brutos (para a leitura de todos os arquivos, finalize com /*.gz). Caso os arquivos .gz estejam compactados em pastas .zip, finalize com /*.zip ao invés de /*.gz. "
    )
    print("AGUARDANDO...:", end="")
    cdrbruto = input()
    # cdrbruto=cdrbruto.replace("'",'').replace('"','').replace("/",'\\')
    orig = glob.glob(cdrbruto)
    vz = vz2 = 0
    if cdrbruto[-3:] == "zip":
        zo = 0
        for tu in orig:
            try:
                b15 = zipfile.ZipFile(tu)
            except Exception:
                print("Falha pasta", tu)
                zo = 1

            b15.close()

        if zo == 1:
            print()
            b80 = input('Para interromper, tecle "p" e depois "Enter" ')
            if b80 == "p":
                sys.exit()

        print(cdrbruto)
        vz2 = 1

    for vz1 in orig:
        if vz1[-2:] == "gz":
            vz = 1
            break

    print()
    # print(cdrbruto)
    # print('Quantidade de arquivos para leitura:',len(orig))
    while vz == 0 and vz2 == 0 and c12 < 3:
        print()
        print("Não foram localizados arquivos para leitura.")
        print("Reveja o caminho informado.")
        cdrbruto = input(
            "Informe o caminho para leitura dos CDRs brutos. AGUARDANDO...:"
        )

        cdrbruto = cdrbruto.replace("'", "").replace('"', "").replace("/", "\\")
        orig = glob.glob(cdrbruto)
        vz = vz2 = 0
        if cdrbruto[-3:] == "zip":
            vz2 = 1

        for vz1 in orig:
            if vz1[-2:] == "gz":
                vz = 1
                break

        # print('Para interromper o processamento digite "e")
        print()
        c12 = c12 + 1

    eo = ""
    eb = cdrbruto.lower()
    for tu in emp:
        if eb.find(tu + "\\") != -1:
            eo = tu
            break
    if eo == "":
        print("- Informe o nome da operadora da qual os CDRs brutos serão lidos.")
        print("AGUARDANDO...:", end="")
        eo = input()
    eo = eo.upper()

    if len(orig) != 0:
        cdrbrutota = str(len(orig))
        print()
        print("Quantidade de arquivos para leitura:", len(orig))
        print()
        print("Estimativa para conclusão da leitura:", len(orig) * 0.3 / 1000, "horas")
        print()

        # b8.close()
        tm = time.asctime().replace(":", "").replace(" ", "")
        print("Caminho para salvar o arquivo resultado (CDRs lidos):")
        print(
            'Tecle "Enter" para salvar o resultado nesta máquina ('
            + diret
            + "\\Resultados\\), ou indique o caminho desejado."
        )
        print("AGUARDANDO...:", end="")
        car = input()
        # car = car.replace("'", "").replace('"', "").replace("/", "\\")
        cdb = (
            str(datetime.now())
            .replace("\n", "")
            .replace(".", "")
            .replace(":", "")
            .replace(" ", "")
            .replace("-", "")
        )
        if car == "":
            car = diret + "\\Resultados\\"
        else:
            if car[-1:] != "\\":
                car = car + "\\"
        print("Resultado em:", car)
        #        b9=open(car+'Inicio.txt','w')
        #        b9.close()
        #        b8=open('caminhobruto.txt','w')
        #        b8.write(cdrbruto+'\n')
        #        b8.write(car+'\n')
        #        b8.write(cdb+'\n')
        #        b8.write(op3+'\n')
        #        b8.close()

        if vz2 == 1:
            print("DESCOMPACTANDO...")

            iicdrbruto = cdrbruto.split("\\")
            xv = iicdrbruto[len(iicdrbruto) - 1]
            cdrbrutodes = cdrbruto.replace(xv, "")

            os.mkdir(cdrbrutodes + "descomp")

            c15 = 0
            cc15 = 0
            a15 = 0
            c9 = 0
            print(len(orig))
            ree = set()
            ree2 = []
            for z2 in orig:
                c9 = c9 + 1

                try:
                    b15 = zipfile.ZipFile(z2)
                except Exception:
                    print("falha pasta", z2)

                a15 = a15 + len(b15.namelist()) - 1

                # if c9==1:
                vee3 = (b15.namelist()[0]).replace("../", "")
                vee = (vee3).split("/")
                ree2.append(vee3)

                vee2 = ""
                for zd in range(len(vee) - 1):
                    vee2 = vee2 + "\\*"
                ree.add(vee2)

                for j15 in b15.namelist():
                    c15 = c15 + 1
                    if c15 > 1:
                        cc15 = 1

                    if cc15 == 1:
                        # jj15=j15.split('\\')
                        jj15 = j15.split("/")

                        # des1=cdrbruto.split('\\');des2=des1[len(des1)-1];des=cdrbruto.replace(des2,'')

                        try:
                            b15.extract(j15, cdrbrutodes + "descomp")
                        except Exception:
                            print("falha arquivo", j15)

                        # d15=glob.glob(car+'descomp'+np+'\\*\\*.gz')
                # d15=glob.glob(car+'descomp'+vee2+'\\*.gz')

            # input('ver desc')

            if len(ree) == 1:
                cdrbruto = cdrbrutodes + "descomp" + vee2 + "\\*.gz"
            else:
                for zu in ree2:
                    zu2 = zu.split("/")
                    if len(zu2) > 2:
                        zu3 = zu[:-1].replace("/", "\\")
                        shutil.move(
                            cdrbrutodes + "descomp\\" + zu3,
                            cdrbrutodes + "descomp\\" + zu2[len(zu2) - 1],
                        )

                cdrbruto = cdrbrutodes + "descomp\\*\\*.gz"


#        if op3=='1':
#            #pp1=subprocess.Popen(['python3','cdrEricsson-ordem-unico001º150102Punico.py'])
#            #pp1=subprocess.Popen(['python','cdrEricsson-ordem-unico001ºGerenciador.py'])
#            pp2=subprocess.Popen(['python','Acumulador.py',vac,eo,car,cdb,cdrbruto,cdrbrutota,op3,sa])
#        if op3=='2' or op3=='3':
#            pp2=subprocess.Popen(['python','Acumulador.py',vac,eo,car,cdb,cdrbruto,cdrbrutota,op3,sa])
#            #pp1=subprocess.Popen(['python','cdrNokiaTeste-1º.py'])
#        if op3=='4':
#            pp1=subprocess.Popen(['python','Acumulador.py',vac,eo,car,cdb,cdrbruto,cdrbrutota,op3,sa])
#        if op3=='5':
#            pp2=subprocess.Popen(['python','Acumulador.py',vac,eo,car,cdb,cdrbruto,cdrbrutota,op3,sa])
#            #pp2=subprocess.Popen(['python','cdrDados-Gerenciador.py',vac,eo,car,cdb,cdrbruto,cdrbrutota])
print()
print()

if vam == "i":
    print("=/= Os arquivos individuais estarão na pasta:", eo + cdb)
# print('O acompanhamento da leitura pode ser efetuado por meio do arquivo "AcompanhamentoLeitura".')
# print('Há registro da execução a cada 10% de execução, aproximadamente.')
print()
print("O percentual de execução pode ser acompanhado conforme a seguir:.......")
print()
# print('O arquivo de acompanhamento encontra-se no mesmo diretório em que será gravado o arquivo resultado:')

# print(car)


import os
import time
import datetime
import shutil
import glob
import sys
from datetime import datetime

diret = os.getcwd()
# cdb=''
ti = datetime.now()
print()
print("Início de leitura...", ti)
print()
tp3 = 2
aacc = 0
td9 = 0
# vac=sys.argv[1];eo=sys.argv[2];car=sys.argv[3];cdb=sys.argv[4];cdrbruto=sys.argv[5];cdrbrutota=sys.argv[6];tip=sys.argv[7];sa=sys.argv[8]
tip = op3

tip2 = ""
if op3 == "8":
    tip2 = op3
    tip = "1"

qp = 5  # define o número de processos que atuam simultaneamente. Sugere-se que esse número seja igual ao número de nucleos de processamento da máquina menos um ou dois
aca2 = 5
print(vac, eo)

arli = open("arquivosparaleitura.txt", "w")
arnli = open("arquivosnaolidos.txt", "w")
ar = set()
anr = set()
tcd = ""
vo = ["1", "2", "3", "4", "5"]

##if tip=='1':
##    vac1=vac
##    vac='1'
vac1 = vac
pas = set()
arqb = glob.glob(cdrbruto)

# zc1=0
# for zc in arqb:
#    zc1=zc1+1
#    if zc1==981:
#        print(zc)
#        break
# print(kk)

eee = ""
if tip == "1":
    eee = "Ericsson"
if tip == "2":
    eee = "Nokia"


if tip in vo:
    tcd = "Voz" + eee
if tip == "6":
    tcd = "Dados"
if tip2 == "8" or tip == "9" or tip == "7":  # or tip=='6':
    tcd = "Volte"
if tip == "10":
    tcd = "Stir"
if vac == "a":
    da = car + eo + "-" + tcd + cdb[0:12] + ".txt"
    # acu=open(da,'a')

    if tip in vo or vam == "u":
        acu = open(da, "w")
    if tip == "6":  # or tip=='7' or tip=='8' or tip=='9':
        if vam == "u":
            acu.write(
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
            os.mkdir(car + eo + cdb + tcd)
    if tip == "7":
        if vam == "u":
            acu.write(
                "Originador(list-Of-Calling-Party-Address);Data(recordOpeningTime);Hora;TipodeCDR(role-of-Node);called-Party-Address(NúmeroChamado);dialled-Party-Address(NúmeroTeclado);List-Of-Called-Asserted-Identity;Duration;Célula(accessNetworkInformation);IMSI(List-of-Subscription-ID);IMEI(private-User-Equipment-Info);MSC-Number;network-Call-Reference;causeForRecordClosing;interOperatorIdentifiers;sIP-Method\n"
            )
        else:
            os.mkdir(car + eo + cdb + tcd)

    if tip == "10":
        if vam == "u":
            acu.write(
                "Originador(list-Of-Calling-Party-Address);Data(recordOpeningTime);Hora;TipodeCDR(role-of-Node);called-Party-Address(NúmeroChamado);dialled-Party-Address(NúmeroTeclado);List-Of-Called-Asserted-Identity;Duration;Célula(accessNetworkInformation);IMSI(List-of-Subscription-ID);IMEI(private-User-Equipment-Info);MSC-Number;network-Call-Reference;causeForRecordClosing;interOperatorIdentifiers;sIP-Method\n"
            )
        else:
            os.mkdir(car + eo + cdb + tcd)

    if tip == "9":
        if vam == "u":
            acu.write("Data;Hora;Originador;TipoCDR;NúmeroChamado;Duração;Célula\n")
        else:
            os.mkdir(car + eo + cdb + tcd)
    #            ca10=open(car+eo+cdb+'\\Cabeçalho.txt','w')
    #            ca10.write('Tipo de CDR'+';'+'listOfTrafficVolumes'+';'+'Location'+';'+'servedMSISDN'+';'+'listOfServiceData'+';'+'recordSequenceNumber'+';'+'CauseforRecClosing'+';'+'ChargingID'+';'+'duration'+';'+'ggsnAddress'+';'+'openning time;StartTime;Diagnostics;Radio;ServedIMSI;;;Arquivo'+'\n')
    #            ca10.close()
    if tip in vo and vam != "u":
        os.mkdir(car + eo + cdb + tcd)
else:
    # os.mkdir(car+eo+cdb+tcd)
    os.mkdir(car + eo + cdb)
    for i in arqb:
        ii = i.split("\\")
        pas.add(ii[len(ii) - 2])
    for i in pas:
        # os.mkdir(car+eo+cdb+tcd+'\\'+i)
        os.mkdir(car + eo + cdb + "\\" + i)
#    if tip=='5' or tip=='10':
#        ca10=open(car+eo+cdb+'\\Cabeçalho.txt','w')
#        ca10.write('Tipo de CDR'+';'+'listOfTrafficVolumes'+';'+'Location'+';'+'servedMSISDN'+';'+'listOfServiceData'+';'+'recordSequenceNumber'+';'+'CauseforRecClosing'+';'+'ChargingID'+';'+'duration'+';'+'ggsnAddress'+';'+'openning time;StartTime;Diagnostics;Radio;ServedIMSI;;;Arquivo'+'\n')
#        ca10.close()


# vac=eo=car=cdb=''
##cpp=open('caminhobruto.txt')
##cdrbruto=cpp.readline().replace('\n','')
##car=cpp.readline().replace('\n','')
##cdb=cpp.readline().replace('\n','')
##cpp.close()
##pro=str(os.getpid())

##ev=open(car+'AcompanhamentoLeitura'+'-'+cdb+'.txt','w')

for i15 in range(1, qp + 1):
    npc = str(i15)

    pp = "pp" + npc

    if tip == "7":
        # pp=subprocess.Popen(['python',diret+'\cdrDados-Gerenciado.py',npc,vac,eo,car,cdb,cdrbruto,str(qp)])
        pp = subprocess.Popen(
            [
                "python",
                diret + "\\Volte3gpp.py",
                npc,
                vac,
                eo,
                car,
                cdb,
                cdrbruto,
                str(qp),
                sa,
            ]
        )

    if tip == "10":
        # pp=subprocess.Popen(['python',diret+'\cdrDados-Gerenciado.py',npc,vac,eo,car,cdb,cdrbruto,str(qp)])
        pp = subprocess.Popen(
            [
                "python",
                diret + "\\stirtim.py",
                npc,
                vac,
                eo,
                car,
                cdb,
                cdrbruto,
                str(qp),
                sa,
            ]
        )

    if tip == "9":
        # pp=subprocess.Popen(['python',diret+'\cdrDados-Gerenciado.py',npc,vac,eo,car,cdb,cdrbruto,str(qp)])
        pp = subprocess.Popen(
            [
                "python",
                diret + "\\VolteClaro.py",
                npc,
                vac,
                eo,
                car,
                cdb,
                cdrbruto,
                str(qp),
                sa,
            ]
        )

    if tip == "6":
        # pp=subprocess.Popen(['python',diret+'\cdrDados-Gerenciado.py',npc,vac,eo,car,cdb,cdrbruto,str(qp)])
        # pp=subprocess.Popen(['python',diret+'\\rodaDados.py',npc,vac,eo,car,cdb,cdrbruto,str(qp),sa])
        pp = subprocess.Popen(
            [
                "python",
                diret + "\\cdrDados.py",
                npc,
                vac,
                eo,
                car,
                cdb,
                cdrbruto,
                str(qp),
                sa,
            ]
        )

    if tip == "1":
        # pp=subprocess.Popen(['python',diret+'\cdrDados-Gerenciado.py',npc,vac,eo,car,cdb,cdrbruto,str(qp)])
        # pp=subprocess.Popen(['python',diret+'\\rodaericsson.py',npc,vac,eo,car,cdb,cdrbruto,str(qp),sa,tip2])
        pp = subprocess.Popen(
            [
                "python",
                # diret + "\\cdrVozEricsson.py",
                npc,
                vac,
                eo,
                car,
                cdb,
                cdrbruto,
                str(qp),
                sa,
                tip2,
            ]
        )
    if tip == "4":
        # pp=subprocess.Popen(['python',diret+'\cdrDados-Gerenciado.py',npc,vac,eo,car,cdb,cdrbruto,str(qp)])
        pp = subprocess.Popen(
            [
                "python",
                diret + "\\rodahuawei.py",
                npc,
                vac,
                eo,
                car,
                cdb,
                cdrbruto,
                str(qp),
                sa,
            ]
        )
    if tip == "2" or tip == "3" or tip == "5":
        # pp=subprocess.Popen(['python',diret+'\cdrDados-Gerenciado.py',npc,vac,eo,car,cdb,cdrbruto,str(qp)])
        # pp=subprocess.Popen(['python',diret+'\\rodanokia.py',npc,vac,eo,car,cdb,cdrbruto,str(qp),sa,tip])
        pp = subprocess.Popen(
            [
                "python",
                diret + "\\cdrVozNokia.py",
                npc,
                vac,
                eo,
                car,
                cdb,
                cdrbruto,
                str(qp),
                sa,
                tip,
            ]
        )
# cdb=cdrbruto[-30:].replace("/",'').replace('.','').replace('*','')
opera = ""


k6 = 0
k5 = 0
ld = []
nldo = []

# aux=os.listdir('sinalfim/')
# e1=''

k55 = 0
k56 = 0  ##                                    if ve[4:14]=='a229bf4582' and ve[-6:]=='800145':
##                                        m=m+24
##                                        #print(na,dt,dh,nb,du)
##                                        ca2=dtf+' '+dhf;ca1=dt+' '+dh
##                                        if len(ca2)==len(ca1):
##                                            s = datetime.strptime(ca2,'%Y-%m-%d %H-%M-%S')
##
##                                            t = datetime.strptime(ca1,'%Y-%m-%d %H-%M-%S')
##
##                                            dif = (s-t);dif=dif.total_seconds()
##                                            du2=str(int(dif))
##
##
##                                    #vv=na+';'+dt+';'+dh+';'+tch+';'+nb+';'+ntt+';'+nbb+';'+du+';'+cel+';'+imsi+';'+imei+';'+msc+';'+ref+';'+ctt+';'+ro+'&'+rd+';'+me
##                                    vv=dt+';'+dh+';'+tcd+';'+me3+';'+me+';'+ho4+';'+ho5+';'+ho6+';'+ho7
##
##                                    pp.append(vv)
##                                    #tas.add(tag)#+tas2)
##                                    tas2=''
##
##                                    na=nb=dt=dh=du=cel=dtf=dhf=tch=ho=me=vm=dt2=dh2=dt3=dh3=du2=zc=ro=rd=ref=ctt=''
##                                    tu=imsi=ntt=tu2=imei=msc=nbb=zc2=''

k57 = 0

pr = set()
tam = {}
rea = 0

print(len(arqb))
aca = int(len(arqb) * aca2 / 100)
aca4 = aca

if vac == "a":
    n11 = 0
    nas3 = set()
    nr11 = ""
    ve11 = 0
    while k56 != len(arqb):
        tp41 = glob.glob(car + "f" + cdb + "*")
        try:
            for z2 in tp41:
                cp = open(z2)

                if vam == "u" or tip in vo:
                    for y2 in cp:
                        # print(y2)
                        #                        ve8=y2.find('05/09/2018')
                        #                        if ve8!=-1:
                        # if y2[0:2]=='55':
                        # print(y2);print(kk)

                        acu.write(y2)

                    cp.close()

                if tip == "6" and (vam == "n" or vam == "d" or vam == "nada"):
                    rea = 0

                    for y2 in cp:
                        #                        print(y2)
                        y22 = y2.split(";")
                        if vam == "d":
                            sar = y22[11][0:13].replace("/", "-").replace(" ", "-")
                            if y22[11] == "":
                                if y22[10] == "":
                                    sar = "semdata"
                                else:
                                    sar = (
                                        y22[10][0:13]
                                        .replace("/", "-")
                                        .replace(" ", "-")
                                    )
                        else:
                            # sar=(y22[3].replace('f',''))[-11:][0:5]
                            sar = (y22[3].replace("f", ""))[-11:][0:4]

                            if y22[3] == "":
                                sar = "semnumero"

                        if sar + nr11 not in pr:
                            rea = rea + 1
                            reas = str(rea)
                            reas = open(
                                car + eo + cdb + tcd + "\\" + sar + nr11 + ".txt", "w"
                            )
                            reas.write(
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
                            pr.add(sar + nr11)
                            tam[sar + nr11] = reas
                            # reas.write(y2)
                            nas3.add(sar)

                        if sar + nr11 in pr:
                            #                            ve9=0
                            #                            try:
                            #                                y22=y2.split(';')
                            #                                y23=y22[2].split('-')
                            #                                if y22[0]=='55' and y23[2] in lac9:
                            #                                    ve9=1
                            #                            except IndexError:
                            #                                pass
                            #
                            #
                            #                            if ve9==1:
                            if 4 > 3:
                                try:
                                    tam[sar + nr11].write(y2)
                                except OSError:
                                    tam[sar + nr11].write(y2)

                    #                            print(sar)
                    #                            input()
                    cp.close()
                    if len(tam) > 7999:
                        n11 = n11 + 1
                        nr11 = "-" + str(n11)
                        for zu2 in tam:
                            tam[zu2].close()

                if (tip == "9") and (vam == "n" or vam == "d" or vam == "nada"):
                    rea = 0

                    for y2 in cp:
                        #                        print(y2)
                        y22 = y2.split(";")
                        if vam == "d":
                            sar = (
                                y22[0] + "-" + y22[1][0:2]
                            )  # [0:13].replace('/','-').replace(' ','-')
                            if y22[0] == "":
                                if y22[7] == "":
                                    sar = "semdata"
                                else:
                                    sar == y22[7] + "-" + y22[8][
                                        0:2
                                    ]  # y22[10][0:13].replace('/','-').replace(' ','-')
                        else:
                            # sar=(y22[2].replace('f',''))[-11:][0:4]

                            if len(y22[2]) > 9:
                                # sar=(y22[0].replace('f',''))[-11:][0:4]

                                if y22[2][0:2] == "55" and (
                                    len(y22[2].replace("f", "")) == 12
                                    or len(y22[2].replace("f", "")) == 13
                                ):
                                    sar = y22[2][2:6]
                                else:
                                    if len(y22[2].replace("f", "")) == 10:
                                        sar = y22[2][0:4]
                                    else:
                                        sar = (y22[2].replace("f", ""))[-11:][0:4]

                            if y22[2] == "":
                                sar = "semnumero"

                        if sar + nr11 not in pr:
                            rea = rea + 1
                            reas = str(rea)
                            reas = open(
                                car + eo + cdb + tcd + "\\" + sar + nr11 + ".txt", "w"
                            )
                            reas.write(
                                "Data;Hora;Originador;TipoCDR;NúmeroChamado;Duração;Célula\n"
                            )
                            pr.add(sar + nr11)
                            tam[sar + nr11] = reas
                            # reas.write(y2)
                            nas3.add(sar)

                        if sar + nr11 in pr:
                            #                            ve9=0
                            #                            try:
                            #                                y22=y2.split(';')
                            #                                y23=y22[2].split('-')
                            #                                if y22[0]=='55' and y23[2] in lac9:
                            #                                    ve9=1
                            #                            except IndexError:
                            #                                pass
                            #
                            #
                            #                            if ve9==1:
                            if 4 > 3:
                                tam[sar + nr11].write(y2)

                    #                            print(sar)
                    #                            input()
                    cp.close()
                    if len(tam) > 7999:
                        n11 = n11 + 1
                        nr11 = "-" + str(n11)
                        for zu2 in tam:
                            tam[zu2].close()

                if (tip == "7" or tip == "10") and (
                    vam == "n" or vam == "d" or vam == "nada"
                ):
                    rea = 0

                    for y2 in cp:
                        #                        print(y2)
                        y22 = y2.split(";")
                        if vam == "d":
                            sar = (
                                y22[1] + "-" + y22[2][0:2]
                            )  # [0:13].replace('/','-').replace(' ','-')
                            if y22[1] == "":
                                sar = "semdata"

                        #                                if y22[7]=='':
                        #                                    sar='semdata'
                        #                                else:
                        #                                    sar==y22[7]+'-'+y22[8][0:2]#y22[10][0:13].replace('/','-').replace(' ','-')
                        else:
                            if len(y22[0]) > 9:
                                # sar=(y22[0].replace('F','''10'))[-11:][0:4]

                                if y22[0][0:2] == "55" and (
                                    len(y22[0].replace("F", "")) == 12
                                    or len(y22[0].replace("F", "")) == 13
                                ):
                                    sar = y22[0][2:6]
                                else:
                                    if len(y22[0].replace("F", "")) == 10:
                                        sar = y22[0][0:4]

                                    else:
                                        sar = (y22[0].replace("F", ""))[-11:][0:4]

                            else:
                                if y22[0] == "":
                                    sar = "semnumero"
                                else:
                                    sar = "poucosdigitos"

                        if sar + nr11 not in pr:
                            rea = rea + 1
                            reas = str(rea)

                            reas = open(
                                car + eo + cdb + tcd + "\\" + sar + nr11 + ".txt", "w"
                            )
                            reas.write(
                                "Originador(list-Of-Calling-Party-Address);Data(recordOpeningTime);Hora;TipodeCDR(role-of-Node);called-Party-Address(NúmeroChamado);dialled-Party-Address(NúmeroTeclado);List-Of-Called-Asserted-Identity;Duration;Célula(accessNetworkInformation);IMSI(List-of-Subscription-ID);IMEI(private-User-Equipment-Info);MSC-Number;network-Call-Reference;causeForRecordClosing;interOperatorIdentifiers;sIP-Method\n"
                            )
                            pr.add(sar + nr11)
                            tam[sar + nr11] = reas
                            # reas.write(y2)
                            nas3.add(sar)

                        if sar + nr11 in pr:
                            #                            ve9=0
                            #                            try:
                            #                                y22=y2.split(';')
                            #                                y23=y22[2].split('-')
                            #                                if y22[0]=='55' and y23[2] in lac9:
                            #                                    ve9=1
                            #                            except IndexError:
                            #                                pass
                            #
                            #
                            #                            if ve9==1:
                            if 4 > 3:
                                tam[sar + nr11].write(y2)

                    #                            print(sar)
                    #                            input()
                    cp.close()
                    if len(tam) > 7999:
                        n11 = n11 + 1
                        nr11 = "-" + str(n11)

                        for zu2 in tam:
                            tam[zu2].close()

                pj2 = z2.find("N.txt")
                if pj2 != -1:
                    nldo.append(z2)
                #                else:
                #                    arli.write(z2+'\n')
                os.remove(z2)
                k56 = k56 + 1
                k57 = k57 + 1

                #                if k56>aca:
                #                    print(int(k56*100/len(arqb)),'%')
                #                aca=k56+aca
                if k57 == aca:
                    # print(''('AGUARDANDO...','green'),end='')
                    print(str(int(k56 * 100 / len(arqb))) + "%")
                    k57 = 0

        except PermissionError:
            pass
        except FileNotFoundError:
            pass

    for zu in tam:
        tam[zu].close()

    if nr11 != "":
        for z11 in nas3:
            t53 = glob.glob(car + eo + cdb + tcd + "\\" + z11 + "*")

            ve15 = 0
            for z12 in t53:
                ve15 = ve15 + 1
                if ve15 == 1:
                    a50 = open(z12, "a")
                    req = z12
                else:
                    a51 = open(z12)
                    a51.readline()
                    for z13 in a51:
                        a50.write(z13)
                    a51.close()
                    os.remove(z12)
            a50.close()
            b4 = req.split("-")

            b5 = b4[len(b4) - 1].replace(".txt", "")

            b6 = req.replace("-" + b5, "")
            os.rename(req, b6)
    #    else:
    #            t56=glob.glob(car+eo+cdb+tcd+'\\*.txt')
    #            for z20 in t56:
    #                req2=z20.replace('-0','')
    #                os.rename(z20,req2)

    if tip in vo or vam == "u":
        acu.close()
    for r6 in nldo:
        r6 = (r6.split(";"))[1].replace("N.txt", "")
        arnli.write(r6 + "\n")
        print()
        print()
        print(
            'Não lido ou lido parcialmente (veja arquivos "arquivosnaolidos" e "arquivosparaleitura"):'
        )
        print(r6)
else:
    tp42 = glob.glob(car + eo + cdb + "\\*\\*f*.txt")
    aca3 = len(tp42)
    while len(tp42) != len(arqb):
        tp42 = glob.glob(car + eo + cdb + "\\*\\*f*.txt")

        if len(tp42) > aca3:
            if len(tp42) > aca4:
                print(str(int(len(tp42) * 100 / len(arqb))) + "%", end=" ")
                aca4 = len(tp42) + aca
        aca3 = len(tp42)
    for pj in tp42:
        pj1 = pj.find("N.txt")
        if pj1 != -1:
            arnli.write(pj)
            print()
            print()
            print(
                'Não lido ou lido parcialmente (veja arquivos "arquivosnaolidos" e "arquivosparaleitura"):'
            )
            print(pj)
pz1 = 0
for pz in arqb:
    pz1 = pz1 + 1
    arli.write(str(pz1) + ";" + pz + "\n")
arli.close()
arnli.close()
print()
print("Duração da leitura: ", datetime.now() - ti)
print()
ti2 = datetime.now()
if vac1 == "a" and tip in vo:
    print("Início de consolidação e ordenação...", ti2)
    print()
    if tip == "1":
        # p=subprocess.call(['python3','setupOrdena.py','build_ext','--inplace'])
        p = subprocess.call(
            ["python", "cdrEricssonVozOrdenaAglutina.py", car, cdb, eo, da]
        )

        # p2=subprocess.call(['python3','rodaOrdena.py',car,cin,eo,da])
    ##    print(p,p2,'ok')
    if tip == "2" or tip == "3" or tip == "5":
        # p=subprocess.call(['python3','cdrNokiaVozOrdenaAglutina.py',car,cin,eo,da])
        # p=subprocess.call(['python','setupOrdenaNokia.py','build_ext','--inplace'])
        # p=subprocess.call(['python','rodaOrdenaNokia.py',car,cdb,eo,da])
        p = subprocess.call(
            ["python", diret + "\\cdrNokiaVozOrdenaAglutina.py", car, cdb, eo, da]
        )
    if tip == "4":
        p = subprocess.call(
            ["python", "cdrHuaweiVozOrdenaAglutina.py", car, cdb, eo, da]
        )


if vac == "a" and tip in vo and vam == "u":
    print("Duração da consolidação e ordenação: ", datetime.now() - ti2)
    print()
    print("Duração total: ", datetime.now() - ti)


if tip in vo and (vam == "n" or vam == "d" or vam == "nada") and vac == "a":
    print("Duração da consolidação e ordenação: ", datetime.now() - ti2)
    print()
    print("Início da redistribuição de CDRs nos tipos escolhidos de arquivos de saída")

    tp41 = glob.glob(car + "Voz*" + cdb + "*")
    if len(tp41) == 1:
        sar = ""
        pr = set()
        tam = {}
        rea = 0
        n9 = 0
        nas3 = set()
        te30 = 1
        nas4 = set()
        n3 = 0
        while te30 == 1:
            cp = open(tp41[0])

            # rea=0
            cp.readline()
            pr = set()
            tam = {}
            rea = 0
            sar = ""
            y28 = ""
            for y2 in cp:
                #                        print(y2)
                y22 = y2.split(";")
                if vam == "d":
                    if tip == "2" or tip == "3" or tip == "5":
                        sar = y22[3][0:13].replace("/", "-").replace(" ", "-")
                        if y22[3] == "":
                            sar = "semdata"
                    if tip == "1":
                        sar = (
                            y22[2].replace("/", "-").replace(" ", "-")
                            + "-"
                            + y22[3][0:2]
                        )
                        if y22[2] == "":
                            sar = "semdata"
                    if tip == "4":
                        sar = y22[2][0:13].replace("/", "-").replace(" ", "-")
                        if y22[2] == "":
                            sar = "semdata"
                else:
                    if tip == "2" or tip == "3" or tip == "5":
                        y28 = y22[7].replace("f", "")
                        if len(y28) > 9:
                            if y28[0:2] == "55" and (len(y28) == 12 or len(y28) == 13):
                                sar = y28[2:6]
                            else:
                                if len(y28) == 10:
                                    sar = y28[0:4]
                                else:
                                    sar = (y28)[-11:][0:4]

                        else:
                            if y28 == "":
                                sar = "semnumero"
                            else:
                                sar = "poucosdigitos"

                    #                                        if y22[7][0:2]=='55':
                    #                                            sar=y22[7][2:6]
                    #                                        else:
                    #                                            sar=(y22[7].replace('f',''))[-11:][0:4]
                    #
                    #                                        if y22[7]=='':
                    #                                            sar='semnumero'
                    if tip == "1":
                        y28 = y22[1].replace("f", "")
                        if len(y28) > 9:
                            if y28[0:2] == "55" and (len(y28) == 12 or len(y28) == 13):
                                sar = y28[2:6]
                            else:
                                if len(y28) == 10:
                                    sar = y28[0:4]
                                else:
                                    sar = (y28)[-11:][0:4]

                        else:
                            if y28 == "":
                                sar = "semnumero"
                            else:
                                sar = "poucosdigitos"
                        # if len(y22[1]).replace('f','')
                    #                                        sar=(y22[1].replace('f',''))[-11:][0:4]
                    #
                    #                                        if y22[1]=='':
                    #                                            sar='semnumero'
                    if tip == "4":
                        y28 = y22[3].replace("f", "")
                        if len(y28) > 9:
                            if y28[0:4] == "1955" and (
                                len(y28) == 14 or len(y28) == 15
                            ):
                                sar = y28[4:8]
                            else:
                                if len(y28) == 10:
                                    sar = y28[0:4]
                                else:
                                    sar = (y28)[-11:][0:4]

                        else:
                            if y28 == "":
                                sar = "semnumero"
                            else:
                                sar = "poucosdigitos"

                #                                        sar=(y22[3].replace('f',''))[-11:][0:4]
                #
                #                                        if y22[3]=='':
                #                                            sar='semnumero'

                #                                if len(nas)<8000 and na not in nas4:
                #            if na not in nas:
                #                nas.add(na)
                #                naq=naq+1
                #                naq2=str(naq)
                #                naq2=open(db+'/'+na+'.txt','w')
                #                naq2.write('Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;PMM;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;Subscription_Type_ou_IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto'+'\n')
                #                tam[na]=naq2
                #                nas4.add(na)
                #
                #        if na in tam:
                #            tam[na].write(i)
                #        if n==0:
                #            nas3.add(na)
                #
                #    a.close()

                if len(pr) < 8000 and sar not in nas4:
                    if sar not in pr:
                        rea = rea + 1
                        reas = str(rea)
                        reas = open(car + eo + cdb + tcd + "\\" + sar + ".txt", "w")
                        if tip == "1":
                            reas.write(
                                "Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;IMSI;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto"
                                + "\n"
                            )
                        if tip == "2" or tip == "3" or tip == "5":
                            reas.write(
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
                        if tip == "4":
                            reas.write(
                                "TipodeCDR;ReferenciadeRede;DataHora;Origem;Destino;Duracao;Causefortermination;Diagnóstico;Célula;ReferenciaCentral;Atendimento;Ocupaçãocanaltráfego;Arquivo"
                                + "\n"
                            )
                        pr.add(sar)
                        tam[sar] = reas

                        nas4.add(sar)
                        # reas.write(y2)

                if sar in tam:
                    tam[sar].write(y2)

                if n9 == 0:
                    nas3.add(sar)

            #                            print(sar)
            #                            input()
            cp.close()
            n9 = n9 + 1

            for z in tam:
                tam[z].close()
                n3 = n3 + 1

            if len(nas3) == n3:
                te30 = 0

        sar = ""
        pr = set()
        tam = {}
        rea = 0
        n9 = 0
        nas3 = set()
        te30 = 1
        nas4 = set()
        n3 = 0

        os.remove(tp41[0])

    #                        tp48=glob.glob(car+cdb+'*')
    #                        for zi in tp48:
    #                            zii=zi.split('\\')
    #                            cons=zii[len(zii)-1]
    #                            os.rename(zi,car+eo+cdb+'\\'+cons+'.txt')
    else:
        print("Não foi identificado arquivo para separação")
        print()
if vz2 == 1:
    print("Excluindo descompactação...")
    shutil.rmtree(cdrbrutodes + "descomp")

print("Processamento encerrado.")
if tip in vo and (vam == "n" or vam == "d"):
    print()
    print("Duração total:", datetime.now() - ti)
    print()

rff = open(car + eo + cdb + tcd + "FIM.txt", "w")
rff.close()

##print('Tecle "Enter" para finalizar')
##
##input()


# for i in range(80000000):
#    b8=1
# quit()

##def cdr(xy):
##
##    cdef list ppp,pp,ad
##
##
##    cdef int tso,nn,xx,du,tord,tma,so
if 4>3:

    import os,gzip,binascii,time, datetime,shutil,glob,tarfile,sys,subprocess,io,shelve
    from datetime import datetime
    from operator import itemgetter
    #ti9=datetime.now()
    diret=os.getcwd()+'\\'
    tord=6000000# tamanho máximo a ordenar na memória (trecho: ordenar)
    tma=5000000# tamanho máximo de arquivo a ser ordenado de uma vez na memória (trecho: ordenar)
    #npp=sys.argv[1];tord=int(sys.argv[2])
    car=sys.argv[1];cdb=sys.argv[2];oe=sys.argv[3];da=sys.argv[4]
    da9=da
    #cdb='2018-07-18 17-58-48,228891';car=''
    #da=car+'Acumula'+cdb+'.txt'
    #da=car+oe+'Acumula'+cdb+'.txt'
    xx=15

    tm=time.asctime().replace(':','').replace(' ','')
    tr=datetime.now()
##    print(tr)
    icn='s'
    opid={'0':'sID','02':'TIM','03':'TIM','04':'TIM','05':'CLARO','06':'CLARO','08':'CLARO','12':'CLARO','14':'CLARO','16':'OI','31':'OI','24':'OI','23':'VIVO','13':'VIVO','19':'VIVO','21':'VIVO','10':'VIVO','11':'VIVO'}

    if len(glob.glob(car+'Arqparciais'+cdb))!=0:#Ordenar - início - versão 07/2018
        shutil.rmtree(car+'Arqparciais'+cdb)
    os.mkdir(car+'Arqparciais'+cdb)

    aaq=[]
    cc=0
    pr=set()
    tam={}
    tamo=[]
    aae={}
    soa=set()
    #d=open(da)





    rea=0
    #while rea==0:
    d=open(da)

    d6=open(car+cdb+'unico.txt','w')
    #d7=open(car+cdb+'pconsolidar.txt','w')
    ve9=0
    for i in d:

        if i[0:3]=='ORI' or i[0:3]=='TER':
            ve9=1
            #d7.write(i)
            #pr.add(i[0:xx])
            cc=cc+1
    ##        if cc/tord==int(cc/tord):
    ##            print(cc)
            if i[0:xx]in tam:
                tam[i[0:xx]]=tam[i[0:xx]]+1
            else:
                tam[i[0:xx]]=1
        else:
            jj=i.split(';')
            j2=jj[11].split(':')
            try:
                du=int(j2[0])*3600+int(j2[1])*60+int(j2[2])
            except ValueError:
                if jj[11]=='':
                    du=0

            da2='20'+jj[3].replace('/','-')
            dah=da2+';'+jj[4]
            d6.write(jj[2]+';'+jj[8]+';'+dah+';'+jj[0]+';'+jj[1]+';'+jj[5]+';'+jj[6]+';'+jj[7]+';'+jj[9]+';'+jj[10]+';'+str(du)+';'+jj[12]+';'+jj[13]+';'+jj[14]+';'+jj[15]+';'+jj[16]+';'+jj[17]+';'+jj[18]+';'+jj[19]+';'+jj[20]+';'+jj[21]+';'+jj[22]+';'+jj[23]+';'+jj[24]+';'+jj[25])


    d.close()
    d6.close()
    #d7.close()
    #os.remove(da)
    #da=car+cdb+'pconsolidar.txt'
##    print(len(tam))

    if len(tam)!=0:

        tamo=sorted(tam.items(),key=itemgetter(0))


        so=0
        ie=tamo[0][0]
        for i in tamo:
            if i[1]>tord:
                soa.add(i[0])
            so=so+i[1]
        ##    print('tamo',i[0],i[1])
        ##    print(so)
            if so>tma:
                ie=i[0]
                so=i[1]
            aae[i[0]]=ie
            pr.add(ie)





        ##    if len(pr)>600:
        ##        xx=xx-1
        ##        print(xx)
        ##        rea=0
        ##        cc=0
        ##        pr=set()
        ##        tam={}
        ##    else:
        ##        rea=1

    ##    print(xx)    D:\Monitoramento\processados
    ##    print(len(pr))
    ##    print(datetime.now()-tr)


        if len(glob.glob(car+'Auxiliar'+cdb))!=0:
            shutil.rmtree(car+'Auxiliar'+cdb)
        os.mkdir(car+'Auxiliar'+cdb)

        pra=open(car+'Auxiliar'+cdb+'\\pr','w')
        for i in pr:
            pra.write(i+'\n')
        pra.close()
        aaea=open(car+'Auxiliar'+cdb+'\\aae','w')
        for i in aae:
            aaea.write(i+'|'+aae[i]+'\n')
        aaea.close()


        import dividearq
        dividearq.div(xx,car,cdb,da)



    ##    for i in pr:
    ##        globals()['a'+i]=open(diret+'Arqparciais'+cdb+'/'+i+'.txt','w')
    ##    d=open(da)
    ##    for j in d:
    ##        #print(aae[j[0:xx]])
    ##        b=globals()['a'+aae[j[0:xx]]]
    ##        #b=globals()['a'+j[0:xx]]
    ##        b.write(j)
    ##    d.close()
    ##
    ##    for i in pr:
    ##        b=globals()['a'+i]
    ##        b.close()

    ##    print(datetime.now()-tr)

        ad=glob.glob(car+'Arqparciais'+cdb+'\\*.txt')
        ad.sort()
        os.remove(da)
        re=open(car+cdb+'ord3.txt','w')
        ppp=[]
        for t in ad:
            zi=(t.split('\\'))
            zi=zi[len(zi)-1].replace('.txt','')
    ##        print(t)
            if zi in soa:
    ##            print('soa',zi)
            #if (os.path.getsize(t))>tma:
                xx=xx+1
                tam={}#ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
                pr=set()
                pr1=[]
                pr2={}
                pp=[]
                import os
                d=open(t)
                #d.readline()
                for i in d:

                    pr.add(i[0:xx])
                    if i[0:xx]in tam:
                        tam[i[0:xx]]=tam[i[0:xx]]+1
                    else:
                        tam[i[0:xx]]=1
                d.close()
                for i in pr:
                        pr1.append(i)
                pr1.sort()
                tso=0
                nn=1
                for i in pr1:
    ##    ##            print(i,tam[i])
                    tso=tam[i]+tso
                    if tso<=tord:
                        pr2[i]=nn
                    else:
                        nn=nn+1
                        tso=tam[i]
                        pr2[i]=nn
                for i in range(pr2[pr1[0]],pr2[pr1[len(pr1)-1]]+1):
                    d=open(t)
                    #d.readline()
                    for i1 in d:
                        if pr2[i1[0:xx]]==i:
                            pp.append(i1)
                    d.close()
                    pp.sort()
    ##                print(i,len(pp))
                    for i2 in pp:
                        re.write(i2)
                    pp=[]
                os.remove(t)
                pr=set()
                pr1=[]
                pr2={}
                tam={}
            else:
                d=open(t)
                for i3 in d:
                    ppp.append(i3)
                d.close()
                ppp.sort()
                for i3 in ppp:
                    re.write(i3)
                ppp=[]
                os.remove(t)
    ##        print(datetime.now()-tr)
        re.close()#ordenar - fim
    ##    print(datetime.now()-tr)



        #os.remove(da)
        re4=open(car+cdb+'ord3.txt')
        r=open(car+cdb+'unico.txt','a')
        con=open(car+cdb+'consolidado.txt','w')
        j=re4.readline()
        jj=j.split(';')


        j2=jj[11].split(':')
        try:
            du=int(j2[0])*3600+int(j2[1])*60+int(j2[2])
        except ValueError:
            if jj[11]=='':
                du=0

        da2='20'+jj[3].replace('/','-')
        dah=da2+';'+jj[4]
        ref=jj[2]
        ref2=jj[8]
        ref3=jj[9]


        for i in re4:
            tf=1
            ii=i.split(';')

            i2=ii[11].split(':')
            if ii[2]!='':
                #if ii[2]==ref and (ii[0]=='ORI' or ii[0]=='TER' or ii[0]=='ROA'):
                if ii[2]==ref and (ii[0]=='ORI' or ii[0]=='TER') and ii[8]==ref2:
                    con.write(j)
                    while ii[2]==ref and ii[8]==ref2:
                        con.write(i)
                        try:
                            du=du+int(i2[0])*3600+int(i2[1])*60+int(i2[2])

                        except ValueError:
                            du=ii[11]
                        except TypeError:
                            du=ii[11]

                        ref=ii[2]
                        ref2=jj[8]
                        ref3=jj[9]
                        ju=i.split(';')
                        i=re4.readline()
                        if i=='':
                            break
                        ii=i.split(';')
                        i2=ii[11].split(':')
        ##            print(ju[5]+';'+ju[6]+';'+ju[7]+';'+dah+';'+ju[10]+';'+ju[11]+';'+ju[12]+';'+ju[13]+';'+ju[14]+';'+ju[15]+';'+ju[16]+';'+str(du)+';'+ju[18]+';'+ju[19]+';'+ju[20]+';'+ju[21]+';'+ju[22]+';'+ju[23]+';'+ju[24]+';'+ju[25]+';'+ju[26]+';'+ju[27])
        ##            print(kk)
        ##                con.write(ju[1]+';'+ju[2]+';'+dah+';'+ju[0]+';'+ju[5]+';'+ju[6]+';'+ju[7]+';'+ju[8]+';'+ju[9]+';'+ju[10]+';'+str(du)+';'+ju[12]+';'+ju[13]+';'+ju[14]+';'+ju[15]+';'+ju[16]+';'+ju[17]+';'+ju[18]+';'+ju[19]+';'+ju[20]+';'+ju[21]+';'+ju[22])
        ##                r.write(ju[1]+';'+ju[2]+';'+dah+';'+ju[0]+';'+ju[5]+';'+ju[6]+';'+ju[7]+';'+ju[8]+';'+ju[9]+';'+ju[10]+';'+str(du)+';'+ju[12]+';'+ju[13]+';'+ju[14]+';'+ju[15]+';'+ju[16]+';'+ju[17]+';'+ju[18]+';'+ju[19]+';'+ju[20]+';'+ju[21]+';'+ju[22])
                    con.write(ju[2]+';'+ju[8]+';'+dah+';'+ju[0]+';'+ju[1]+';'+ju[5]+';'+ju[6]+';'+ju[7]+';'+ju[9]+';'+ju[10]+';'+str(du)+';'+ju[12]+';'+ju[13]+';'+ju[14]+';'+ju[15]+';'+ju[16]+';'+ju[17]+';'+ju[18]+';'+ju[19]+';'+ju[20]+';'+ju[21]+';'+ju[22]+';'+ju[23]+';'+ju[24]+';'+ju[25])
                    r.write(ju[2]+';'+ju[8]+';'+dah+';'+ju[0]+';'+ju[1]+';'+ju[5]+';'+ju[6]+';'+ju[7]+';'+ju[9]+';'+ju[10]+';'+str(du)+';'+ju[12]+';'+ju[13]+';'+ju[14]+';'+ju[15]+';'+ju[16]+';'+ju[17]+';'+ju[18]+';'+ju[19]+';'+ju[20]+';'+ju[21]+';'+ju[22]+';'+ju[23]+';'+ju[24]+';'+ju[25])
                    tf=0
                    j=i
                    if j=='':
                        break
                    jj=i.split(';')
                    j2=jj[11].split(':')
                    try:
                        du=int(j2[0])*3600+int(j2[1])*60+int(j2[2])

                    except ValueError:
                        if jj[11]=='':
                            du=0
                        else:
                            du=jj[11]
                    da2='20'+jj[3].replace('/','-')
                    dah=da2+';'+jj[4]
                    ref=jj[2]
                    ref2=jj[8]
                    ref3=jj[9]
                    #print(i)
                else:
        ##            print(jj[5]+';'+jj[6]+';'+jj[7]+';'+dah+';'+jj[10]+';'+jj[11]+';'+jj[12]+';'+jj[13]+';'+jj[14]+';'+jj[15]+';'+jj[16]+';'+str(du)+';'+jj[18]+';'+jj[19]+';'+jj[20]+';'+jj[21]+';'+jj[22]+';'+jj[23]+';'+jj[24]+';'+jj[25]+';'+jj[26])
        ##            print(kk)
        ##                r.write(jj[1]+';'+jj[2]+';'+dah+';'+jj[0]+';'+jj[5]+';'+jj[6]+';'+jj[7]+';'+jj[8]+';'+jj[9]+';'+jj[10]+';'+str(du)+';'+jj[12]+';'+jj[13]+';'+jj[14]+';'+jj[15]+';'+jj[16]+';'+jj[17]+';'+jj[18]+';'+jj[19]+';'+jj[20]+';'+jj[21]+';'+jj[22])
                    r.write(jj[2]+';'+jj[8]+';'+dah+';'+jj[0]+';'+jj[1]+';'+jj[5]+';'+jj[6]+';'+jj[7]+';'+jj[9]+';'+jj[10]+';'+str(du)+';'+jj[12]+';'+jj[13]+';'+jj[14]+';'+jj[15]+';'+jj[16]+';'+jj[17]+';'+jj[18]+';'+jj[19]+';'+jj[20]+';'+jj[21]+';'+jj[22]+';'+jj[23]+';'+jj[24]+';'+jj[25])
                    j=i
                    if j=='':
                        break
                    jj=i.split(';')
                    j2=jj[11].split(':')
                    #print(i)
                    try:
                        du=int(j2[0])*3600+int(j2[1])*60+int(j2[2])
                    except ValueError:
                        if jj[11]=='':
                            du=0
                        else:
                            du=jj[11]
                    da2='20'+jj[3].replace('/','-')
                    dah=da2+';'+jj[4]
                    ref=jj[2]
                    ref2=jj[8]
                    ref3=jj[9]
        if tf==1:
        ##        r.write(jj[1]+';'+jj[2]+';'+dah+';'+jj[0]+';'+jj[5]+';'+jj[6]+';'+jj[7]+';'+jj[8]+';'+jj[9]+';'+jj[10]+';'+str(du)+';'+jj[12]+';'+jj[13]+';'+jj[14]+';'+jj[15]+';'+jj[16]+';'+jj[17]+';'+jj[18]+';'+jj[19]+';'+jj[20]+';'+jj[21]+';'+jj[22])
            r.write(jj[2]+';'+jj[8]+';'+dah+';'+jj[0]+';'+jj[1]+';'+jj[5]+';'+jj[6]+';'+jj[7]+';'+jj[9]+';'+jj[10]+';'+str(du)+';'+jj[12]+';'+jj[13]+';'+jj[14]+';'+jj[15]+';'+jj[16]+';'+jj[17]+';'+jj[18]+';'+jj[19]+';'+jj[20]+';'+jj[21]+';'+jj[22]+';'+jj[23]+';'+jj[24]+';'+jj[25])
        re4.close()
        r.close()
        con.close()

        os.remove(car+cdb+'ord3.txt')

        #print(datetime.now()-tr)
    if ve9==0:
        os.remove(da9)
    da=car+cdb+'unico.txt'
    xx=2

    if len(glob.glob(car+'Arqparciais'+cdb))==1:#Ordenar - início - versão 07/2018
        shutil.rmtree(car+'Arqparciais'+cdb)
    ap3=glob.glob(car+'Arqparciais'+cdb)
    while len(ap3)==1:#teste
        ap3=glob.glob(car+'Arqparciais'+cdb)#teste
    os.mkdir(car+'Arqparciais'+cdb)
    for ap8 in range(10000000):#teste
        ap10=1#teste
    aaq=[]
    cc=0
    pr=set()
    tam={}
    tamo=[]
    aae={}
    soa=set()
    d=open(da)


    for i in d:
        #pr.add(i[0:xx])
        cc=cc+1
##        if cc/tord==int(cc/tord):
##            print(cc)
        if i[0:xx]in tam:
            tam[i[0:xx]]=tam[i[0:xx]]+1
        else:
            tam[i[0:xx]]=1
    d.close()

    tamo=sorted(tam.items(),key=itemgetter(0))
    so=0
    ie=tamo[0][0]
    for i in tamo:
        if i[1]>tord:
            soa.add(i[0])
        so=so+i[1]
    ##    print('tamo',i[0],i[1])
    ##    print(so)
        if so>tma:
            ie=i[0]
            so=i[1]
        aae[i[0]]=ie
        pr.add(ie)
##    print(len(tam))
##    print(xx)
##    print(len(pr))
##    print(datetime.now()-tr)


    if len(glob.glob(car+'Auxiliar'+cdb))==1:
        shutil.rmtree(car+'Auxiliar'+cdb)
    os.mkdir(car+'Auxiliar'+cdb)

    pra=open(car+'Auxiliar'+cdb+'\\pr','w')
    for i in pr:
        pra.write(i+'\n')
    pra.close()
    aaea=open(car+'Auxiliar'+cdb+'\\aae','w')
    for i in aae:
        aaea.write(i+'|'+aae[i]+'\n')
    aaea.close()


    import dividearq
    dividearq.div(xx,car,cdb,da)

##    for i in pr:
##        globals()['a'+i]=open(car+'Arqparciais'+cdb+'/'+i+'.txt','w')
##    d=open(da)
##    for j in d:
##        #b=globals()['a'+j[0:xx]]
##        b=globals()['a'+aae[j[0:xx]]]
##        b.write(j)
##    d.close()
##    for i in pr:
##        b=globals()['a'+i]
##        b.close()

##    print(datetime.now()-tr)
    ad=glob.glob(car+'Arqparciais'+cdb+'\\*.txt')
    ad.sort()
    re=open(car+cdb+'ord4.txt','w')
    os.remove(da)
    re.write('Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;IMSI;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;IMEI;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto'+'\n')
    ppp=[]
    for t in ad:
        zi=(t.split('\\'))
        zi=zi[len(zi)-1].replace('.txt','')
##        print(t)
        if zi in soa:
##            print('soa',zi)
        #if (os.path.getsize(t))>tma:

            xx=xx+1
            tam={}#ordenar - início - verificar o tamanho máximo a ordenar na memória (tord)
            pr=set()
            pr1=[]
            pr2={}
            pp=[]
            import os
            d=open(t)
            #d.readline()
            for i in d:
                pr.add(i[0:xx])
                if i[0:xx]in tam:
                    tam[i[0:xx]]=tam[i[0:xx]]+1
                else:
                    tam[i[0:xx]]=1
            d.close()
            for i in pr:
                    pr1.append(i)
            pr1.sort()
            tso=0
            nn=1
            for i in pr1:
    ##            print(i,tam[i])
                tso=tam[i]+tso
                if tso<=tord:
                    pr2[i]=nn
                else:
                    nn=nn+1
                    tso=tam[i]
                    pr2[i]=nn
            for i in range(pr2[pr1[0]],pr2[pr1[len(pr1)-1]]+1):
                d=open(t)
                #d.readline()
                for i1 in d:
                    if pr2[i1[0:xx]]==i:
                        pp.append(i1)
                d.close()
                pp.sort()
##                print(i,len(pp))
                for i2 in pp:
                    re.write(i2)
                pp=[]
            os.remove(t)
            pr=set()
            pr1=[]
            pr2={}
            tam={}
        else:
            d=open(t)
            for i3 in d:
                ppp.append(i3)
            d.close()
            ppp.sort()
            for i3 in ppp:
                re.write(i3)
            ppp=[]
            os.remove(t)
##        print(datetime.now()-tr)
    re.close()#ordenar - fim
##    print(datetime.now()-tr)
    #os.remove(da)
    g=open(car+cdb+'ord4.txt','r')
    me=''
    an=''
    op='0'
    for i in g:
        ii=i.split(';')
        if (ii[4]=='ORI' or ii[4]=='TER') and ii[7]!='':
    ##        print(ii)
            ii21=ii[2].split('-')
            ii61=ii[7].split('-')
            me=ii21[1]
            an=ii21[0]
            op=ii61[1][0:2]
            break
    g.close()
    if ve9==0:
        rop=oe
    else:
        rop=opid[op]
    os.rename(car+cdb+'ord4.txt',car+'VozEricsson'+'-'+cdb+'-'+rop+'-'+me+an+'.txt')

    if len(glob.glob(car+'Arqparciais'+cdb))==1:
        shutil.rmtree(car+'Arqparciais'+cdb)
    if len(glob.glob(car+'Auxiliar'+cdb))==1:
        shutil.rmtree(car+'Auxiliar'+cdb)
##    print(datetime.now()-tr)
#print(datetime.now()-ti9)
quit()








    ##tam={}#ordenar - início - verificar variável tord (tamanho máximo a ordenar na memória)
    ##pr=set()
    ##pr1=[]
    ##pr2={}
    ##pp=[]
    ##da=car+cdb+'unico.txt'
    ##xx=2# define aproximadamente a quantidade de grupos de pré-ordenação; é desejável que não haja mais de 1000 grupos
    ##import os
    ##d=open(da,'r')
    ###d.readline()
    ##for i in d:
    ####    ii=i.split(';')
    ####    pr.add(ii[4][0:xx])
    ##    pr.add(i[0:xx])
    ##    if i[0:xx]in tam:
    ##        tam[i[0:xx]]=tam[i[0:xx]]+1
    ##    else:
    ##        tam[i[0:xx]]=1
    ##d.close()
    ####for i in tam:
    ####    print(i,tam[i])
    ##for i in pr:
    ##        pr1.append(i)
    ##pr1.sort()
    ##tso=0
    ##nn=1
    ##for i in pr1:
    ####    print(i,tam[i])
    ##    tso=tam[i]+tso
    ##    if tso<=tord:
    ##        pr2[i]=nn
    ##    else:
    ##        nn=nn+1
    ##        tso=tam[i]
    ##        pr2[i]=nn
    ####for i in pr2:
    ####    print(i,pr2[i])
    ####print(pr1[len(pr1)-1])
    ####print(pr2[pr1[0]],pr2[pr1[len(pr1)-1]])
    ##re=open(car+cdb+'ord4.txt','w')
    ##re.write('Referencia;Origem;Data;Hora;Tipo_de_chamada;Bilhetador;PMM;1stCelA;Outgoing_route;Destino;Type_of_calling_subscriber;TTC;Call_position;Fault_code;EOS_info;Internal_cause_and_location;Disconnecting_party;BSSMAP_cause_code;Time_for_calling_party_traffic_channel_seizure;Time_for_called_party_traffic_channel_seizure;Call_identification_number;Translated_number;Subscription_Type;TimefromRregistertoStartofCharging;InterruptionTime;Arquivobruto'+'\n')
    ##for i in range(pr2[pr1[0]],pr2[pr1[len(pr1)-1]]+1):
    ####    print(i)
    ##    d=open(da,'r')
    ##    #d.readline()
    ##    for i1 in d:
    ####            ii1=i1.split(';')
    ####            if ii1[4][0:xx]==i:
    ####                pp.append(ii1[4]+';'+ii1[5]+';'+ii1[2]+';'+ii1[3]+';'+ii1[1]+';'+ii1[0]+';'+ii1[6]+';'+ii1[7]+';'+ii1[8]+';'+ii1[9]+';'+ii1[10]+';'+ii1[11]+';'+ii1[12]+';'+ii1[13]+';'+ii1[14]+';'+ii1[15]+';'+ii1[16]+';'+ii1[17]+';'+ii1[18]+';'+ii1[19]+';'+ii1[20]+';'+ii1[21])
    ##        if pr2[i1[0:xx]]==i:
    ##            pp.append(i1)
    ##    d.close()
    ##    pp.sort()
    ##    for i2 in pp:
    ####            ii2=i2.split(';')
    ####            re.write(ii2[5]+';'+ii2[4]+';'+ii2[2]+';'+ii2[3]+';'+ii2[0]+';'+ii2[1]+';'+ii2[6]+';'+ii2[7]+';'+ii2[8]+';'+ii2[9]+';'+ii2[10]+';'+ii2[11]+';'+ii2[12]+';'+ii2[13]+';'+ii2[14]+';'+ii2[15]+';'+ii2[16]+';'+ii2[17]+';'+ii2[18]+';'+ii2[19]+';'+ii2[20]+';'+ii2[21])
    ##        re.write(i2)
    ##    pp=[]
    ##pr=set()
    ##pr1=[]
    ##pr2={}
    ##tam={}
    ##re.close()#ordenar - fim
    ###os.remove("/Disk3T_03/CDRprocessamento/TIM/"+res+'.txt')
    ##os.remove(da)
    ##g=open(car+cdb+'ord4.txt','r')
    ##me=''
    ##an=''
    ##op='0'
    ##for i in g:
    ##    ii=i.split(';')
    ##    if (ii[4]=='ORI' or ii[4]=='TER') and ii[7]!='':
    ####        print(ii)
    ##        ii21=ii[2].split('-')
    ##        ii61=ii[7].split('-')
    ##        me=ii21[1]
    ##        an=ii21[0]
    ##        op=ii61[1][0:2]
    ##        break
    ##g.close()
    ##os.rename(car+cdb+'ord4.txt',car+'ResEricsson'+'-'+tm+'-'+opid[op]+'-'+me+an+'.txt')
    ##
    ##print(datetime.now()-tr)

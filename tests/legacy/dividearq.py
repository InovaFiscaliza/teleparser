def div(xx,car,cdb,da):
    import os,gzip,binascii,time, datetime,shutil,glob,tarfile,sys,subprocess,io,shelve
    from datetime import datetime
    from operator import itemgetter
    diret=os.getcwd()+'\\'
    #xx=int(sys.argv[1]);car=sys.argv[2];cdb=sys.argv[3]
    #da=car+'Acumula'+cdb+'.txt'
    #xx=20


    pr=set()
    aae={}
    a=open(car+'Auxiliar'+cdb+'\\pr')
    for i in a:
        i=i.replace('/','-')

        pr.add(i.replace('\n',''))
    a.close()
    b=open(car+'Auxiliar'+cdb+'\\aae')
    for i in b:
        i=i.replace('/','-')

        i=i.replace('\n','')
        ii=i.split('|')
        aae[ii[0]]=ii[1]

    b.close()


    for i in pr:
        i=i.replace('/','-')

        globals()['a'+i]=open(car+'Arqparciais'+cdb+'\\'+i+'.txt','w')
    d=open(da)
    for j in d:
        j=j[0:xx].replace('/','-')+j[xx:]

        #print(aae[j[0:xx]])
        b10=j[0:xx]
        if b10 in aae:
            b=globals()['a'+aae[j[0:xx]]]
            #b=vars()['a'+j[0:xx]]
            j=j[0:xx].replace('-','/')+j[xx:]

            b.write(j)



    d.close()

    for i in pr:
        i=i.replace('/','-')
        b=globals()['a'+i]
        b.close()
    #print(datetime.now()-tr)

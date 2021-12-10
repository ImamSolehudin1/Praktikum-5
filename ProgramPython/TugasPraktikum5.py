import os,sys
Oc = os.system
while True:
    print("")
    print("" )
    c = input("T)ambah Data, U)bah Data, H)apus Data, C)ari Data, L)ihat Data, K)eluar: ")
    if c.lower() == 'k':
        break
    elif c.lower() == 't':
        i = open('database.txt','a')
        print(" Tambah Data")
        while (True):
            nama = input(" Nama : ")
            nim  = int(input(" NIM  : "))
            tugas  = int(input(" TUGAS  : "))                
            uts  = int(input(" UTS  : "))
            uas  = int(input(" UAS  : "))
            break
            
        akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
        i.write('\nNama : '+nama+'|Nim : '+str(nim)+'|Tugas : '+str(tugas)+'|UTS : '+str(uts)+'|UAS : '+str(uas)+"|Akhir : "+str(akhir)+'\n')
        i.close()
        Oc("clear")

    elif c.lower() == 'l':
        print("Lihat Data")
        i = open('database.txt','r').read().splitlines()
        print(" ========================================================================")
        print(" ||============================= DAFTAR NILAI =========================||")
        print(" ||====================================================================||")
        print(" ||     NAMA        |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR ||")        
        print(" ||====================================================================||")
        for l in i:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = (l1.strip().split('|'))
                print((' ||')+(nama[:15]).ljust(17)+('| ')+(nim).ljust(17)+('| ')+(tugas).ljust(6)+('| ')+(uts).ljust(6)+('| ')+(uas).ljust(6)+('| ')+(akhir).ljust(6)+('||'))

        print(" ||=================|==================|=======|=======|=======|=======||")
    elif c.lower() == 'c':
        print("Mencari Data")
        cari = input(' Masukan Nama: ')
        i = open('database.txt','r').read().splitlines()
        print(" ||======================================================================")
        print(" ||=========================== DAFTAR KONTAK ==========================||")
        print(" ||====================================================================||")
        print(" ||     NAMA        |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR ||")        
        print(" ||====================================================================||")
        for l in i:
            if l == '':
                pass
            elif cari in l:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = l1.strip().split('|')
                print((' ||')+(nama).ljust(17)+('| ')+(nim).ljust(17)+('| ')+(tugas).ljust(6)+('| ')+(uts).ljust(6)+('| ')+(uas).ljust(6)+('| ')+(akhir).ljust(6)+('||'))
        print(" ||=================|==================|=======|=======|=======|=======||")
    elif c.lower() == 'h':
        print("Menghapus Data")
        u = open('database.txt','r').read().splitlines()
        hapus = input(' Masukan Nama : ')
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = l1.strip().split('|')
                if str(nama) == str(hapus):
                    print('Menghapus %s'%(hapus))
                    pass
                else:      
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')        
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n",'')
            new2.write(i2)
        new2.close()
    elif c.lower() == 'u':
        print("Mengubah Data")
        u = open('database.txt','r').read().splitlines()
        target = input(' Masukan Nama : ')
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = l1.strip().split('|')
                if nama == target:
                    print(' Mengubah Data %s'%(target))
                    while (True):
                        nama = input(" Nama : ")
                        nim  = int(input(" NIM  : "))
                        tugas  = int(input(" TUGAS  : "))
                        uts  = int(input(" UTS  : "))
                        uas  = int(input(" UAS  : "))
                        break
                    akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
                    edit  =('Nama : '+nama+'|Nim : '+str(nim)+'|Tugas : '+str(tugas)+'|UTS : '+str(uts)+'|UAS : '+str(uas)+"|Akhir : "+str(akhir)+'\n')
                    nm.append(edit+'\n')
                else:      
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')        
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n","\n")
            new2.write(i2+'\n')
        new2.close()

    else:
        print("")

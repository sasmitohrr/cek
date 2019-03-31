from texttable import Texttable
table = Texttable()

def gajih():
    nama = []
    jabatan = []
    gaji = []
    jawab = "y"
    while (jawab == 'y'):
        nama.append(input("Masukkan nama: "))
        jab = input("Jabatan: ")
        jabatan.append(jab)
        if (jab == 'Programmer'):
            gaji.append(3000000)
        elif (jab == 'Manajer'):
            gaji.append(5000000)
        else:
            gaji.append(1000000)
        jawab = input("Tambah lagi? ")

    for i in nama:
        idx = nama.index(i)
        table.add_rows([['No','Nama','Jabatan','Gaji'],[1+idx,i,jabatan[idx],gaji[idx]]])                                                                                                                                                                                                                                                                                                                                                
    print (table.draw())



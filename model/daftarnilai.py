print("Program Input Data mahasiswa")
print("____________________________")
print("=== Data Nilai Mahasiswa ===")
print("============================")

data = {}

def input_data():
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = int(input ("Nilai Tugas : "))
    uas = int(input("Nilai UAS : "))
    uts = int(input("Nilai UTS : "))
    a = tugas * 30 / 100
    b = uas * 35 / 100
    c = uts * 35 /100
    akhir = a + b + c


    return {'nim':nim,
            'nama':nama,
            'tugas':tugas,
            'uas':uas,
            'uts':uts,
            'akhir':akhir
            }
def cetak (data={}):
    print("___________________________________________________________________")
    print("| NO |    NIM    |      NAMA      | TUGAS |  UAS  |  UTS  | AKHIR |")
    print("===================================================================")
    if len(data) <= 0:
        print ("===========================BELUM ADA DATA==========================")
    else:
        no = 1
        for x in data.values():
            print("| {0:2} | {1:9} | {2:14} | {3:5} | {4:5} | {5:5} | {6:5.2f} |".format
                (no,x["nim"],x["nama"],x["tugas"],
                x["uas"],x["uts"],float(x["akhir"])))
            no += 1
        print("===================================================================")
while True:
    print("\n=================================")
    c = input("(L) Lihat, (T) Tambah, (U) Ubah, \n"
                     "(H) Hapus, (C) Cari, (K) Keluar: ")
    print("===================================")

    #lihat Data
    if c.lower() =='l':
        print("Daftar data")
        cetak(data)

    #menambahkan Data
    elif c.lower() =='t':
        print("Input Data")
        d = input_data()
        data[d['nama']] = d

    #Mengubah Data
    elif c.lower() =='u':
        nama = input("Masukan nama untuk mengubah data: ")
        if nama in data.keys():
            print("Masukan Data yang diubah :")
            ubah = input("(Semua), (Nama), (NIM), "
                      "(Tugas), (UTS), (UAS) : ")
            if ubah.lower() =="semua":
                print("_______________________")
                print("Ubah Data {}".format(nama))
                print("-----------------------")
                d['nim'] = input("Ubah NIM : ")
                d['tugas'] = int(input("Ubah Nilai Tugas: "))
                d['uas'] = int(input("Ubah Nilai UAS : "))
                d['uts'] = int(input("Ubah Nilai UTS : "))
            elif ubah.lower() =="nama":
                d['nama'] = input("Ubah Nama : ")
            elif ubah.lower() =="nim":
                d['nim'] = input("Ubah Nim : ")
            elif ubah.lower() =="tugas":
                d['tugas'] = int(input("Ubah Nilai Tugas : "))
            elif ubah.lower() =="uts":
                d['uts'] = int(input("Ubah Nilai UTS : "))
            elif ubah.lower() =="uas":
                d['uas'] = int(input("Ubah Nilai UAS : "))
            data[nama]= d

        else:
            print("'{}' Tidak Ditemukan".format(nama))

    #menghapus data
    elif c.lower() =='h':
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in data.keys():
            del data[nama]
            print("Data '{}' dihapus".format(nama))
        else :
            print("'{}' Tidak Ditemukan".format(nama))
    #mencari data
    elif c.lower() =='c':
        print("Mencari Daftar Nilai : ")
        print("=======================")
        nama = input("Masukan nama untuk mencari daftar nilai : ")
        if nama in data.keys():
            print("Nama {0}, dengan NIM : {1}\n"
                  "Nilai Tugas: {2}, UTS: {3}, dan UAS: {4}\n"
                  "dan nilai akhir {5}".format(nama, d['nim'],
                                               d['tugas'], d['uts'],
                                               d['uas'], d['akhir']))
            data[nama]= d
        else :
            print("'{}' Tidak ditemukan".format(nama))

    #mengakhiri
    elif c.lower() =='k':
        break
    else:
        print("Pilih Menu yang tersedia")
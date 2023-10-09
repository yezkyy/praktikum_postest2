from prettytable import PrettyTable
import os
import sys
os.system ("cls")

tabel = PrettyTable()
tabel.field_names = ["No Barang", "Nama Barang", "Harga Barang"]

# Fungsi menambahkan barang ke daftar
def tambah_barang(no_barang, nama_barang, harga_barang):
    tabel.add_row([no_barang, nama_barang, harga_barang])

# Database Barang
tambah_barang("1", "Router Wireless RB951Ui-2HND", "740.000")
tambah_barang("2", "MikroTik hAP lite RB941-2nD", "377.000")
tambah_barang("3", "Huawei Quidway S3026 Switch Hub", "950.000")
tambah_barang("4", "Huawei Quidway S3928TP Switch Hub", "550.000")
tambah_barang("5", "Mikrotik Switch RB260GSP", "745.000")
tambah_barang("6","Routerboard CSS326", "2.566.000")
tambah_barang("7","Routerboard CSS610", "3.550.000")
tambah_barang("8","Huawei HG8546M Wireless Modem Router", "210.000")
tambah_barang("9","Router Huawei HG8245A", "135.000")
tambah_barang("10","ZTE WIRELESS F663N V3A", "289.000")

#membuat fungsi pada 2 Mode Login yaitu admin dan pembeli
def login():
    while True:
        print("=" * 10 + "Selamat Datang di Toko Hardware Jaringan" + "=" * 10)
        print("[1]. Admin")
        print("[2]. Pembeli")
        pilihan = input("Silakan Pilih Mode Login : ")
        if pilihan == "1":
            admin()
        elif pilihan == "2":
            pembeli()
            break
        else:
            print("Mode Login Tidak ada, silakan coba kembali!")
            return login()

#Login Mode Admin
def admin():
    while True:
        print("=" * 10 + "Selamat Datang Admin!" + "=" * 10)
        print("[1]. Tambah Barang")
        print("[2]. Hapus Barang")
        print("[3]. Lihat Barang")
        print("[4]. Perbarui Barang")
        print("[5]. Keluar/Kembali ke Mode Login")
        fitur = input("Silakan Pilih Fitur Yang diinginkan : ")
        if fitur == "1":
            tambah_barang_admin()
        elif fitur == "2":
            hapusbarang()
        elif fitur == "3":
            lihatbarang()
        elif fitur == "4":
            perbaruibarang()
        elif fitur == "5":
            mode_login = input ("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Kembali) : ").capitalize()
            if mode_login == "Keluar":
                print("Terimakasih Telah Menggunakan Program ini ^-^")
                sys.exit()
            elif mode_login == "Kembali":
                login()
        else:
            print("Tidak ada fitur silakan coba lagi")

#Fitur admin Tambah Barang
def tambah_barang_admin():
    while True:
        no_barang = input("Masukan Nomor Barang: ")
        nama_barang = input("Masukan Nama Barang: ")
        harga_barang = input("Masukan Harga Barang: ")
        tambah_barang(no_barang, nama_barang, harga_barang)
        print(f"Nomor Barang [{no_barang}] dengan nama [{nama_barang}] Berhasil Ditambahkan seharga [Rp.{harga_barang}]")
        pilihan = input("Apakah Ingin menambahkan barang lagi? (y/n): ")
        if pilihan == "n":
            break

#Fitur admin hapus barang
def hapusbarang():
    while True:
        lihatbarang()
        no_barang = input("Masukan Nomor Barang yang ingin dihapus : ")

        for row in tabel._rows:
            if row[0] == no_barang:
                tabel.del_row(tabel.rows.index(row))
        print(f"Nomor Barang {no_barang} dengan Nama Barang telah dihapus")
        pilihan = input("Apakah Ingin menghapus barang lagi? (y/n): ")
        if pilihan == "n":
            break

#Fitur admin lihat barang
def lihatbarang():
    print(tabel)

#Fitur admin Perbarui Barang
def perbaruibarang():
    lihatbarang()
    no_barang = input("Masukan Nomor Barang awal : ")
    ubah_barang_harga = input("Pilih yang akan diubah (Nama/Harga) : ").capitalize()
    nilai_baru = input(f"Masukan {ubah_barang_harga} baru : ")

    for row in tabel._rows:
        if row[0] == no_barang:
            index = tabel._rows.index(row)
            if ubah_barang_harga == "Nama":
                tabel._rows[index][1] = nilai_baru
            elif ubah_barang_harga == "Harga":
                tabel.rows[index][2] = (nilai_baru)
            else:
                print ("Data Tidak Valid")
                return perbaruibarang()
    print(f"Barang dengan Nomor {no_barang} berhasil diubah.")

#Login Mode Pembeli
def pembeli():
    print("=" * 10 + "Selamat Datang Pembeli!" + "=" * 10)
    nama_pembeli = input("Sebutkan Nama Anda : ")
    print("=" * 10 + f"Halo Selamat datang {nama_pembeli} di Toko Hardware Jaringan ^-^" + "=" * 10)
    
    while True:
        lihatbarang()
        while True:
            no_barang = input("Masukan Nomor Barang yang ingin dibeli : ")

            found = False  # Untuk mengecek apakah barang dengan nomor tersebut ada
            for row in tabel._rows:
                if row[0] == no_barang:
                    found = True #Jika barang ada otomatis akan lanjut mengisi Kuantitas Barang
                    kuantitas = int(input("Masukan Kuantitas Barang yang anda inginkan : "))
                    harga_barang = float(row[2].replace(".", ""))  # Mengganti koma menjadi titik untuk memisahkan desimal
                    total_harga = kuantitas * harga_barang
                    print(f"Anda telah membeli {kuantitas} {row[1]} seharga Rp.{total_harga:,.0f}")  # Menggunakan ,.0f untuk memformat mata uang dengan tanda koma sebagai pemisah ribuan
                    sys.exit()
            if not found: #Jika no barang tidak ada otomatis akan diulang ke No Barang input dan mendapatkan Notifikasi
                print("Nomor Barang tidak valid. Barang dengan nomor tersebut tidak ada. Silakan coba lagi.")

login()
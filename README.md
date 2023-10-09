# Praktikum PosTest 2

# Profil Diri

Nama : Muhammad Rizky Setiawan
NIM : 2309116039
Kelas : A
Tema : Toko Hardware Jaringan (Contoh Mikrotik,Huawei,Cisco,dsb)

# Flowchart

![Flowchart Postest 2](https://github.com/yezkyy/praktikum_postest2/assets/115384028/33769939-022c-4ff4-b67b-385b593cf10f)

# Menu Login

![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/eccf37f7-4aba-4e31-a1a2-15888b33a022)

Gambar diatas menunjukan user akan dipilih sesuai rolenya yaitu ada Admin dan Pembeli.

# <sub>Penjelasan Menu mode Login</sub>

  1. Admin
     Untuk Admin bisa melakukan sistem CRUD(Create,Read,Update,Delete) pada database barang.
  2. Pembeli
     Sedangkan pembeli hanya dapat melakukan transaksi pada barang yang telah disediakan.

* **Seandainya jika user menginputkan angka mode selain 1 dan 2**

![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/fa3993b8-f164-4f3f-8fbb-29b017c16a96)

jika user menginputkan angka selain 1 dan 2 otomatis akan kembali ke Menu Mode Login

# Mode Admin

![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/74b390e8-3767-47f2-8653-44d1f6cc236e)

pada mode admin, user akan diberikan 5 Fitur seperti gambar diatas dan user diminta untuk menginputkan fitur sesuai dengan angka fitur yang disediakan.

# <sub>Penjelasan Fitur Admin</sub>

1. Tambah Barang
   
   ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/3b3252f7-a43c-40b4-ae26-e1d6ff311dc1)

    untuk masuk ke fitur "Tambah Data" inputkan angka 1

   ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/5b688241-a38e-4fef-8771-eac70cf7188f)

    disini admin akan diminta memasukan Nomor Barang terbaru, lalu Nama Barang dan Nama Harga sesuai keingininan admin. Setelah selesai Admin akan ditanya kembali apakah ingin menambah barang lagi dengan sistem looping (y/n)

  * **Seandainya jika admin menginputkan "y"**
    
     ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/b468da48-83c7-474c-b84a-1e23a1256a10)

    jika admin input "y" otomatis admin akan terlooping ke "Nomor Barang" dan sampai seperti tadi.

  * **Seandainya jika admin menginputkan "n"**
    
    ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/4e7cc92b-20ee-4a35-a561-dd9632c1577f)

    jika admin input "n" otomatis admin akan ter direct ke Fitur Admin kembali.

2. Hapus Barang
   * **Before**
     
     ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/e045da15-0ab6-4b5a-919d-f709f1761881)

   * **After**

     ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/53142d86-158a-4048-86d9-0d54e497b508)

    Terlihat pada No Barang "11" telah terhapus saat admin menggunakan fitur Hapus barang dan juga ditawari perulangan yang sama seperti "Tambah Barang".

3. Lihat Barang

  ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/4fc539a7-8095-4fc0-9e25-de0b818b16ff)

  fitur ini digunakan untuk melihat barang apa saja yang tersedia. disaat Barang sudah muncul dalam output otomatis akan looping kembali ke fitur.

4. Perbarui Barang

    ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/5bb3d138-0ecf-43df-b006-79d907bbc0ca)

   gambar di atas ini merupakah contoh Perubahan Data Barang dan yang dirubah adalah Nama Barangnya

    ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/5dcd17e6-fffa-4be1-8593-9a2a1c2b9050)

    dan saat Nama Barang telah diubah otomatis saat kita lihat maka otomatis seperti gambar diatas di barang Nomor "10"

   ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/0ceac197-a63d-46e2-a035-a6d25b4df3a2)

    begitu pula dengan harga yang ingin diubah pada nomor barang "10" gambar diatas admin menginputkan harga baru yang menjadi nilai baru.

   ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/5a638fa1-40e5-4a20-8105-e45f584d5118)

    dan setelah diubah dan diliat pada table otomatis harga barang akan berubah dengan kita yang inputkan pada nomor barang "10" tadi.

   * **Seandainya jika admin menginputkan Nilai yang tidak valid**

     ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/08ee765d-f1d9-4a9b-9bc9-f2469b758f88)

    jika admin menginputkan Nilai yang tidak Valid,program memang tetap berlanjut meminta input tetapi disaat menampilkan output dinyatakan gagal dan data perubahaan barang tadi tidak akan terubah pada database tersebut.

5. Keluar atau Kembali ke Mode Login
   
   disini admin jika sudah cukup menggunakan fiturnya, admin bisa memilih fitur ke 5 yaitu Keluar atau Kembali ke Mode Login. Disaat memilih admin akan diberikan dua opsi yaitu Keluar yang bisa diartikan langsung keluar exit dari program dan Kembali ke Mode Login yang otomatis ketika admin input "Kembali",admin akan diarahkan ke Mode Login.

   ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/4ac2c035-838f-4229-9524-35fb4530695e)


    * **Jika Admin input "Keluar"**
     
     ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/2840d18a-b9d8-4c05-ba35-4067521c3727)

    * **Jika Admin input "Kembali"**
  
      ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/15c76700-b7ee-42fd-8c6c-c6e7f0485abe)

# <sub> Bagaimana saat di menu fitur Admin input angka yang bukan dari range 1-5? </sub>

  ![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/fc6c5e66-1abe-40b2-b7b9-390c8a30bf49)

  jawabannya adalah otomatis admin akan terlooping ke fitur kembali dan mendapatkan notifikasi bahwa nomor fitur yang diinputkan tidak ada.

# Menu Pembeli

![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/62fffc5f-08d4-4300-9e12-e94ef13f101d)

disaat user menginputkan angka 2 otomatis user akan masuk ke Mode Pembeli yang dimana akan langsung ditampilkan output dari database barang menggunakan pretty table yang telah disediakan pada baris pemograman maupun pada fitur Tambah,Hapus,Perbarui Barang pada mode Admin. Kemudian disini pembeli akan diminta untuk memasukan No Barang yang diinginkan.

![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/6f830fa4-0451-4caf-80cc-2ea6201e7dce)

seperti gambar diatas pembeli akan diminta no barang setelah menginputkan nomor barang, kemudian pembeli akan diminta input berapa barang/kuantitas barang yang diinginkan pembeli. saat disini program akan menggunakan prosesnya yaitu harga barang akan dikalikan dengan kuantitas barang yang sehingga output nya menampilkan total barang hasil perkalian tadi. Dan disini

* **Seandainya jika pembeli menginputkan No Barang yang tidak ada dalam database**
  
![image](https://github.com/yezkyy/praktikum_postest2/assets/115384028/f46908ca-66bf-431c-acd2-ff03ba961836)

disini contoh implementasinya adalah pembeli menginputkan angka "11" sedangkan nomor barang yang tersedia tidak ada angka 11 otomatis pembeli akan terlooping ke Input nomor barang yang ingin dibeli kembali dan diberikan notifikasi bahwa nomor barang yang diinputkan tidak tersedia.

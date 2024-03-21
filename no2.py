def tampilkan_profil_mahasiswa(**kwargs):
    nama = kwargs.get("nama")
    nim = kwargs.get("nim")
    prodi = kwargs.get("prodi")
    hobi = kwargs.get("hobi")

    print(f"Mahasiswa Prodi {prodi} Unjani Yogyakarta")
    print(f"Dengan nama {nama}")
    print(f"Mempunyai NIM {nim}")
    print(f"Memiliki Hobi {hobi}")


print("Profile Mahasiswa UNJANI Yogyakarta")
nama = input("Nama : ")
nim = input("NIM : ")
prodi = input("Prodi : ")
hobi = input("Hobi : ")

tampilkan_profil_mahasiswa(nama=nama, nim=nim, prodi=prodi, hobi=hobi)

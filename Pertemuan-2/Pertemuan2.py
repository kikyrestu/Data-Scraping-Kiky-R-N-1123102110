import os

def buat_folder(nama_folder):
    if not os.path.exists(nama_folder):
        os.makedirs(nama_folder)
        print(f"[SUKSES] Folder '{nama_folder}' telah dibuat.")
    else:
        print(f"[INFO] Folder '{nama_folder}' sudah ada.")

buat_folder("Scraping")

def buat_berkas(path_berkas):
    f = open(path_berkas, "w")
    f.write("")
    f.close()
    print(f"[SUKSES] Berkas '{path_berkas}' telah dibuat.")

buat_berkas("new_file.txt")

def tambah_teks(path_berkas, isi_teks):
    with open(path_berkas, "a", encoding="utf-8") as f:
        f.write(isi_teks)
    print(f"[CATAT] Menambahkan teks ke '{path_berkas}'.")

tambah_teks("new_file.txt", "\nHello, Sekai!")

def baca_berkas(path_berkas):
    with open(path_berkas, "r", encoding="utf-8") as f:
        for baris in f.readlines():
            print(baris.rstrip())

baca_berkas("new_file.txt")

def pemeriksaan_berkas(path_berkas):
    return os.path.exists(path_berkas)

print("[CEK] new_file.txt ada? ->", pemeriksaan_berkas("new_file.txt"))

def kosongkan_berkas(path_berkas):
    with open(path_berkas, "w", encoding="utf-8") as f:
        f.write("")
    print(f"[SUKSES] Isi '{path_berkas}' telah dikosongkan.")

kosongkan_berkas("new_file.txt")

def hapus_berkas(path_berkas):
    os.remove(path_berkas)
    print(f"[HAPUS] Berkas '{path_berkas}' telah dihapus.")

hapus_berkas("new_file.txt")

for nomor in range(1, 11):
    print(nomor)

nasi_padang_tersedia = False

if nasi_padang_tersedia:
    print("Nasi Padang: tersedia")
else:
    print("Nasi Padang: tidak tersedia")

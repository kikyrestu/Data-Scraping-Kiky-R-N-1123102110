import os

def kosongkan_berkas(path_berkas):
    direktori = os.path.dirname(path_berkas)
    if direktori and not os.path.exists(direktori):
        os.makedirs(direktori)
    with open(path_berkas, 'w', encoding='utf-8') as f:
        pass
    print(f"[SUKSES] '{path_berkas}' telah dikosongkan.")

def buat_berkas_dengan_isi(path_berkas):
    with open(path_berkas, 'w', encoding='utf-8') as f:
        f.write("Halo, ini isi berkas baru!\n")
        f.write("Baris kedua dari berkas.\n")
    with open(path_berkas, 'r', encoding='utf-8') as f:
        konten = f.read()
        return konten

konten = buat_berkas_dengan_isi("Scaping/test.txt")
print("Isi berkas:")
print(konten)

def tulis_berkas(path_berkas, isi):
    direktori = os.path.dirname(path_berkas)
    if direktori and not os.path.exists(direktori):
        os.makedirs(direktori)
    with open(path_berkas, 'w', encoding='utf-8') as f:
        f.write(isi)
    print(f"[SUKSES] Menulis ke '{path_berkas}'.")

def baca_berkas(path_berkas):
    if os.path.exists(path_berkas):
        with open(path_berkas, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "[ERROR] Berkas tidak ditemukan."

lintasan = "Scaping/test.txt"
tulis_berkas(lintasan, "Halo Dunia!\nIni baris kedua.")
konten = baca_berkas(lintasan)
print("Isi berkas:")
print(konten)

import os

def buat_berkas(path_berkas):
    direktori = os.path.dirname(path_berkas)
    if direktori and not os.path.exists(direktori):
        os.makedirs(direktori)
    with open(path_berkas, 'w', encoding='utf-8') as f:
        pass
    print(f"[SUKSES] Berkas '{path_berkas}' dibuat.")

def tambah_baris(path_berkas, isi):
    direktori = os.path.dirname(path_berkas)
    if direktori and not os.path.exists(direktori):
        os.makedirs(direktori)
    with open(path_berkas, 'a', encoding='utf-8') as f:
        f.write(isi + "\n")
    print(f"[SUKSES] Menambahkan ke '{path_berkas}'.")

def baca_berkas(path_berkas):
    if os.path.exists(path_berkas):
        with open(path_berkas, 'r', encoding='utf-8') as f:
            konten = f.read()
            print(konten)
            return konten
    else:
        print("[ERROR] Berkas tidak ditemukan.")
        return None

buat_berkas("scraping/file.txt")
tambah_baris("scraping/file.txt", "This is a line")
tambah_baris("scraping/file.txt", "This is another line")
baca_berkas("scraping/file.txt")

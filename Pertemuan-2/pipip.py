import os

def tulis_berkas(path_berkas, isi, mode='w'):
    direktori = os.path.dirname(path_berkas)
    if direktori and not os.path.exists(direktori):
        os.makedirs(direktori)
    with open(path_berkas, mode, encoding='utf-8') as f:
        f.write(isi + "\n")
    print(f"[SUKSES] Menulis ke '{path_berkas}' (mode={mode}).")

def baca_berkas(path_berkas):
    if os.path.exists(path_berkas):
        with open(path_berkas, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "[ERROR] Berkas tidak ditemukan."

lintasan = "Scaping/test.txt"
tulis_berkas(lintasan, "Baris pertama", mode='w')
tulis_berkas(lintasan, "Baris kedua", mode='a')
tulis_berkas(lintasan, "Baris ketiga", mode='a')
konten = baca_berkas(lintasan)
print("Isi berkas:")
print(konten)

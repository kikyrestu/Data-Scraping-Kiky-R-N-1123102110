import os

def tulis_berkas(path_berkas, isi_teks, mode='w'):
    direktori = os.path.dirname(path_berkas)
    if direktori and not os.path.exists(direktori):
        os.makedirs(direktori)
    with open(path_berkas, mode, encoding='utf-8') as f:
        f.write(isi_teks + "\n")
    print(f"[SUKSES] Menulis ke '{path_berkas}' (mode={mode}).")

def baca_berkas(path_berkas):
    if os.path.exists(path_berkas):
        with open(path_berkas, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "[ERROR] Berkas tidak ditemukan."

lintasan_berkas = "Scaping/hasil_matematika.txt"

print("=== Kalkulator Sederhana ===")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("\nPilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

pilihan = input("Masukkan pilihan (1-4): ")

if pilihan == "1":
    hasil = a + b
    deskripsi = f"{a} + {b} = {hasil}"
elif pilihan == "2":
    hasil = a - b
    deskripsi = f"{a} - {b} = {hasil}"
elif pilihan == "3":
    hasil = a * b
    deskripsi = f"{a} * {b} = {hasil}"
elif pilihan == "4":
    if b != 0:
        hasil = a / b
        deskripsi = f"{a} / {b} = {hasil}"
    else:
        deskripsi = "[ERROR] Pembagian dengan nol."
else:
    deskripsi = "[ERROR] Pilihan tidak valid."

tulis_berkas(lintasan_berkas, deskripsi, mode='a')

print("\nHasil operasi:")
print(deskripsi)

print("\nRiwayat operasi di berkas:")
print(baca_berkas(lintasan_berkas))

print("\nSelesai.")

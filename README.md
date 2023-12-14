# ECB-Enskripsi-Kriptografi
Tentu, berikut ini adalah contoh README untuk proyek GitHub yang berisi tentang fungsi `encrypt_ecb` untuk enkripsi ECB dengan Python:

---

# Encrypt ECB Function

Implementasi fungsi Python untuk melakukan enkripsi ECB menggunakan metode XOR dan pergeseran bit.

## Deskripsi

Fungsi `encrypt_ecb` ini mengambil plaintext dalam format hexadesimal dan kunci dalam format biner. Proses enkripsi ECB melibatkan beberapa langkah:

1. Konversi Plaintext Hex ke Binary
2. Pemecahan Plainteks menjadi Blok-blok 4 bit
3. Enkripsi Setiap Blok menggunakan Operasi XOR dan Pergeseran Bit

## Penggunaan

Untuk menggunakan fungsi `encrypt_ecb`, pastikan Python telah terpasang di lingkungan Anda. Jalankan skrip `main.py` dan ikuti instruksi berikut:

1. Masukkan Plainteks (dalam format hex)
2. Masukkan Kunci (dalam format binary)

Setelah masukan diberikan, fungsi akan mengenkripsi teks dan menampilkan hasil enkripsi ECB.

## Contoh Penggunaan

```python
from encrypt_ecb import encrypt_ecb

# Masukkan Plainteks dan Kunci
plaintext_hex = "1A3F"
key_binary = "1010"

# Enkripsi ECB
encrypted_result = encrypt_ecb(plaintext_hex, key_binary)

# Hasil Enkripsi 

print("Hasil Enkripsi ECB:", encrypted_result)
```

[!]ss1.png


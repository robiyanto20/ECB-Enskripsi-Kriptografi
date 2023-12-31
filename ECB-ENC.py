# Nama: ROBIYANTO
# NIM: 312210098
# KELAS : TI.21.A1

def encrypt_ecb(plaintext_hex, key_binary):
    # Konversi plaintext hex ke binary
    plaintext_binary = bin(int(plaintext_hex, 16))[2:]

    # Bagi plainteks menjadi blok-blok 4 bit
    blocks = [plaintext_binary[i:i+4] for i in range(0, len(plaintext_binary), 4)]

    # Enkripsi ECB
    encrypted_blocks = []
    for block in blocks:
        # XOR dengan kunci
        xor_result = ''.join(str(int(b) ^ int(k)) for b, k in zip(block, key_binary))

        # Geser 1 bit ke kiri
        shifted_result = xor_result[1:] + xor_result[0]

        # Konversi hasil ke desimal dan tambahkan ke hasil enkripsi
        encrypted_blocks.append(str(int(shifted_result, 2)))

    return encrypted_blocks

def main():
    print("MASUKKAN INPUT DATA")
    print("di bawah ini !!")

    # Input plainteks dan kunci
    plaintext_hex = input("Masukkan Plainteks (hex): ")
    key_binary = input("Masukkan Kunci (binary): ")

    # Enkripsi ECB
    encrypted_result = encrypt_ecb(plaintext_hex, key_binary)

    # Cetak hasil enkripsi
    print("Hasil Enkripsi ECB:", encrypted_result)

if __name__ == "__main__":
    main()
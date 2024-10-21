import math

# Fungsi untuk menghitung luas lingkaran
def luas_lingkaran():
    while True:
        try:
            # Meminta input jari-jari dari pengguna
            r = float(input("Masukkan jari-jari lingkaran: "))
            
            # Memeriksa apakah jari-jari lebih besar dari 0
            if r > 0:
                # Menghitung luas lingkaran
                luas = math.pi * r ** 2
                print(f"Luas lingkaran dengan jari-jari {r} adalah {round(luas, 2)}")
                # Keluar dari loop jika input valid
            else:
                print("Jari-jari harus lebih ybesar dari 0.")

                # Menanyakan apakah ingin mengulang program
            ulang = input("Apakah Anda ingin mengulang program? (y/n): ").lower()
            if ulang != 'y':
                print("Terima kasih telah menggunakan program ini.")
                break  # Keluar dari loop jika pengguna tidak ingin mengulang

        except ValueError:
            # Jika input bukan angka
            print("Input harus berupa angka.")

# Memanggil fungsi
luas_lingkaran()
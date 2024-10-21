def convert_temperature():
    while True:
        try:
            # Meminta input nilai suhu dari pengguna
            value = float(input("Masukkan nilai suhu: "))
            unit = input("Masukkan unit suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ").upper()
            
            # Proses konversi berdasarkan unit yang dimasukkan
            if unit == 'C':
                # Konversi dari Celsius ke Fahrenheit
                converted = (value * 9/5) + 32
                print(f"{value}°C sama dengan {round(converted, 2)}°F")
                # Keluar dari loop setelah input valid
            elif unit == 'F':
                # Konversi dari Fahrenheit ke Celsius
                converted = (value - 32) * 5/9
                print(f"{value}°F sama dengan {round(converted, 2)}°C")
                  # Keluar dari loop setelah input valid
            else:
                print("Unit tidak dikenali, gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")

                # Menanyakan apakah ingin mengulang program
            ulang = input("Apakah Anda ingin mengulang program? (y/n): ").lower()
            if ulang != 'y':
                print("Terima kasih telah menggunakan program ini.")
                break  # Keluar dari loop jika pengguna tidak ingin mengulang
            
        except ValueError:
            # Jika input nilai suhu tidak valid (bukan angka)
            print("Nilai suhu harus berupa angka. Silahkan coba lagi")

# Memanggil fungsi
convert_temperature()
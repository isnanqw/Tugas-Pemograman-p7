# latihan1.py
# Program untuk menampilkan n bilangan acak yang lebih kecil dari 0.5
from random import random
# Input nilai n saat runtime
n = int(input("Masukkan nilai N: "))
# Loop menggunakan for untuk jumlah n, dan while untuk memastikan nilai < 0.5
for i in range(1, n + 1):
    while True:
        a = random()  # Generate bilangan acak antara 0.0 dan 1.0
        if a < 0.5:   # Cek apakah < 0.5
            print(f"data ke: {i} => {a}")
            break     # Keluar dari while jika kondisi terpenuhi
print("Selesai")

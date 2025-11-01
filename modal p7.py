# latihan2.py
# Program menghitung total keuntungan investasi selama 8 bulan
# Modal awal
modal_awal = 100000000  # 100 juta
# Inisialisasi variabel
total_laba = 0
# Loop untuk 8 bulan
for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba_persen = 0  # Bulan 1-2: Belum ada laba
    elif bulan <= 4:
        laba_persen = 1  # Bulan 3-4: Laba 1%
    elif bulan <= 7:
        laba_persen = 5  # Bulan 5-7: Laba 5%
    else:
        laba_persen = 2  # Bulan 8: Laba 2% (turun 3% dari 5%)
    # Hitung laba bulan ini
    laba_bulan_ini = modal_awal * (laba_persen / 100)
    total_laba += laba_bulan_ini
    # Tampilkan informasi per bulan
    print(f"laba bulan ke-{bulan} sebesar: {int(laba_bulan_ini)}")
print(f"Total laba adalah: {int(total_laba)}")
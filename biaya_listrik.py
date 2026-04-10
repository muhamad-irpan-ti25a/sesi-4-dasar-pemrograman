kwh= int(input("Masukkan ada brapa kwh :"))

if kwh <= 100:
    biaya = kwh * 500
elif kwh <=300:
    biaya = kwh * 1000
elif kwh <=1000:
    biaya = kwh * 2000

print(biaya)

bilangan = int(input("masukkan bilangan :"))

if bilangan % 2 == 0:
    hasil = "genap"
else:
    hasil = "ganjil"

print(hasil)

nilai = int(input("masukkan nilai : "))

if nilai > 75:
    keputusan = "Lulus"
elif nilai >= 50:
    keputusan = "Boleh Perbaikan"
elif nilai < 50:
    keputusan = "tidak lulus dan tidak bisa perbaikan"

print(keputusan)

nilai = int(input("masukkan nilai :"))
absensi = int(input("masukkan absensi :"))

if (nilai > 70 and absensi > 50):
    hasil_keputusan = "lulus"
elif (nilai < 70 and absensi > 70 or nilai > 70 and absensi < 50):
    hasil_keputusan = "tidak lulus tapi bisa perbaikan"
else:
    hasil_keputusan = "tidak lulus dan tidak bisa perbaikan"

print(hasil_keputusan)
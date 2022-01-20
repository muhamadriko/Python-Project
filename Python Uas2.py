import random
import cmath
program = True
y=""
while program :
  print("========== =============== ==========")
  print("========== APLIKASI MATMAT ==========")
  print("========== =============== ==========")
  print("\t DAFTAR PROGRAM")
  print("\t 1.Kalkulator Suhu")
  print("\t 2.Permainan Matematika")
  print("\t 3.Bilangan Ganjil/Genap")
  print("\t 4.Luas")
  print("\t 5.Kuadrat")
  print("\t 6. Volume kubus")
  print("\t 7.Bilangan Positif/ Negatif")
  pilihan = int(input("masukkan Pilihanmu : "))
  if pilihan == 1:
    print("Pilihan derajat suhu")
    print("1.Celcius")
    print("2.Reamur")
    print("3.Fahrenheit")
    print("4.Kelvin")
    print("---------------------")
    suhu = int(input("Masukkan suhu saat ini : "))
    pilihan =int(input("Suhu pada Derajat [1...4]:"))
    if (pilihan == 1 ):
      hasil1 = float(4/5 * suhu)
      hasil2 = float((9 * suhu) / 5 + 32)
      hasil3 = float(suhu + 273.15)
      jenisX = "C"
      jenis1 = "R"
      jenis2 = "F"
      jenis3 = "K"
    elif (pilihan == 2 ):
      hasil1 = float((5/4) * suhu)
      hasil2 = float((9/4 * suhu) + 32)
      hasil3 = float((5/4 * suhu) + 273)
      jenisX = "R"
      jenis1 = "C"
      jenis2 = "F"
      jenis3 = "K"             
    elif (pilihan == 3 ):
      hasil1 = float((suhu - 32) * 5 / 9)
      hasil2 = float(4/9 * (suhu-32))
      hasil3 = float(((suhu - 32) * 5 / 9) + 273.15)
      jenisX = "F"
      jenis1 = "C"
      jenis2 = "R"
      jenis3 = "K"
    elif (pilihan == 4 ):
      hasil1 = float(suhu - 273.15)
      hasil2 = float(((suhu - 273.15) * 9 / 5)+32)
      hasil3 = float(4/5 * (suhu-273))
      jenisX = "K"
      jenis1 = "C"
      jenis2 = "F"
      jenis3 = "R"

    else:
      print("Inputan tidak sesuai!! Perhatikan Penulisan Input")

    print(suhu,jenisX,"=","{:.1f}".format(hasil1),jenis1)
    print(suhu,jenisX,"=","{:.1f}".format(hasil2),jenis2)
    print(suhu,jenisX,"=","{:.1f}".format(hasil3),jenis3)

  elif pilihan == 2:
    angka= random.randint(1, 100)
    print("Permainan Tebak angka")
    print("Tebaklah mulai dari 0 hingga 100")
    percobaan = int(input("kesempatan yang kamu inginkan : "))
    print('Kami telah memiliki angka, silakan tebak!')
    for tebak in range(percobaan):
      jawaban = int(input(f'\n[Percobaan {tebak + 1}] Masukkan angka: '))

      if jawaban == angka:
        print('Selamat, tebakanmu benar!')
        break
      else:
        print('Tebakanmu terlalu','kecil' if jawaban < angka else 'besar')
    else:
      print(f'\nSayang sekali, kamu sudah salah menebak')
  elif pilihan == 3:
    print("1.ganjil")
    print("2.genap")

    pilihan = int(input("Masukan Pilihan : "))
    a = int(input("masukkan Bilangan "))
    if pilihan == 1:
        for x in range (a):
          if x % 2 == 1:
              print(x)
    elif pilihan == 2:
        for x in range(a) :
            if x % 2 == 0:
                print(x)
    else:
      print("masukkan Pilihan yang benar")
  elif pilihan ==4 :
    print("\t 1.Lingkaran")
    print("\t 2.Presegi")
    print("\t 3.Pythagoras")
    print("\t 4.Segitiga")
    pilihan = int(input("masukkan Pilihanmu : "))
    if pilihan == 1:
      p = 3,14
      r = float(input(" Jari-Jari : "))
      x = (p*r*r)
      print("luas Lingkaran adalah : ",x)
    elif pilihan == 2:
      S= input("sisi = ")
      T= (S*S)
      print("luas Persegi adalah : ",T)
    elif pilihan == 3:
      sisi1= input("sisi 1 = ")
      sisi2= input("sisi 2 = ")
      c = sisi1 * sisi1
      d = sisi2 * sisi2
      e = c + d
      f = e**0.5
      print("panjang pythagoras adalah : ",f)
    elif pilihan == 4:
      alas = float(input('Tulis Alas Segitiga: '))
      tinggi = float(input('Tulis Tinggi Segitiga: '))
      luas = (alas * tinggi) / 2
      print('Luas Segitiga adalah %0.2f' %luas)
    else:
      print("pilihanmu tidak ada")
  elif pilihan == 5 :
    print("\t 1.akar kuadrat")
    print("\t 2.Persamaan Kuadrat")
    pilihan = int(input("masukkan Pilihanmu : "))
    if pilihan == 1:
      angka = float(input('Tuliskan Angka: '))
      akar_kuadrat = angka ** 0.5
      print('Akar Kuadrat dari %0.3f adalah %0.3f'%(angka ,akar_kuadrat))
    elif pilihan == 2:
      a = int(input('Tulis a: '))
      b = int(input('Tulis b: '))
      c = int(input('Tulis c: '))
      d = (b**2) - (4*a*c)
      x1 = (-b-cmath.sqrt(d))/(2*a)
      x2 = (-b+cmath.sqrt(d))/(2*a)
      print('Hasil Persamaan Kuadrat adalah {0} dan {1}'.format(x1,x2))
  elif pilihan == 6:
    sisi = float(input('Tulis Sisi Kubus: '))
    volume = sisi ** 3
    print('Volume Kubus adalah %0.2f' %volume)
  elif pilihan == 7:
    angka = float(input("Tulis Sebuah Angka: "))
    if angka > 0:
      print("Angka Positif") 
    elif angka == 0:
      print("Angka Nol")
    else:
      print("Angka Negatif")
  else:
    print("Nomer yang kamu pilih tidak ada")
  y=input("apakah anda ingin mengulang perhitungan (y/n)?")
  if y == "y":
    continue
  else:
    break

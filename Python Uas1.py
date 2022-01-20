import pandas as pd
import requests
import tabulate
from tabulate import tabulate 

response = requests.get("https://api.abcfdab.cfd/students/")
data = response.json()
datafix = data['data']
print("1 Tampilkan semua data tabulate")
print("2 Tampilkan berdasarkan limit")
print("3 cari berdasarkan nim")
print("0 exit")
pilihan = int(input("Pilih Menu > "))
if pilihan == 1:
  dataset = datafix
  header = dataset[0].keys()
  rows =  [x.values() for x in dataset]
  print(tabulate.tabulate(rows, header))
elif pilihan == 2:
  df = pd.DataFrame(datafix)
  p = int(input("masukkan limit : "))
  hasil = df.head(p)
  print(hasil)
elif pilihan == 3:
  a = input("masukkan nim : " )
  res = next(item for item in datafix if item["nim"] == a )
  print(tabulate(res, headers=['id', 'nim', 'nama', 'jk', 'jurusan', 'alamat']))
elif pilihan == 0:
  exit

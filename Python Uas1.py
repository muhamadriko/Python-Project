import mysql.connector
import os

#KONEKSI

config=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_akademik_0143"
)

def select_all_data():
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0143"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("data tidak tersedia")
    else:
        for data in results:
            print(data)
def range_data():
    nim = input("Masukkan limit : ")
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0143 WHERE id BETWEEN 1 AND %s"
    val = (nim,)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("data tidak tersedia")
    else:
        for data in results:
            print(data)
            
def select_single_data():
    nim = input("Masukkan NIM yang dicari: ")
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0143 WHERE nim=%s"
    val = (nim,)
    cursor.execute(sql, val)
    results = cursor.fetchone()

    if cursor.rowcount < 0:
        print("data tidak tersedia")
    else:
        for data in results:
            print(data)

def menu():
    print("1. Select all Data")
    print("2. Cari Data berdasar limit")
    print("5. Cari Data berdasar nim")
    print("0. Keluar")

    option = input("Pilih Menu> ")

    os.system("clear")

    if option == "1":
        select_all_data()
    elif option == "2":
        range_data()
    elif option == "3":
        select_single_data()
    elif option == "0":
        exit()
    else:
        print("Pilih Menu yang valid")

if __name__ == '__main__':
    while(True):
        menu()            

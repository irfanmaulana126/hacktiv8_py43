a = input("masukan angka: ")
a = eval(a) # ini langsung menentukan tipe data 

while a > 0:
    if a == 10:
        break
    if a % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")
    print("jumlah tusuk gigi {}".format(a))
    a = a - 1

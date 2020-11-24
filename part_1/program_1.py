# materi bisa di baca" lagi di link https://cs231n.github.io/python-numpy-tutorial/
# https://drive.google.com/drive/folders/1jWS6yVPffPzgOhJH14zsQIpOfymKgBop?usp=sharing

print("Helo world")
# mencetak angka
print(1 + 1) # tambah
print(1 - 1) # kurang
print(1 * 1) # kali
print(1 / 1) # bagi
print(1 // 1) # bagi dengang pengambilan nilai desimal
print(1 ** 1) # pangkat
print(1 % 1) # modulus
print(type(5)) # jenis type data int, float, double, bloean, bilangan koplek
print(type(4.0))
print(type(True))
print(type(5))
# contoh bilangan komplek
print(type(5+1j))

# operasi perbandingan
print(4 == 5)
print(4 != 5)
print(4 > 5)
print(4 < 5)
print(4 >= 5)
print(4 <= 5)

if 5 > 10 :
    print("false")
else:
    print("true")

a = input("input parameter 1: ")
b = input("input parameter 2: ")

print(int(a)+int(b))

# substring

a = "provinsi Jawa Barat"

print(a[:7])
print(a[9:12])
print(a[12:])

# tupple -> tidak dapat dirubah setelah di definisika (imutable)
b = ('a','b', 1, 2.5,('c','d','e'),10)

# list -> dapat dirubah walaupun sudah di definisikan (mutable)
c = ['asd','zxc',1000,('asdas','asd')]

# cara menambahkan list dengan append ex nama_list.append("isi yang mau ditambahkan") 
# cara menambahkan list dengan append ex nama_list.append(index_list,"isi yang mau ditambahkan") 
# cara menghapus list dalam index dengan menggunakan fungsi remove ex nama_list.remov("property")
# dict {'nama':'irfan','umur':12}
# himpunan set([1,2,3,4])



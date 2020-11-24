a = []
tot = 0
tambah = 'y'
while tambah != 'n' :
    if tambah == 'y':
        b = input("Mau makan apa: ")
        a.append(b)
    tambah = input("Tambah lagi (y/n)?")
    tambah.lower()


print('*'*50)
print("\n Jumlah Pesanan anda {}".format(len(a)))

# for i in a:
#     print("Pesanan anda {}".format(i))
i = 0
while i < len(a):
    print("Pesanan anda {}".format(a[i]))
    i = i + 1

print('*'*50)

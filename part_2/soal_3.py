from random import randint 
print("*" * 50)
print("Tebak angka guys")
print("*" * 50)

a =  randint(1,10)
print("saya memikirkan angka 1-10")
print("ayo tebak angka saya")
b = input("masukan tebakan anda (1-10)")
b = eval(b)
i = 0
while b != a:
    if b > a:
        print("tebakan terlalu besar")
    else:
        print("tebakan terlalu kecil")

    b = input("masukan tebakan anda (1-10) ")
    b = eval(b)
    i = i+1

i = i + 1
print("tebakan anda benar")
print("jumlah tebakan anda {}".format(i))

# ini kodingan mas afif
# n = 0
# while True:
#     n += 1 
#     tebakan = int(input("masukan angka anda (1 - 10)"))

#     if tebakan == a:
#         break
#     elif tebakan > a:
#         print("nilai terlalu besar")
#     else:
#         print("nilai terlalu kecil")

# print("tebakan anda benar")
# print("jumlah tebakan anda {}".format(n))

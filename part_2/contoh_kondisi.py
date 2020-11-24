a = input("masukan nila: ")
a = eval(a) # ini langsung menentukan tipe data 
print("nilai a: {}".format(a))
if a >= 10:
    if a > 15:
        print("a lebih dari 15")
    else:
        print("a kurang dari 15")
    
    if a % 2 == 0:
        print("ganap")
        print("a bernilai lebih dari 10")
    else:
        print("ganjil")
        print("a bernilai lebih dari 10")        
else:
    if a > 15:
        print("a lebih dari 15")
    else:
        print("a kurang dari 15")
    
    if a % 2 == 0:
        print("ganap")
        print("a bernilai kurang dari 10")
    else:
        print("ganjil")
        print("a bernilai kurang dari 10")        

print("program selesai")
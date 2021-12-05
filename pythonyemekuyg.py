

print(" -- Semih Usta'nın Mutfağı -- ")



yemekayıt = open("yemektarifleri.txt", "w") 
yemekayıt.write(input("Yemek Adı Giriniz = " )) 
yemekayıt.write(input("Yemek Tarifi Giriniz = " ))
yemekayıt.close()

dosya = open("yemektarifleri.txt","r")
oku = dosya.read()
print("Yemek Adı ve Tarifiniz = " ,oku)
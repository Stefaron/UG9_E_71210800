#input
a = int(input("Suku pertama :"))
n = int(input("Banyaknya suku :"))
r = int(input("rasio :"))

#proses
hasil = (a*((r**n)-1))/(r-1)
print("Jumlah suku ke 11 yaitu,", hasil)

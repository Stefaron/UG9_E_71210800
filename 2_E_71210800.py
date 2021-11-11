print("Test case 1 :")

#input
nama = input("Nama :")
ttl = input("Tempat tanggal lahir :")

a = nama.split()
b = ttl.split()

#proses
print("Haloo!", a[-1], ",", nama.replace(a[-1]," "))
print("Anda lahir di", b[0], "pada tanggal", b[1], b[2], b[3])

print()
print()

print("Test case 2 :")

#input
nama = input("Nama :")
ttl = input("Tempat tanggal lahir :")

a = nama.split()
b = ttl.split()

#proses
print("Haloo!", a[-1], ",", nama.replace(a[-1]," "))
print("Anda lahir di", b[0], "pada tanggal", b[1], b[2], b[3])

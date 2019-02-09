xprint ("Menentukan bilangan terbesar dari 3 bilangan yang di input oleh user")
print ("Masukan 3 bilangan yang anda inginkan!")
a=int(input("Masukan bilangan pertama = "))
b=int(input("Masukan bilangan kedua = "))
c=int(input("Masukan bilangan ketiga = "))

if a>b and a>c:
	if b>c:
		print (a, 'adalah bilangan terbesar dan', c, 'bilangan terkecil')
	else:
		print (a, 'adalah bilangan terbesar dan', b, 'bilangan terkecil')
elif b>a and b>c:
	if b>a:
		print (b, 'adalah bilangan terbesar dan', c, 'bilangan terkecil')
	else:
		print (b, 'adalah bilangan terbesar dan', a, 'bilangan terkecil')
else:
	if a>b:
		print (c, 'adalah bilangan terbesar dan', b, 'bilangan terkecil')
	else:
		print (c, 'adalah bilangan terbesar dan', a, 'bilangan terkecil')

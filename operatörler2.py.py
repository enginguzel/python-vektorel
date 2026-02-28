a = 5
b = c = d = 7 # hepsini birbirine eşitleme
e,f,g = 2,8,"Ankara" # sıralı atama
print(a,b,c,d,e,f,g)
print(a*b,b,c,d,e,f,g*e)


a = 5==4

# print(a += 15) # atama işlemleri değer döndürmez, bu şekilde kullanılamaz.
print(a)

b +=3 ; print(b)
b *= 2 ; print(b)
b /= 3 ; print(b)
b=20 ; b //= 3 ; print(b)
b = 3 ; b **=3
print(b)
b %=5
print(b)
b = 10 % 3
print(b)

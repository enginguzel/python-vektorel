a = 5
b = 3.7
toplam = a + b
print(f"a degiskeninin degeri : (a), tipi : {type(a)}")
print(f"b degiskeninin degeri : (b)")
print(f"toplam : (a + b)")

print(type(b))

# str, float, int ile type değiştirilebilir

print(a*2)
a = str(a)
print(a*2)
a = float(a)
print(a*2)
print(b*2)

c = a<b
print(c)
print(type(c))
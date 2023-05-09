# list
# uygulama içerisindie anlık olarak vizim için deper tutan bir yapıdır. Birden fazla tipte farklı tipte değer tutabilir. Listeler RAM üzerinde tutulduğu için uygulama çalıştığı sürece üzerine yeni eklenen deperleri saklarlar. Yani uygulama kapatıldığında ilk haline döner.
# Örneğin bir futbol takımları listem olsun
# futbol_taktmlarii = ["Beşiktaş", "Galatasaray", "Adanademir Spor"]
# Uygulama öalıştırdığın bu kşste tam olarak yukardakş yapıda RAM'in Heap alanına çıkartır
#  Uygulama run time'da yeni çalışıyor. aşağıdaki kod öalıştığnı varsayalım.
# futbol_taktmlarii.append("Trabzonspor")
# Artık listem 4 elemanlı lakin yyugulama shutdown edildiğinde ilk yarıtıldığı hale geri dönecektir çünkü listeler RAM'de saklanır
# Listeler index mantığı ile çalışır yani listenin birinci elemanına erişme istersem
# futbol_taktmlarii[0] demem gerekir.

# top_boxers = ["Mike Tyson", "Muhammed Ali", "Lenox Lewis", "Evander Holyfild", "Rocky Marciano"]
# .append() => fonksiyonu ile listenin sonuna yeni bir eleman ekleriz.
# top_boxers.append("George Forman")
# insert() fonksiyonu listenin her hangi bir index deperine eleman ekleme işlemini yerine getirir.
# aldığı ilk oarametre index değerini
# ikinci parametre ise value temsil eder.
# top_boxers.insert(1, "Floyd Mayweater")
# remove() => listeden silmesini istediğmiz item'in değerini kendisine vererek silme işlemini gerçekleştirir.
# top_boxers.remove("Lenox Lewis")
# clear => fonksiyonu listenin alayını siliyor
# top_boxers.clear()
# pop() => verilen index değrinde ki elemanı siler
# top_boxers.pop(4)
# extend() => iki farklı lisyei birleştirmeye yarar
# currnet_boxar = ["Tyson Fury", "Deantony Wilder", "Antony Jasua"]
# top_boxers.extend(currnet_boxar)
# print(top_boxers)

# movies = ["Fight Club", "Matrix", "Interstailler", "Inception"]
# for i in movies:
#    print(i)

# for i in range(0, len(movies)):
#    print(movies[i])

# region Example-1
"""
from  random import randint
x = []
y = []
z = []
for i in range(10):
    x.insert(i, randint(0, 100))
    y.insert(i, randint(0, 100))

    z.insert(i, x[i] + y[i])

    print(f'{i, x[i]} + {i, y[i]} = {i, z[i]}')
print(z)
"""
# endregion

# region Example-2
"""
x = input("Bir kelime giriniz: ")
y = []
z = ["a", "e", "ı", "i", "u", "ü", "o", "ö"]
b_s = 0
t = []
for i in x:
    if i in z:
        if i not in y:
            y.append(i)
    elif i == " ":
        b_s += 1
    elif i.isdigit():
        t.append(i)
print(y)
print(b_s)
print(t)
"""
# endregion

# region Example-3
"""
from string import punctuation
x = input("Şifre giriniz: ")
s = True
for i in x:
    if i <= 16:
        s = False
        print("Yeni şifre gir")
    elif i.isdigit():
        s = False
        print("Yeni şifre gir") 
    elif i == punctuation:
        s = False
        print("Yeni şifre gir")
    elif i.isupper() == True:
        s = False
        print("Yeni şifre gir")
"""
# endregion

# region Example-4
"""
from string import punctuation
x = input("Şifre: ")
s = True
f = True
k = True
if len(x) >= 16:
    for i in x:
        if i.isdigit():
            s = True
        elif i in punctuation:
            f = False
        elif i.isupper():
            k = True
    if s and f and k:
        print("Şfre onaylandı")
    else:
        print("Yeni şifre gir")
else:
    print("Şifre 16 karakterli olmalı..")
"""
# endregion

# list Comprehansion
# raklmarı bir listeye ekleme
# sayılar = []
# for i in range(10)
#   sayılar.append(i)
# print(sayılar)

# print([i for i in range(10)])

# print({i**2 for i in range(10)})

#print({i**2 for i in range(101) if i % 3 == 0})
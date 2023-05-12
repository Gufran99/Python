# region Example-1

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

# endregion

# region Example-2

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

# endregion

# region Example-3

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

# endregion

# region Example -4

sayılar = []
for i in range(0, 10):
    sayılar.append(i)
print(sayılar)

# endregion

# region Example -5

from random import randint
lst = []
for i in range(0, 10):
    x = randint(0, 101)
    lst.append(x)
print(lst)

# endregion

# region Example -6

from random import randint
lis = []
for i in range(0, 10):
    x = randint(0, 100)
    if x % 3 == 0:
        print(x)
        lis.append(x**2)
print(lis)

# endregion

# region Example -7

x = input("Bir cümle yazın: ")
harf = []
for i in range(0, len(x)):
    if x[i] != " ":
        harf.append(x[i])
print(harf)
# endregion

# region Example -8

x = input("Bir cümle yazın: ")
harf = []
for i in x:
    if i != " ":
        harf.append(i)
print(harf)

# endregion

# region Example -9
sayilar = []
for i in range(10):
   sayilar.append(i)
print(sayilar)
# endregion

print([i for i in range(10)])

print({i**2 for i in range(10)})

print({i**2 for i in range(101) if i % 3 == 0})

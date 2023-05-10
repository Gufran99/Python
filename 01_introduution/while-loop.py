# region Example -1

sayac = 0
toplam = 0

while sayac <= 10:
    x = int(input("Lütfen bir sayı giriniz: "))
    toplam += x
    sayac += 1
print(f'Sayıların toplamı: {toplam}')

# endregion

# region Example-2

sayac = 0
while sayac <= 100:
    print(sayac)
    sayac += 1

# endregion

# region Example -3

sayac = 1
c_s = 0
t_s = 0
while sayac <= 101:
    if sayac % 2 == 0:
        c_s += 1
    else:
        t_s += 1
    sayac += 1
print(f'Çift sayılar: {c_s} \nTek sayılar:{t_s}')


# endregion

# region Example -4

sayac = 1
cs = 0
ts = 0

while sayac <= 100:
    if sayac % 2 == 0:
        cs += 1
        sayac += 1
    else:
        ts += 1
        sayac += 1
print(f'{cs} tane çift sayı vardır')
print(f'{ts} tane tek sayı vardır')

# endregion

# region Example -5

sayac = 1
cst = 0
tst = 0

while sayac <= 100:
    if sayac % 2 == 0:
        cst += sayac
    else:
        tst += sayac
    sayac += 1
print(f'Çift sayıların toplamı: {cst}')
print(f'Tek sayıların toplamı: {tst}')

# endregion

# region Example -6

p_t_l = ['+', '-', '*', '/', 'e']
while True:
    i = input("İşlem işareti giriniz: ")
    if i in p_t_l:
        # in operötörü ile bir liste içerisinde item varsa True yoksa Folse döner.  Yani burda kullanıcının girdi işlem bizim işlem türü listemizde varsa True yoksa False dönecekç

        if i == ("e"):
            break
        else:
            x = int(input("Sayı giriniz: "))
            y = int(input("Sayı giriniz: "))
            if i == ("+"):
                print(x+y)
            elif i == ("-"):
                print(x-y)
            elif i == ("*"):
                print(x*y)
            elif i == ("/"):
                print(x/y)
    else:
        print("Lütfen doğru bir işlem türü giriniz..'")

# endregion

# region Example -7

sayac = 0
tst = 0
while sayac <= 101:
    sayac += 1
    if sayac % 2 == 0:
        continue
    tst += sayac
print(f'Tek sayıların toplamı: {tst}')

# endregion

# region Example -8

from datetime import datetime
sayac = 1950
y = int(input("Yıl giriniz: "))
in_exist = False
while sayac <= datetime.now().year:
    if y == sayac:
        print("Bulundu")
        in_exist = True
        break
    sayac += 1
if not in_exist:
    print("Bulunamadı")

# endregion

# region Example -9
x = int(input("Bir sayı giriniz: "))
y = int(input("Bir sayı giriniz: "))
z = int(input("Bir sayı giriniz: "))
st = 0
while x < y:
    st = st + x + z
    x += z
print(st)
# endregion

# region Example -10
import random
x =random.randint(1, 100)
hak = 3

while x > 0:
    hak -= 1
    t = int(input("Tahminizi Griniz: "))
    if hak == 0:
        print(f'Bilemediniz cevap:{x}')
        break
    if x == t:
        print("Bildiniz")
        break
    elif x < t:
        print("Bilemediniz daha küçük")
    elif x > t:
        print("Bilemediniz daha büyük")

# endregionn

# region Example -11

x = int(input("Bir sayı giriniz: "))
b = 2
is_prime = True
if x == 1 or x <= 0:
    is_prime = False
    print("Sıfır ve Negatif sayılar asal değildir...")
else:
    while b < x:
        if x % b == 0:
            is_prime = False
        else:
            b += 1
        if is_prime == True:
                print("Asal sayı.")
                break
        else:
                print("Asal sayı değil")
                break

# endregion

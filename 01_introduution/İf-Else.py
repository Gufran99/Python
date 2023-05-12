# region Example -1

x = int(input("bir sayı gir: "))

if x % 2 == 0:
    print("çiftir")
else:
    print("tektir")

# endregion

# region Example -2

x = int(input("sayı gir: "))
y = int(input("sayı gir: "))

if x > y:
    print(f'{x} büyüüktür')
else:
    print(f'{y} büyüktür')

# endregion

# region Example -3

x = int(input("Sayı gir: "))
if x > 0:
    print("pozitiftir")
elif x < 0:
    print("negatiftir")
else:
    print("nötr")

# endregion

# region Example -4

x = input("mevsim giriniz: ").lower()
if x == ("kış"):
    print("Aralık", "Ocak", "Şubat")
elif x == ("ilk bahar"):
    print("Mart", "Nisan", "Mayıs")
elif x == ("yaz"):
    print("Haziran", "Temmuz", "Ağustos")
elif x == ("son bahar"):
    print("Eylül", "Ekim", "Kasım")
else:
    print("Böyle bir mevsim yok.")

# endregion

# region Example -5

x = int(input("Kaç gün kullandığnızı giriniz: "))

if x <= 365:
    print("1. serbis yılında")
elif 365 < x <= 365*2:
    print("2. serbis yılında")
elif 365*2 < x <= 365*3:
    print("3. serbis yılında")
else:
    print("Arabayı değiştir lütfen")

# endregion

# region Example -6

x = int(input("sayı gir: "))
y = int(input("sayı gir: "))
z = int(input("sayı gir: "))

if x > z and x > y:
    print(f'{x} büyüktür')
elif y > z and y > x:
    print(f'{y} büyüktür')
elif z > y and z > x:
    print(f'{z} büyüktür')
else:
    print("Sayılar birbirine eşit olabilir")

# endregion

# region Example -7

u_n = input("kulanıcı adı: ")
p = int(input("şifre: "))

if u_n == ("gufran") and p == (123):
    print("Hoşgeldiniz.")
else:
    print("Tanıyamadım")

# endregion

# region Example -8

x = int(input("kitap sayısı giriniz: "))
k_f = 5

if x <= 20:
    toplam =(x*k_f)*0.95
    print(toplam)
elif 20 < x <= 50:
    toplam = (x * k_f) * 0.90
    print(toplam)
elif 50 < x <= 75:
    toplam = (x * k_f) * 0.85
    print(toplam)
elif 75 < x <= 100:
    toplam = (x * k_f) * 0.75
    print(toplam)
else:
    print("Bölye bir indirim aralığmız yok")

# endregion

# region Example -9

urun = input("Bir ürün ismi giriniz: ").capitalize()

if urun == ("Domates") or urun == ("Çilek") or urun == ("Armut"):
    print("Sebze Reyonu.")
elif urun == ("Fare") or urun == ("Kulaklık") or urun == ("Yazıcı"):
    print("Teknoloji Reyonu.")
elif urun == ("Rimel") or urun == ("Allık") or urun == ("Ruj"):
    print("Kozmetik Reyonu.")
else:
    print("Böyle bir ürünümüz yok.")

# endregion

# region Example -10

a_t = input("Araba türünü giriniz: ").capitalize()
t = int(input("Hızı giriniz: "))

if a_t == ("Araba"):
    if t > 60:
        print("cezalı")
    else:
        print("cezalı değil")
elif a_t == ("Motor"):
    if t > 90:
        print("cezalı")
    else:
        print("cezalı değil")
elif a_t == ("Kamyon"):
    if t > 40:
        print("cezalı")
    else:
        print("cezalı değil")
else:
    print("Böyel bir araba türü yok... ")

# endregion

# region Example -11

u_n = input("Kulanıcı adı giriniz: ")
p = input("Şifre giriniz: ")

n_l = u_n.split(" ")

if n_l[0].lower() == ("gufran") and p == '123':
    b = float(input("Boyunuzu giriniz: "))
    k = float(input("Klolnuzu Giriniz: "))
    i = (k/b**2)
    if 0 < i <= 18.5:
        print("Zayıf")
    elif 18.5 < i <= 24.9:
        print("Normal")
    elif 24.9 < i <= 29.9:
        print("Kilolu")
    elif 29.9 < i <= 34.9:
        print("Fazla Kilolu")
    elif 34.9 < i <= 39.9:
        print("Obez")
    else:
        print("Böyle bir indeks yok.. ")
else:
    print("Hatalı giriş! ")

# endregion

# region Example -12

from math import sqrt

a = int(input("Birinci kat sayı: "))
b = int(input("İkinci kat sayı: "))
c = int(input("Üçüncü kat sayı: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = -b - sqrt(delta) / 2 * a
    x2 = -b + sqrt(delta) / 2 * a
    print(f'2 real kök bulunmaltadır. \nx1 ==> {x1}\nx2 ==> {x2}')
elif delta == 0:
    x1 = -b - sqrt(delta) / 2 * a
    print(f'real kök bulunmaltadır. \nx1 ==> {x1}')
else:
    print("There is no real root")

# endregion

# region Example -13

v = float(input("Vize: "))
f = float(input("Final: "))
o = float(input("Ödev: "))

ort = (v * 0.3 + f * 0.6 + o * 0.1)

if 90 <= ort <= 100:
    print("AA")
elif 85 <= ort <= 89:
    print("BA")
elif 80 <= ort <= 84:
    print("BB")
elif 75 <= ort <= 79:
    print("CB")
elif 70 <= ort <= 74:
    print("CC")
elif 65 <= ort <= 69:
    print("CD")
elif 60 <= ort <= 64:
    print("DD")
elif 55 <= ort <= 59:
    print("DC")
elif 50 <= ort <= 54:
    print("FD")
else:
    print("FF")

# endregion

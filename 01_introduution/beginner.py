# region Example -1
#Kulanıcıdan alınan 2 adet sayı üzerinden temel 4 işlemi yapan uygulama

sayi_1 = int (input("Lütfen bir sayı giriniz: "))
sayi_2 = int (input("Lütfen bir sayı giriniz: "))

toplam = sayi_1 + sayi_2
print(f'{sayi_1} + {sayi_2} = {toplam}')

cıkarma = sayi_1 - sayi_2
print(f'{sayi_1} - {sayi_2} = {cıkarma}')

carpma = sayi_1 * sayi_2
print(f'{sayi_1} * {sayi_2} = {carpma}')

bolme = sayi_1 / sayi_2
print(f'{sayi_1} / {sayi_2} = {bolme}')

# endregion

# region Example -2
"""
Kullanıcıdan alınan kenar bilgisine göre bir karenin alanını ve çevresini hesaplayan uygulama
"""

x = int (input("Lütfen sayı girin: "))

alan = x**2
cevre = x*4

input(alan)
input(cevre)

# endregion

# region Example -3

x = int(input("Uuzun kenarı girin: "))
y = int(input("kısa kenarı giriniz: "))

alan = x*y
cevre = 2*(x+y)

print(f'alan={alan}')
print(f'cevre={cevre}')

# endregion

# region Example -4

t = float(input("Tabanı gşrşnşz: "))
h = float(input("Yüksekliği giriniz: "))

alan= t*h/2
print(f'alan={alan}')

# endregion

# region Example -5

x = int(input("Sayı giriniz: "))
y = int(input("Sayı giriniz: "))
z = (x**2)+(y**2)
print(z)

# endregion

# region Example -6
# Kullanıcıdan tam adını alalım
# isim.soyisim@bilgiadam.com mail adresini oluşturalım ekrana basalım.

f_n = input("Tam Adınız: ").lower()
n_l = f_n.split(" ")
print(f'{n_l[0]}.{n_l[-1]}@bilgeadam.com')

# endregion



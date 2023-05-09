
# Dğişken (Variable
# yazılım dillerinde değişkeleri bezetebiliriz. Nasıl ki gündelik hayatımızda kutularda eşyalar salayabiliyorsak yazılımda değişkenler içerisinde anlık olarak değerler saklayabiliriz.

# Diğer proglama dilelerinde değişken tanımlama ilk önce değişkeni tipi sonra adını ve sonrada üzerine değer atarız. Burada şu hususa dikkat etmeliyiz. Değişkenimizi tanımlarken (declare) bir değişken tipine onu bağladık. Yani uygulama çalıştığı sürece "x" değişkeninin tipi "int". Burda ki önemki nokta arık "x" değeişkenine string bir değer atayamam.
# int x = 10

# Pythonda değişken tanımlarken hangi bir tip belirtmiyoruz.
# x = 10
# Bir tip belirlemediğmiz için değişkenimiz anlık olarak içerisine atılan değerin tipine bürünmektedir.
# x = "mike tyson"

#first_name = "Burak Yılmaz"

#print(first_name)
# Burada print() bulit-in fonksiyonu aracılığı ile değişken üzerinde tutulan ifadeyi ekrana yazdırdık.

#first_name = 10
# Yukardaki satırda first_name değişkeni içerisinde 10 değerini atadık. Gördüğünüz gibi isterseniz değeri değişlen içerisine atayabiliyoruz. Bu özelik C, C++, C#, Java, PHP  gibi proglamlmaa dilerinde bulunmamaktadır.
#print(first_name)
# print() algoritmada jullandığmız output olarak düşünebilirsiniz.

# region Example -1
#Kulanıcıdan alınan 2 adet sayı üzerinden temel 4 işlemi yapan uygulama
#Kulalanıcıdan input alırken python içerisinde buil-in olarak bulunan input() fonksiyonunu kullanıyoruz. Daha sonra kullanıcıyı doğru yönlendirmek için içerisine bir mesaj yazıyoruz. Lakin şunu unutmayalım kullanıcıdan her değer aldğımızda bize gelen vakunun tşpş strşng. Artimatiksel işlem yapmak istediğmizde bize gelne değeri int değişkeni tipine döndürmemiz lazm.
"""
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
"""
# endregion

# region Example -2
"""
Kullanıcıdan alınan kenar bilgisine göre bir karenin alanını ve çevresini hesaplayan uygulama
"""
"""
x = int (input("Lütfen sayı girin: "))

alan = x**2
cevre = x*4

input(alan)
input(cevre)
"""
# endregion

# region Example -3
"""
x = int(input("Uuzun kenarı girin: "))
y = int(input("kısa kenarı giriniz: "))

alan = x*y
cevre = 2*(x+y)

print(f'alan={alan}')
print(f'cevre={cevre}')
"""
# endregion

# region Example -4
"""
t = float(input("Tabanı gşrşnşz: "))
h = float(input("Yüksekliği giriniz: "))

alan= t*h/2
print(f'alan={alan}')
"""
# endregion

# region Example -5
"""
x = int(input("bir sayı gir: "))

if x % 2 == 0:
    print("çiftir")
else:
    print("tektir")
"""
# endregion

# region Example -6
"""
x = int(input("sayı gir: "))
y = int(input("sayı gir: "))

if x > y:
    print(f'{x} büyüüktür')
else:
    print(f'{y} büyüktür')
"""
# endregion

# region Example -7
"""
x = int(input("Sayı gir: "))
if x > 0:
    print("pozitiftir")
elif x < 0:
    print("negatiftir")
else:
    print("nötr")
"""
# endregion

# region Example -8
"""
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
"""
# endregion

# region Example -9
"""
x = int(input("Kaç gün kullandığnızı giriniz: "))

if x <= 365:
    print("1. serbis yılında")
elif 365 < x <= 365*2:
    print("2. serbis yılında")
elif 365*2 < x <= 365*3:
    print("3. serbis yılında")
else:
    print("Arabayı değiştir lütfen")
"""
# endregion

# region Example -10
"""
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
"""
# endregion

# region Example -11
"""
u_n = input("kulanıcı adı: ")
p = int(input("şifre: "))

if u_n == ("beast") and p == (123):
    print("Welcome Major")
else:
    print("Tanıyamadım")
"""
# endregion

# region Example -12
"""
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
"""
# endregion

# region Example -13
"""
urun = input("Bir ürün ismi giriniz: ").capitalize()

if urun == ("Domates") or urun == ("Çilek") or urun == ("Armut"):
    print("Sebze Reyonu.")
elif urun == ("Fare") or urun == ("Kulaklık") or urun == ("Yazıcı"):
    print("Teknoloji Reyonu.")
elif urun == ("Rimel") or urun == ("Allık") or urun == ("Ruj"):
    print("Kozmetik Reyonu.")
else:
    print("Böyle bir ürünümüz yok.")
"""
# endregion

# region Example -14
"""
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
"""
# endregion

# region Example -15
"""
u_n = input("Kulanıcı adı giriniz: ")
p = input("Şifre giriniz: ")
# Kullanıcının ismi birden fazla kelime içerebilir. Bu yüzden bize gelen string ifade içerisinde bulunan boşluk karakterinden ifademizi aşağıda split ediyoruz yani parçalıyoruz. split() fonksiyonu bizden aşağıda ki kullanımında bir parametre istedi bizde bırda boşluk karakterini kullandık. split() işini bitirdikten sonra bize bir liste döndü. bu elde etiğimiz listeyide 'n_l' isimli değişkene atadık.
n_l = u_n.split(" ")
# artık n_l listesinin index değerlerini bulunan ifadelere istediğim gibi erişebikirim aşağıda sıfırncı indexte tutulan değeri prin ettik.
# print(n_l[0])
# Login işlemi
# Kulanıcının ilk adı ve şifresi ile login olsu

if n_l[0].lower() == ("burak") and p == '123':
    b = float(input("Boyunuzu giriniz: "))
    k = float(input("Klolnuzu Giriniz: "))
    i = (k/b)**2
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
"""
# endregion

# region Example -16
"""
sayac = 0
toplam = 0

while sayac <= 10:
    x = int(input("Lütfen bir sayı giriniz: "))
    toplam += x
    sayac += 1
print(f'Sayıların toplamı: {toplam}')
"""
# endregion

# region Example -17
"""
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
"""
# endregion

# region Example -18
"""
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
"""
# endregion

# region Example -19
"""
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
"""
# endregion

# region Example -20
"""
sayac = 0
tst = 0
while sayac <= 101:
    sayac += 1
    if sayac % 2 == 0:
        continue
    tst += sayac
print(f'Tek sayıların toplamı: {tst}')
"""
# endregion

# region Example -21
"""
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
"""
# endregion

# region Example -22
"""x = int(input("Bir sayı giriniz: "))
y = int(input("Bir sayı giriniz: "))
z = int(input("Bir sayı giriniz: "))
st = 0
while x < y:
    st = st + x + z
    x += z
print(st)"""
# endregion

# region Example -22
"""import random
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
"""
# endregionn

# region Example -23
"""
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
"""
# endregion

# region Example -24
"""
best_heavy_weiglths = ["Mike Tyson", "Muhammed Ali", "Lenox Lewis", "Evaander Holyfiled"]
for boxar in best_heavy_weiglths:
    print(boxar)
"""
# endregion

# region Example -25
"""
best_heavy_weiglths = ["Mike Tyson", "Muhammed Ali", "Lenox Lewis", "Evaander Holyfiled"]
x = input("Bir boxar giriniz: ").title()
for boxar in best_heavy_weiglths:
    if x == boxar:
        print(boxar)
        break
    else:
        print("Böyle biri yok")
        break
"""
# endregion

# region Example -26
"""
x = int(input("Sayı giriniz: "))
y = int(input("Sayı giriniz: "))
z = (x**2)+(y**2)
print(z)
"""
# endregion

# region Example -27
"""
from math import sqrt
#Uyarı: Python'da aritmatiksel işlemler için bulunan bir modül bulumaktadır. Bu modülün adı "math". Karakök işlemi için  bu modül içerisinde
# bulunma sqrt() fonksiyonundan faydalanıcağız Bu modülden faydalana bilmek için çalışma dosyamıza bu modülü import etmemiz gerekmemektedir
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
"""
# endregion

# region Example -28
"""
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
"""
# endregion

# region Example -29
# Kullanıcıdan tam adını alalım
# isim.soyisim@bilgiadam.com mail adresini oluşturalım ekrana basalım.
"""
f_n = input("Tam Adınız: ").lower()
n_l = f_n.split(" ")
print(f'{n_l[0]}.{n_l[-1]}@bilgeadam.com')
"""
# endregion

# region Example-30
"""
sayac = 0
while sayac <= 100:
    print(sayac)
    sayac += 1
"""
# endregion

# region Example -31
"""
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

"""
# endregion
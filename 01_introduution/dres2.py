
#For Loop
#For Loop geçmeden önce incelememiz gereken bir kaç tane yardımcı oparetör ve fonksiyon bulunmaktadır. Bunlar 'in' be 'not in' ayrıca range() fonksiyonlarıdır.

# "in" operatörü bir liste içerisinde araman ifade geçmiyırsa araman ifade True  geçiyorsa  Fakse döner. Şunu unutmayalaım string ifadelerde karakter dizileridir yani bir string ifadeye "in" operatörünü kullanabiliriz.

# "not in " opertörü ise "in" operatörünün tam tersi mantıkla çalışır aranan ifade geçmiyorsa True geçiyorsa Fase döner.

#name = 'Mike Tyson'

#print('b' in name)
#print('m' in name)
#print('M' in name)

#print('b' not in name)
#print('M' not in name)

# range() fonksiyonu for loop ile sıklıkla kulanıllan bir yapıdır.
# ranfe(100) fonksioynu içerisine burda olduğu gibi 100 değrini verirsek bize 0-99 arasıdnaki bir tam sayi ifadesi döner
# unutmayın range içersinie bir argüman verildiğinde varlilen argüman "n" kabıl edersek "n-1" kadar çalışır. Ayrıca yine aynı senaryıda rage default olarak sıfırdan başladı. Biz aksini söylediğmiz sürece range default olarak gep sıfırdan başlayacaktır.

#for i in  range(10):
    #print(i) burda print() fonksiyonuu değerleri alt alta yazmaktadır. Buna yan yana yazdırmanın yolunu buşun.

# range() donksiyouna 2 argüman verirsek örneğin 5 ile10 5 ten başlayarak 0 kadar bir sayı listesi döner.
# range() fonksiyonunu 2 argiman verildiğinde birinci argüman başlangıç değeri ijinci argüman bittiş değirini temsil eder.

#for i in range(5, 10):
 #   print(i)

 # ranfe() 3 argüman verirsek 1 .argüman başlangıç 2. arhüman bitiş. 3. argüman ise adım miktarıı temsil eder.
#for i in range(1, 21, 2):
#   print(i)

# region Exaöple -1
"""
cst = 0
tst = 0
for i in range(1, 101): # while loop plduğu gibi adım miktarını biz arrtırmıyoruz aksini söylemediğmiz sürece 1 olarak yani dafuşt bir bakul edilip çalışır
    if i % 2 == 0:
        cst += i
    else:
        tst += i

print(f'Çiflerin Toplamı: {cst} \nTeklerin toplamı: {tst}')
"""
# endregion

# region Exaöple -2
# kullanıcıdan başlangıç, bittiş ve adım miktarını alalım. Bu şartlaraın bağlı kullanarak her bir adımda ki sayının karesi olarak ekrana yazdıralım
#çıktıyı şu formatta istiyorum 1. adımdaki sonuç: 2
"""
x = int(input("Başlangıç sayısını giriniz: "))
y = int(input("Bitiş sayısını giriniz: "))
z = int(input("Adım miktarını giriniz: "))
karelerin_toplam = 0
counter = 1
for i in range(x, y, z):
    karelerin_toplam = i**2
    print(f'{counter}. adımda ==> {karelerin_toplam}')
    counter += 1
"""
# endregion

# region Example -3
# Kulanıcıdan alınan sayı asalmı değil mi
"""
x = int(input("Bir sayı giriniz: "))
if x <= 0:
    print("Sıfır ve Negatif sayılar asal değildir...")
else:
    is_prime = True
    if x == 1:
        is_prime = False

    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break

    if is_prime: #burda is_prime değişkeni ğzerine true varsa if bloğu tetiklnecek
        print(f'{x} asaldır.')
    else:
        print(f'{x} asal değildir.')
"""
# endregion

# region Example -4
"""
c = 1
for i in range(0, 1001, 10):
    print(f'{c}. adımda ==> {i} + {10} = {i + 10} ')
    c += 1
"""
# endregion

# region Example -5
"""
for i in range(1, 11):
    for a in range(1, 11):
        print(f'{a} * {i} = {a*i}')
    print("================")
"""
# endregion

# region Example -6
"""
x = int(input("Kenar uzunluğnu giriniz: "))
for i in range(0, x):
    for a in range(0, x):
        print("*", end='')
    print(" ")
"""
# endregion

# region Example -7
"""
x = int(input("Kenar uzunluğnu giriniz: "))
y = 1
for i in range(0, x):
    for a in range(0, y):
        print("*", end='')
    y += 1
    print(" ")
"""
# endregion

# region Example -8
"""
x = int(input("Kenar uzunluğnu giriniz: "))
for i in range(0, x):
    for a in range(0, x):
        if a <= i:
            print("*", end='')
    print(" ")
"""
# endregion

# region Example -9
"""
sayılar = []
for i in range(0, 10):
    sayılar.append(i)
print(sayılar)
"""
# endregion

# region Example -10
"""
from random import randint
lst = []
for i in range(0, 10):
    x = randint(0, 101)
    lst.append(x)
print(lst)
"""
# endregion

# region Example -11
"""
from random import randint
lis = []
for i in range(0, 10):
    x = randint(0, 100)
    if x % 3 == 0:
        print(x)
        lis.append(x**2)
print(lis)
"""
# endregion

# region Example -12
# Kullanıcıdan  bir söz öbeği alıyoruz.
# Örneğin ben burak yılmaz
# yukarda ki örnek söz öbeğideki her bri harfi listeye ekleyin
# Yol 1
# söz öbeği içerisinde adım adım dolaşarak
"""
x = input("Bir cümle yazın: ")
harf = []
for i in range(0, len(x)):
    if x[i] != " ":
        harf.append(x[i])
print(harf)
"""
# Yol 2
# söz öbeğindeli her bir harfi döngüye itarate ederek yapın
"""
x = input("Bir cümle yazın: ")
harf = []
for i in x:
    if i != " ":
        harf.append(i)
print(harf)
"""
# endregion
# region Example -24

best_football_player = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Ronaldinho"]
for footballer in best_football_player:
    print(footballer)

# endregion

# region Example -25

best_football_player = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Ronaldinho"]
x = input("Bir boxar giriniz: ").title()
for footballer in best_football_player:
    if x == footballer:
        print(footballer)
        break
    else:
        print("Böyle biri yok")
        break

# endregion

# region Exaöple -1

cst = 0
tst = 0
for i in range(1, 101): # while loop plduğu gibi adım miktarını biz arrtırmıyoruz aksini söylemediğmiz sürece 1 olarak yani dafuşt bir bakul edilip çalışır
    if i % 2 == 0:
        cst += i
    else:
        tst += i

print(f'Çiflerin Toplamı: {cst} \nTeklerin toplamı: {tst}')

# endregion

# region Exaöple -2
# kullanıcıdan başlangıç, bittiş ve adım miktarını alalım. Bu şartlaraın bağlı kullanarak her bir adımda ki sayının karesi olarak ekrana yazdıralım
#çıktıyı şu formatta istiyorum 1. adımdaki sonuç: 2

x = int(input("Başlangıç sayısını giriniz: "))
y = int(input("Bitiş sayısını giriniz: "))
z = int(input("Adım miktarını giriniz: "))
karelerin_toplam = 0
counter = 1
for i in range(x, y, z):
    karelerin_toplam = i**2
    print(f'{counter}. adımda ==> {karelerin_toplam}')
    counter += 1

# endregion

# region Example -3
# Kulanıcıdan alınan sayı asalmı değil mi

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

# endregion


# region Example -4

c = 1
for i in range(0, 1001, 10):
    print(f'{c}. adımda ==> {i} + {10} = {i + 10} ')
    c += 1

# endregion

# region Example -5

for i in range(1, 11):
    for a in range(1, 11):
        print(f'{a} * {i} = {a*i}')
    print("================")

# endregion

# region Example -6

x = int(input("Kenar uzunluğnu giriniz: "))
for i in range(0, x):
    for a in range(0, x):
        print("*", end='')
    print(" ")

# endregion

# region Example -7

x = int(input("Kenar uzunluğnu giriniz: "))
y = 1
for i in range(0, x):
    for a in range(0, y):
        print("*", end='')
    y += 1
    print(" ")

# endregion

# region Example -8

x = int(input("Kenar uzunluğnu giriniz: "))
for i in range(0, x):
    for a in range(0, x):
        if a <= i:
            print("*", end='')
    print(" ")

# endregion

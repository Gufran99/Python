# region Example -1

best_football_player = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Ronaldinho"]
for footballer in best_football_player:
    print(footballer)

# endregion

# region Example -2

best_football_player = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Ronaldinho"]
x = input("Bir footballer giriniz: ").title()
is_prime = True
for footballer in best_football_player:
    if x == footballer:
        is_prime = True
        break
    else:
        is_prime = False
if is_prime:
    print(footballer)
else:
    print("Böyle biri yok")
# endregion

# region Exaöple -3

cst = 0
tst = 0
for i in range(1, 101):
    if i % 2 == 0:
        cst += i
    else:
        tst += i

print(f'Çiflerin Toplamı: {cst} \nTeklerin toplamı: {tst}')

# endregion

# region Exaöple -4

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

# region Example -5

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


# region Example -6

c = 1
for i in range(0, 1001, 10):
    print(f'{c}. adımda ==> {i} + {10} = {i + 10} ')
    c += 1

# endregion

# region Example -7

for i in range(1, 11):
    for a in range(1, 11):
        print(f'{a} * {i} = {a*i}')
    print("================")

# endregion

# region Example -8

x = int(input("Kenar uzunluğnu giriniz: "))
for i in range(0, x):
    for a in range(0, x):
        print("*", end='')
    print(" ")

# endregion

# region Example -9

x = int(input("Kenar uzunluğnu giriniz: "))
y = 1
for i in range(0, x):
    for a in range(0, y):
        print("*", end='')
    y += 1
    print(" ")

# endregion

# region Example -10

x = int(input("Kenar uzunluğnu giriniz: "))
for i in range(0, x):
    for a in range(0, x):
        if a <= i:
            print("*", end='')
    print(" ")

# endregion

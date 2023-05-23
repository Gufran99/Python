
# False method
isim = input("Adınızı giriniz: ")
print(f'Merhaba {isim}')
# True method
def hello(tam_isim: str) -> None:
    print(f'Merhaba {tam_isim}')

isim = input("Adınızı giriniz: ")
hello(isim)



# False method
tam_ad = input("Tam isminizi giriniz: ").lower()
print(f'{tam_ad.split(" ")[0]}.{tam_ad.split(" ")[-1]}@gmail.com')
# True method
def gmail(tam_ad: str) -> None:
    print(f'{tam_ad.split()[0]}.{tam_ad.split()[-1]}@gmail.com')

tam_ad = input("Tam isminiz giriniz: ").lower()
gmail(tam_ad)


# False method
x = int(input("Bir sayı giriniz: "))
if x % 2 == 0:
    print(f'{x} sayısı çifttir...')
else:
    print(f'{x} sayısı tektir...')
# True method
def tek_cift(sayi: int) -> None:
    if x % sayi == 0:
        print(f'{sayi} sayısı çifttir...')
    else:
        print(f'{sayi} sayısı tektir...')

x = int(input("Bir sayı giriniz: "))
tek_cift(x)
tek_cift(25)
tek_cift(24)


# False method
x = int(input("Sayı giriniz: "))
if x < 0:
    print("Sıfırdan küçük sayıların faktoriyeleri hesaplanmaz")
else:
    sayac = 1
    if x == 0 and x == 1:
        print(f'Sonuç: {sayac}')
    else:
        while x > 1:
            sayac *= x
            x -= 1
    print(f'Sonuc: {sayac}')
# True method
def faktoriyel(x: int) -> None:
    if x < 0:
        print("Sıfırdan küçük sayıların faktoriyeleri hesaplanmaz")
    else:
        sayac = 1
        if x == 0 and x == 1:
            print(f'Sonuç: {sayac}')
        else:
            while x > 1:
                sayac *= x
                x -= 1
            print(f'Sonuc: {sayac}')

sayi = int(input("Sayı giriniz: "))
faktoriyel(sayi)
faktoriyel(7)
faktoriyel(15)
faktoriyel(1)
faktoriyel(0)
faktoriyel(-1)
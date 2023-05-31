from  pprint import pprint
# False method
kullanici_ad = {
    '1': {
        'kullanici_ad': 'gufran',
        'sifre': '123'
    },
    '2': {
        'kullanici_ad': 'murat',
        'sifre': '123'
    }
}

kulanici_list = []
def giris(kulanici_adi: str, sifre: str) -> None:
    is_ture = False
    for i in range(1, len(kullanici_ad) + 1):
        if kullanici_ad.get(str(i)).get('kullanici_ad') == kulanici_adi and kullanici_ad.get(str(i)).get('sifre') == sifre:
            is_ture = True
            break
    if is_ture:
        print("Grişi yaptınız..")
    else:
        print("bilgilerinizi kontrol ediniz..")

def kayit(kulanici_adi: str, sifre: str) -> None:
    is_ture = False
    for j in range(1, len(kullanici_ad) + 1):
        kulanici_list.append(kullanici_ad.get(str(j)).get('kullanici_ad'))
        if kulanici_adi in kulanici_list:
            is_ture = True
            break
        else:
            kullanici_ad[str(len(kullanici_ad) + 1)] = {
                'kullanici_ad': kulanici_adi, 'sifre': sifre
            }
            break
    if is_ture:
        print('Farklı bir kullanıcı adı deneyin..!')
    else:
        print('Hesabınız oluşturuldu')

def main():
    while True:
        process = input('İşlem giriniz: ').lower()
        if process == 'çıkış':
            break
        elif process == 'giriş yap':
            user_name = input('Kullanıcı Adı: ')
            password = input('Şifre: ')
            giris(user_name, password)
        elif process == 'kayıt ol':
            user_name = input('Kullanıcı Adı: ')
            password = input('Şifre: ')
            kayit(user_name, password)
            pprint(kullanici_ad)
        else:
            print('Lütfen uygun bir işlem türü giriniz..!')

main()
# True method
kullanici_ad = {
    '1': {
        'kullanici_ad': 'gufran',
        'sifre': '123'
    },
    '2': {
        'kullanici_ad': 'murat',
        'sifre': '123'
    }
}

def liste(kullanici_ad: dict) -> list:
    kullanici_ad_list = []

    for i in range(1, len(kullanici_ad) + 1):
        kullanici_ad_list.append(kullanici_ad.get(str(i)).get("kullanici_ad"))

    return kullanici_ad_list

def giris(kullanici_adi: str, sifre: str) -> None:
    is_true = False
    for i in range(1, len(kullanici_ad) + 1):
        if kullanici_ad.get(str(i)).get("kullanici_ad") == kullanici_adi and kullanici_ad.get(str(i)).get("sifre") == sifre:
            is_true = True
            break
    if is_true:
        print("Giriş yaptınız..")
    else:
        print("Bilgilerinizi konturo ediniz..")

def kayıt(kullanici_adi: str, sifre: str) -> None:
    if kullanici_adi in liste(kullanici_ad):
        print("İsim zaten kullanılıyor..")
    else:
        print("Hesabınız oluşturulud..")
        kullanici_ad[str(len(kullanici_ad) + 1)] = {
            'kullanici_ad': kullanici_adi, 'sifre': sifre
        }
def main():
    while True:
        process = input('İşlem giriniz: ').lower()
        if process == 'çıkış':
            break
        elif process == 'giriş yap':
            user_name = input('Kullanıcı Adı: ')
            password = input('Şifre: ')
            giris(user_name, password)
        elif process == 'kayıt ol':
            user_name = input('Kullanıcı Adı: ')
            password = input('Şifre: ')
            kayıt(user_name, password)
            pprint(kullanici_ad)
        else:
            print('Lütfen uygun bir işlem türü giriniz..!')

main()
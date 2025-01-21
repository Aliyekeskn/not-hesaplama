kullanıcı_sayısı = int(input("kaç kullanıcı girilecek:"))
öğrenci_isimleri = []
öğrenci_notları = []

for i in range(kullanıcı_sayısı):
    öğrenci_ismi = input("öğrencinin ismini giriniz:")
    öğrenci_isimleri.append(öğrenci_ismi)
    öğrenci_notu = int(input("öğrencinin notu giriniz:"))
    öğrenci_notları.append(öğrenci_notu)

for i in range(kullanıcı_sayısı):
    if öğrenci_notları[i] < 50:
        print(öğrenci_isimleri[i], "öğrencisinin notu:", öğrenci_notları[i])
        print("durumu: öğrenci kaldı")
    else:
        print(öğrenci_isimleri[i], "öğrencisinin notu:", öğrenci_notları[i])
        print("durumu: öğrenci geçti")




    

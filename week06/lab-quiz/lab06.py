branslar = ("Yazılım", "Tasarım", "Pazarlama")

tum_ogrenciler = []

ogrenci1 = [input("1. Öğrencinin adını girin: ").strip(), ["Yazılım"]]
ogrenci2 = [input("2. Öğrencinin adını girin: ").strip(), ["Tasarım"]]
ogrenci3 = [input("3. Öğrencinin adını girin: ").strip(), ["Pazarlama"]]

tum_ogrenciler.append(ogrenci1)
tum_ogrenciler.append(ogrenci2)
tum_ogrenciler.append(ogrenci3)


baskan = ["Başkan", ["Yazılım"]]
tum_ogrenciler.insert(0, baskan)

print("Toplam Kayıtlı Öğrenci Sayısı:", len(tum_ogrenciler))


silinecek_isim = input("Kulüpten ayrılacak öğrencinin adını girin: ").strip()

for ogrenci in tum_ogrenciler:
    if ogrenci[0] == silinecek_isim:
        tum_ogrenciler.remove(ogrenci)
        break

cikan_ogrenci = tum_ogrenciler.pop()

print("Sistemden en son çıkan öğrenci:", cikan_ogrenci[0])

burak = ["Burak Tan", ["Tasarım"]]
tum_ogrenciler.append(burak)

gecici_liste = sorted(tum_ogrenciler, key=lambda ogrenci: ogrenci[0])

print("\nAlfabetik Sıralanmış Geçici Liste:")
print(gecici_liste)

print("\nOrijinal Liste (Sıralama Öncesi):")
print(tum_ogrenciler)

tum_ogrenciler.sort(key=lambda ogrenci: ogrenci[0])

print("\nKalıcı Olarak Alfabetik Sıralanmış Liste:")
print(tum_ogrenciler)


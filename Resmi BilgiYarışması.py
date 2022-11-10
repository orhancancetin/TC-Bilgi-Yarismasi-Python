#Resmi bir şekilde yazacağım Python Bilgi Yarışması
print("Her TC Vatandaşının bilmesi gereken sorulardan oluşan testime hoşgeldiniz :)")

isim = input("İsim girişi yapınız: ")

print("Teste tekrardan hoş geldin " + isim)

durum = input("Hazır mısın? (evet/hayır)")

dogru = 0

soru_sayisi = 10

if durum.lower() == "evet":
    soru1 = input("1.SORU Türkiye'nin başkenti neresidir?")
    if soru1.lower() == "ankara":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru2 = input("2.SORU Cumhuriyet hangi yıl ilan edilmiştir?")
    if soru2 == "1923":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru3 = input("3.SORU Atatürk'ün Kurtuluş Savaşını başlattığı tarih nedir? (Gün/Ay/Yıl) şeklinde yazılması yeterlidir.")
    if soru3.lower() == "19/05/1919" or "19 Mayıs 1919":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru4 = input("4.SORU TBMM'nin kuruluş tarihi nedir? (Gün/Ay/Yıl) şeklinde yazılması yeterlidir.")
    if soru4.lower() == "23/04/1920" or "23 Nisan 1920":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru5 = input("5.SORU Mustafa Kemal Atatürk'ün en büyük eseri nedir?")
    if soru5.lower() == "Cumhuriyet" or "Türkiye Cumhuriyeti":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru6 = input("6.SORU Medeni Kanun hangi yılda ilan edilmiştir?")
    if soru6 == "1926":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru7 = input("7.SORU Kurtuluş Savaşındaki tek taarruz savaşının ismi nedir?")
    if soru7.lower() == "büyük taarruz":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru8 = input("8.SORU Türkiye kaç bölgeden oluşmaktadır?")
    if soru8.lower() == "yedi" or "7":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")
    
    soru9 = input("9.SORU Hatay'ın anavatana hangi yıl katılmıştır?")
    if soru9 == "1939":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")

    soru10 = input("10.SORU Mustafa Kemal Atatürk'ün vefat tarihi nedir? (Gün/Ay/Yıl) tam olarak belirtiniz.")
    if soru10.lower() == "10/11/1938" or "10 kasım 1938":
        dogru += 1
        print("Tebrikler,cevabınız doğru!!")
    else:
        print("Maalesef,cevabınız yanlış.")


print("Testimiz sona ermiştir katılım gösterdiğiniz için teşekkür ederim.")
puan = (dogru/soru_sayisi) * 100
print("Sayın " + isim + " testin sonucu oluşan puanınız: " + str(puan))
print("Bir dahaki testlere görüşmek üzere :) ")


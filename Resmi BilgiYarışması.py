#Global degiskenler
SONUC = 0
SORU_SAYISI = 2
SORULAR = ["Türkiye'nin başkenti neresidir?", "Cumhuriyet hangi yıl ilan edilmiştir?"]
CEVAPLAR = ["ankara","1923"]
EVET_MESAJ = "Tebrikler, cevabınız doğru!"
YANLIS_MESAJ = "Maalesef, cevabınız yanlış."


def main():
    print("Her TC Vatandaşının bilmesi gereken sorulardan oluşan testime hoşgeldiniz :)")
    isim = input("İsim girişi yapınız: ")
    print("Teste tekrardan hoş geldin " + isim)
    durum = input("Hazır mısın? (e/h)").lower()
    if durum == 'h': #Gelisime hazir
        exit()

    sorulan_soru = 0
    while sorulan_soru < SORU_SAYISI:
        soruSor(sorulan_soru)
        sorulan_soru += 1
    print("Sonuc: ", SONUC)
    exit()


#Soru sorma isini otomatiklestiriyoruz, ona gore puanlari duzenliyor
def soruSor(n):
    global SONUC #bunu degistirdigimiz icin global olarak cagirdik. digerlerine gerek yok
    cevap = input(SORULAR[n]).lower()
    if cevap == CEVAPLAR[n]:
        SONUC += 1
        print(EVET_MESAJ)
        return 0
    else:
        print(YANLIS_MESAJ)
        return 0


if __name__ == "__main__":
    main()

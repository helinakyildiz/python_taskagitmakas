import random

def tas_kagit_makas():
    # Oyun Kuralları
    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!")
    print("Kurallar: Taş, kağıdı yener; Kağıt, makası yener; Makas, taşı yener.")
    print("Oyundan çıkmak için 'q' tuşuna basabilirsiniz.\n")

    # Seçenekler
    secenekler = ["taş", "kağıt", "makas"]
    
    # Sayaçlar
    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0
    oyun_sayisi = 0

    # Ana Oyun Döngüsü
    while True:
        oyun_sayisi += 1
        tur_sayisi = 0
        oyuncu_tur_galibiyet = 0
        bilgisayar_tur_galibiyet = 0
        
        print(f"\n{oyun_sayisi}. Oyuna Başlıyoruz!")

        # Turlar Döngüsü
        while oyuncu_tur_galibiyet < 2 and bilgisayar_tur_galibiyet < 2:
            print("\nSeçenekler: Taş, Kağıt, Makas")
            oyuncu_secimi = input("Seçiminizi yapın: ").lower()

            if oyuncu_secimi == 'q':
                print("Oyundan çıkılıyor...")
                return

            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçim! Lütfen taş, kağıt veya makas seçin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu siz kazandınız!")
                oyuncu_tur_galibiyet += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_tur_galibiyet += 1

            tur_sayisi += 1
            print(f"Skor: Oyuncu {oyuncu_tur_galibiyet} - Bilgisayar {bilgisayar_tur_galibiyet}")

        # Oyun Galibini Belirleme
        if oyuncu_tur_galibiyet == 2:
            print("\nTebrikler! Oyunu kazandınız!")
            oyuncu_galibiyet += 1
        else:
            print("\nMaalesef, bilgisayar oyunu kazandı!")
            bilgisayar_galibiyet += 1

        # Devam Etme İsteği
        devam = input("\nBaşka bir oyun oynamak ister misiniz? (e/h): ").lower()
        if devam != 'e':
            break

    print("\nOyun bitti!")
    print(f"Toplam Oyun Sayısı: {oyun_sayisi}")
    print(f"Son Skor: Oyuncu {oyuncu_galibiyet} - Bilgisayar {bilgisayar_galibiyet}")
    print("Teşekkürler! Tekrar oynayın!")

# Oyunu başlat
tas_kagit_makas()

import time
import random
tahmin_hakki = 6
rastgele_sayi = random.randint(1,100)
rastgele_sayi%2==0
"""**************



Sayı tahmin oyununa hoş geldiniz. 
Bu oyunda kullanıcıdan istenilen, 
1 ile 100 arasında rastgele seçilen bir sayıyı tahmin etmesidir.
Saygılar.



***************"""
while True:
  tahmin = int(input("Tahmininiz: "))
  if tahmin < rastgele_sayi:
    print("Tahmininiz değerlendiriliyor....")
    time.sleep(1)
    print("Lütfen daha büyük bir sayı söyleyiniz")
    tahmin_hakki -= 1
    print("Kalan tahmin hakkınız",tahmin_hakki)
  elif tahmin > rastgele_sayi:
    print("Tahmininiz değelendiriliyor....")
    time.sleep(1)
    print("Lütfen daha küçük bir sayı söyleyiniz....")
    tahmin_hakki -= 1
    print("Kalan tahmin hakkınız", tahmin_hakki)
  else:
    print("Tebrikler Kazandınız!!")
    break
  if tahmin_hakki == 0:
    print("Tahmin hakkınız bitti :(( )))")


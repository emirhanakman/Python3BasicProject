def dortgen_alan_hesapla_v1(genislik, yukseklik):
    alani = int(genislik) * int(yukseklik) #genişlik ile yükseklik değerini çarpıyoruz // kısa kenar ile uzun kenar da denilebilir.
    print ("Alan :", alani ,"m2") #burada alan= alan değeri ve sonuna da m2 ifadesi ekledim.
    return alani
genislik_degeri = input("Genişlik: ") #genislik degerini kullanicidan aliyoruz
yukseklik_degeri = input("Yükseklik: ") #yukseklik degerini kullanicidan alıyoruz
dortgen_alan_hesapla_v1(genislik_degeri, yukseklik_degeri)

def daire_alan_hesapla_v1(yaricap):
    cap=2 
    pi=3.14 #pi sayısının değerini yazıyoruz
    capi = int(yaricap) * cap #yarıçapın çapını 2 ile çarparak buluyoruz.
    print ("Dairenin Alanı :", capi * pi) #çap ile pi değerini çarpınca daire alanı geliyor.
    return capi
yaricap = input("Yarıçapı: ")
daire_alan_hesapla_v1(yaricap)

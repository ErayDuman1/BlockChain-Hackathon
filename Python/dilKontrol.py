class dilKontrol:
    def __init__(self,dosyaAdi):
        self.dosyaAdi=dosyaAdi
        self.metin=self.dosyaOku()
    
    def dosyaOku(self):
        try:
            dosya=open(self.dosyaAdi,"r",encoding='utf8')#Dosya okuma işlemi gerçekleşir.
            return dosya.read()
        except (OSError,FileNotFoundError,IOError):
            print("Dosya okumasında bir hata meydana geldi. (Dosya bulunamadı.)\n")
            return ""

    def kelimeHesapla(self):#Dosyadaki kelime sayısını döndürür.
        metin=self.metin
        kelimeler= metin.split()    #Metni kelimelere böler.
        return len(kelimeler)
        
    def cumleHesapla(self):#Dosyadaki cümle sayısını döndürür.
        metin=self.metin
        metin = metin.replace('?','.')        #Soru işareti karakterini nokta ile değiştirir.
        metin = metin.replace('!','.')         #Ünlem karakterini nokta ile değiştirir.
        metin = metin.replace("...",".")    #Üç nokta karakterini nokta ile değiştirir.

        cumleler= metin.split(".")
        cumleler=list(filter(None, cumleler))#Dosyadan okunduktan sonra list tipine çevirdiğimizde oluşan boş değeri siler.
        return len(cumleler)
    
    def sesliHarfHesapla(self):#Dosyadaki sesli harf sayısını döndürür.
        metin=self.metin
        sesliHarfler = "AEIİOÖUÜaeıioöuü"
        sesliHarfSayisi=0
        for i in metin:
            if i in sesliHarfler:
                sesliHarfSayisi+=1
        return sesliHarfSayisi
    
    def buyukUnluUyumuHesapla(self):#Dosyadaki kelimelerin büyük ünlü uyumuna uyup uymadığını kontrol eder. İki farklı değer döndürür.
        metin=self.metin
        kelimeler= metin.split()    #Metni kelimelere böler.
        kalinUnluler="AIOUaıou"
        inceUnluler="EİÖÜeiöü"
        uyanKelimeSayisi , uymayanKelimeSayisi=0 , 0
        for i in kelimeler:
            kalinUnluSayisi= sum(i.count(kalin) for kalin in kalinUnluler)
            inceUnluSayisi= sum(i.count(ince) for ince in inceUnluler)
            if kalinUnluSayisi != 0 and inceUnluSayisi != 0 :
                uymayanKelimeSayisi+=1
            else:
                uyanKelimeSayisi+=1
        return uyanKelimeSayisi,uymayanKelimeSayisi
    
    def goster(self):#Diğer fonksiyonların sonuçlarını ekrana yazdırır.
        print("Dosyadaki kelime sayısı: ",self.kelimeHesapla())
        print("Dosyadaki cümle sayısı: ",self.cumleHesapla())
        print("Dosyadaki sesli harf sayısı: ",self.sesliHarfHesapla())
        uyanKelimeSayisi,uymayanKelimeSayisi=self.buyukUnluUyumuHesapla()
        print("Büyük ünlü uyumuna uyan kelime sayısı: ",uyanKelimeSayisi,"\n"+
                "Büyük ünlü uyumuna uymayan kelime sayisi: ",uymayanKelimeSayisi)

from sifrelemeYontemleri import sifrelemeYontemleri
from dilKontrol import dilKontrol

class myHelp():
    def __init__(self):
        self.methodGoster()
    def methodGoster(self):
        print("sifrelemeYontemleri(): Parametre olarak şifre ve dosyanın adını alır. Örnek: sifrelemeYontemleri('sifre','dosya.txt'). Bu sınıf sifreleme methodlarının çağırılacağı sınıftır.\n",
              "dosyaOku(): Self dışında parametre almaz. Örnek: dosyaOku(). Dosyadaki verileri değişkene atama yapar.\n",
              "dosyayaYaz(): Self dışında parametre olarak dosyanın içerisine yazılacak metin ve dosyanın adını alır. Örnek: dosyayaYaz('metin','dosya1.txt'). Dosyaya veri aktarmak için kullanılır.\n",
              "simetrikSifreleme(): Self dışında parametre almaz. Örnek: simetrikSifreleme(). Metini simetrik olarak şifreleme yapar.\n",
              "simetrikSifreCozme(): Self dışında parametre almaz. Örnek: simetrikSifreCozme(). Simetrik şifreli metini çözer.\n",
              "asimetrikSifreleme(): Self dışında parametre almaz. Örnek: asimetrikSifreleme(). Metini asimetrik olarak şifreleme yapar.\n",
              "hashSHA256(): Self dışında parametre almaz. Örnek: hashSHA256(). Metini hashSHA256 yöntemi ile şifreler.\n",
              "hashSHA1(): Self dışında parametre almaz. Örnek: hashSHA1(). Metini hashSHA1 yöntemi ile şifreler.\n",
              "hashMD5(): Self dışında parametre almaz. Örnek: hashMD5(). Metini hashMD5 yöntemi ile şifreler.\n",
              "hashBlake2b(): Self dışında parametre almaz. Örnek: hashBlake2b(). Metini hashBlake2b yöntemi ile şifreler.\n",
              "hashBlake2s(): Self dışında parametre almaz. Örnek: hashBlake2s(). Metini hashBlake2s yöntemi ile şifreler.\n",
              "dilKontrol(): Parametre olarak dosyanın adını alır. Örnek dilKontrol('dosya.txt'). Bu sınıf Metin üzerinde hesaplamalar yapan methodlarının çağırılacağı sınıftır.\n",
              "kelimeHesapla(): Self dışında parametre almaz. Örnek: kelimeHesapla(). Metindeki kelime sayısını döndürür.\n",
              "cumleHesapla(): Self dışında parametre almaz. Örnek: cumleHesapla(). Metindeki cümle sayısını döndürür.\n",
              "sesliHarfHesapla(): Self dışında parametre almaz. Örnek: sesliHarfHesapla(). Metindeki sesli harf sayısını döndürür.\n",
              "buyukUnluUyumuHesapla(): Self dışında parametre almaz. Örnek buyukUnluUyumuHesapla(). Metindeki kelimelerin büyük ünlü uyumuna uyup uymadığını kontrol eder. İki farklı değer döndürür.\n",
              "")          


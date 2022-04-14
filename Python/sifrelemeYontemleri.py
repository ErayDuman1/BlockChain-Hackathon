import base64
import hashlib as hasher

from Crypto import Random
from Crypto.Cipher import AES #Simetrik şifrelemenin sınıfı tanımlandı.

from Crypto.PublicKey import RSA #Asimetrik şifrelemenin sınıfı tanımlandı.
from Crypto.Cipher import PKCS1_OAEP

class sifrelemeYontemleri():
    def __init__(self, key, dosyaAdi): 
        self.bs = AES.block_size #AES simetrik şifrelemesinin blok boyutu self.bs nesnesine atandı. 
        self.sKey = hasher.sha256(key.encode()).digest() #Simetrik şifrelemenin anahtarı sha256 yöntemi ile oluşturuldu.
        self.asKey = RSA.generate(2048) #Asimetrik şifrelemenin anahtarı rsa yöntemi ile oluşturuldu.
        
        self.dosyaAdi = dosyaAdi #Dosya işlemleri için dosyanın adı nesnesi ve dosyayı okuma methodu tanımlandı.
        self.metin = self.dosyaOku()

    def dosyaOku(self):
        try:
            dosya = open(self.dosyaAdi, "r", encoding = 'utf8') #Dosya okuma işlemi gerçekleşir.
            return dosya.read()
        except (OSError, FileNotFoundError, IOError):
            print("Dosya okumasında bir hata meydana geldi. (Dosya bulunamadı.)\n")
            return ""
        
    def dosyayaYaz(self, yazilacakMetin, sifrelemeTipi):
        try:
            dosya = open(sifrelemeTipi, "w", encoding='utf8') #Dosya yazma işlemi gerçekleşir.
            dosya.write(yazilacakMetin)
        except (FileNotFoundError):
            print("Dosyaya yazmada bir hata meydana geldi.(Dosya adı .key uzantılı olmalı.)")
        
    def simetrikSifreleme(self):
        try:
            metin = self.metin #Dosyadan alınan veri metin nesnesine atandı.
            metin = self._pad(metin) #Metin 16 bitlik sisteme çevirildi.
            iv = Random.new().read(AES.block_size) #Rastgele blokları olusturuldu ve iv nesnesine atandı.
            cipher = AES.new(self.sKey, AES.MODE_CBC, iv) #Anahtar ve blokları ile cipher olusturuldu.
            aesSifreli = base64.b64encode(iv + cipher.encrypt(metin.encode())) #Simetrik şifreleme yapıldı ve aesSifreli nesnesine atandı.
            self.dosyayaYaz(aesSifreli.decode(), "aesSifreli.key") #aesSifreli.key dosyasına sifreli veri yazıldı.
            return aesSifreli
        except(ValueError):
            print("Lütfen metini tekrar düzenleyin.(Türkçe karakter girmeyiniz.)")
    def simetrikSifreCozme(self):
        sifreliMetin = self.metin #Dosyadan alınan veri sifreliMetin nesnesine atandı.
        sifreliMetin = base64.b64decode(sifreliMetin) #Sifreli veri 64 bitlik sisteme çevirildi.
        iv = sifreliMetin[:AES.block_size] #Sifreli metinin blokları iv nesnesine atandı.
        cipher = AES.new(self.sKey, AES.MODE_CBC, iv) #Anahtar ve blokları ile cipher nesnesi oluşturuldu.
        aesSifresiz = self._unpad(cipher.decrypt(sifreliMetin[AES.block_size:])).decode() #Simetrik şifre çözme yapıldı ve aesSifresiz nesnesine atandı.
        self.dosyayaYaz(aesSifresiz, "aesSifresiz.key") #aesSifresiz.key dosyasına sifresiz veri yazıldı.
        return aesSifresiz
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs) #Dışarıdan gelen veriyi blok sayısı kadar bitlik sisteme çevirildi.
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])] #Dışarıdan gelen veri blok sayısı kadar bitlik sistemden geri çevirildi.

    def aSimetrikSifreleme(self):
        try:
            metin = self.metin
            metin = str.encode(metin) #Metin değişkeni string' e çevirildi.
            private_key = self.asKey.export_key('PEM') #Kapalı şifre oluşturuldu.
            public_key = self.asKey.publickey().exportKey('PEM') #Açık şifre oluşturuldu.
            rsa_public_key = RSA.importKey(public_key) #Açık şifre rsa yöntemi ile eklendi.
            rsa_public_key = PKCS1_OAEP.new(rsa_public_key) #Açık şifre oaep yöntemi ile şifrelendi.
            rsaSifreli = rsa_public_key.encrypt(metin) #Metin verisine şifreleme işlemi yapıldı.
            self.dosyayaYaz(format(rsaSifreli), "rsaSifreli.key")
            return format(rsaSifreli)
        except(ValueError):
            print("Lütfen metini tekrar düzenleyin.(Türkçe karakter girmeyiniz.)")
        
    def hashSHA256(self):
        sifreleyici = hasher.sha256() #sha256 yöntemi ile sifreleyici nesnesi oluşturuldu.
        metin = self.metin
        sifreleyici.update(metin.encode("utf-8")) #Metin byte olarak günceellendi.
        hash = sifreleyici.hexdigest() #Şifrelenmiş veri hash nesnesine atandı.
        self.dosyayaYaz(hash, "SHA256.key")
        return hash
    def hashSHA1(self):
        sifreleyici = hasher.sha1() #sha1 yöntemi ile sifreleyici nesnesi oluşturuldu.
        metin = self.metin
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        self.dosyayaYaz(hash, "SHA1.key")
        return hash
    def hashMD5(self):
        sifreleyici = hasher.md5() #hashMD5 yöntemi ile sifreleyici nesnesi oluşturuldu.
        metin = self.metin
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        self.dosyayaYaz(hash, "MD5.key")
        return hash
    def hashBlake2b(self):
        sifreleyici = hasher.blake2b() #hashBlake2b yöntemi ile sifreleyici nesnesi oluşturuldu.
        metin = self.metin
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        self.dosyayaYaz(hash, "Blake2b.key")
        return hash
    def hashBlake2s(self):
        sifreleyici = hasher.blake2s() #hashBlake2s yöntemi ile sifreleyici nesnesi oluşturuldu.
        metin = self.metin
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        self.dosyayaYaz(hash, "Blake2s.key")
        return hash

    

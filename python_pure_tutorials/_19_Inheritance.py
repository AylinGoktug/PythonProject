class Araba:
    def __init__(self,  marka, model, yil, renk):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.renk=renk

    def calistir(self):
        print(f"Marka : {self.marka}, Model : {self.model}, Yıl : {self.yil}, Renk : {self.renk} çalıştırıldı")

    def durdur(self):
        print(f"Marka : {self.marka}, Model : {self.model}, Yıl : {self.yil}, Renk : {self.renk} durduruldu")

class OtomatikAraba(Araba):
    def __init__(self, marka, model, yil, renk, vites_tipi = "Otomatik"):
        super().__init__(marka, model, yil, renk)
        self.vites_tipi = vites_tipi

    def calistir(self):
        print(f"Marka : {self.marka}, Model : {self.model}, Yıl : {self.yil}, Renk : {self.renk}, Vites Tipi : {self.vites_tipi} modda çalıştırıldı")

    def durdur(self):
        print(f"Marka : {self.marka}, Model : {self.model}, Yıl : {self.yil}, Renk : {self.renk}, Vites Tipi : {self.vites_tipi} modda durduruldu")

araba_ornegi_1 = OtomatikAraba("Opel", "Tigra", 2003, "Sarı")
araba_ornegi_1.calistir()
araba_ornegi_1.durdur()

araba_ornegi_2 = OtomatikAraba("Renault", "Clio", 2014, "Gri", "Yarı Otomatik")
araba_ornegi_2.calistir()
araba_ornegi_2.durdur()
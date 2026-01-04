class ArabaConstructor:
    def __init__(self, marka="Bilinmiyor", model="Bilinmiyor", yil=0, renk="Bilinmiyor"):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk
        print("Araba sınıfına yeni bir araba oluşturuldu")

    def calistir(self):
        print(f"Marka : {self.marka}, Model : {self.model}, Yıl : {self.yil}, Renk : {self.renk}")

    def set_marka(self, marka):
        self.marka = marka

    def get_marka(self):
        return self.marka

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_renk(self, renk):
        self.renk = renk

    def get_renk(self):
        return self.renk

    def set_yil(self, yil):
        if yil >= 2020:
            self.yil = yil
        else:
            print("2020 öncesi yıllar için arabalar sayılmıyor.")

    def get_yil(self):
        return self.yil



araba_ornegi_1 = ArabaConstructor()
araba_ornegi_1.calistir()

araba_ornegi_2 = ArabaConstructor()
araba_ornegi_2.set_marka("BMW")
araba_ornegi_2.set_model("Z5")
araba_ornegi_2.set_yil(2020)
araba_ornegi_2.set_renk("Kırmızı")
araba_ornegi_2.calistir()

araba_ornegi_3 = ArabaConstructor()
araba_ornegi_3.set_marka("Mercedes")
araba_ornegi_3.set_model("i1")
araba_ornegi_3.set_yil(2019)
araba_ornegi_3.set_renk("Siyah")
araba_ornegi_3.calistir()
class ArabaConstructor:
    def __init__(self, marka="Bilinmiyor", model="Bilinmiyor", yil=0, renk="Bilinmiyor"):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk
        print("Araba sınıfına yeni bir araba oluşturuldu")

    def calistir(self):
        print(f"Marka : {self.marka}, Model : {self.model}, Yıl : {self.yil}, Renk : {self.renk}")

araba = ArabaConstructor()
araba.calistir()
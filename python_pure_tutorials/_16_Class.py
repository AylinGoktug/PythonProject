class Araba:

    marka = "Marka yazılmadı"
    model = "Model yazılmadı"
    yil = 0
    renk = "Renk yazılmadı"

    def calistir(self):
        print(f"Marka : {self.marka} Model : {self.model} Yıl : {self.yil} Renk : {self.renk}")

    # calistir(self)

araba_ornegi_1 = Araba()
araba_ornegi_1.calistir()

araba_ornegi_2 = Araba()
araba_ornegi_2.marka = "Audi"
araba_ornegi_2.model = "A3"
araba_ornegi_2.yil = "2026"
araba_ornegi_2.renk = "Beyaz"
araba_ornegi_2.calistir()
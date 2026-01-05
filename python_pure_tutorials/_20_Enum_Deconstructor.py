from datetime import datetime
import logging
import os.path
from enum import Enum
from time import asctime

log_dosya_adi = "araba_log.txt"
log_dosya_yolu = os.path.join(os.getcwd(), log_dosya_adi)

if os.path.exists(log_dosya_yolu):
    yeni_log_dosya_adi = f"araba_log_{len(os.listdir(os.getcwd()))}.txt"
    log_dosya_yolu = os.path.join(os.getcwd(), yeni_log_dosya_adi)
    print(f"Dosya mevcut. Yeni log dosyası oluşturuldu : {yeni_log_dosya_adi}")
else:
    print(f"Log dosyası bulunamadı. Yeni log dosyası oluşturulacak : {log_dosya_adi}")

logging.basicConfig(
    filename=log_dosya_yolu,
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s: %(lineno)s- %(funcName)s %(message)s, '
)


class Renk(Enum):
    KIRMIZI = '\033[91m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    MAVI = '\033[94m'
    BEYAZ = '\033[97m'
    SIFIRLA = '\033[0m'

class YakitTuru(Enum):
    BENZIN = "Benzin",
    DIZEL = "Dizel",
    ELEKTRIK = "Elektrik",
    HIBRIT = "Hibrit"

class Araba:
    def __init__(self, marka:str="Bilinmiyor", model:str="Bilinmiyor", yil:str="1970-01-01", renk:str="Bilinmiyor",
                 fiyat:float=0.0, motor_gucu:float=0.0, yakit_turu:YakitTuru=YakitTuru):
        self.__marka = marka    # private
        self._model = model     # protected
        self.yil:datetime = datetime.strptime(yil, "%Y-%m-%d")          # public
        self.renk = renk        # public
        self.fiyat= fiyat
        self.motor_gucu = motor_gucu
        self.yakit_turu = yakit_turu
        print("Araba sınıfına yeni bir araba oluşturuldu")
        print(f"{Renk.SARI.value} Araba sınıfına {Renk.MAVI.value} yeni bir araba oluşturuldu")
        logging.info(f"Araba sınıfına yeni bir araba oluşturuldu. Marka : {marka}, Model : {model}, Yıl : {yil}, "
                     f"Renk : {renk} Fiyat : {fiyat} Motor Gücü : {motor_gucu} Yakıt Türü : {yakit_turu}")

    def __del__(self):
        logging.info(f"Araba silindi. Marka : {self.__marka} Model : {self._model}")

    def goster_bilgileri(self):
        logging.info(f"Araba bilgileri gösteriliyor. Marka : {self.__marka} Model : {self._model}")
        logging.info(f"Araba bilgileri gösteriliyor. Marka : {self.__marka} Model : {self._model} Yıl : {self.yil.strftime('%Y-%m-%d')} "
                     f"Renk : {self.renk} Fiyat : {self.fiyat} Motor Gücü : {self.motor_gucu} Yakıt Türü : {self.yakit_turu}")


    print("#" * 55)


    def set_marka(self, marka:str) -> None:
        if not isinstance(marka, str):
            raise TypeError("Marka bir string olmalıdır.")
        self.__marka = marka
        logging.info(f"Marka güncellendi {marka}")
        print(f"{Renk.YESIL.value} Marka güncellendi : {marka}")


    def get_marka(self) -> str:
        return self.__marka


    def set_model(self, model: str) -> None:
        if not isinstance(model, str):
            raise TypeError("Model bir string olmalıdır.")
        self._model = model
        logging.info("Model güncellendi : {model}")
        print(f"{Renk.YESIL.value} Model güncellendi : {model}")


    def get_model(self) -> str:
        return self._model


    def set_renk(self, renk : str) -> None:
        if not isinstance(renk, str):
            raise TypeError("Renk bir string olmalıdır.")
        self.renk = renk
        logging.info(f"Renk güncellendi : {renk}")
        print(f"{Renk.YESIL.value} Renk güncellendi : {renk}")


    def get_renk(self) -> str :
        return self.renk


    def set_yil(self, yil : str) -> None:
        if not isinstance(yil, str):
            raise TypeError("Yıl bir string olmalıdır ve 'YYYY-MM-DD' formatında olmalıdır.")
        try:
            self.yil = datetime.strptime(yil, '%Y-%m-%d')
            logging.info(f"Yıl güncellendi : {yil}")
            print(f"{Renk.YESIL.value} Yıl güncellendi : {yil}")
        except ValueError as ve:
            logging.error(f"{Renk.KIRMIZI.value} ValueError : Geçersiz tarih formatı girildi : {ve}")
            print(f"Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında giriniz. {Renk.SIFIRLA.value}")
        finally:
            print(f"{Renk.SARI.value} Tarih işlemi bitti. {Renk.SIFIRLA.value}")


    def get_yil(self) -> str :
        return self.yil.strftime('%Y-%m-%d')

    def set_fiyat(self, fiyat : float) -> None:
        if not isinstance(fiyat, (float, int)) or fiyat < 0:
            raise ValueError("Fiyat sıfırdan küçük olamaz ve sayısal bir değer olmalıdır")
        self.fiyat = float(fiyat)
        logging.info(f"Fiyat güncellendi : {fiyat}")
        print(f"{Renk.YESIL.value} Fiyat güncellendi : {fiyat}")

    def get_fiyat(self) -> float:
        return self.fiyat

    def set_motor_gucu(self, motor_gucu : float) -> float:
        if not isinstance(motor_gucu, (float, int)) or motor_gucu < 0:
            raise TypeError("Motor gücü sıfırdan küçük olamaz ve sayısal bir değer olmalıdır")
        self.motor_gucu = float(motor_gucu)
        logging.info(f"Motor gücü güncellendi : {motor_gucu}")
        print(f"{Renk.YESIL.value} Motor gücü güncellendi : {motor_gucu}")

    def get_motor_gucu(self) -> float :
        return self.motor_gucu

    def set_yakit_turu(self, yakit_turu : YakitTuru) -> None:
        if not isinstance(yakit_turu, YakitTuru):
            raise TypeError("Yakıt türü bir YakitTuru Enum değeri olmalıdır.")
        self.yakit_turu=YakitTuru
        logging.info(f"Yakıt Türü güncellendi : {YakitTuru}")
        print(f"{Renk.YESIL.value} Yakıt türü güncellendi : {yakit_turu}")

    def get_yakit_turu(self) -> YakitTuru:
        return self.yakit_turu


    print("#" * 55)

araba_ornegi_1 = Araba()
araba_ornegi_1.goster_bilgileri()

araba_ornegi_2 = Araba()
araba_ornegi_2.set_marka("Opel")
araba_ornegi_2.set_model("Tigra")
araba_ornegi_2.set_yil("1991-01-01")
araba_ornegi_2.set_renk("Sarı")
araba_ornegi_2.set_fiyat(3750.0)
araba_ornegi_2.set_motor_gucu(90.0)
araba_ornegi_2.set_yakit_turu(YakitTuru.BENZIN)
araba_ornegi_2.goster_bilgileri()
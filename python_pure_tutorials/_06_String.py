#======================================================
#       STRING
#======================================================
from itertools import count

metin1 = 'metin1'
print(( metin1))

metin2="metin5"
print(metin2)
print(metin2[0])
print(metin2[-1])

metin_data = """ Bu
birden fazla
satırdan
oluşan
bir metindir
"""
print(metin_data)

# Immutability ( Değişmezlik)
# String'ler O
# Python'da değiştirilemezdir :

metin4 = "metin4"
metin4 = "4"
print(metin4)   # 4 verir ama
#   metin4[4] = "5"
# print(metin4)     # Hata verir

metin3 = "Malatya Elazığ Bingöl Malatya"
print(metin3)
print(type(metin3))

metin5 = "İstanbul"
print("Harf sayısı : ",len(metin5))


# Çoğaltma :

print("Kelime Sayısı : ", metin5 * 4, sep= " * ")


metin6 = "вщьнф"
print(metin6)

metin71="Python"
metin72="Dersi"
yazi=metin71 + " " + metin72
print(yazi)

# join

liste = ["Python", "Dersi"]
print(" ".join(liste))


# Slicing

metin8 = "Python"
print(metin8[1:4])
print(metin8[0:3])
print(metin8[:3])
print(metin8[3:])
print(metin8[3:6])


# String format

name = "Aylin"
id  = 11
print(f"Merhaba Benim Adım {name} ve id'im {id}")


# alt string bulma

metin9 = "Python Programlama Dili"
print(metin9.find("programlama"))
print(metin9.find("Programlama"))


# yer değiştirme

print(metin9.replace("Python", "Java"))


# upper

print(metin9.upper())
print(metin9.isupper())
print(metin9.upper().isupper())


# lower

print(metin9.lower())
print((metin9.islower()))
print((metin9.lower().islower()))


# casefold

metin10 = "ß"
print(metin10.casefold())


# endswith ile startswith

metin11= "Merhaba Python"
print(metin11.endswith("Python"))
print(metin11.startswith("Python"))

print(metin11.startswith("Merhaba"))
print(metin11.endswith("Merhaba"))


# index ile substring bulma : bulunan ilk indisi gösterir

metin12 = ("Python öğren, Python uygula")
print(metin12.index("öğren"))
print(metin12.index("Python"))
print(metin12.index("Python",8,20))


# capitalize : Sadece ilk kelimenin ilk harfi büyük

metin13 = "merhaba python dili"
print(metin13.capitalize())


# title : Tüm kelimelerin ilk harfleri büyük

print(metin12.title())
print(metin13.title())


# strip : ifade başındaki ve sonundaki boşlukları kaldırır

metin14 = "    Python Programlama Dili    "
print(metin14.strip())
print(len(metin14))
print(len(metin14.strip()))


# split

metin151 = "Python Programlama Diline Hoşgeldiniz"
metin152 = metin151.split()
print(metin152[0])
print(metin152[1])
print(metin152[2])
print(metin152[3])


# for

metin16 = "Python"
for temp in metin16:
    print(temp)


# ord() ve chr()

print(ord('A'))
print(chr(65))


# id

metin17 = "Merhaba"
metin18 = metin17 + " Dünya"
#print(id(metin17))
#print(id(metin18))


# regex

import re

metin19 = "Python 101 Dersi"
pattern = r"\d+"
sonuc = re.findall(pattern, metin19)
print(sonuc)


# İleri Düzey Formatlama

print(r"C:\Kullanıcı\Dosya")
print(r"C:\Kullanıcı\Dosya\nAltSatır")
print("C:\Kullanıcı\Dosya\nAltSatır")


# center(width, char)

metin16="Python"
print(metin16.center(20,"*"))


# search

metin12 = "Python öğren, Python uygula"
metin16 = "Python"
print(metin16 + " kelimesi " + str(metin12.count(metin16)) + " defa geçer.")


# encode (encoding, errors)

metin16 = "Python"
print(metin16.encode("utf-8"))


# expandtabs (tabsize)

metin20 = "Python\tProgramlama"
print(metin20.expandtabs(50))


# isalnum (sadece alpha-numeric mi kontrol eder)

metin21="Python44"
print(metin21.isalnum())


# isalpha (Sadece harf içerip içermediğini belirler)

metin16 = "Python"
print(metin16.isalpha())


# isdigit (Sadece rakam içerip içermediğini kontrol eder)

metin22 = "123456"
print(metin22.isdigit())


# dir()

print(dir("Java"))


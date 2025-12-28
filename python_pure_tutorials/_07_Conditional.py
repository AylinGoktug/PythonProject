number = -5

if (number > 0):
    print("Pozitif Sayı")
else:
    print("Negatif Sayı")


number = 5

if (number > 0):
    print("Pozitif Sayı")
else:
    print("Negatif Sayı")


terna = "Pozitif Sayı" if number > 0 else "Negatif Sayı"
print(terna)

# if(number > 0) ? "Pozitif" : "Negatif"    # Python'da çalışmıyor


if (number == 1):
    print("Bir")
elif(number == 2):
    print("İki")
elif (number == 3):
    print("Üç")
else:
    print("1<= x <= 5")


# Pozitif - Çift - Tek

if (number > 0):
    if(number % 2 == 0):
        print("Çift Sayı")
    else:
        print("Tek Sayı")
else:
    print("Negatif Sayı")


# pass kullanımı :

number_pass = int(input("Lütfen bir sayı giriniz : "))
if number_pass > 0:
    if number_pass % 2 == 0:
        print("Çift Sayı")
    else:
        print("Tek Sayı")
else:
    print("Negatif Sayı")

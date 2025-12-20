# Python dinamik türlü yüksek seviyeli interpreter bir dildir
from token import NUMBER

# Değişken türleri genel kurallar vardır

# Değişken isimlendirmelerde _ underscore kullanılır

# snake_case
#===========================================================
#                NUMBER
#===========================================================

number1=10
number2=-10
PI_NUMBER=3.14159
print(f"number1 : {number1}, number2 : {number2}, PI_NUMBER : {PI_NUMBER}")


#===========================================================
 #               STRING
#===========================================================


string1="Merhabalar Güzel İnsanlar-1"
string2="Merhabalar Güzel İnsanlar-2"
print(f"string1 : {string1}, string2 : {string2}")


#===========================================================
 #               BOOLEAN
#===========================================================

is_login = True
print(f"Giriş yapıldı mı ? : {is_login}")
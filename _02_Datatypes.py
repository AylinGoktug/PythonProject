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
print(type(number1))


#===========================================================
 #               STRING
#===========================================================


string1="Merhabalar Güzel İnsanlar-1"
string2="Merhabalar Güzel İnsanlar-2"
print(f"string1 : {string1}, string2 : {string2}")
print(type(string1))


#===========================================================
 #               BOOLEAN
#===========================================================

is_login = True
print(f"Giriş yapıldı mı ? : {is_login}")
print(type(is_login))


#===========================================================
 #               VARIABLE
#===========================================================


number3,number4,number5=3,4,5
#number3=3
#number4=4
#number5=5


#===========================================================
 #               CONST
#===========================================================

DATA_CONNECTION = 255


#===========================================================
 #               LIST
#===========================================================


my_list1=[1,2,3,4,"İstanbul"]
my_list2=[5,6,7,8,"Ankara", True, 14.53]

print(f"list1) : {my_list1}")
print(f"list2) : {my_list2}")
print(type(my_list1))



#===========================================================
 #               TUPLE
#===========================================================

my_tuple = (1,2,3,4,"İstanbul")
print(f"my_tuple : {my_tuple}")
print(type(my_tuple))



#===========================================================
 #               SET
#===========================================================

my_set = {1,1,1,2,2,3,4,"İstanbul"}
print(f"my_set : {my_set}")
print(type(my_set))



#===========================================================
 #               DICTIONARY
#===========================================================

person={
    "name" : "Aylin",
    "surname" : "Göktuğ",
    "is_login" : True,
    "Age" : 47
}
print(person)
print(type(person))

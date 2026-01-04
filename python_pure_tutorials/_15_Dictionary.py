empty_dictionary = {}
my_dictionary = {
    "isim" : "Aylin",
    "soyisim" : "Göktuğ",
    "yaş" : 47,
    "adres" : {
        "il" : "Ankara",
        "ilçe" : "Eryaman"
    }
}

print(my_dictionary)
print(my_dictionary["isim"])
print(my_dictionary["adres"]["il"])

my_dict_cast = dict(isim = "Aylin", soyisim = "Göktuğ")
print(my_dict_cast)
print(my_dict_cast["isim"])

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key,value in my_dictionary.items():
    print(f"{key} : {value}")

print(my_dictionary.get("isim"))
print(my_dictionary.get("isim44"))

my_dictionary.update({"Meslek" : "Mühendis"})
print(my_dictionary)

my_dictionary.pop("yaş")
print(my_dictionary)

new_dictionry = my_dictionary.copy()
print(f"Copy", new_dictionry)

my_dictionary.clear()
print(my_dictionary)

data = {"isim" : "Aylin", "Yas" : 47}
print(data)
print(type(data))

import json

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

from collections import Counter

my_list = ["elma", "armut", "elma", "çilek"]
count = Counter(my_list)
print(count)

my_list2 = ["elma", "armut", "elma", "çilek", "çilek", "çilek", "çilek"]
count = Counter(my_list2)
print(count)
empty_tuple = ()
single_element_tuple = (5,)
a_tuple = (1,)
multi_tuple = (1, 2, 3, 4)
my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple[1:4])
print(my_tuple[:3])
print(my_tuple[::2])

print(my_tuple.count(2))

coordinates = (10.0, 20.0)
print(f"Koordinatlar : {coordinates}")

def person_info():
    return "Ali", 30, "Mühendis"

name, age, job = person_info()

print(f"Adı : {name}, Yaşı : {age}, İşi : {job}")

tuple1 = ("Java", "Python", "C++")

for lang in tuple1:
    print(lang)

my_list = [1, 2, 3, 4]
tuple2 = tuple(my_list)
print(tuple2)

my_new_list = list(tuple2)
print(my_new_list)

tuple2 = (1, 2, 3, 4)
print(4 in tuple2)
print(5 not in tuple2)
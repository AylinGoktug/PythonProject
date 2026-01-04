empty_set = set ()
my_set_1 = {1, 2, 2, 3}
print(my_set_1)

my_set_2 = set({1, 2, 2, 3})
print(my_set_2)

my_set_2.add(4)
print(my_set_2)

my_set_2.remove(1)
print(my_set_2)

my_set_2.add(5)
print(my_set_2)

removed = my_set_2.pop()
print(removed)
print(my_set_2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set2.union(set1))

print(set1.intersection(set2))
print(set2.intersection(set1))

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

for item in my_set_2:
    print(item)

print(set1 | set2)
print(set2 | set1)
print(set1 - set2)
print(set2 - set1)
print(set1 & set2)
print(set2 & set1)
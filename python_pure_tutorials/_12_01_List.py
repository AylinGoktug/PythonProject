list_data_1 = [1, 2, 3, 4, 5, 6, 7, 0]
list_data_2 = [1, 2, 3, 4, 5, 6, 7, 8, "İstanbul", True, 44.23]

print(f"İlk eleman: {list_data_1[0]}")
print(f"İlk eleman: {list_data_2[0]}")

print(f"Eleman Sayısı: {list_data_1.count(0)}")
print(f"Eleman Sayısı: {list_data_2.count(0)}")

print(f"Son elemanı: {list_data_1[len(list_data_1)-1]}")
print(f"Son elemanı: {list_data_2[len(list_data_2)-1]}")

print(list_data_1[1:4])
print(list_data_1[:4])
print(list_data_1[3:])
print(list_data_1[::3])

print(list_data_2[1:4])
print(list_data_2[:4])
print(list_data_2[3:])
print(list_data_2[::3])

list_data_1.append(44)
list_data_2.append(44)

print(list_data_1)
print(list_data_2)

list_data_1.remove(1)
list_data_2.remove(1)

print(list_data_1)
print(list_data_2)

list_data_1.sort()
#list_data_2.sort()

print(list_data_1)
#print(list_data_2)

list_data_1.reverse()
list_data_2.reverse()

print(list_data_1)
print(list_data_2)

for item in list_data_1:
    print(item)

for item in list_data_2:
    print(item)

squares = [x^2 for x in range(10)]
print(squares, end=" ")
print()

print(44 in list_data_1)
print(44.23 in list_data_2)

print(9 in list_data_1)
print(22 in list_data_2)

print(8 not in list_data_1)
print((55 not in list_data_2))

print(7 not in list_data_1)
print(8 not in list_data_2)

nested_list = [[1,2,3],[4,5,6]]
print(f"Nested List : {nested_list[0][1]}")
print(f"Nested List: {nested_list[1][1]}")
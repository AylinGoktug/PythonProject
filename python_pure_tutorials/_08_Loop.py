# for loop  :   iterable'dır

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for temp in number:
    print(temp)

for temp in range(0, 10):
    print(temp)

for i in range(0, 10, 2):
    print(i)



# While loop

i = 0
while i <= 5:
    print(i)
    i+=1

# while : break, continue, pass

"""
1 ile 10 arasındaki sayıların toplamını al
Eğer sayılarda 5 varsa toplamadan diğer döngüye geç
Eğer sayı 10 dan büyükse döngüyü bitir
Eğer sayı 6 ya eşitse o anlık hiçbir şey yapma
"""

total = 0
for i in range(1, 1100, 1):
    if i == 5:
        continue
    elif i > 10:
        break
    elif i == 6:
        pass
        print("Bu satırda hiçbir şey yapılmadığını bildirir")
    total += 1
print("Toplam : ", total)


for j in range(1, 11):
    for i in range(1, 11):
        print(f"{i} * {j} = {i * j : < 10}", end="\t")
    print()
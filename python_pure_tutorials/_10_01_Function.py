def hesap_topla1():
    sayi1 = 10
    sayi2 = 20
    sayi3 = sayi1 + sayi2
    print(f"Toplam 1 : {sayi3}")

hesap_topla1()

def hesap_topla2(sayi1, sayi2):
    sayi3 = sayi1 + sayi2
    print(f"Toplam 2 : {sayi3}")

hesap_topla2(10,20)

def hesap_topla3(sayi1, sayi2 = 90):
    sayi3 = sayi1 + sayi2
    print(f"Toplam 3 : {sayi3}")

hesap_topla3(10)

def hesap_topla4():
    sayi1 = 10
    sayi2 = 20
    sayi3 = sayi1 + sayi2
    return sayi3

print(f"Toplam 4 : {hesap_topla4()}")

def hesap_topla5(sayi1 = 40, sayi2 = 60):
    sayi3 = sayi1 + sayi2
    return sayi3

result5=hesap_topla5()
print(f"Topla 5 : {result5}")

global_variable = 99
def hesap_topla6():
    global global_variable
    print(global_variable)
    local_variable = 11
    print(local_variable)

hesap_topla6()
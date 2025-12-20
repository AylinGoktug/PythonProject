# Single Comment


"""
Multiple Comment
"""

#===================================================================
#                              PRINT
#===================================================================

print("Python Öğreniyorum")

print("Python","Java","Nodejs")

print("Python" "Java" "Nodejs")

print(1453)
print(14.53)
print(14,53)

#===================================================================
#                              SEPERATED
#===================================================================

print("Merhabalar","Güzel","İnsanlar", sep="*")
print("Merhabalar","Güzel","İnsanlar", sep=" * ")

#===================================================================
#                                 END
#===================================================================

print("Merhabalar","Python","Öğreniyorum", "***", "Dünyasına","Hoşgeldiniz")

print("Merhabalar","Python","Öğreniyorum", end=" *** ")
print("Dünyasına","Hoşgeldiniz")

#===================================================================
#                              DOCSTRING
#===================================================================
print(""" 
Merhabalar Python Öğreniyorum *** Dünyasına Hoşgeldiniz
""")

#===================================================================
#                              ESCAPE
#===================================================================

print(""" 
Merhabalar Python Öğreniyorum *** \n\tDünyasına Hoşgeldiniz
""")


# Değişken isimlendirmelerinde :

#String name="Aylin"
#let name="Aylin"

name="Aylin"
surname="Goktug"

isim="Aylin"
soyisim="Göktuğ"

tc_number=12345678901
is_login=False

print("Adım : ",name)
print("Soyadım : ,surname")

print("Adım : ",name, "\nSoyadım : " ,surname)

# 1. YOL :
print("Adım : ",name, "Soyadım : " ,surname)


# 2. YOL :

print("Adım : %s Soyadım : %s " %(name, surname))

#v 3. YOL :

print(f"Adım : {name}, Soyadım : {surname}")
for i in range(11):
    if i % 2 == 0:
        print(i)
print("-------------------------------")


for a in range(11):
    if a % 2 != 0:
        print(a)
print("------------------------------")


liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
for element in liste:
    print(element)

    for element in liste:
        if element > 0:
            print(element)

            nombre_element_positifs = 0
            for element in liste:
                if element > 0:
                    nombre_element_positifs += 1
                    print(nombre_element_positifs)



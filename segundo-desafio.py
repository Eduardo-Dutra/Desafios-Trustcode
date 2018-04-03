from random import randint

lista1 = [randint(0, 5000000) for x in range(500)]
lista2 = [randint(0, 5000000) for x in range(50000)]

for i in lista2:
    for j in lista1:
        if i == j:
            print(i)
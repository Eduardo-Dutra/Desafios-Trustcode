n = int(input("Digite um número: "))

for x in range(1, n + 1):
    cont = 0
    for y in range(1, x + 1):
        if x % y == 0:
            cont += 1
    if cont == 2:
        print(x)
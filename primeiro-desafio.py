n = int(input("Informe um número para pesquisa: "))

# CRIAÇÃO DE UMA LISTA DE INTEIROS ORDENADA APENAS PARA TESTE
teste = list(range(300))

check = False
for i in teste:
    if i == n:
        check = True
        break
if check:
    print("%d está na posição %d" % (n, i))
else:
    print("%d não está na lista" % n)
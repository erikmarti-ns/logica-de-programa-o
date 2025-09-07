soma = 0

for i in range(1, 101):
    if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
        soma += i

    print("Soma dos numeros é:", soma)
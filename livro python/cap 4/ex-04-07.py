valor = int(input("Informe o valor do produto: "))
numparc = int(input("Informe o número de parcelas: "))
valparc = 0

for c in range(1, numparc):
    valparc = valor/c
    print(f"{c}x de R$ {int(valparc)}")
# Escreva um programa que leia 3 números: a, b e n. O programa deve imprimir o resultado da seguinte expressão: i(a-bi+i)

a = 5
b = 4
n = 2
somatorio = 0
for i in range(1, n+1):
    somatorio += i * ( a - ( b * i) + i)
    print(somatorio)
#Escreva um programa que leia um número n e calcule o somatório
# do quadrado dos números naturais de 1 até n
n = 5
somatorio = 0
for i in range(1, n+1):
    somatorio += i ** 2
print(somatorio)
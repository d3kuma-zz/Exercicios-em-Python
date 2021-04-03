
##Capítulo 3.11 - Notação científica ou exponencial

print(5.1 * 10**(-2)) #0.051
print(3.4 * 10**(-4))
#Para calcular a notação científica, fazemos o seguinte cálculo:
# Cálculo de a
# 1 - Pegamos os números diferentes de zero depois da vírgula
# (Ex.: 0.51 = 51)
# 2 - Dividimos o primeiro em inteiro e o restante em decimal
# (5.1)
#Cálculo de b
# 3 - Contamos todos os zeros antes e somamos com + 1
# (1 zero + 1 = 2)
#
# 4 - Pegamos o a e multiplicamos por 10 elevado
# ao b negativo.
#
# Fórmula = a * 10 ** (-b)
#
# (5 * 10**(-2) = 0.051
#
# Outros exemplos:
# 0.00034 = 3.4 * 10**(-4)
# 34 > 3.4
# 3 zeros + 1 = 4
# 3.4 * 10**(-4)

print(1.548*10**3)

#Para números inteiros, basta "quebrar" o número igual acima e contar a parte decimal, que é o expoente do 10.
#1548 = 1.548 quebrando em decimal
#3 casas decimais = 10**3

print(1.2*10**(-20)) #Resultado = 1.2e-20 = 0.000000000000000000012
#Perceba que o Python resume os zeros para e-20. Esta forma é chamada de
# forma cifrada.
#Logo, a conversão para forma cifrada é a seguinte:
#
# 1 - Pega o número diferente de zero.
# 1.2
# 2 - Faça a conta para calcular o b e escreva depois de "e-"
#São 19 zeros + 1 = 20
#1.2e-20
print(10**-100)
#1e-100
#Entendendo de outra forma, elevo 100 vezes para trás, com 100 zeros
#antes do número 10.

# Funciona também para números inteiros
print(1.2*10**(20))
#1.2e+20 = 1.20000000000000000000


# n1 = 0.000000513532181
# print(n1)
# 5.13532181e-7

# 59012210122
# print(5.9012210122 * 10**10)








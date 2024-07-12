#Exercicio 1:

number = input('Digite um número \n')

if float(number) > 0:
    print('O número é positivo.')
elif float(number) == 0:
    print('O número é 0.')
else:
    print('O número é negativo.')

#   -------------------------------------------------  #

#Exercicio 2:

for i in range(10):
    if i % 2 == 0:
        print(i)

#   -------------------------------------------------  #

#Exercicio 3:

def calcular_fatorial(numero):
    resultado = 1
    for i in range (1, numero + 1):
        resultado *= i
    return resultado

numero = int(input('Digite um número'))
resultado = calcular_fatorial(numero)
print (resultado)

#   -------------------------------------------------  #

#Exercicio 4:

number = input('Digite um número')

if float(number) % 2 > 0:
    print('o número é primo')
else:
    print('O número não é primo')

#   -------------------------------------------------  #

#Exercicio 5:
resultado = 0

for i in range(1, 101):
        resultado += i

print(resultado)

#   -------------------------------------------------  #

#Exercicio 6:

num = 0

while num <= 10:
    print (num)
    num += 1

#   -------------------------------------------------  #

#Exercicio 7:
var = 0
lista = []

for i in range(5):
    lista.append(int(input("Digite um número: ")))
    var += lista[i]
print(var)

#   -------------------------------------------------  #

#Exercicio 8:

ano = int(input("Escreva um ano \n"))

if ano % 4 == 0 or ano % 400 == 0:
    print ('Ano é Bissexto  ')
else:
    print ('Ano não é bissexto  ')

#   -------------------------------------------------  #
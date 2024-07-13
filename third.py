#Exercicio 1

import random

for i in range(21):
    if i % 2 == 0:
        print(i)

# ------------------------------- #

#Exercicio 2

var = 0
lista = []

for i in range(0, 51):
    if i % 2 == 0:
        var += i
print(var)

# ------------------------------- #

#Exercicio 3

var = 0

for i in range (0, 100):
    if i % 2 == 0:
        var += i

media = var / 50

print(media)

# ------------------------------- #

#Exercicio 4

number = int(input("Digite um número para ser feito a tabuada "))

for i in range(1, 11):
    print(number, "X", i, "=", number * i)

# ------------------------------- #

#Exercicio 5

a = input("Digite uma letra: \n")

if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print('É uma vogal')
else:
    print('É uma consoante')

# ------------------------------- #

#Exercicio 6

var = 0

for i in range (1, 100):
    if i % 2 > 0:
        var += i

media = var / 50

print(media)

# ------------------------------- #

#Exercicio 7

ano = int(input('Digite um ano'))

if ano % 2 == 0 or ano % 400 == 0:
    print ('Ano é de copa ')
elif ano < 1930:
    print ('Não existia a copa ainda  ')
else:
    print('O ano não é de copa')


# ------------------------------- #

#Exercicio 8

lista = [1, 2, 3, 4, 5, 6]
elemento = random.choice(lista)

print('O dado foi lançado, e o numero é!',elemento)

# ------------------------------- #

#Exercicio 9

peso = float(input("Digite o seu peso \n"))
altura = float(input("Digite a sua estatura \n"))

IMC = peso  / (altura * altura)

print(IMC)

# ------------------------------- #

#Exercicio 10

opcao = int(input('Digite a opção que você quer: \n + 1- Adição \n + 2- Subtração \n + 3- Multiplicação \n + 4- Divisão'))

number = int(input('Digite um número: \n'))
number_one = int(input('Digite um número: \n'))

if opcao == 1:
    print(number + number_one)
elif opcao == 2:
    subtracao = number - number_one
    print(subtracao)
elif opcao == 3:
    multiplicacao = number * number_one
    print(multiplicacao)
elif opcao == 4:
    divisao = number * number_one
    print(divisao)
    
# ------------------------------- #

#Exercicio 11

lista = [1, 2, 3, 4, 5, 6]

sorte = int(input('Tente adivinhar o dado \n'))
elemento = random.choice(lista)

if sorte == elemento:
    print('Acertou!')
else:
    print('Errou!')
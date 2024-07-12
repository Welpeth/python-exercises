import time

#1 exercicio:

first = 1; second = 3; third = 5
resultado = first + second + third

print ('A soma deles fica ', resultado)
media = resultado / 3

print ('Calculando a média...')
time.sleep(2)

print ('E a média dos resultados é ', media)

# ---------------------------------------------------------- #

#exercicio 2

print('[+] Bem vindo ao calculo de área de retângulos!')
time.sleep(3)
name = input('[+] Qual o seu nome? \n')

base = input('Escreva a base do retângulo: \n')
altura = input ('E qual a altura do retângulo? \n')
retangulo = int(base) * int(altura)

print('[+] Calculando Área...')
time.sleep(4)

print('A área é ', retangulo)

# ---------------------------------------------------------- #

#exercicio 3

largura = input('[+] A largura da sua pscina \n'); altura = input('[+] A altura de sua pscina \n'); comprimento = input('[+] O comprimento \n')
cubagem = float(largura) * float(altura) * float(comprimento)

preco = float(cubagem) * 100

print ('[+] O preço da sua pscina é ', float(preco), "R$")

# ---------------------------------------------------------- #

#exercicio 4

number = input('[+] Digite um número \n')

print ('O seu antecessor é ', int(number) - 1, 'E seu sucessor é ', int(number) + 1)

# ---------------------------------------------------------- #

#exercicio 5

number = input('[+] Digite um número \n')
reajuste = float(number) * 0.15

print ('O número é ', number, 'com o reajuste fica ', reajuste + float(number))

# ---------------------------------------------------------- #

#exercicio 6

productName = input('Digite o nome do produto \n')
productPrice = input('Digite o preço do produto \n')
productReajuste = float(productPrice) * 0.85

print ('O produto', productName, 'tem o preço', productPrice, ', e vai ser vendido com o reajuste de 85%, ficando', (float(productReajuste) + float(productPrice)))

# ---------------------------------------------------------- #

#exercicio 7

escolha = input("Digite a opção que você quer utilizar! \n + Fahrenheit(F) \n + Kelvin (K) \n + Réaumur (Re) \n + Rankine (Ra) \n")

C = input('Escreva a temperatura em graus celsius \n')

F = float(C) * 1.8 + 32; K = float(C) + 273.15; Re = float(C) * 0.8; Ra = float(C) * 1.8 + 32 + 459.67

if escolha == 'F' or escolha == 'Fahrenhite':
    print('A temperatura em Fahrenheit é', F)
elif escolha == 'K' or escolha == 'Kelvin':
    print('A temperatura em Kelvin é', K)
elif escolha == 'Re' or escolha == 'Réamur':
    print('A temperatura em Réamur é', Re)
else:
    print('A temperatura em Rankine é', Ra)
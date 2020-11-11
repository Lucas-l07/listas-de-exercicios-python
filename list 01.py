# Introdução a Programação Estruturada

# 01 - Dados dois inteiros a = 30 e b = 40,
# calcule sua soma e aprensente na tela.

a = 30
b = 40
soma = a + b
print(f"A soma de {a} e {b} é {soma}")

print()

# 02 - Dados três inteiros a = 30, b = 40 e c = 20,
# faça um programa que calcule sua multiplicação e
# apresente na tela.

a = 30
b = 40
c = 20
multiplication = a * b * c
print(f"A multiplicação de {a}, {b} e {c} é {multiplication}")

print()

# 03 - Dados dois inteiros a = 40 e b = 40, calcule
# sua divisão e apresente na tela.

a = 40
b = 40
divisionNumbers = a / b
print(f"A divisão de {a} e {b} é {divisionNumbers}")

print()

# 04 - Dados dois inteiros a = 50 e b = 25, calcule
# sua subtração e apresente na tela.

a = 50
b = 25
subtraction = a - b
print(f"A subtração de {a} e {b} é {subtraction}")

print()

# 05 - Crie um programa que espera uma entrada do nome
# do usuário, e após digitar pergunte como ele está.

name = str(input("Digite seu nome: ")).strip()
firstName = name.split()
print(f"Olá, {firstName[0]}! Como você está?")

print()

# 06 - Codifique o programa abaixo e analise os resultados:

# a_str e b_str guardam strings
a_str = input("Digite o primeiro numero: ")
b_str = input("Digite o segundo numero : ")

# a_int e b_int guardam inteiros
a_int = int(a_str) # converte string / texto para inteiro
b_int = int(b_str) # converte string / texto para inteiro

# calcule a soma entre valores que são números inteiros
soma = a_int + b_int

# imprima a soma
print("A soma de", a_int, "+", b_int, "é igual a ", soma)

print()

# 07 - A função int() converte um dado String para um número
# inteiro. Construa um programa que converte o String "123456".

text = "123456"
number = int(text)

print()

# 08 - Construa um programa que divida dois números inteiros
# a = 3 e b = 2, e devolva apenas a parte inteira do resutlado
# (o número sem as casas depois da vírgula)

a = 3
b = 2
result = a / b
print(f"Resultado inteiro de {a}/{b} é {int(result)}")

print()

# 09 - Construa um programa que arredonde o número 5,9874
# com duas casas decimais usando o comando round.

a = 5.9874
result = round(a)
print(result)

print()

# 10 - Codifique o programa a respeito de formatação de strings
# abaixo, e analise os resultados:

print("Teste de formatação de string")
myInteger = 12345
myFloat = 3.14159
myString = "Curso de Python"

print()

print("Integer:", myInteger)
print("Decimal %d e um integer %d" % (myInteger, myInteger))
print("Integer Hexadecimal %x" % myInteger)

print()

print("Float", myFloat)
print("Defeaut %f" % myFloat)
print("Exponencial %e" % myFloat)
print("Justificar Direita (%10d)" % myFloat)
print("Justificar Esquerda (%-10d)" % myFloat)

print()

print("Para 9 digitos %.9d" % myInteger)
print("3 digitos depois do decimal (float) %.3f" % myFloat)
print("Dez e cinco caracteres permitidos na string:")
print("(%.10s) (%.5s)" % (myString, myString))

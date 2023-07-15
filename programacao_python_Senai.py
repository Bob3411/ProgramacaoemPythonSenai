# Exercício 01 – Crie uma variável chamada "idade" e atribua um valor inteiro a ela.
# Verifique se a idade é maior ou igual a 18 e imprima "Maior de idade" ou "Menor de
# idade" de acordo com a condição.

# idade = 18

# if idade >= 18:
# 	print("Maior de idade")
# else:
# 	print("Menor de idade")	


# Exercício 02 - Crie uma variável chamada "número" e atribua um valor inteiro a ela.
# Verifique se o número é positivo, negativo ou zero e imprima a mensagem
# correspondente.

# numero = -5
# if numero > 0:
# 	print("Positivo")
# elif numero < 0:
# 	print("Negativo")
# else:
# 	print("Zero")
	
# Exercício 03 - Crie duas variáveis, "nota1" e "nota2", e atribua valores numéricos a elas.
# Verifique se a média das notas é maior ou igual a 7 e imprima "Aprovado" ou
# "Reprovado" de acordo com a condição.


# nota1 = 7
# nota2 = 9
# media = (nota1 + nota2) / 2
# if media >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")

# Exercício 04 - Crie uma variável chamada "idade" e atribua um valor inteiro a ela.
# Verifique se a idade está dentro do intervalo de 18 a 30 (inclusive) e imprima a
# mensagem "Idade válida" ou "Idade inválida" de acordo com a condição.

# idade = int(input("Digite a idade:"))
# if idade >= 18 and idade <= 30:
#     print("Idade válida")
# else:
#     print("Idade inválida")

# Exercício 05 - Crie uma variável chamada "numero" e atribua um valor inteiro a ela.
# Verifique se o número é par ou ímpar e imprima a mensagem correspondente.

# numero = int(input("Digite um número:"))
# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Ímpar")


# Exercício 06 - Crie uma variável chamada "horario" e atribua um valor inteiro
# representando a hora do dia (em formato 24 horas). Verifique se o horário está dentro
# do período da manhã (das 6h às 12h), da tarde (das 12h às 18h) ou da noite (das 18h
# às 23h) e imprima a mensagem correspondente.

# horario = int(input("Digite o horário:"))
# if horario >= 0 and horario < 6:
#     print("Madrugada")
# elif horario >= 6 and horario <= 12:
#     print("Manhã")
# elif horario > 12 and horario < 18:
#     print("Tarde")
# elif horario >= 18 and horario <= 23:
#     print("Noite")
# elif horario == 24:
#     print("Madrugada")
# else:
#     print("Horário inválido")

# Exercício 07 - Crie uma variável chamada "peso" e atribua um valor numérico a ela.
# Verifique se o peso está dentro do intervalo de 50 a 100 (inclusive) e imprima a
# mensagem "Peso válido" ou "Peso inválido" de acordo com a condição.

# peso = int(input("Digite o peso:"))
# if peso >= 50 and peso <= 100:
#     print("Peso válido")
# else:
#     print("Peso inválido")

# Exercício 08 - Crie uma variável chamada "numero" e atribua um valor inteiro a ela.
# Verifique se o número é múltiplo de 3 e de 5 ao mesmo tempo e imprima a mensagem
# correspondente.

# numero = int(input("Digite um número:"))
# if numero % 3 == 0 and numero % 5 == 0:
#     print("Múltiplo de 3 e de 5")
# else:
#     print("Não é múltiplo de 3 e de 5")

# Exercício 09 - Crie uma variável chamada "ano" e atribua um valor inteiro
# representando um ano. Verifique se o ano é bissexto (divisível por 4, mas não por 100,
# exceto se for divisível por 400) e imprima a mensagem correspondente.
  
# ano = int(input("Digite um ano:"))
# if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#     print("Ano bissexto")
# else:
#     print("Ano não é bissexto")

# Exercício 10 - Crie uma variável chamada "salario" e atribua um valor numérico a ela.
# Verifique se o salário é maior do que 1000 e menor do que 2000 ao mesmo tempo e
# imprima a mensagem correspondente.

# salario = int(input("Digite o salário:"))
# if salario > 1000 and salario < 2000:				
# 			print("Salário válido")

# Exercício 11 - Faça um Programa que peça dois números e imprima o maior deles.
# numero1 = int(input("Digite o 1 º número:"))
# numero2 = int(input("Digite o 2 o número:"))
# if numero1 > numero2:
#     print("O maior número é:", numero1)
# else:
#     print("O maior número é:", numero2)

# Exercício 12 - Faça um Programa que peça um valor e mostre na tela se o valor é
# positivo ou negativo.
# numero = int(input("Digite um número:"))
# if numero > 0:
#     print(f"O número {numero} é positivo")
# else:
#     print(f"O número {numero} é negativo")

# Exercício 13 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# letra = str(input("Digite F ou M:"))
# if letra == "F" or letra == "f":
#     print("Feminino")
# elif letra == "M" or letra == "m":
#     print("Masculino")
# else:
#     print("Sexo inválido")

# Exercício 14 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# letra = str(input("Digite uma letra:"))
# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print("Vogal")
# else:
#     print("Consoante")	

# Exercício 15 - Faça um programa para a leitura de duas notas parciais de um aluno. O
# programa deve calcular a média alcançada por aluno e apresentar:
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# • A mensagem "Reprovado", se a média for menor do que sete;
# • A mensagem "Aprovado com Distinção", se a média for igual a dez.

# nota1 = float(input("Digite a 1a nota:"))
# nota2 = float(input("Digite a 2a nota:"))
# media = (nota1 + nota2) / 2
# if media >= 7:
#     print("Aprovado")
# elif media < 7 and media >= 5:
#     print("Recuperação")
# else:
#     print("Reprovado")	
# if media == 10:
#     print("Aprovado com Distinção")

# Exercício 16 - Faça um Programa que leia três números e mostre o maior deles.
# num1 = int(input("Digite o 1o número:"))
# num2 = int(input("Digite o 2o número:"))
# num3 = int(input("Digite o 3o número:"))
# if num1 > num2 and num1 > num3:
#     print(f"O maior número é: {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"O maior número é: {num2}")
# else:
#     print(f"O maior número é: {num3}")

# Exercício 17 - Faça um Programa que leia três números e mostre o maior e o menor deles.
# num1 = int(input("Digite o 1o número:"))
# num2 = int(input("Digite o 2o número:"))
# num3 = int(input("Digite o 3o número:"))
# if num1 > num2 and num1 > num3:
#     print(f"O maior número é: {num1}")	

# elif num2 > num1 and num2 > num3:
#     print(f"O maior número é: {num2}")
# else:
#     print(f"O maior número é: {num3}")
	
# if num1 < num2 and num1 < num3:
#     print(f"O menor número é: {num1}")
	
# elif num2 < num1 and num2 < num3:
#     print(f"O menor número é: {num2}")
	
# else:
#     print(f"O menor número é: {num3}")

# Exercício 18 - Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# preco1 = float(input("Digite o 1o preço:"))
# preco2 = float(input("Digite o 2o preço:"))
# preco3 = float(input("Digite o 3o preço:"))
# if preco1 < preco2 and preco1 < preco3:
#     print(f"O produto mais barato é: {preco1}")
# elif preco2 < preco1 and preco2 < preco3:
#     print(f"O produto mais barato é: {preco2}")
# else:
#     print(f"O produto mais barato é: {preco3}")		

# Exercício 19 - Faça um Programa que leia três números e mostre-os em ordem
# decrescente.

num1 = int(input("Digite o 1o número:"))
num2 = int(input("Digite o 2o número:"))
num3 = int(input("Digite o 3o número:"))

Num_Maior = max(num1, num2, num3)
Num_Menor = min(num1, num2, num3)
Num_Inter = num1 + num2 + num3 - Num_Maior - Num_Menor
if num1 > num2 and num1 > num3:
  
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")
else:
    print(f"O maior número é: {num3}")
if num1 < num2 and num1 < num3:
    print(f"O menor número é: {num1}")
elif num2 < num1 and num2 < num3:
    print(f"O menor número é: {num2}")
else:
    print(f"O menor número é: {num3}")
		




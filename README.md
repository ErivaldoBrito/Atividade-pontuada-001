# Atividade Pontuada de Lógica de Programação

# 01 - Corrigindo código

## Descrição

Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu. O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

1. A quantidade de números pares e ímpares.
2. A quantidade de números positivos e negativos.
3. A quantidade de números inseridos.
4. O maior e o menor número.
5. A média de números pares.
6. A média de números ímpares.
7. A média de todos os números inseridos.
8. Mostrar os números lidos na ordem inversa.

## Código

```python
# Variáveis para armazenar os números
numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))
numero3 = int(input("Digite o 3º número: "))
numero4 = int(input("Digite o 4º número: "))
numero5 = int(input("Digite o 5º número: "))

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0

# Processando cada número
if numero1 % 2 == 0:
    quantidade_pares += 1
    soma_pares += numero1
else:
    quantidade_impares += 1
    soma_impares += numero1

if numero1 < 0:
    quantidade_negativos += 1
elif numero1 > 0:
    quantidade_positivos += 1

maior_numero = max(maior_numero, numero1)
menor_numero = min(menor_numero, numero1)

soma_geral += numero1

# Processando o segundo número
if numero2 % 2 == 0:
    quantidade_pares += 1
    soma_pares += numero2
else:
    quantidade_impares += 1
    soma_impares += numero2

if numero2 > 0:
    quantidade_positivos += 1
elif numero2 < 0:
    quantidade_negativos += 1

maior_numero = max(maior_numero, numero2)
menor_numero = min(menor_numero, numero2)

soma_geral += numero2

# Processando o terceiro número
if numero3 % 2 == 0:
    quantidade_pares += 1
    soma_pares += numero3
else:
    quantidade_impares += 1
    soma_impares += numero3

if numero3 > 0:
    quantidade_positivos += 1
elif numero3 < 0:
    quantidade_negativos += 1

maior_numero = max(maior_numero, numero3)
menor_numero = min(menor_numero, numero3)

soma_geral += numero3

# Processando o quarto número
if numero4 % 2 == 0:
    quantidade_pares += 1
    soma_pares += numero4
else:
    quantidade_impares += 1
    soma_impares += numero4

if numero4 > 0:
    quantidade_positivos += 1
elif numero4 < 0:
    quantidade_negativos += 1

maior_numero = max(maior_numero, numero4)
menor_numero = min(menor_numero, numero4)

soma_geral += numero4

# Processando o quinto número
if numero5 % 2 == 0:
    quantidade_pares += 1
    soma_pares += numero5
else:
    quantidade_impares += 1
    soma_impares += numero5

if numero5 > 0:
    quantidade_positivos += 1
elif numero5 < 0:
    quantidade_negativos += 1

maior_numero = max(maior_numero, numero5)
menor_numero = min(menor_numero, numero5)

soma_geral += numero5

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

# Mostrando números na ordem inversa
numeros_invertidos = [numero5, numero4, numero3, numero2, numero1]

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros_invertidos}")

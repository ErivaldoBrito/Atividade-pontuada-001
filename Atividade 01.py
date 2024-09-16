import os
os.system("cls | clear")

# Variaveis para armazenar os numeros

numero3 = int(input("Digite o 3º número: ")) 

# Variaveis para armazenar as estatísticas

quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
maior_numero = 0
menor_numero = 0


# Processando o terceiro número
if numero3 % 2 == 0:
    quantidade_pares += 1
   
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

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 3

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")


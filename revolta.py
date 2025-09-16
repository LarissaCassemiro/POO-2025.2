# Há uma disputa para saber qual grupo é mais forte: rebeldes ou soldados
# A lógica deve consistir em descobrir qual é mais forte
        # Os numeros impares representa os soldados 
        # Os numeros pares representa os rebeldes 

# Com uma lista de numeros inteiros, 
    # deve ser somado os numeros que são impares e os numeros que são pares
        # e assim observar quem é mais forte 

# a ENTRADA  deve conter: 
        # - Um numero inteiro que determine o tamanho da sequencia (1 ≤ n ≤ 50).
        # - Numeros inteiros 'i' (1 ≤ i ≤ 50).

# a SAÍDA deve conter: 
        #"soldados" se a soma dos números ímpares for maior que a soma dos números pares.
        #"rebeldes" se a soma dos números pares for maior que a soma dos números ímpares.
        #"empate" se ambas as somas forem iguais. 



N = int(input().strip())

soma_pares = 0
soma_impares = 0

for _ in range(N):
    i = int(input().strip())
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

if soma_impares > soma_pares:
    print("soldados")
elif soma_pares > soma_impares:
    print("rebeldes")
else:
    print("empate")

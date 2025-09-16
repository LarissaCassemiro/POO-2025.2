# O código deve seguir a lógica de que dois individuos estão apostando entre si 
#   quem melhor estima a quantidade de patas de animais presentes na fazenda

#A ENTRADA deve ter: 
        # - um numero inteiro representando o valor estimado pelo Chico
        # - um numero inteiro representando o valor estimado pelo Cebolinha
        # - um numero inteiro representando a quantidade de animais no local

#Deve haver uma lista que represente cada animal da fazenda:
        # 'v' = vaca 4 patas
        # 'g' = galinha 2 patas
        # 'c' = cavalo 4 patas 

# A SAÍDA deve conter:
        # A soma total das patas dos animais 
        # O nome de quem chegou mais perto, ou acertou, ou "empate"

chico = int(input().strip())
cebolinha = int(input().strip())
qtd_animais = int(input().strip())

patas = {
    'v': 4,
    'g': 2,
    'c': 4
}

totalpatas = 0
for i in range(qtd_animais):
    animal = input().strip().lower()
    total_patas += patas[animal]

print(total_patas)

dist_chico = abs(total_patas - chico)
dist_cebolinha = abs(total_patas - cebolinha)

if dist_chico < dist_cebolinha:
    print("chico bento")
elif dist_cebolinha < dist_chico:
    print("cebolinha")
else:
    print("empate")
# Este código consiste na lógica do jokenpo, ou melhor - pedra, papel, tesoura - #
# A entrada deverá conter a opção que o jogador enviar:
    # 'P' = pedra
    # 'PP' = papel
    # 'T' = tesoura 

# Deve haver duas variáveis representando 'jogador 1' e 'jogador 2' 
# A LÓGICA É: 
        # QUANDO O JOGADOR 1 GANHAR DO JOGADOR 2, DEVE IMPRIMIR "VITÓRIA DO JOGADOR 1"
        # QUANDO O JOGADOR 2 GANHAR DO JOGADOR 1, DEVE IMPRIMIR "VITÓRIA DO JOGADOR 2"
        # QUANDO AMBOS ESCOLHEREM A MESMA COISA, DEVE IMPRIMIR "JOGADA EMPATADA"

jogador1 = input()
jogador2 = input()


if jogador1 == jogador2:
    print ("JOGADA EMPATADA")

elif (jogador1 == 'P' and jogador2 == 'T') or \
    (jogador1 == 'PP'and jogador2 == 'P') or \
    (jogador1 == 'T' and jogador2 == 'PP'):
    print("VITÓRIA DO JOGADOR 1")

else: 
    print("VITÓRIA DO JOGADOR 2")





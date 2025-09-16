# O código consiste na lógica da amarelinha 

# A ENTRADA deve conter:
    # - Um número inteiro N que representa o lugar na sequência onde a pedra caiu
 # A SAÍDA deve conter: 
        # - Uma lista de números entre 0 e 9, e o número 10 deve ser substituido por "céu"

N = int(input())

numeros = list(range (0, 11))

resultado = []
for i in numeros: 
    if i == N: 
        continue
    elif i == 10:
        resultado.append("céu")  
    else:
        resultado.append(i)


        print(resultado)
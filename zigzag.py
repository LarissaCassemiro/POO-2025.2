# Este cógigo deve seguir a seguinte lógica: 
# Em uma sequência de números, deve ser considerados: 
    # - Imprimir "zigzag" se o número for divisível por 3 e também por 5
    # - Imprimir "zig" se o número for divisísel por 3
    # - Imprimir "zag" se o número for divisível por 5

#A entrada dos dados deve ser 
        # - Uma linha para marcar o inicio da sequência 
        # - Uma linha para marcar o fim da sequência 

inicio = int(input())
fim = int(input())

for i in range (inicio, fim + 1):
    if i % 3 == 0 and i % 5 == 0:
        print ("zigzag")

    elif i % 3 == 0:
        print("zig")
    elif i % 5 == 0:
        print("zag")
    else:
        print(i)


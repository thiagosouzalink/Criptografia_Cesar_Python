
"""
Arquivo para ler e validar entradas
Autor: Thiago Souza
"""

# Função para validar um valor
def ler_valor(txt):
    while True:
        valor = input(txt)
        try:
            valor = int(valor)
        except:
            print("Houve um erro ao ler o valor, tente novamente...\n")
            continue
        else:
            if valor < 0:
                print("Você digitou um valor negativo, tente novamente\n")
            else:
                break

    return valor

# Função para ler opção do usuário
def definir_opcao(texto_opcao, op1, op2):
    opcao = ler_valor(texto_opcao[0] + texto_opcao[1] + texto_opcao[2])
    while opcao != op1 and opcao != op2:
        print("Você digitou um valor inválido, tente novamente")
        opcao = ler_valor(texto_opcao[0] + texto_opcao[1] + texto_opcao[2])

    return opcao
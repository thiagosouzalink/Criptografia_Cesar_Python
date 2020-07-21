
"""
Projeto Criptografia de César
Autor: Thiago Souza
"""

from funcoes_criptografia import *
from entradas import *

chave = ler_valor("Digite o valor da chave: ") # Recebe o valor da chave

# Texto exibido em opções
texto_opcao = ["\nVocê quer escrever uma mensagem ou ler um arquivo?",
               "\n1 - Escrever mensagem\n2 - Ler arquivo",
               "\nDigite sua opção, [1] ou [2]: "]
opcao = definir_opcao(texto_opcao, 1, 2) # Recebe a opção do usuário

# Texto exibido em tipos
texto_tipo = ["\nVocê deseja Criptografar ou Descriptografar uma mensagem?",
                   "\n1 - Criptografar\n2 - Descriptografar",
                   "\nDigite sua opção, [1] ou [2]: "]
tipo = definir_opcao(texto_tipo, 1, 2) # Recebe o tipo do usuário

# Verifica a opção e seu respectivo tipo informado pelo usuário
if opcao == 1:
    if tipo == 1:
        mensagem = input("Digite a mensagem a ser cifrada: ").strip()
        mensagem_cifrada = criptografar(mensagem, chave)
        print(f"\nNova mensagem cifrada: {mensagem_cifrada}")
        print("\nMensagem cifrada com sucesso!")

    else:
        mensagem = input("Digite a mensagem a ser defifrada: ").strip()
        mensagem_cifrada = descriptografar(mensagem, chave)
        print(f"\nMensagem decifrada: {mensagem_cifrada}")
        print("\nMensagem decifrada com sucesso!")

else:
    if tipo == 1:
        cifrardoc("mensagem.txt", "mensagem_cifrada.txt", chave)
        print("Mensagem cifrada com sucesso!")
    else:
        decifrardoc("mensagem_cifrada.txt", "mensagem_decifrada.txt", chave)
        print("Mensagem decifrada com sucesso!")
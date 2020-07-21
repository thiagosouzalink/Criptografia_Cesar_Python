
"""
Arquivos com funções utilizadas na Criptogafia de César
Autor: Thiago Souza
"""

# Função para Criptografar a mensagem
def criptografar(mensagem, chave):
    # Constrói alfabeto extraído da tabela ASCII (Somente letras minúsculas)
    alfabeto = []
    for i in range(97, 123): # Intervalo de letras minúsculas na tabela.
        alfabeto.append(chr(i))

    tam_alfabeto = len(alfabeto)
    cifrada = ""

    # Laço para ler a mensagem
    for caracter in mensagem:
        nova_letra = caracter
        # Verifica se o caracter pertence ao alfabeto
        if caracter.lower() in alfabeto:
            indice = alfabeto.index(caracter.lower())
            nova_letra = alfabeto[(indice + chave)%tam_alfabeto]
            if caracter.isupper():
                nova_letra = nova_letra.upper()

        cifrada = cifrada + nova_letra
    return cifrada

# Função para descriptografar a mensagem
def descriptografar(mensagem, chave):
    return criptografar(mensagem, -chave)


# Função para escrever em um arquivo a mensagem cifrada
def cifrardoc(fonte, destino, chave):
    # Obtêm a mensagem de um arquivo
    arquivo = open(fonte, 'r')
    msg = arquivo.read()
    arquivo.close()

    cifrada = criptografar(msg, chave)

    # Escreve mensagem criptografada em um arquivo
    arquivo = open(destino, "w")
    arquivo.write(cifrada)
    arquivo.close()
    print("Arquivo de mensagem cifrada executada com sucesso!")

# Função para escrever em um arquivo a mensagem decifrada
def decifrardoc(fonte, destino, chave):
    # Obtêm a mensagem de um arquivo
    arquivo = open(fonte, 'r')
    msg = arquivo.read()
    arquivo.close()

    decifrada = descriptografar(msg, chave)

    # Escreve mensagem criptografada em um arquivo
    arquivo = open(destino, "w")
    arquivo.write(decifrada)
    arquivo.close()
    print("Arquivo de mensagem cifrada executada com sucesso!")



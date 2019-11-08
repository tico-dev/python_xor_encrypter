# -*- coding: utf-8 -*-
# Esse código tem 2 linguagens de comentário, Português e Inglês.
# This code has 2 comment languages, Portuguese and English.
# ----------------------------- Funções ----------------------------- #
from random import randint


def key():
    chave = []
    for c in range(50):
        chave.append(chr(randint(500, 700)))
    print('------------------------------------------\n')
    print('Sua chave:\n' + ''.join(chave) + '\n')
    print('\n------------------------------------------')
    return chave


def encrypt():

    # -------------- Chave -------------- #

    raw_key_list = []
    raw_key_ord = []
    raw_key_bin = []


    # Usuário digita a chave (NOT NULL)
    key_decisao = input("\nAperte 'Enter' para uma chave ser criada automaticamente (recomendado),\n"
                        "ou digite uma chave para criptografar sua mensagem.\n"
                        "[User]: ")

    if key_decisao == '' or key_decisao is None:
        raw_key = key()
    else:
        raw_key = key_decisao                                   # Set the key
        while len(raw_key) < 1:                                 # If the user don't write anything:
            raw_key = input('\nFavor digite uma chave: ')       # Ask for a Key


    # Coloca todos os caracteres em uma lista e: transforma em numero
    for c in raw_key:
        raw_key_list.append(c)                 # Put all characters from the Key in a list and:
        raw_key_ord.append(ord(c))             # turn into number


    # ------------- Mensagem ------------- #

    raw_text_list = []
    raw_text_ord = []
    raw_text_bin = []

    raw_text = input('Digite sua mensagem: ')                   # User write the Message
    while len(raw_text) < 1:                                    # If the user don't write anything:
        raw_text = input('\nFavor digite uma mensagem: ')       # Ask for a Message


    # Coloca todos os caracteres em uma lista e: transforma em numero
    for c in raw_text:
        raw_text_list.append(c)      # Put all characters from the Message in a list and:
        raw_text_ord.append(ord(c))  # turn into number


    # Transforma os números em binário (sem '0b')
    for c in range(len(raw_text)):
        raw_text_bin.append(bin(raw_text_ord[c]).replace('0b', ''))  # Turn into binary number (without '0b')


    # ------------------------------------------------------------------------------------------------------- #

    # Transforma os números em binário (sem '0b')
    for c in range(len(raw_key)):
        raw_key_bin.append(bin(raw_key_ord[c]).replace('0b', ''))  # Turn into binary number (without '0b')


    # Clona os bits da chave até o tamanho da chave se igualar à da mensagem
    count = 0
    for c in range(len(raw_text_bin)):
        while len(raw_text_bin) > len(raw_key_bin):                # If the Message is longer than the Key then:
            raw_key_bin.append(str(raw_key_bin[count]))            # Clone the Key until the Key and Message has the same length.
            count += 1

    # ------------------ Igualando os binários ---------------------- #


    # Se a chave for MAIOR, exclui os últimos bits até terem o mesmo tamanho
    while len(raw_text_bin) < len(raw_key_bin):                    # If the Key is longer than the Message then:
        raw_key_bin.pop()                                          # Pop out the lasts caracters from the Key until the Key and Message has the same length.


    # Iguala a quantidade de bits por binário para comparar bit a bit
    # Acrescentando '0' à esquerda ('0' à esquerda em binário é ignorado)
    for posicao in range(len(raw_text_bin)):
        while len(raw_text_bin[posicao]) < len(raw_key_bin[posicao]):   # Text:
            raw_text_bin[posicao] = '0' + raw_text_bin[posicao]         # equals number of characters in binary (left '0')

        while len(raw_text_bin[posicao]) > len(raw_key_bin[posicao]):   # Key:
            raw_key_bin[posicao] = '0' + raw_key_bin[posicao]           # equals number of characters in binary (left '0')
    print('------------------------------------------')

    # ._________________________________.    # ._________________________________.
    # |                                 |    # |                                 |
    # |Applying the bitwise xor operator|    # |Aplicando operador xor bit-a-bit |
    # |                                 |    # |                                 |
    # | Example:                        |    # | Examplo:                        |
    # |       1100001 (bin 'a')         |    # |       1100001 (bin 'a')         |
    # |       1100010 (bin 'b')         |    # |       1100010 (bin 'b')         |
    # | xor:  0000011 (encrypted)       |    # | xor:  0000011 (criptografado)   |
    # |                                 |    # |                                 |
    # |  bits: 1 and 1 returns 0        |    # |  bits: 1 e 1 retorna 0          |
    # |  bits: 0 and 0 returns 0        |    # |  bits: 0 e 0 retorna 0          |
    # |  bits: 1 and 0 returns 1        |    # |  bits: 1 e 0 retorna 1          |
    # |  bits: 0 and 1 returns 1        |    # |  bits: 0 e 1 retorna 1          |
    # ._________________________________.    # ._________________________________.

    xor = []

    # Junta a lista pra comparar bit a bit
    texto_junto = '.'.join(raw_text_bin)            # 'Join' text_bin to compare bit by bit
    key_junta = '.'.join(raw_key_bin)               # 'Join' key_bin to compare bit by bit


    # Como eu juntei a lista do texto com '.'(ponto final),
    # agora vou juntar a lista XOR para que seja preenchida apenas com números (usei o número 2, pois é um algarismo numérico que não existe em binário)
    for c in range(len(texto_junto)):
        if texto_junto[c] == '.':                       # As I had joined the text with '.',
            xor.append('2')                             # now I will join the XOR list with '2' (xor list will be filled with numbers only)

        # Aplica xor:
        else:
            # Se bits forem iguais: retorna 0
            if texto_junto[c] == key_junta[c]:          # If (1 and 1) or (0 and 0):
                xor.append('0')                         # Returns 0

            # Se bits forem diferentes: retorna 1
            else:                                       # If not:
                xor.append('1')                         # Returns 1


    # Junta a lista XOR e transforma em hexadecimal
    # (apenas para o front ficar mais limpo)
    xor = ''.join(xor)                                  # Joins xor list
    hexa = hex(int(xor))                                # turn the joined list in hexadecimal
    print('Sua mensagem Criptografada:')
    print(hexa.replace('0x', ''))                       # print(hexadecimal with out '0x' in the begging)
    print('------------------------------------------\n')


def decrypt():
    # Usuário digitará a mensagem em hexadecimal.
    texto_criptografado = input('Digite sua mensagem criptografada:\n')         # Input the encrypted text

    # Mensagem não pode ser vazia (NOT NULL)
    while len(texto_criptografado) < 1:                                         # if the user dont write anything:
        texto_criptografado = input('Favor digite uma mensagem: ')              # print('Please type something.')


    # Tratamento para tirar de uma lista, interpretar cada item e retornar uma lista nova.
    texto_sem_hexa = str(int(texto_criptografado, 16))                          # Retorns the binary code behind the hexadecimal
    texto_descriptografar = texto_sem_hexa.split('2')                           # Turns it on a new list (splited with '2')

    # ----- Chave ----- #

    raw_key_list = []
    raw_key_ord = []
    raw_key_bin = []


    # Usuário digita a chave
    raw_key = input('\nDigite sua chave:')                                       # Input the key

    # Chave não pode ser vazia (NOT NULL)
    while len(raw_key) < 1:                                                     # if the user dont write anything:
        raw_key = input('Favor digite uma chave: ')                             # print('Please write the key.')


    # Coloca todos os caracteres em uma lista e: transforma em numero e:
    for c in raw_key:
        raw_key_list.append(c)                                                  # Put all characters from the Message in a list and:
        raw_key_ord.append(ord(c))                                              # turn into number


    # transforma o numero em binário
    for c in range(len(raw_key)):
        raw_key_bin.append(bin(raw_key_ord[c]).replace('0b', ''))               # Turn into binary number (without '0b')


    # Clona os bits da chave até o tamanho da chave se igualar à da mensagem
    count = 0
    for c in range(len(texto_descriptografar)):
        while len(texto_descriptografar) > len(raw_key_bin):                    # If the Message is longer than the Key then:
            raw_key_bin.append(str(raw_key_bin[count]))                         # Clone the Key until the Key and Message has the same length.
            count += 1

    # ------------------ Igualando os binários ---------------------- #

    # Se a chave for MAIOR, exclui os últimos bits até terem o mesmo tamanho
    while len(texto_descriptografar) < len(raw_key_bin):                        # If the Key is longer than the Message then:
        raw_key_bin.pop()                                                       # Pop out the lasts caracters from the Key until the Key and Message has the same length.


    # Iguala a quantidade de bits por binário para comparar bit a bit
    # Acrescentando '0' à esquerda ('0' à esquerda em binário é ignorado)
    for posicao in range(len(texto_descriptografar)):
        while len(texto_descriptografar[posicao]) < len(raw_key_bin[posicao]):      # Text:
            texto_descriptografar[posicao] = '0' + texto_descriptografar[posicao]   # equals number of characters in binary (left '0')

        while len(texto_descriptografar[posicao]) > len(raw_key_bin[posicao]):      # Key?
            raw_key_bin[posicao] = '0' + raw_key_bin[posicao]                       # equals number of characters in binary (left '0')



    # Junta as listas para comparar bit-a-bit
    texto_junto = '.'.join(texto_descriptografar)         # 'Join' texto_junto to compare bit by bit
    key_junta = '.'.join(raw_key_bin)                     # 'Join' key_junta to compare bit by bit
    descriptografado_bin = []
    descriptografado = []

    # Como eu juntei a lista do texto com '.'(ponto final),
    # agora vou juntar a lista Descriptografada com '.' também (para ficarem iguais para comparação)
    for c in range(len(texto_junto)):
        if texto_junto[c] == '.':                         # As I had joined the text with '.',
            descriptografado_bin.append('.')              # I'll join the decrypted text with '.' too


        # Aplica Xor
        else:
            # Se bits forem iguais: retorna 0
            if texto_junto[c] == key_junta[c]:            # If (1 and 1) or (0 and 0):
                descriptografado_bin.append('0')          # Returns 0

            # Se bits forem diferentes: retorna 1
            else:                                         # If (1 and 0) or (0 and 1):
                descriptografado_bin.append('1')          # Returns 1



    # Junta a lista Descriptografado, e depois separa novamente onde for '.' (ponto final)
    descriptografado_bin = ''.join(descriptografado_bin)            # Joins decrypted_bin list
    descriptografado_bin = descriptografado_bin.split('.')          # then split where '.'


    # Transforma o número binário (XOR) em número inteiro, e transforma o número inteiro em caracter (função CHR)
    for c in descriptografado_bin:
        descriptografado.append(chr(int(c, 2)))                     # Transform binary code into number and then transform the int value to character (CHR function)

    # Print da mensagem descriptografada (FINAL)
    print('------------------------------------------')
    print('Sua mensagem: ', ''.join(descriptografado))              # Print the decrypted text (END)
    print('------------------------------------------\n')


# ----------------------------- Front Inicial ----------------------------- #
# ------------------------------- Front End ------------------------------- #


while True:
    decisao = input(
        '[1] Digite "1" para Criptografar;\n'
        '[2] Digite "2" para Descriptografar;\n'
        '[3] Digite "3" para Sair.\n'
        '[User]: ')

    # Precione '1' para criptografar
    if decisao == '1':                                      # Press '1' to encrypt
        print('---------------Criptografar---------------')
        encrypt()

    # Precione '2' para descriptografar
    if decisao == '2':                                      # Press '2' to decrypt
        print('-------------Descriptografar-------------')
        decrypt()

    # Precione '3' para sair
    if decisao == '3':                                      # Press '3' to exit
        print('Programa fechado.')
        break

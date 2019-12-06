# importamos apenas a função 'randint' da biblioteca 'random':
# ela gera números inteiros 'aleatórios' que estiverem dentro de um intervalo.
from random import randint


def key():
    # Lista onde será guardado os caracteres da chave (valores em alfanumérico).
    chave = []
   
    # Laço que rodará por cada caracter na mensagem (+15: a chave terá o 15 caracteres a mais que a mensagem):
    for c in range(len(mensagem) + 15):
        
        # Adiciona um caracter aleatório que esteja entre a posição 500 e posição 700 de acordo com a sua representação numérica
        chave.append(chr(randint(500, 700)))
        
    # Mostra a chave para o usuário em forma de string.
    print('\nSua chave:\n' + ''.join(chave) + '\n')

    # Quando a função for agregada à uma variavel, o valor retornado será a chave.
    return chave

# Função que criptografa e descriptografa a mensagem:
def encrypt_decrypt():
    
    # Lista onde será guardado os caracteres após o operador XOR(valores em alfanumérico)
    xor = []


    # Laço que rodará 1 vez por cada caracter na mensagem:
    for c in range(len(mensagem)):

        # Primeiro faz a criptografia/descriptografia usando o operador XOR (^) entre os caracteres na posição C da mensagem e da chave,
        # Depois transforma o resultado do da operação em caractere, de acordo com a sua representação numérica
        xor.append(chr(ord(mensagem[c]) ^ (ord(_chave[c]))))

    # Mostra a mensagem para o usuário em forma de string
    # ("join" é usado para juntar os valores da lista, formando uma string)
    print('Sua mensagem:\n')
    print(''.join(xor))
    print('\n')

# Interface (rodará até que o usuário force a parada ("BREAK").
while True:

    # Decisão é a variável que guardará a opção selecionada pelo usuário.
    decisao = input(
        '[1] Digite "1" para Criptografar;\n'
        '[2] Digite "2" para Descriptografar;\n'
        '[3] Digite "3" para Sair.\n'
        '[User]: ')

    # Direciona as opções para suas respectivas funções:
    # Se a opção selecionada for '1':
    #
    # Criptografar:
    #   - Usuário digita a mensagem que quer criptografar (o programa guardará em forma de lista);
    #   - A função KEY() gera uma chave aleatória (e grava na variável '_chave');
    #   - Direciona o usuário para a função ENCRYPT_DECRYPT(), que criptografará a mensagem.
    if decisao == '1':
        print('---------------Criptografar---------------')
        mensagem = list(input('Digite sua mensagem para criptografar:\n'))
        _chave = key()
        encrypt_decrypt()

    # Se a opção selecionada for '2':
    #
    # Descriptografar:
    #   - Usuário digita a mensagem que quer descriptografar (o programa guardará em forma de lista);
    #   - Usuário digita a chave de descriptografia (o programa guardará em forma de lista);
    #   - Direciona o usuário para a função ENCRYPT_DECRYPT(), que descriptografará a mensagem.           
    elif decisao == '2':
        print('-------------Descriptografar-------------')
        mensagem = list(input('Digite sua mensagem criptografada:\n'))
        _chave = list(input('Digite sua chave:\n'))

        # Validador de chave: Verifica se a chave é (no mínimo) do tamanho da mensagem.
        while len(_chave) < len(mensagem):
            print('A chave deve ser maior do que a mensagem\n')
            _chave = list(input('Digite sua chave:\n'))
        encrypt_decrypt()

    # Se a opção selecionada for '3':
    # Interrompe o programa.
    elif decisao == '3':
        print('Programa fechado.')
        break

    # Válvula de escape: se o usuário selecionar um opção não válida:
    # repete o loop com uma mensagem de erro.
    else:
        print('\nSelecione uma opção válida:\n')
        pass


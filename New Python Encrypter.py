from random import randint

def key():
    chave = []
    for c in range(50):
        chave.append(chr(randint(500, 700)))
    print('\nSua chave:\n' + ''.join(chave) + '\n')
    return chave


def encrypt():
    criptografado = []
    for c in range(len(mensagem)):
        criptografado.append(chr(ord(mensagem[c]) ^ (ord(_chave[c]))))
    print('Sua mensagem criptografada:\n')
    print(''.join(criptografado))
    print('\n')


while True:
    decisao = input(
        '[1] Digite "1" para Criptografar;\n'
        '[2] Digite "2" para Descriptografar;\n'
        '[3] Digite "3" para Sair.\n'
        '[User]: ')


    if decisao == '1':
        print('---------------Criptografar---------------')
        _chave = key()
        mensagem = list(input('Digite sua mensagem:\n'))
        encrypt()

    if decisao == '2':
        print('-------------Descriptografar-------------')
        mensagem = list(input('Digite sua mensagem criptografada:\n'))
        _chave = list(input('Digite sua chave:\n'))
        while len(_chave) < len(mensagem):
            print('A chave deve ser maior do que a mensagem\n')
            _chave = list(input('Digite sua chave:\n'))
        encrypt()

    if decisao == '3':
        print('Programa fechado.')
        break

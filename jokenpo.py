from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('''\033[1;1;33mEscolha uma opção: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
print('-='*20)
jogador = int(input('\033[0;0;32mDigite sua opção:\033[m '))
computador = randint(0, 2)
print('\033[0;0;36m### JO ###\033[m')
sleep(1)
print('\033[0;0;36m### KEN ###\033[m')
sleep(1)
print('\033[0;0;36m### PÔ!! ###\033[m')
print('O computador escolheu \033[0;0;33m{}\033[m'.format(itens[computador].upper()))
print('Você escolheu \033[0;0;33m{}\033[m.'.format(itens[jogador].upper()))
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('\033[0;0;34mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[0;0;34mVENCEU!\033[m')
    elif jogador == 2:
        print('\033[0;0;34mPERDEU!\033[m')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('\033[0;0;34mPERDEU!\033[m')
    elif jogador == 1:
        print('\033[0;0;34mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[0;0;34mGANHOU!\033[m')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('\033[0;0;34mGANHOU!\033[m')
    elif jogador == 1:
        print('\033[0;0;34mPERDEU!\033[m')
    elif jogador == 2:
        print('\033[0;0;34mEMPATE!\033[m')
    else:
        print('JOGADA INVALIDA!')



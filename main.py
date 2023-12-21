from batalha import Batalha
from guerreiro import Guerreiro
from monstro import Monstro
from mago import Mago

while True:
    print('- OPONENTE 1 - ')
    print('Digite o tipo de guerreiro que deseja batalhar: ')
    op = input('Guerreiro, Mago ou Monstro: ').lower()
    if op == 'guerreiro':
        oponente1 = Guerreiro('Guerreiro', 800, 200, 500, 1)
        break
    elif op == 'mago':
        oponente1 = Mago('Mago', 700, 250, 400, 1)
        break
    elif op == 'monstro':
        oponente1 = Monstro('Monstro', 900, 150, 600, 1)
        break
    else:
        print('Personagem inválido! Tente novamente')

print("-------------------------------------------------------------------")

while True:
    print('- OPONENTE 2 - ')
    print('Digite o tipo de guerreiro que deseja batalhar: ')
    op = input('Guerreiro, Mago ou Monstro: ').lower()
    if op == 'guerreiro':
        oponente2 = Guerreiro('Guerreiro', 800, 200, 500, 1)
        break
    elif op == 'mago':
        oponente2 = Mago('Mago', 700, 250, 400, 1)
        break
    elif op == 'monstro':
        oponente2 = Monstro('Monstro', 900, 150, 600, 1)
        break
    else:
        print('Personagem inválido! Tente novamente')

batalha = Batalha(oponente1, oponente2)
print(batalha.batalha())

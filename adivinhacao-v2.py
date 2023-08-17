#   Imports
import random as rdm

def jogar():
    #   Start
    print('#-------------------------------#')
    print('Bem vindo ao jogo de Adivinhação')
    print('#-------------------------------#\n')

    # Níveis de dificuldade:
    print('Escolha seu nível de dificuldade')
    print('| [1] para Fácil \n| [2] para Média \n| [3] para Difícil')
    dificuldade = int(input('Digite o número correspondente à dificuldade: '))
    
    if (dificuldade == 1):
        total_de_tentativas = 9
        numero_secreto = rdm.randrange(1, 26)
        numero_range = 25
        pontos = 80
        print(f'\nVocê escolheu o nível Fácil - Você tem {total_de_tentativas} tentativas!\nVocê começa com {pontos} pontos!')
    elif (dificuldade == 2):
        total_de_tentativas = 6
        numero_secreto = rdm.randrange(1, 26) + 10
        numero_range = 35
        pontos = 60
        print(f'\nVocê escolheu o nível Médio - Você tem {total_de_tentativas} tentativas!\nVocê começa com {pontos} pontos!')
    elif (dificuldade == 3):
        total_de_tentativas = 3
        numero_secreto = rdm.randrange(1, 26) + 20
        numero_range = 45
        pontos = 40
        print(f'\nVocê escolheu o nível Médio - Você tem {total_de_tentativas} tentativas!\nVocê começa com {pontos} pontos!')
    else:
        print('Opção invalida, escolha uma opção válida!')
        jogar()


    # Laço de repetição
    # while (rodada <= total_de_tentativas):

    for rodada in range(1, total_de_tentativas + 1):
        print(f'{numero_secreto}')
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute = int(input(f'Chute um número de 1 a {numero_range}: '))
        
        if (chute < 1 or chute > numero_range):
            print(f'\nVocê deve digitar um número entre 1 e 20')
            continue

    # Variáveis
        acertou = numero_secreto == chute
        maior = numero_secreto > chute
        menor = numero_secreto < chute

    # Condições
    
        if (acertou):
            print(f'\nVocê chutou {chute} e acertou!\nSua pontuação é de: {pontos}\n')
            break
       
        elif (menor):
            print(f'\nVocê errou! O Número Secreto é menor que {chute}!\n')
            pontos_perdidos = numero_secreto - chute
            pontos -= pontos_perdidos
            print('')
        
        elif (maior):
            print(f'\nVocê errou! O Número Secreto é maior que {chute}!\n')
            pontos_perdidos = numero_secreto - chute
            pontos -= pontos_perdidos
    
        if (pontos <= 0):
            print(f'Você perdeu por pontos! O número secreto era {numero_secreto}!')
            break
        
        elif (total_de_tentativas == rodada):
            print(f'Você perdeu por tentativas! O número secreto era {numero_secreto}!')
            break


    print('Fim do jogo')

jogar()
import forca
import adivinhacao_v2

def escolhe_jogo():
    print('#-------------------------#')
    print('Escolha um dos jogos abaixo:')
    print('[1] para Forca \n[2] para Adivinhação\n[3] para Encerrar')
    jogo = int(input('Digite o jogo que quer jogar: '))
    print('#-------------------------#')

    if (jogo == 1):
        print('Vamos começar com o jogo da Forca!\n')
        forca.jogar()
    elif (jogo == 2):
        print('Vamos começar com o jogo da Forca!\n')
        adivinhacao_v2.jogar()
    elif (jogo == 3):
        print('Jogos encerrados!')
    else:
        print('Opção inválida.')
        escolhe_jogo()
if (__name__ == "__main__"):
    escolhe_jogo()
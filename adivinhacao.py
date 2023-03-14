import random

# Jogo de Adivinhação v1.0
# Alura - Python: Começando com a Linguagem
# Aluno: Leonard Barbosa

print('\n')
print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')
print('\n')

# nível dificuldade
def escolha_nivel():
    global tentativas
    print('Escolha um nível de dificuldade.')
    print('(1) Fácil | (2) Médio | (3) Difícil')
    nivel = int(input('Digite seu nível de dificuldade: '))
    if (nivel >= 1 or nivel <= 3):
        if (nivel == 1):
            tentativas = 10
            jogada()
        elif (nivel == 2):
            tentativas = 5
            jogada()
        elif (nivel == 3):
            tentativas = 3
            jogada()
        else:
            print('Não existe este nível de dificuldade')
            return escolha_nivel()

def jogada():
    numero_secreto = random.randint(1, 30)
    pontos = 100
    for rodada in range(1, tentativas + 1):
        print('\nTentativa {} de {}'.format(rodada, tentativas))
        chute = int(input('Digite um número entre 1 e 30: '))
        print('Você digitou: ', chute)

        if (chute < 1 or chute > 30):
            print('Você precisa digitar um número entre 1 e 30.')
            return jogada()

        # variáveis loop
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        # funções loop
        if (acertou):
            print('\n**************************************')
            print('Você Acertou!')
            print('O número secreto era: ', numero_secreto)
            print('Sua pontuação final foi de {} pontos!'.format(pontos))
            print('**************************************')
            break
        else:
            if (maior):
                print('Você errou! O seu chute foi maior que o número secreto!')

            elif (menor):
                print('Você errou! O seu chute foi menor que o número secreto!')

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        if (pontos <= 0):
            print('\n**************************************')
            print('Você perdeu por PONTOS!')
            print('O número secreto era: ', numero_secreto)
            print('Sua pontuação foi de {} pontos'.format(pontos))
            print('**************************************')
            break

        if (rodada == tentativas):
            print('\n**************************************')
            print('Você perdeu por TENTATIVAS!')
            print('O número secreto era: ', numero_secreto)
            print('Sua pontuação foi de {} pontos'.format(pontos))
            print('**************************************')
            break

escolha_nivel()
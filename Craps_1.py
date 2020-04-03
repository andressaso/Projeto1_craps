#----------------------------------------------------------------------#
# - Imports:

import random

#----------------------------------------------------------------------#
# - Introdução:

nome=input("Digite seu nome: ")
fichas=1000

print("")
print("Bem vindo, {0} ao jogo Craps!".format(nome))
print("bjcnjnndkjnkjsndkjdkjsdjksbd")

#----------------------------------------------------------------------#
# - Loop Principal:

while fichas > 0:
    print("")
    print("------------------------------")
    print("Você esta na 1° fase: Come Out")
    print("Você tem {0} fichas.".format(fichas))
    print("")

    print('Escolha seu tipo de aposta:')
    print('- Pass Line')
    print('- Field')
    print('- Any Craps')
    print('- Twelve')
    qual_aposta=input('Opção: ')

#----------------------------------------------------------------------#
# - Modo 'Pass Line':

    if qual_aposta == 'Pass Line' or qual_aposta == 'Pass line' or qual_aposta == 'pass line' or qual_aposta == 'PASS LINE':
        dado_um=random.randint(1,6)
        dado_dois=random.randint(1,6)
        soma_dados = (dado_um + dado_dois)

        aposta=int(input('Quantas fichas você vai querer apostar? '))
        while aposta > fichas:
            print("Inválido, você está apostando mais do que tem.")
            aposta=int(input('Digite novamente: '))

        fichas-=aposta

        if soma_dados in [7,11]:
            fichas += aposta*2

            print("")
            print('Você ganhou, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados in [2,3,12]:
            fichas += 0

            print("")
            print('Você perdeu, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))


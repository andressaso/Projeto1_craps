#----------------------------------------------------------------------#
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------#
# - Imports:

import random

#----------------------------------------------------------------------#
# - Configurações do Jogo:

fichas = 1000

bem_vindo = "O PyCraps é um jogo de dados como os de cassinos desenvolvido em python.\n\nNele existem 4 modos de jogo, sendo eles:\n- Pass Line\n- Field\n- Any Craps\n- Twelve\n\nCada um deles com suas regras, ganhos e riscos!\nBoa Sorte!\n"

invalido = "Inválido! Digite uma das opções acima."
invalido_aposta = "Inválido! Você não tem fichas o suficiente para apostar esse valor!"

ganhou = 'Você ganhou, a soma dos seus dados foi: '
perdeu = 'Você perdeu, a soma dos seus dados foi: '

#----------------------------------------------------------------------#
# - Introdução:

nome = input("Digite seu nome: ")

print("")
print("-------------------------------------------------------")
print("Bem vindo ao PyCraps, {0}!".format(nome))
print(bem_vindo)

print("Você deseja ver as regras?")
print("- Sim")
print("- Não")

tutorial=input("Opção: ")
while tutorial!="NÃO" and tutorial!="NAO" and tutorial!="Não" and tutorial!="Nao" and tutorial!="N" and tutorial!="não" and tutorial!="nao" and tutorial!="n" and tutorial!="SIM" and tutorial!="Sim" and tutorial!="S" and tutorial!="sim" and tutorial!="s":
    print(invalido)
    tutorial=input("Opção: ")
    
if tutorial=="NÃO" or tutorial=="NAO" or tutorial=="Não" or tutorial=="Nao" or tutorial=="N" or tutorial=="não" or tutorial=="nao" or tutorial=="n":
    print("\nOk, Boa sorte!")
if tutorial=="SIM" or tutorial=="Sim" or tutorial=="S" or tutorial=="sim" or tutorial=="s":

    print("-------------------------------------------------------")
    print("\nREGRAS:\n\nVocê pode escolher o modo que quiser e quantas vezes quiser, desde que ainda tenha fichas. Sempre antes de começar será perguntado em qual modo você quer jogar e quanto você irá apostar e logo depois você poderá jogar os dados.\n\nNo modo 'Pass Line', há 3 resultados possíveis de acordo com os valores obtidos nos dados. Se a soma dos dados for 7 ou 11, você mantém a quantia de fichas que apostou e recebe mais uma vez esse valor. Caso a soma seja 2,3 ou 12, você irá perder na hora o valor apostado. Caso a soma seja qualquer um dos outros números (4,5,6,9 ou 10), você poderá jogar repetidamente os dados, sem perder nem ganhar fichas, até que a soma seja a mesma que você tirou anteriormente. Por fim, caso a soma seja 7 você perde tudo o que tiver apostado.\n\nNo modo 'Field', há 4 possibilidades diferentes. Se a soma for 2, você ganhará 2 vezes o que apostou, caso seja 12 você ganha 3 vezes o que apostou, se a soma for 5,6,7,8 você perde o que apostou e, por último, se for 3,4,9,10 ou 11 você ganhará de volta a quantia que foi apostada.\n\nNo modo 'Any Craps', existem apenas dois resultados possíveis, se a soma for 2,3 ou 12 você ganha 7 vezes a quantia que apostou, caso seja qualquer outro número, você perde o que apostou.\n\nNo último modo, chamado 'Twelve', existem também apenas dois resultados, se você tirar 12 você ganhará 30 vezes o que apostou, e se tirar qualquer outro número diferente de 12 você perderá o que apostou.\n\nSempre ao final de cada rodada será perguntado se você deseja jogar mais, caso queira basta escrever 'sim', se não desejar jogar mais basta digitar 'não' e o jogo será encerrado.\n")
    print("-------------------------------------------------------")
    
    pronto=input("Pronto para jogar? ")
    while pronto!="SIM" and pronto!="Sim" and pronto!="S" and pronto!="sim" and pronto!="s" and pronto!="CLARO" and pronto!="Claro" and pronto!="claro":
        pronto=input("Ok, diga quando estiver...\nE agora, está pronto para jogar? ")
   
#----------------------------------------------------------------------#
# - Loop Principal:

while fichas>0:
    print("")
    print("------------------------------")
    print("Você esta na 1° fase: Come Out")
    print("Você tem {0} fichas.".format(fichas))
    print("------------------------------") 

    print("")
    print('Escolha seu tipo de aposta:')
    print('- Pass Line')
    print('- Field')
    print('- Any Craps')
    print('- Twelve')
    qual_aposta=input('Opção: ')
    while qual_aposta!='Pass Line' and qual_aposta!='Pass line' and qual_aposta!='pass line' and qual_aposta!='PASS LINE' and qual_aposta!='Field' and qual_aposta!='field' and qual_aposta!='FIELD' and qual_aposta!='Any Craps' and qual_aposta!='Any craps' and qual_aposta!='any craps' and qual_aposta!='ANY CRAPS' and qual_aposta!='Twelve' and qual_aposta!='twelve' and qual_aposta!='TWELVE' and qual_aposta!='12':
        print(invalido)
        qual_aposta=input('Opção: ')
        
    aposta=int(input('Quantas fichas você vai querer apostar? '))
    while aposta > fichas:
        print(invalido_aposta)
        aposta=int(input('Digite novamente: '))
    fichas-=aposta
    
    dado_um=random.randint(1,6)
    dado_dois=random.randint(1,6)
    soma_dados=(dado_um+dado_dois)
    print("")
    enter=input("--------------------------------------\nPressione 'ENTER' para jogar os dados:\n--------------------------------------\n")
    while enter!='':
        enter=input("Pressione 'ENTER' para jogar os dados.")
        

#----------------------------------------------------------------------#
# - Modo 'Pass Line':

    if qual_aposta=='Pass Line' or qual_aposta=='Pass line' or qual_aposta=='pass line' or qual_aposta=='PASS LINE':
        if soma_dados in [7,11]:
            fichas+=aposta*2

            print("")
            print(ganhou,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados in [2,3,12]:
            fichas+=0

            print("")
            print(perdeu,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados in [4,5,6,8,9,10]:

            print("")
            print('Você está na fase Point e para ganhar você deverá tirar o mesmo valor que tirou na soma dos dados da jogada anterior.')
            print("A soma dos seus dados foi {0}.".format(soma_dados))

            while True:
                dado_um_P=random.randint(1,6)
                dado_dois_P=random.randint(1,6)
                soma_dados_P=(dado_um_P+dado_dois_P)
                print("")
                enter=input("--------------------------------------\nPressione 'ENTER' para jogar os dados:\n--------------------------------------\n")
                while enter!='':
                    enter=input("Pressione 'ENTER' para jogar os dados.")

                if soma_dados==soma_dados_P:
                    fichas+=aposta

                    print("")
                    print("Você ganhou de volta as suas fichas que foram apostados, a soma dos seus dados foi {0}.".format(soma_dados))
                    print('Você tem {0} fichas agora.'.format(fichas))
                    break

                if soma_dados_P==7:
                    fichas+=0

                    print("")
                    print('Você perdeu, a soma dos seus dados jogados pela 2° vez foi 7.')
                    print('Você tem {0} fichas agora.'.format(fichas))
                    break

                else:
                    print("")
                    print("Você continuará na fase Point, não ganhou nem perdeu fichas e os dados serão lançados novamente.")
                    print("A soma dos seus dados jogados dessa vez foi {0}.".format(soma_dados_P))

        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
        ficar_ou_nao=input("Opção: ")
        while ficar_ou_nao!="NÃO" and ficar_ou_nao!="NAO" and ficar_ou_nao!="Não" and ficar_ou_nao!="Nao" and ficar_ou_nao!="N" and ficar_ou_nao!="não" and ficar_ou_nao!="nao" and ficar_ou_nao!="n" and ficar_ou_nao!="SIM" and ficar_ou_nao!="Sim" and ficar_ou_nao!="S" and ficar_ou_nao!="sim" and ficar_ou_nao!="s":
            print(invalido)
            ficar_ou_nao=input("Opção: ")
        if ficar_ou_nao=="NÃO" or ficar_ou_nao=="NAO" or ficar_ou_nao=="Não" or ficar_ou_nao=="Nao" or ficar_ou_nao=="N" or ficar_ou_nao=="não" or ficar_ou_nao=="nao" or ficar_ou_nao=="n":
            break
        if ficar_ou_nao=="SIM" or ficar_ou_nao=="Sim" or ficar_ou_nao=="S" or ficar_ou_nao=="sim" or ficar_ou_nao=="s":
            print()

#----------------------------------------------------------------------#
# - Modo 'Field':

    if qual_aposta=='Field' or qual_aposta=='field' or qual_aposta=='FIELD':
        if soma_dados==2:
            fichas+=aposta*2

            print("")
            print(ganhou,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados==12:
            fichas+=aposta*3

            print("")
            print(ganhou,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados in [5,6,7,8]:
            fichas+=0

            print("")
            print(perdeu,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados in [3,4,9,10,11]:
            fichas+=aposta

            print("")
            print("Você ganhou de volta as suas fichas que foram apostados, a soma dos seus dados foi {0}.".format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
        ficar_ou_nao=input("Opção: ")
        while ficar_ou_nao!="NÃO" and ficar_ou_nao!="NAO" and ficar_ou_nao!="Não" and ficar_ou_nao!="Nao" and ficar_ou_nao!="N" and ficar_ou_nao!="não" and ficar_ou_nao!="nao" and ficar_ou_nao!="n" and ficar_ou_nao!="SIM" and ficar_ou_nao!="Sim" and ficar_ou_nao!="S" and ficar_ou_nao!="sim" and ficar_ou_nao!="s":
            print(invalido)
            ficar_ou_nao=input("Opção: ")
        if ficar_ou_nao=="NÃO" or ficar_ou_nao=="NAO" or ficar_ou_nao=="Não" or ficar_ou_nao=="Nao" or ficar_ou_nao=="N" or ficar_ou_nao=="não" or ficar_ou_nao=="nao" or ficar_ou_nao=="n":
            break
        if ficar_ou_nao=="SIM" or ficar_ou_nao=="Sim" or ficar_ou_nao=="S" or ficar_ou_nao=="sim" or ficar_ou_nao=="s":
            print()

#----------------------------------------------------------------------#
# - Modo 'Any Craps':

    if qual_aposta=='Any Craps' or qual_aposta=='Any craps' or qual_aposta=='any craps' or qual_aposta=='ANY CRAPS':
        if soma_dados in [2,3,12]:
            fichas+=aposta*7

            print("")
            print(ganhou,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        else:
            print("")
            print(perdeu,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
        ficar_ou_nao=input("Opção: ")
        while ficar_ou_nao!="NÃO" and ficar_ou_nao!="NAO" and ficar_ou_nao!="Não" and ficar_ou_nao!="Nao" and ficar_ou_nao!="N" and ficar_ou_nao!="não" and ficar_ou_nao!="nao" and ficar_ou_nao!="n" and ficar_ou_nao!="SIM" and ficar_ou_nao!="Sim" and ficar_ou_nao!="S" and ficar_ou_nao!="sim" and ficar_ou_nao!="s":
            print(invalido)
            ficar_ou_nao=input("Opção: ")
        if ficar_ou_nao=="NÃO" or ficar_ou_nao=="NAO" or ficar_ou_nao=="Não" or ficar_ou_nao=="Nao" or ficar_ou_nao=="N" or ficar_ou_nao=="não" or ficar_ou_nao=="nao" or ficar_ou_nao=="n":
            break
        if ficar_ou_nao=="SIM" or ficar_ou_nao=="Sim" or ficar_ou_nao=="S" or ficar_ou_nao=="sim" or ficar_ou_nao=="s":
            print()

#----------------------------------------------------------------------# 
# - Modo 'Twelve':

    if qual_aposta=='Twelve' or qual_aposta=='twelve' or qual_aposta=='TWELVE' or qual_aposta=='12':
        if soma_dados==12:
            fichas+=aposta*30

            print("")
            print(ganhou,'12. A quantia de fichas que você apostou multiplicou por 30.')
            print('Você tem {0} fichas agora.'.format(fichas))

        else:
            fichas+=0

            print("")
            print(perdeu,'{0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
        ficar_ou_nao=input("Opção: ")
        while ficar_ou_nao!="NÃO" and ficar_ou_nao!="NAO" and ficar_ou_nao!="Não" and ficar_ou_nao!="Nao" and ficar_ou_nao!="N" and ficar_ou_nao!="não" and ficar_ou_nao!="nao" and ficar_ou_nao!="n" and ficar_ou_nao!="SIM" and ficar_ou_nao!="Sim" and ficar_ou_nao!="S" and ficar_ou_nao!="sim" and ficar_ou_nao!="s":
            print(invalido)
            ficar_ou_nao=input("Opção: ")
        if ficar_ou_nao=="NÃO" or ficar_ou_nao=="NAO" or ficar_ou_nao=="Não" or ficar_ou_nao=="Nao" or ficar_ou_nao=="N" or ficar_ou_nao=="não" or ficar_ou_nao=="nao" or ficar_ou_nao=="n":
            break
        if ficar_ou_nao=="SIM" or ficar_ou_nao=="Sim" or ficar_ou_nao=="S" or ficar_ou_nao=="sim" or ficar_ou_nao=="s":
            print()

#----------------------------------------------------------------------#
# - Finalização do Game:

print("")
print("")
print("")

if fichas>0:          
    print("")
    print("--------------------------------------------")
    print("PARABÉNS!!!")
    print("Você finalizou o jogo com {0} fichas.".format(fichas))
    print("--------------------------------------------")
    print("")

else:
    print("")
    print("----------------------------------------")
    print("Você perdeu o jogo e ficou com 0 fichas.")
    print("----------------------------------------")
    print("")

print("")
print("")
print("")
print("")
print("----------------------")
print("OBRIGADO POR JOGAR!")
print("Feito por:")
print("- Maria Eduarda Torres")
print("- Andressa Silva de Oliveira")
print("----------------------")
print("")
print("")
print("")
print("")

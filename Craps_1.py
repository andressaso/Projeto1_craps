#----------------------------------------------------------------------#
# - Imports:

import random

#----------------------------------------------------------------------#
# - Introdução:

nome=input("Digite seu nome: ")
fichas=1000

print("")
print("Bem vindo ao jogo Craps, {0}!".format(nome))
print("Boa sorte! ")

#----------------------------------------------------------------------#
# - Loop Principal:

while fichas > 0:
    print("")
    print("------------------------------")
    print("Você está na fase inicial: Come Out")
    print("Você tem {0} fichas.".format(fichas))
    print("")

    print('Escolha o seu tipo de aposta:')
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
            print("Inválido, você está apostando mais fichas do que tem.")
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
    
        if soma_dados in [4,5,6,8,9,10]:
            print("")
            print('Você está na fase Point e para ganhar você deverá tirar o mesmo valor que tirou na soma dos dados da jogada anterior.')
            print("A soma dos seus dados foi {0}.".format(soma_dados))
    
            while True:
                dado_um_P=random.randint(1,6)
                dado_dois_P=random.randint(1,6)
                soma_dados_P = (dado_um_P + dado_dois_P)
    
                if soma_dados == soma_dados_P:
                    fichas += aposta
    
                    print("")
                    print("Você ganhou de volta as suas fichas que foram apostados, a soma dos seus dados foi {0}.".format(soma_dados))
                    print('Você tem {0} fichas agora.'.format(fichas))
                    break
    
                if soma_dados_P == 7:
                    fichas += 0
    
                    print("")
                    print('Você perdeu, a soma dos seus dados jogados pela 2° vez foi 7.')
                    print('Você tem {0} fichas agora.'.format(fichas))
                    break
    
                else:
                    print("")
                    print("Você continuará na fase Point, não ganhou nem perdeu fichas e os dados serão lançados novamente.")
                    print("A soma dos seus dados jogados pela 2° vez foi {0}.".format(soma_dados_P))
                    print("Pressione 'ENTER' para joagr o dado de novo.")
                    enter=input("Jogar dados novamente: ")
    
        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
        ficar_ou_nao=input("Opção: ")
        if ficar_ou_nao=="NÃO" or ficar_ou_nao=="NAO" or ficar_ou_nao=="Não" or ficar_ou_nao=="Nao" or ficar_ou_nao=="N" or ficar_ou_nao=="não" or ficar_ou_nao=="nao" or ficar_ou_nao=="n":
            break
        if ficar_ou_nao=="SIM" or ficar_ou_nao=="Sim" or ficar_ou_nao=="S" or ficar_ou_nao=="sim" or ficar_ou_nao=="s":
            print()     
            
        

#----------------------------------------------------------------------#
# - Modo 'Field':

    if qual_aposta == 'Field' or qual_aposta == 'field' or qual_aposta == 'FIELD':
        dado_um=random.randint(1,6)
        dado_dois=random.randint(1,6)
        soma_dados = (dado_um + dado_dois)

        aposta=int(input('Quantas fichas você vai querer apostar? '))
        while aposta > fichas:
            print("Inválido")
            aposta=int(input('Digite novamente: '))

        fichas-=aposta

        if soma_dados == 2:
            fichas += aposta*2

            print("")
            print('Você ganhou, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados == 12:
            fichas += aposta*3

            print("")
            print('Você ganhou, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados in [5,6,7,8]:
            fichas += 0

            print("")
            print('Você perdeu, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        if soma_dados in [3,4,9,10,11]:
            fichas += aposta

            print("")
            print("Você ganhou de volta as suas fichas que foram apostadas, a soma dos seus dados foi {0}.".format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
        ficar_ou_nao=input("Opção: ")
        if ficar_ou_nao=="NÃO" or ficar_ou_nao=="NAO" or ficar_ou_nao=="Não" or ficar_ou_nao=="Nao" or ficar_ou_nao=="N" or ficar_ou_nao=="não" or ficar_ou_nao=="nao" or ficar_ou_nao=="n":
            break
        if ficar_ou_nao=="SIM" or ficar_ou_nao=="Sim" or ficar_ou_nao=="S" or ficar_ou_nao=="sim" or ficar_ou_nao=="s":
            print()

#----------------------------------------------------------------------#
# - Modo 'Any Craps':

    if qual_aposta == 'Any Craps' or qual_aposta == 'Any craps' or qual_aposta == 'any craps' or qual_aposta == 'ANY CRAPS':
        dado_um=random.randint(1,6)
        dado_dois=random.randint(1,6)
        soma_dados = (dado_um + dado_dois)

        aposta=int(input('Quantas fichas você vai querer apostar? '))
        while aposta > fichas:
            print("Inválido")
            aposta=int(input('Digite novamente: '))

        fichas-=aposta

        if soma_dados in [2,3,12]:
            fichas+=aposta*7

            print("")
            print('Você ganhou, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        else:
            print("")
            print('Você perdeu, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
        ficar_ou_nao=input("Opção: ")
        if ficar_ou_nao=="NÃO" or ficar_ou_nao=="NAO" or ficar_ou_nao=="Não" or ficar_ou_nao=="Nao" or ficar_ou_nao=="N" or ficar_ou_nao=="não" or ficar_ou_nao=="nao" or ficar_ou_nao=="n":
            break
        if ficar_ou_nao=="SIM" or ficar_ou_nao=="Sim" or ficar_ou_nao=="S" or ficar_ou_nao=="sim" or ficar_ou_nao=="s":
            print()

#----------------------------------------------------------------------# 
# - Modo 'Twelve':

    if qual_aposta == 'Twelve' or qual_aposta == 'twelve' or qual_aposta == 'TWELVE' or qual_aposta=='12':
        dado_um=random.randint(1,6)
        dado_dois=random.randint(1,6)
        soma_dados = (dado_um + dado_dois)

        aposta=int(input('Quantas fichas você vai querer apostar? '))
        while aposta > fichas:
            print("Inválido")
            aposta=int(input('Digite novamente: '))

        fichas-=aposta

        if soma_dados == 12:
            fichas += aposta*30

            print("")
            print('Você ganhou, a soma dos seus dados foi 12. A quantia de fichas que você apostou foi multiplicada por 30.')
            print('Você tem {0} fichas agora.'.format(fichas))

        else:
            fichas += 0

            print("")
            print('Você perdeu, a soma dos seus dados foi {0}.'.format(soma_dados))
            print('Você tem {0} fichas agora.'.format(fichas))

        print("")
        print('A rodada acabou.')
        print("- Caso queira continuar apostando digite 'sim'.")
        print("- Caso queira parar de apostar digite 'não'.")
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
print("")        
print("")        
print("")
print("")        
print("")        
print("")
print("")        
print("")        
print("")
print("")        
print("")        
print("")
print("")        
print("")        
print("")
print("")        
print("")        
print("")
print("")        
print("")        
print("")          
         
if fichas > 0:          
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
print("OBRIGADO POR JOGAR")       
print("Feito por:") 
print("- Maria Eduarda Torres")
print("- Andressa Silva de Oliveira")
print("----------------------")
print("")
    


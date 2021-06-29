from affiche import *
from init import *
from colored import *
from case import *

reset = attr('reset')
color = fg(49)
color2= bg(115)+fg(22)
color3= fg(49)
color3bis=bg(49)
color4= fg(32)
color5= bg(29)+fg(0)
color6=fg(222)
color7=bg(222)+fg(0)

t=1 #Variable des tours
rund=1 #Variable des tours dans le module case
jeu=True #Variable pour que le jeu tourne
roundstr=str(rund) #rund mais en string


#Premier petit menu
print("\n")
print(color4+"─────────────────────────────────────────────────────────────"+reset)
demande=input(color3+"Bienvenue sur le jeu d'échec.\n- Pour jouer a deux tappez 1\n--> "+reset)
print(color4+"─────────────────────────────────────────────────────────────"+reset)
print('')
#Tant que le résultat n'est pas 1, je boucle
while demande != '1':
    print(color4+"─────────────────────────────────────────────────────────────"+reset)
    demande=input(color3+"Bienvenue sur le jeu d'échec.\n- Pour jouer a deux tappez 1\n--> "+reset)
    print(color4+"─────────────────────────────────────────────────────────────"+reset)
    print('')


#Demande des pseudos
a=0
print(color4+"─────────────────────────────────"+reset)
pseudo_1=input(color5+"Joueur 1 "+reset+color3+" : Entrez votre pseudo \n--> "+reset)
print(color4+"─────────────────────────────────"+reset)
print(" ")
print(color4+"─────────────────────────────────"+reset)
pseudo_2=input(color5+"Joueur 2 "+reset+color3+" : Entrez votre pseudo \n--> "+reset)
print(color4+"─────────────────────────────────"+reset)

#Corps du jeu, structure...
print(" ")
if demande=='1':
    while jeu == True :
        while(t<50):
            print(" ")
            roundstr=" "+str(rund)+" "
            print(color6+f"────────────────── JEU D'ECHECS : TOUR "+reset,color7+roundstr+reset,color6+f"────────────────────"+reset)
            print('\n')
            echequier()
            affichage()
            print(' ')
            victoire=deplacement(rund)
            if victoire==1 or victoire ==2 :
                if victoire==1:
                    print("")
                    print(color3bis+"                                                                                                   "+reset)
                    print(color3+"\nC'est fini ! Le roi de l'équipe noire est mort ! L'équipe blanche l'emporte ! Bravo",pseudo_2+"\n"+reset)
                    print(color3bis+"                                                                                                   "+reset)
                    print("")
                if victoire==2:
                    print("")
                    print(color3bis+"                                                                                                   "+reset)
                    print(color3+"\nC'est fini ! Le roi de l'équipe blanche est mort ! L'équipe noire l'emporte ! Bravo",pseudo_1+"\n"+reset)
                    print(color3bis+"                                                                                                   "+reset)
                    print("")
                t=50
            
            rund+=1
            t+=1
        jeu=False  #J'arrête la boucle de jeu

#Fin du jeu
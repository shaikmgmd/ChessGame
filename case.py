from affiche import *
from colored import *
from coups import *
from random import *

reset = attr('reset')
color = fg(9)

def deplacement(rund):
    
    tour=True

    while tour == True:
        
        if rund%2 == 0:
            a=0
            
            #Je récupère les coordonées de mes pièces alliés avant le déplacement des pièces
            y=0
            b=tabN[y]
            z=0
            tab_des_pos=[]
            while y < len(tabN):
                b=tabN[y]
                tab_des_pos.append(b['position'])
                y+=1
            print("")
            
            #Je récupère les coordonées de mes pièces alliés avant le déplacement des pièces
            y=0
            b=tabB[y]
            z=0
            tab_des_pos_2=[]
            while y < len(tabB):
                b=tabB[y]
                tab_des_pos_2.append(b['position'])
                y+=1

            print('────────────────────────────────────────────────────────────────')
            print("%s%s Tour de l'équipe noire %s" % (fg(15), bg(16), attr(0)))
            print('────────────────────────────────────────────────────────────────')
            print("%s%s Quelle pièce voulez vous deplacer ? %s" % (fg(15), bg(16), attr(0)))
            print('────────────────────────────────────────────────────────────────')
            chaine=str(input('%s Piece à déplacer : %s' % (fg(39), attr(0))))
            while chaine not in tab_des_pos or chaine=='':
                print('────────────────────────────────────────────────────────────────')
                print("%s Cette pièce n'est pas dans le jeu ou n'est pas dans votre équipe ou vous n'avez rien saisi, recommencez. %s" % (fg(1), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                print("%s%s Quelle pièce voulez vous deplacer ? %s" % (fg(15), bg(16), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                chaine=str(input('%s Piece à déplacer : %s' % (fg(39), attr(0))))
            print('────────────────────────────────────────────────────────────────')
            

            #Pour connaître le type de pièce, afin d'utiliser le module coups
            y=0
            b=tabN[y]
            z=0
            while y < len(tabN):
                b=tabN[y]
                if chaine == b['position']:
                    z=b['type']
                y+=1

            #On cherche a connaître le ctype de pièce, pour ensuite l'envoyer en tant que paramètre pour sa fonction dans le module coups
            if z=='♟':
                a=pions_deplacement_noir_1(chaine,z) #On envoie les variables dans le module coups
            elif z=='♜':
                a=tour_deplacement_noir(chaine,z) #On envoie les variables dans le module coups
            elif z=='♞':
                a=cavalier_deplacement_noir(chaine,z) #On envoie les variables dans le module coups
            elif z=='♝':
                a=fou_deplacement_noir(chaine,z) #On envoie les variables dans le module coups
            elif z=='♚':
                a=roi_deplacement_noir(chaine,z) #On envoie les variables dans le module coups
            elif z=='♛':
                a=dame_deplacement_noir(chaine,z) #On envoie les variables dans le module coups
      
            #Eviter de sauter les alliés pour le fou, la tour, la dame.
                #Supprimer d'abord les coordonnées impossible
            
            if z=='♜' or z=='♝' or z=='♛':
                o=0
                while o < len(a):
                    c=0
                    m=a[o]
                    while c < len(tab_des_pos):
                        n=tab_des_pos[c]
                        if m==n:
                            a.pop(o)
                        c+=1
                    o+=1
                #Maintenant, essayons de faire en sorte qu'ils ne puissent sauter les alliés

            print('────────────────────────────────────────────────────────────────')
            print("%s%s Vers où voulez vous le déplacer ? %s" % (fg(15), bg(16), attr(0)))
            print('────────────────────────────────────────────────────────────────')
            lieu=str(input('%s Déplacer vers : %s' % (fg(39), attr(0))))
            while lieu not in coordones or lieu==chaine:
                print('────────────────────────────────────────────────────────────────')
                print("%s Cette pièce n'est pas dans le jeu ou vous ne pouvez vous déplacer à la coordonée saisie car vous y êtes déjà, recommencez. %s" % (fg(1), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                print("%s%s Vers où voulez vous le déplacer ? %s" % (fg(15), bg(16), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                lieu=str(input('%s Déplacer vers : %s' % (fg(39), attr(0))))
            print('────────────────────────────────────────────────────────────────')
            while (lieu not in a) or (lieu in tab_des_pos) :
            
                print("%s Recommencez, vous pouvez aller la-bàs car ce n'est pas possible ou il y a déjà une de vos pièces. %s" % (fg(1), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                lieu=str(input('%s Déplacer vers : %s' % (fg(39), attr(0))))
                print('────────────────────────────────────────────────────────────────')

            #Deplacement du pion sur l'échequier
            i=0
            x=tabN[i]
            while i < len(tabN):
                x=tabN[i]
                if chaine==x['position']:
                    index = coordones.index(chaine)
                    ech[index]="0"
                    if lieu in tab_des_pos_2 :  
                        x2=tab_des_pos_2.index(lieu)
                        del tabB[x2]
                    x['position']=lieu
                    tabN[i] = x
                    i=len(tabN)
                else:
                    i+=1
            
             
            #Je récupère les coordonées de mes pièces alliés
            y=0
            b=tabN[y]
            z=0
            tab_des_pos=[]
            while y < len(tabN):
                b=tabN[y]
                tab_des_pos.append(b['position'])
                y+=1

            #Je récupère les types de mes pièces alliés une fois le déplacement effectué
            y=0
            b=tabN[y]
            z=0
            tab_des_types=[]
            while y < len(tabN):
                b=tabN[y]
                tab_des_types.append(b['type'])
                y+=1

            #Je récupère les types des ennemis une fois le déplacement effectué
            y=0
            b=tabB[y]
            z=0
            tab_des_types_2=[]
            while y < len(tabB):
                b=tabB[y]
                tab_des_types_2.append(b['type'])
                y+=1
            
            #On verifie si le roi est mort ou pas.

            y=0
            roi_blanc='♔'
            if roi_blanc not in tab_des_types_2 :
                gagnant=2
                return gagnant
        

        if rund%2 != 0:
            a=0
            
            #Je récupère les coordonées de mes pièces alliés avant le déplacement des pièces
            y=0
            b=tabB[y]
            z=0
            tab_des_pos=[]
            while y < len(tabB):
                b=tabB[y]
                tab_des_pos.append(b['position'])
                y+=1

            print("")
            #Je récupère les coordonées de mes pièces ennemi avant le déplacement des pièces
            y=0
            b=tabN[y]
            z=0
            tab_des_pos_2=[]
            while y < len(tabN):
                b=tabN[y]
                tab_des_pos_2.append(b['position'])
                y+=1            
            
            print('────────────────────────────────────────────────────────────────')
            print("%s%s Tour de l'équipe blanche %s" % (fg(16), bg(15), attr(0)))
            print('────────────────────────────────────────────────────────────────')
            print("%s%s Quelle pièce voulez vous deplacer ? %s" % (fg(16), bg(15), attr(0)))
            print('────────────────────────────────────────────────────────────────')
            chaine=str(input('%s Piece à déplacer : %s' % (fg(39), attr(0))))
            while chaine not in tab_des_pos or chaine=='':
                print('────────────────────────────────────────────────────────────────')
                print("%s Cette pièce n'est pas dans le jeu ou n'est pas dans votre équipe ou vous n'avez rien saisi, recommencez. %s" % (fg(1), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                print("%s%s Quelle pièce voulez vous deplacer ? %s" % (fg(16), bg(15), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                chaine=str(input('%s Piece à déplacer : %s' % (fg(39), attr(0))))
            print('────────────────────────────────────────────────────────────────')
            

            #Pour connaître le type de pièce, afin d'utiliser le module coups
            y=0
            b=tabB[y]
            z=0
            while y < len(tabB):
                b=tabB[y]
                if chaine == b['position']:
                    z=b['type']
                y+=1

            #On cherche a connaître le ctype de pièce, pour ensuite l'envoyer en tant que paramètre pour sa fonction dans le module coups
            if z=='♙':
                a=pions_deplacement_blanc_1(chaine,z) #On envoie les variables dans le module coups
            elif z=='♖':
                a=tour_deplacement_blanc(chaine,z) #On envoie les variables dans le module coups
            elif z=='♘':
                a=cavalier_deplacement_blanc(chaine,z) #On envoie les variables dans le module coups
            elif z=='♗':
                a=fou_deplacement_blanc(chaine,z) #On envoie les variables dans le module coups
            elif z=='♔':
                a=roi_deplacement_blanc(chaine,z) #On envoie les variables dans le module coups
            elif z=='♕':
                a=dame_deplacement_blanc(chaine,z) #On envoie les variables dans le module coups

            #Eviter de sauter les alliés pour le fou, la tour, la dame.
                #Supprimer d'abord les coordonnées impossible
            
            if z=='♖' or z=='♗' or z=='♕':
                o=0
                while o < len(a):
                    c=0
                    m=a[o]
                    while c < len(tab_des_pos):
                        n=tab_des_pos[c]
                        if m==n:
                            a.pop(o)
                        c+=1
                    o+=1
                #Maintenant, essayons de faire en sorte qu'ils ne puissent sauter les alliés


            print('────────────────────────────────────────────────────────────────')
            print("%s%s Vers où voulez vous le déplacer ? %s" % (fg(16), bg(15), attr(0)))
            print('────────────────────────────────────────────────────────────────')
            lieu=str(input('%s Déplacer vers : %s' % (fg(39), attr(0))))
            while lieu not in coordones or lieu==chaine:
                print('────────────────────────────────────────────────────────────────')
                print("%s Cette pièce n'est pas dans le jeu ou vous ne pouvez vous déplacer à la coordonée saisie car vous y êtes déjà, recommencez. %s" % (fg(1), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                print("%s%s Vers où voulez vous le déplacer ? %s" % (fg(15), bg(15), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                lieu=str(input('%s Déplacer vers : %s' % (fg(39), attr(0))))
            print('────────────────────────────────────────────────────────────────')
            while (lieu not in a) or (lieu in tab_des_pos)  :
                print("%s Recommencez, vous ne pouvez pas aller la-bàs car ce n'est pas possible ou il y a déjà une de vos pièces. %s" % (fg(1), attr(0)))
                print('────────────────────────────────────────────────────────────────')
                lieu=str(input('%s Déplacer vers : %s' % (fg(39), attr(0))))
                print('────────────────────────────────────────────────────────────────')

            #Deplacement du pion sur l'échequier
            i=0
            
            x=tabB[i]
            
            while i < len(tabB):
                x=tabB[i]
                if chaine==x['position']:
                    index = coordones.index(chaine)
                    ech[index]="0"
                    if lieu in tab_des_pos_2 :
                        x2= tab_des_pos_2.index(lieu)
                        del tabN[x2]
                    x['position']=lieu
                    tabB[i] = x
                    i=len(tabB)
                else:
                    i+=1
 
            
            #Je récupère les coordonées de mes pièces alliés une fois le déplacement effectué
            y=0
            b=tabB[y]
            z=0
            tab_des_pos=[]
            while y < len(tabB):
                b=tabB[y]
                tab_des_pos.append(b['position'])
                y+=1

            #Je récupère les types de mes pièces alliés une fois le déplacement effectué
            y=0
            b=tabB[y]
            z=0
            tab_des_types=[]
            while y < len(tabB):
                b=tabB[y]
                tab_des_types.append(b['type'])
                y+=1
            
            #Je récupère les types des pièces ennemies une fois le déplacement effectué
            y=0
            b=tabN[y]
            z=0
            tab_des_types_2=[]
            while y < len(tabN):
                b=tabN[y]
                tab_des_types_2.append(b['type'])
                y+=1

            #On verifie si le roi est mort ou pas.
            y=0
            roi_noir='♚'
            if roi_noir not in tab_des_types_2 :
                gagnant=1
                return gagnant
            
        rund+=1
        tour=False

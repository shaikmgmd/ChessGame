from init import *

reset = attr('reset')
color = fg(222)
color2 = fg(39)
color3= fg(198)
color4=fg(240)
color5=fg(231)
color6=fg(8)

#Fonction qui va afficher le tableau ech[] du module init sous forme d'échequier
def affichage():

    #Faire la première ligne avec a,b,c,d,e,f,g,h (couleurs+barres)
    i=0
    ligne=color+'   │'+reset
    while i < 8 :
        ligne=ligne+color2+chr(97+i).rjust(3).ljust(6)+reset+color+"│"+reset
        i+=1
    print(ligne)

    #Afficher les pièces des deux équipes avec des couleurs différentes avec les barres + les chiffres
    i=0
    x=0
    ligne=''
    t=0
    a=""
    while i < 8:
        j=0
        print('%s────────────────────────────────────────────────────────────────%s' % (fg(222), attr(0)))
        ligne=color3+chr(56-i).ljust(3)+reset+color+"│"+reset
        while j < 8 :
            if ech[t]=="0":
                ligne=ligne+a.rjust(3).ljust(6)+color+"│"+reset
            elif ech[t]=='♖' or ech[t]=='♘' or ech[t]=='♗' or ech[t]=='♕' or ech[t]=='♔' or ech[t]=='♙':
                ligne=ligne+color5+ech[t].rjust(3).ljust(6)+reset+color+"│"+reset
            elif ech[t]=='♜' or ech[t]=='♞' or ech[t]=='♝' or ech[t]=='♛' or ech[t]=='♚' or ech[t]=='♟':
                ligne=ligne+color6+ech[t].rjust(3).ljust(6)+reset+color+"│"+reset
            t+=1
            j+=1
        print(ligne+color3+chr(56-i).rjust(3)+reset)
        i+=1
    
    #Faire la première ligne avec a,b,c,d,e,f,g,h (couleurs+barres)
    print('%s────────────────────────────────────────────────────────────────%s' % (fg(222), attr(0)))
    ligne=color+'   │'+reset
    i=0
    while i < 8 :
        ligne=ligne+color2+chr(97+i).rjust(3).ljust(6)+reset+color+"│"+reset
        i+=1
    print(ligne)
    
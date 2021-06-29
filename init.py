from colored import *

res = attr('reset')
color=fg(240)
color1=fg(231)
color2=fg(8)


#Tableau des pièces/coordonnées initiales/deplacements de l'équipe blanche
tabB=[{'type':'♖','position':'a1','deplacement':[]},
      {'type':'♘','position':'b1','deplacement':[]},
      {'type':'♗','position':'c1','deplacement':[]},
      {'type':'♕','position':'d1','deplacement':[]},
      {'type':'♔','position':'e1','deplacement':[]},
      {'type':'♗','position':'f1','deplacement':[]},
      {'type':'♘','position':'g1','deplacement':[]},
      {'type':'♖','position':'h1','deplacement':[]},
      {'type':'♙','position':'a2','deplacement':[]},
      {'type':'♙','position':'b2','deplacement':[]},
      {'type':'♙','position':'c2','deplacement':[]},
      {'type':'♙','position':'d2','deplacement':[]},
      {'type':'♙','position':'e2','deplacement':[]},
      {'type':'♙','position':'f2','deplacement':[]},
      {'type':'♙','position':'g2','deplacement':[]},
      {'type':'♙','position':'h2','deplacement':[]}]


#Tableau des pièces/coordonnées initiales/deplacements de l'équipe noire
tabN=[{'type':'♜','position':'a8','deplacement':[]},
      {'type':'♞','position':'b8','deplacement':[]},
      {'type':'♝','position':'c8','deplacement':[]},
      {'type':'♛','position':'d8','deplacement':[]},
      {'type':'♚','position':'e8','deplacement':[]},
      {'type':'♝','position':'f8','deplacement':[]},
      {'type':'♞','position':'g8','deplacement':[]},
      {'type':'♜','position':'h8','deplacement':[]},
      {'type':'♟','position':'a7','deplacement':[]},
      {'type':'♟','position':'b7','deplacement':[]},
      {'type':'♟','position':'c7','deplacement':[]},
      {'type':'♟','position':'d7','deplacement':[]},
      {'type':'♟','position':'e7','deplacement':[]},
      {'type':'♟','position':'f7','deplacement':[]},
      {'type':'♟','position':'g7','deplacement':[]},
      {'type':'♟','position':'h7','deplacement':[]}]


#Tableaux des coordonées possibles dans l'échequier --> aussi utilisée dans le module case pour boucler 
coordones=["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", 
           "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
           "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", 
           "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
           "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
           "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
           "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
           "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]


#Tableau de l'échequier initiale
ech=['0']*64


#Fonction qui permet de placer les pièces dans le tableau ech[]
def echequier():
    
    #On remplit avec les pièces de l'équipe noire
    i=0
    while i < len(tabN):
         x=tabN[i]
         i2=0
         coordo='0'
         while i2 < len(coordones):
             coordo=coordones[i2]
             if coordo == x['position']:
                 ech[i2]=x['type']
                 i2=len(coordones)
             else:
                 i2+=1
         i+=1
    
    #On remplit avec les pièces de l'équipe blanche
    i=0
    while i < len(tabB):
         x=tabB[i]
         i2=0
         coordo='0'
         while i2 < len(coordones):
             coordo=coordones[i2]
             if coordo == x['position']:
                 ech[i2]=x['type']
                 i2=len(coordones)
             else:
                 i2+=1
         i+=1
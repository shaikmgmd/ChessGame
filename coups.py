from init import *

reset = attr('reset')
color = fg(222)

#Déplacements pour les pions | Pour le tour 1, ils peuvent avancer de 2 cases.
def pions_deplacement_blanc_1(coord_b,piece):
    if coord_b=="a2" and piece=='♙':
        tab_p=['a3','a4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b2" and piece=='♙':
        tab_p=['b3','b4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c2" and piece=='♙':
        tab_p=['c3','c4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d2" and piece=='♙':
        tab_p=['d3','d4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p    
    if coord_b=="e2" and piece=='♙':
        tab_p=['e3','e4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g2" and piece=='♙':
        tab_p=['g3','g4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h2" and piece=='♙':
        tab_p=['h3','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a3" and piece=='♙':
        tab_p=['a4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a4" and piece=='♙':
        tab_p=['a5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a5" and piece=='♙':
        tab_p=['a6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a6" and piece=='♙':
        tab_p=['a7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a7" and piece=='♙':
        tab_p=['a8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b3" and piece=='♙':
        tab_p=['b4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b4" and piece=='♙':
        tab_p=['b5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b5" and piece=='♙':
        tab_p=['b6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b6" and piece=='♙':
        tab_p=['b7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b7" and piece=='♙':
        
        tab_p=['b8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c3" and piece=='♙':
        
        tab_p=['c4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c4" and piece=='♙':
        
        tab_p=['c5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c5" and piece=='♙':
        
        tab_p=['c6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c6" and piece=='♙':
        
        tab_p=['c7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c7" and piece=='♙':
        
        tab_p=['c8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d3" and piece=='♙':
        
        tab_p=['d4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d4" and piece=='♙':
        
        tab_p=['d5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d5" and piece=='♙':
        
        tab_p=['d6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d6" and piece=='♙':
        
        tab_p=['d7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d7" and piece=='♙':
        
        tab_p=['d8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e3" and piece=='♙':
        
        tab_p=['e4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e4" and piece=='♙':
        
        tab_p=['e5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e5" and piece=='♙':
        
        tab_p=['e6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e6" and piece=='♙':
        
        tab_p=['e7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e7" and piece=='♙':
        
        tab_p=['e8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f3" and piece=='♙':
        
        tab_p=['f4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f4" and piece=='♙':
        
        tab_p=['f5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f5" and piece=='♙':
        
        tab_p=['f6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f6" and piece=='♙':
        
        tab_p=['f7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f7" and piece=='♙':
        
        tab_p=['f8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g3" and piece=='♙':
        
        tab_p=['g4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g4" and piece=='♙':
        
        tab_p=['g5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g5" and piece=='♙':
        
        tab_p=['g6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g6" and piece=='♙':
        
        tab_p=['g7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g7" and piece=='♙':
        
        tab_p=['g8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h3" and piece=='♙':
        
        tab_p=['h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h4" and piece=='♙':
        
        tab_p=['h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h5" and piece=='♙':
        
        tab_p=['h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h6" and piece=='♙':
        
        tab_p=['h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h7" and piece=='♙':
        
        tab_p=['h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p

def pions_deplacement_noir_1(coord_n,piece):
    if coord_n=="a7" and piece=='♟':
        tab_p=['a6','a5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b7" and piece=='♟':
        tab_p=['b6','b5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c7" and piece=='♟':
        tab_p=['c6','c5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d7" and piece=='♟':
        tab_p=['d6','d5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p    
    if coord_n=="e7" and piece=='♟':
        tab_p=['e6','e5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f7" and piece=='♟':
        tab_p=['f6','f5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g7" and piece=='♟':
        tab_p=['g6','g5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h7" and piece=='♟':
        tab_p=['h6','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a6" and piece=='♟':    
        tab_p=['a5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a5" and piece=='♟':
        tab_p=['a4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a4" and piece=='♟':
        tab_p=['a3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a3" and piece=='♟':
        tab_p=['a2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a2" and piece=='♟':
        tab_p=['a1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b6" and piece=='♟':
        tab_p=['b5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b5" and piece=='♟':
        tab_p=['b4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b4" and piece=='♟':
        tab_p=['b3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b3" and piece=='♟':
        tab_p=['b2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b2" and piece=='♟':
        tab_p=['b1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c6" and piece=='♟':
        tab_p=['c5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c5" and piece=='♟':
        tab_p=['c4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c4" and piece=='♟':
        tab_p=['c3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c3" and piece=='♟':
        tab_p=['c2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c2" and piece=='♟':
        tab_p=['c1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d6" and piece=='♟':
        tab_p=['d5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d5" and piece=='♟':
        tab_p=['d4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d4" and piece=='♟':
        tab_p=['d3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d3" and piece=='♟':
        tab_p=['d2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d2" and piece=='♟':
        tab_p=['d1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e6" and piece=='♟':
        tab_p=['e5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e5" and piece=='♟':
        tab_p=['e4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e4" and piece=='♟':
        tab_p=['e3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e3" and piece=='♟':
        tab_p=['e2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e2" and piece=='♟':
        tab_p=['e1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f6" and piece=='♟':
        tab_p=['f5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f5" and piece=='♟':
        tab_p=['f4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f4" and piece=='♟':
        tab_p=['f3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f3" and piece=='♟':
        tab_p=['f2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f2" and piece=='♟':
        tab_p=['f1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g6" and piece=='♟':
        tab_p=['g5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g5" and piece=='♟':
        tab_p=['g4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g4" and piece=='♟':
        tab_p=['g3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g3" and piece=='♟':
        tab_p=['g2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g2" and piece=='♟':
        tab_p=['g1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h6" and piece=='♟':
        tab_p=['h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h5" and piece=='♟':
        tab_p=['h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h4" and piece=='♟':
        tab_p=['h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h3" and piece=='♟':
        tab_p=['h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h2" and piece=='♟':
        tab_p=['h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p

#La tour | Déplacements de la tour
def tour_deplacement_noir(coord_n,piece):
    if coord_n=="a8" and piece=='♜':
        tab_p=['a7','a6','a5','a4','a3','a2','a1','b8','c8','d8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a7" and piece=='♜':
        tab_p=['a8','a6','a5','a4','a3','a2','a1','b7','c7','d7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a6" and piece=='♜':
        tab_p=['a8','a7','a5','a4','a3','a2','a1','b6','c6','d6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a5" and piece=='♜':
        tab_p=['a8','a7','a6','a4','a3','a2','a1','b5','c5','d5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a4" and piece=='♜':
        tab_p=['a8','a7','a6','a5','a3','a2','a1','b4','c4','d4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a3" and piece=='♜':
        tab_p=['a8','a7','a6','a5','a4','a2','a1','b3','c3','d3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a2" and piece=='♜':
        tab_p=['a8','a7','a6','a5','a4','a3','a1','b2','c2','d2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="a1" and piece=='♜':
        tab_p=['a8','a7','a6','a5','a4','a3','a2','b1','c1','d1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b8" and piece=='♜':
        tab_p=['b7','b6','b5','b4','b3','b2','b1','a8','c8','d8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b7" and piece=='♜':
        tab_p=['b8','b6','b5','b4','b3','b2','b1','a7','c7','d7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b6" and piece=='♜':
        tab_p=['b8','b7','b5','b4','b3','b2','b1','a6','c6','d6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b5" and piece=='♜':
        tab_p=['b8','b7','b6','b4','b3','b2','b1','a5','c5','d5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b4" and piece=='♜':
        tab_p=['b8','b7','b6','b5','b3','b2','b1','a4','c4','d4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b3" and piece=='♜':
        tab_p=['b8','b7','b6','b5','b4','b2','b1','a3','c3','d3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b2" and piece=='♜':
        tab_p=['b8','b7','b6','b5','b4','b3','b1','a2','c2','d2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="b1" and piece=='♜':
        tab_p=['b8','b7','b6','b5','b4','b3','b2','a1','c1','d1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c8" and piece=='♜':
        tab_p=['c7','c6','c5','c4','c3','c2','c1','a8','b8','d8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c7" and piece=='♜':
        tab_p=['c8','c6','c5','c4','c3','c2','c1','a7','b7','d7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c6" and piece=='♜':
        tab_p=['c8','c7','c5','c4','c3','c2','c1','a6','b6','d6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c5" and piece=='♜':
        tab_p=['c8','c7','c6','c4','c3','c2','c1','a5','b5','d5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c4" and piece=='♜':
        tab_p=['c8','c7','c6','c5','c3','c2','c1','a4','b4','d4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c3" and piece=='♜':
        tab_p=['c8','c7','c6','c5','c4','c2','c1','a3','b3','d3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c2" and piece=='♜':
        tab_p=['c8','c7','c6','c5','c4','c3','c1','a2','b2','d2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="c1" and piece=='♜':
        tab_p=['c8','c7','c6','c5','c4','c3','c2','a1','b1','d1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d8" and piece=='♜':
        tab_p=['d7','d6','d5','d4','d3','d2','d1','a8','b8','c8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d7" and piece=='♜':
        tab_p=['d8','d6','d5','d4','d3','d2','d1','a7','b7','c7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d6" and piece=='♜':
        tab_p=['d8','d7','d5','d4','d3','d2','d1','a6','b6','c6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d5" and piece=='♜':
        tab_p=['d8','d7','d6','d4','d3','d2','d1','a5','b5','c5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d4" and piece=='♜':
        tab_p=['d8','d7','d6','d5','d3','d2','d1','a4','b4','c4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d3" and piece=='♜':
        tab_p=['d8','d7','d6','d5','d4','d2','d1','a3','b3','c3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d2" and piece=='♜':
        tab_p=['d8','d7','d6','d5','d4','d3','d1','a2','b2','c2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="d1" and piece=='♜':
        tab_p=['d8','d7','d6','d5','d4','d3','d2','a1','b1','c1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e8" and piece=='♜':
        tab_p=['e7','e6','e5','e4','e3','e2','e1','a8','b8','c8','d8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e7" and piece=='♜':
        tab_p=['e8','e6','e5','e4','e3','e2','e1','a7','b7','c7','d7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e6" and piece=='♜':
        tab_p=['e8','e7','e5','e4','e3','e2','e1','a6','b6','c6','d6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e5" and piece=='♜':
        tab_p=['e8','e7','e6','e4','e3','e2','e1','a5','b5','c5','d5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e4" and piece=='♜':
        tab_p=['e8','e7','e6','e5','e3','e2','e1','a4','b4','c4','d4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e3" and piece=='♜':
        tab_p=['e8','e7','e6','e5','e4','e2','e1','a3','b3','c3','d3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e2" and piece=='♜':
        tab_p=['e8','e7','e6','e5','e4','e3','e1','a2','b2','c2','d2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="e1" and piece=='♜':
        tab_p=['e8','e7','e6','e5','e4','e3','e2','a1','b1','c1','d1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f8" and piece=='♜':
        tab_p=['f7','f6','f5','f4','f3','f2','f1','a8','b8','c8','d8','e8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f7" and piece=='♜':
        tab_p=['f8','f6','f5','f4','f3','f2','f1','a7','b7','c7','d7','e7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f6" and piece=='♜':
        tab_p=['f8','f7','f5','f4','f3','f2','f1','a6','b6','c6','d6','e6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f5" and piece=='♜':
        tab_p=['f8','f7','f6','f4','f3','f2','f1','a5','b5','c5','d5','e5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f4" and piece=='♜':
        tab_p=['f8','f7','f6','f5','f3','f2','f1','a4','b4','c4','d4','e4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f3" and piece=='♜':
        tab_p=['f8','f7','f6','f5','f4','f2','f1','a3','b3','c3','d3','e3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f2" and piece=='♜':
        tab_p=['f8','f7','f6','f5','f4','f3','f1','a2','b2','c2','d2','e2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="f1" and piece=='♜':
        tab_p=['f8','f7','f6','f5','f4','f3','f2','a1','b1','c1','d1','e1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g8" and piece=='♜':
        tab_p=['g7','g6','g5','g4','g3','g2','g1','a8','b8','c8','d8','e8','f8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g7" and piece=='♜':
        tab_p=['g8','g6','g5','g4','g3','g2','g1','a7','b7','c7','d7','e7','f7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g6" and piece=='♜':
        tab_p=['g8','g7','g5','g4','g3','g2','g1','a7','b6','c6','d6','e6','f6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g5" and piece=='♜':
        tab_p=['g8','g7','g6','g4','g3','g2','g1','a5','b5','c5','d5','e5','f5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g4" and piece=='♜':
        tab_p=['g8','g7','g6','g5','g3','g2','g1','a4','b4','c4','d4','e4','f4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g3" and piece=='♜':
        tab_p=['g8','g7','g6','g5','g4','g2','g1','a3','b3','c3','d3','e3','f3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g2" and piece=='♜':
        tab_p=['g8','g7','g6','g5','g4','g3','g1','a2','b2','c2','d2','e2','f2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="g1" and piece=='♜':
        tab_p=['g8','g7','g6','g5','g4','g3','g2','a1','b1','c1','d1','e1','f1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h8" and piece=='♜':
        tab_p=['h7','h6','h5','h4','h3','h2','h1','a8','b8','c8','d8','e8','f8','g8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h7" and piece=='♜':
        tab_p=['h8','h6','h5','h4','h3','h2','h1','a7','b7','c7','d7','e7','f7','g7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h6" and piece=='♜':
        tab_p=['h8','h7','h5','h4','h3','h2','h1','a6','b6','c6','d6','e6','f6','g6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h5" and piece=='♜':
        tab_p=['h8','h7','h6','h4','h3','h2','h1','a5','b5','c5','d5','e5','f5','g5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h4" and piece=='♜':
        tab_p=['h8','h7','h6','h5','h3','h2','h1','a4','b4','c4','d4','e4','f4','g4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h3" and piece=='♜':
        tab_p=['h8','h7','h6','h5','h4','h2','h1','a3','b3','c3','d3','e3','f3','g3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h2" and piece=='♜':
        tab_p=['h8','h7','h6','h5','h4','h3','h1','a2','b2','c2','d2','e2','f2','g2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_n=="h1" and piece=='♜':
        tab_p=['h8','h7','h6','h5','h4','h3','h2','a1','b1','c1','d1','e1','f1','g1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    
def tour_deplacement_blanc(coord_b,piece):
    if coord_b=="a8" and piece=='♖':
        tab_p=['a7','a6','a5','a4','a3','a2','a1','b8','c8','d8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a7" and piece=='♖':
        tab_p=['a8','a6','a5','a4','a3','a2','a1','b7','c7','d7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a6" and piece=='♖':
        tab_p=['a8','a7','a5','a4','a3','a2','a1','b6','c6','d6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a5" and piece=='♖':
        tab_p=['a8','a7','a6','a4','a3','a2','a1','b5','c5','d5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a4" and piece=='♖':
        tab_p=['a8','a7','a6','a5','a3','a2','a1','b4','c4','d4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a3" and piece=='♖':
        tab_p=['a8','a7','a6','a5','a4','a2','a1','b3','c3','d3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a2" and piece=='♖':
        tab_p=['a8','a7','a6','a5','a4','a3','a1','b2','c2','d2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="a1" and piece=='♖':
        tab_p=['a8','a7','a6','a5','a4','a3','a2','b1','c1','d1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b8" and piece=='♖':
        tab_p=['b7','b6','b5','b4','b3','b2','b1','a8','c8','d8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b7" and piece=='♖':
        tab_p=['b8','b6','b5','b4','b3','b2','b1','a7','c7','d7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b6" and piece=='♖':
        tab_p=['b8','b7','b5','b4','b3','b2','b1','a6','c6','d6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b5" and piece=='♖':
        tab_p=['b8','b7','b6','b4','b3','b2','b1','a5','c5','d5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b4" and piece=='♖':
        tab_p=['b8','b7','b6','b5','b3','b2','b1','a4','c4','d4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b3" and piece=='♖':
        tab_p=['b8','b7','b6','b5','b4','b2','b1','a3','c3','d3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b2" and piece=='♖':
        tab_p=['b8','b7','b6','b5','b4','b3','b1','a2','c2','d2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="b1" and piece=='♖':
        tab_p=['b8','b7','b6','b5','b4','b3','b2','a1','c1','d1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c8" and piece=='♖':
        tab_p=['c7','c6','c5','c4','c3','c2','c1','a8','b8','d8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c7" and piece=='♖':
        tab_p=['c8','c6','c5','c4','c3','c2','c1','a7','b7','d7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c6" and piece=='♖':
        tab_p=['c8','c7','c5','c4','c3','c2','c1','a6','b6','d6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c5" and piece=='♖':
        tab_p=['c8','c7','c6','c4','c3','c2','c1','a5','b5','d5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c4" and piece=='♖':
        tab_p=['c8','c7','c6','c5','c3','c2','c1','a4','b4','d4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c3" and piece=='♖':
        tab_p=['c8','c7','c6','c5','c4','c2','c1','a3','b3','d3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c2" and piece=='♖':
        tab_p=['c8','c7','c6','c5','c4','c3','c1','a2','b2','d2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="c1" and piece=='♖':
        tab_p=['c8','c7','c6','c5','c4','c3','c2','a1','b1','d1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d8" and piece=='♖':
        tab_p=['d7','d6','d5','d4','d3','d2','d1','a8','b8','c8','e8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d7" and piece=='♖':
        tab_p=['d8','d6','d5','d4','d3','d2','d1','a7','b7','c7','e7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d6" and piece=='♖':
        tab_p=['d8','d7','d5','d4','d3','d2','d1','a6','b6','c6','e6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d5" and piece=='♖':
        tab_p=['d8','d7','d6','d4','d3','d2','d1','a5','b5','c5','e5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d4" and piece=='♖':
        tab_p=['d8','d7','d6','d5','d3','d2','d1','a4','b4','c4','e4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d3" and piece=='♖':
        tab_p=['d8','d7','d6','d5','d4','d2','d1','a3','b3','c3','e3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d2" and piece=='♖':
        tab_p=['d8','d7','d6','d5','d4','d3','d1','a2','b2','c2','e2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="d1" and piece=='♖':
        tab_p=['d8','d7','d6','d5','d4','d3','d2','a1','b1','c1','e1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e8" and piece=='♖':
        tab_p=['e7','e6','e5','e4','e3','e2','e1','a8','b8','c8','d8','f8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e7" and piece=='♖':
        tab_p=['e8','e6','e5','e4','e3','e2','e1','a7','b7','c7','d7','f7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e6" and piece=='♖':
        tab_p=['e8','e7','e5','e4','e3','e2','e1','a6','b6','c6','d6','f6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e5" and piece=='♖':
        tab_p=['e8','e7','e6','e4','e3','e2','e1','a5','b5','c5','d5','f5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e4" and piece=='♖':
        tab_p=['e8','e7','e6','e5','e3','e2','e1','a4','b4','c4','d4','f4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e3" and piece=='♖':
        tab_p=['e8','e7','e6','e5','e4','e2','e1','a3','b3','c3','d3','f3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e2" and piece=='♖':
        tab_p=['e8','e7','e6','e5','e4','e3','e1','a2','b2','c2','d2','f2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="e1" and piece=='♖':
        tab_p=['e8','e7','e6','e5','e4','e3','e2','a1','b1','c1','d1','f1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f8" and piece=='♖':
        tab_p=['f7','f6','f5','f4','f3','f2','f1','a8','b8','c8','d8','e8','g8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f7" and piece=='♖':
        tab_p=['f8','f6','f5','f4','f3','f2','f1','a7','b7','c7','d7','e7','g7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f6" and piece=='♖':
        tab_p=['f8','f7','f5','f4','f3','f2','f1','a6','b6','c6','d6','e6','g6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f5" and piece=='♖':
        tab_p=['f8','f7','f6','f4','f3','f2','f1','a5','b5','c5','d5','e5','g5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f4" and piece=='♖':
        tab_p=['f8','f7','f6','f5','f3','f2','f1','a4','b4','c4','d4','e4','g4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f3" and piece=='♖':
        tab_p=['f8','f7','f6','f5','f4','f2','f1','a3','b3','c3','d3','e3','g3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f2" and piece=='♖':
        tab_p=['f8','f7','f6','f5','f4','f3','f1','a2','b2','c2','d2','e2','g2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="f1" and piece=='♖':
        tab_p=['f8','f7','f6','f5','f4','f3','f2','a1','b1','c1','d1','e1','g1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g8" and piece=='♖':
        tab_p=['g7','g6','g5','g4','g3','g2','g1','a8','b8','c8','d8','e8','f8','h8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g7" and piece=='♖':
        tab_p=['g8','g6','g5','g4','g3','g2','g1','a7','b7','c7','d7','e7','f7','h7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g6" and piece=='♖':
        tab_p=['g8','g7','g5','g4','g3','g2','g1','a7','b6','c6','d6','e6','f6','h6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g5" and piece=='♖':
        tab_p=['g8','g7','g6','g4','g3','g2','g1','a5','b5','c5','d5','e5','f5','h5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g4" and piece=='♖':
        tab_p=['g8','g7','g6','g5','g3','g2','g1','a4','b4','c4','d4','e4','f4','h4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g3" and piece=='♖':
        tab_p=['g8','g7','g6','g5','g4','g2','g1','a3','b3','c3','d3','e3','f3','h3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g2" and piece=='♖':
        tab_p=['g8','g7','g6','g5','g4','g3','g1','a2','b2','c2','d2','e2','f2','h2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="g1" and piece=='♖':
        tab_p=['g8','g7','g6','g5','g4','g3','g2','a1','b1','c1','d1','e1','f1','h1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h8" and piece=='♖':
        tab_p=['h7','h6','h5','h4','h3','h2','h1','a8','b8','c8','d8','e8','f8','g8']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h7" and piece=='♖':
        tab_p=['h8','h6','h5','h4','h3','h2','h1','a7','b7','c7','d7','e7','f7','g7']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h6" and piece=='♖':
        tab_p=['h8','h7','h5','h4','h3','h2','h1','a6','b6','c6','d6','e6','f6','g6']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h5" and piece=='♖':
        tab_p=['h8','h7','h6','h4','h3','h2','h1','a5','b5','c5','d5','e5','f5','g5']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h4" and piece=='♖':
        tab_p=['h8','h7','h6','h5','h3','h2','h1','a4','b4','c4','d4','e4','f4','g4']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h3" and piece=='♖':
        tab_p=['h8','h7','h6','h5','h4','h2','h1','a3','b3','c3','d3','e3','f3','g3']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h2" and piece=='♖':
        tab_p=['h8','h7','h6','h5','h4','h3','h1','a2','b2','c2','d2','e2','f2','g2']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p
    if coord_b=="h1" and piece=='♖':
        tab_p=['h8','h7','h6','h5','h4','h3','h2','a1','b1','c1','d1','e1','f1','g1']
        print(color+f"Allez en : {' ou '.join(tab_p)}"+reset)
        return tab_p

#Roi | Déplacement du roi
def roi_deplacement_blanc(coordo_rb,piece_rb):

    if coordo_rb=="h1" and piece_rb=='♔':
        tab_p=['h2','g1','g2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb=="g1" and piece_rb=='♔':
        tab_p=['h1','f1','g2','h2','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb=="f1" and piece_rb=='♔':
        tab_p=['g1','e1','f2','g2','e2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb=="e1" and piece_rb=='♔':
        tab_p=['e2','f1','d1','f2','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d1" and piece_rb == '♔':
        tab_p = ['d2', 'e1', 'c1','e2','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c1" and piece_rb == '♔':
        tab_p = ['c2', 'd1', 'b1','b2','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b1" and piece_rb == '♔':
        tab_p = ['b2', 'c1', 'a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a1" and piece_rb == '♔':
        tab_p = ['a2', 'b1','b2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h2" and piece_rb == '♔':
        tab_p = ['h3', 'g2', 'g3','h1','g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h2" and piece_rb == '♔':
        tab_p = ['h3', 'g2', 'g3','h1','g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "g2" and piece_rb == '♔':
        tab_p = ['h2', 'h3', 'g3','f3','f2','f1','c1','h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "f2" and piece_rb == '♔':
        tab_p = ['g1', 'g2', 'g3','f3','e1','e2','e3','f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "e2" and piece_rb == '♔':
        tab_p = ['f1', 'f2', 'f3','e3','d1','d2','d3','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d2" and piece_rb == '♔':
        tab_p = ['e1', 'e2', 'e3','c1','c2','c3','d1','d3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c2" and piece_rb == '♔':
        tab_p = ['d1', 'd2', 'd3','b1','b2','b3','c3','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b2" and piece_rb == '♔':
        tab_p = ['c1', 'c2', 'c3','b3','b1','a1','a2','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a2" and piece_rb == '♔':
        tab_p = ['a1', 'a3', 'b1','b2','b3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h3" and piece_rb == '♔':
        tab_p = ['h4', 'h2', 'g2','g3','g4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "g3" and piece_rb == '♔':
        tab_p = ['g2', 'g4', 'f2','f3','f4','h2','h3','h4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "f3" and piece_rb == '♔':
        tab_p = ['f4', 'f2', 'g2','g3','g4','e2','e3','e4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "e3" and piece_rb == '♔':
        tab_p = ['e4', 'e2', 'f2','f3','f4','d2','d3','d4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d3" and piece_rb == '♔':
        tab_p = ['d4', 'd2', 'e2','e3','e4','c2','c3','c4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c3" and piece_rb == '♔':
        tab_p = ['c4', 'c2', 'd2','d3','d4','b2','b3','b4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b3" and piece_rb == '♔':
        tab_p = ['b4', 'b2', 'c2','c3','c4','a2','a3','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a3" and piece_rb == '♔':
        tab_p = ['a4', 'a2', 'b2','b3','b4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h4" and piece_rb == '♔':
        tab_p = ['h3', 'h5', 'g3','g4','g5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "g4" and piece_rb == '♔':
        tab_p = ['g5', 'g3', 'h3','h4','h5','f3','f4','f5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "f4" and piece_rb == '♔':
        tab_p = ['f5', 'f3', 'g3','g4','g5','e3','e4','e5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "e4" and piece_rb == '♔':
        tab_p = ['e5', 'e3', 'f3','f4','f5','d3','d4','d5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d4" and piece_rb == '♔':
        tab_p = ['d5', 'd3', 'e3','e4','e5','c3','c4','c5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c4" and piece_rb == '♔':
        tab_p = ['c5', 'c3', 'd3','d4','d5','b3','b4','b5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b4" and piece_rb == '♔':
        tab_p = ['b5', 'b3', 'c3','c4','c5','a3','a4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a4" and piece_rb == '♔':
        tab_p = ['a5', 'a3', 'b3','b4','b5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h5" and piece_rb == '♔':
        tab_p = ['h6', 'h4', 'g4','g5','g6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "g5" and piece_rb == '♔':
        tab_p = ['g4', 'g6', 'h4','h5','h6','f4','f5','f6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "f5" and piece_rb == '♔':
        tab_p = ['f4', 'f6', 'g4','g5','g6','e4','e5','e6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "e5" and piece_rb == '♔':
        tab_p = ['e4', 'e6', 'f4','f5','f6','d4','d5','d6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d5" and piece_rb == '♔':
        tab_p = ['d4', 'd6', 'e4','e5','e6','c4','c5','c6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c5" and piece_rb == '♔':
        tab_p = ['c4', 'c6', 'b4','b5','b6','d4','d5','d6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b5" and piece_rb == '♔':
        tab_p = ['b4', 'b6', 'c4','c5','c6','a4','a5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a5" and piece_rb == '♔':
        tab_p = ['a4', 'a6', 'b4','b5','b6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h6" and piece_rb == '♔':
        tab_p = ['h7', 'h5', 'g5','g6','g7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "g6" and piece_rb == '♔':
        tab_p = ['g7', 'g5', 'h5','h6','h7','f5','f6','f7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "f6" and piece_rb == '♔':
        tab_p = ['f7', 'f5', 'g5','g6','g7','e5','e6','e7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "e6" and piece_rb == '♔':
        tab_p = ['e7', 'e5', 'f5','f6','f7','d5','d6','d7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d6" and piece_rb == '♔':
        tab_p = ['d7', 'd5', 'e5','e6','e7','c5','c6','c7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c6" and piece_rb == '♔':
        tab_p = ['c7', 'c5', 'd5','d6','d7','b5','b6','b7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b6" and piece_rb == '♔':
        tab_p = ['b7', 'b5', 'c5','c6','c7','a5','a6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a6" and piece_rb == '♔':
        tab_p = ['a7', 'a5', 'b5','b6','b7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h7" and piece_rb == '♔':
        tab_p = ['h8', 'h6', 'g6','g7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "g7" and piece_rb == '♔':
        tab_p = ['g8', 'g6', 'h6','h7','h8','f6','f7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "f7" and piece_rb == '♔':
        tab_p = ['f8', 'f6', 'g6','g7','g8','e6','e7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "e7" and piece_rb == '♔':
        tab_p = ['e8', 'e6', 'f6','f7','f8','d6','d7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d7" and piece_rb == '♔':
        tab_p = ['d8', 'd6', 'e6','e7','e8','c6','c7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c7" and piece_rb == '♔':
        tab_p = ['c8', 'c6', 'd6','d7','d8','b6','b7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b7" and piece_rb == '♔':
        tab_p = ['b8', 'b6', 'c6','c7','c8','a6','a7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a7" and piece_rb == '♔':
        tab_p = ['a8', 'a6', 'b6','b7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "h8" and piece_rb == '♔':
        tab_p = ['h7', 'g7', 'g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "g8" and piece_rb == '♔':
        tab_p = ['g7', 'h7', 'h8','f7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "f8" and piece_rb == '♔':
        tab_p = ['f7', 'g7', 'g8','e7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "e8" and piece_rb == '♔':
        tab_p = ['e7', 'f7', 'f8','d7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "d8" and piece_rb == '♔':
        tab_p = ['d7', 'e7', 'e8','c7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "c8" and piece_rb == '♔':
        tab_p = ['c7', 'd7', 'd8', 'b7', 'b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "b8" and piece_rb == '♔':
        tab_p = ['b7', 'c7', 'c8', 'a7', 'a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rb == "a8" and piece_rb == '♔':
        tab_p = ['a7', 'b7', 'b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p

def roi_deplacement_noir(coordo_rn, piece_rn):

    if coordo_rn == "h1" and piece_rn == '♚':
        tab_p = ['h2', 'g1', 'g2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g1" and piece_rn == '♚':
        tab_p = ['h1', 'f1', 'g2', 'h2', 'f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f1" and piece_rn == '♚':
        tab_p = ['g1', 'e1', 'f2', 'g2', 'e2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e1" and piece_rn == '♚':
        tab_p = ['e2', 'f1', 'd1', 'f2', 'd2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d1" and piece_rn == '♚':
        tab_p = ['d2', 'e1', 'c1', 'e2', 'c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c1" and piece_rn == '♚':
        tab_p = ['c2', 'd1', 'b1', 'b2', 'd2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b1" and piece_rn == '♚':
        tab_p = ['b2', 'c1', 'a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a1" and piece_rn == '♚':
        tab_p = ['a2', 'b1', 'b2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h2" and piece_rn == '♚':
        tab_p = ['h3', 'g2', 'g3', 'h1', 'g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h2" and piece_rn == '♚':
        tab_p = ['h3', 'g2', 'g3', 'h1', 'g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g2" and piece_rn == '♚':
        tab_p = ['h2', 'h3', 'g3', 'f3', 'f2', 'f1', 'c1', 'h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f2" and piece_rn == '♚':
        tab_p = ['g1', 'g2', 'g3', 'f3', 'e1', 'e2', 'e3', 'f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e2" and piece_rn == '♚':
        tab_p = ['f1', 'f2', 'f3', 'e3', 'd1', 'd2', 'd3', 'e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d2" and piece_rn == '♚':
        tab_p = ['e1', 'e2', 'e3', 'c1', 'c2', 'c3', 'd1', 'd3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c2" and piece_rn == '♚':
        tab_p = ['d1', 'd2', 'd3', 'b1', 'b2', 'b3', 'c3', 'c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b2" and piece_rn == '♚':
        tab_p = ['c1', 'c2', 'c3', 'b3', 'b1', 'a1', 'a2', 'a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a2" and piece_rn == '♚':
        tab_p = ['a1', 'a3', 'b1', 'b2', 'b3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h3" and piece_rn == '♚':
        tab_p = ['h4', 'h2', 'g2', 'g3', 'g4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g3" and piece_rn == '♚':
        tab_p = ['g2', 'g4', 'f2', 'f3', 'f4', 'h2', 'h3', 'h4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f3" and piece_rn == '♚':
        tab_p = ['f4', 'f2', 'g2', 'g3', 'g4', 'e2', 'e3', 'e4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e3" and piece_rn == '♚':
        tab_p = ['e4', 'e2', 'f2', 'f3', 'f4', 'd2', 'd3', 'd4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d3" and piece_rn == '♚':
        tab_p = ['d4', 'd2', 'e2', 'e3', 'e4', 'c2', 'c3', 'c4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c3" and piece_rn == '♚':
        tab_p = ['c4', 'c2', 'd2', 'd3', 'd4', 'b2', 'b3', 'b4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b3" and piece_rn == '♚':
        tab_p = ['b4', 'b2', 'c2', 'c3', 'c4', 'a2', 'a3', 'a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a3" and piece_rn == '♚':
        tab_p = ['a4', 'a2', 'b2', 'b3', 'b4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h4" and piece_rn == '♚':
        tab_p = ['h3', 'h5', 'g3', 'g4', 'g5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g4" and piece_rn == '♚':
        tab_p = ['g5', 'g3', 'h3', 'h4', 'h5', 'f3', 'f4', 'f5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f4" and piece_rn == '♚':
        tab_p = ['f5', 'f3', 'g3', 'g4', 'g5', 'e3', 'e4', 'e5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e4" and piece_rn == '♚':
        tab_p = ['e5', 'e3', 'f3', 'f4', 'f5', 'd3', 'd4', 'd5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d4" and piece_rn == '♚':
        tab_p = ['d5', 'd3', 'e3', 'e4', 'e5', 'c3', 'c4', 'c5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c4" and piece_rn == '♚':
        tab_p = ['c5', 'c3', 'd3', 'd4', 'd5', 'b3', 'b4', 'b5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b4" and piece_rn == '♚':
        tab_p = ['b5', 'b3', 'c3', 'c4', 'c5', 'a3', 'a4', 'a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a4" and piece_rn == '♚':
        tab_p = ['a5', 'a3', 'b3', 'b4', 'b5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h5" and piece_rn == '♚':
        tab_p = ['h6', 'h4', 'g4', 'g5', 'g6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g5" and piece_rn == '♚':
        tab_p = ['g4', 'g6', 'h4', 'h5', 'h6', 'f4', 'f5', 'f6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f5" and piece_rn == '♚':
        tab_p = ['f4', 'f6', 'g4', 'g5', 'g6', 'e4', 'e5', 'e6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e5" and piece_rn == '♚':
        tab_p = ['e4', 'e6', 'f4', 'f5', 'f6', 'd4', 'd5', 'd6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d5" and piece_rn == '♚':
        tab_p = ['d4', 'd6', 'e4', 'e5', 'e6', 'c4', 'c5', 'c6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c5" and piece_rn == '♚':
        tab_p = ['c4', 'c6', 'b4', 'b5', 'b6', 'd4', 'd5', 'd6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b5" and piece_rn == '♚':
        tab_p = ['b4', 'b6', 'c4', 'c5', 'c6', 'a4', 'a5', 'a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a5" and piece_rn == '♚':
        tab_p = ['a4', 'a6', 'b4', 'b5', 'b6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h6" and piece_rn == '♚':
        tab_p = ['h7', 'h5', 'g5', 'g6', 'g7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g6" and piece_rn == '♚':
        tab_p = ['g7', 'g5', 'h5', 'h6', 'h7', 'f5', 'f6', 'f7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f6" and piece_rn == '♚':
        tab_p = ['f7', 'f5', 'g5', 'g6', 'g7', 'e5', 'e6', 'e7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e6" and piece_rn == '♚':
        tab_p = ['e7', 'e5', 'f5', 'f6', 'f7', 'd5', 'd6', 'd7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d6" and piece_rn == '♚':
        tab_p = ['d7', 'd5', 'e5', 'e6', 'e7', 'c5', 'c6', 'c7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c6" and piece_rn == '♚':
        tab_p = ['c7', 'c5', 'd5', 'd6', 'd7', 'b5', 'b6', 'b7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b6" and piece_rn == '♚':
        tab_p = ['b7', 'b5', 'c5', 'c6', 'c7', 'a5', 'a6', 'a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a6" and piece_rn == '♚':
        tab_p = ['a7', 'a5', 'b5', 'b6', 'b7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h7" and piece_rn == '♚':
        tab_p = ['h8', 'h6', 'g6', 'g7', 'g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g7" and piece_rn == '♚':
        tab_p = ['g8', 'g6', 'h6', 'h7', 'h8', 'f6', 'f7', 'f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f7" and piece_rn == '♚':
        tab_p = ['f8', 'f6', 'g6', 'g7', 'g8', 'e6', 'e7', 'e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e7" and piece_rn == '♚':
        tab_p = ['e8', 'e6', 'f6', 'f7', 'f8', 'd6', 'd7', 'd8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d7" and piece_rn == '♚':
        tab_p = ['d8', 'd6', 'e6', 'e7', 'e8', 'c6', 'c7', 'c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c7" and piece_rn == '♚':
        tab_p = ['c8', 'c6', 'd6', 'd7', 'd8', 'b6', 'b7', 'b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b7" and piece_rn == '♚':
        tab_p = ['b8', 'b6', 'c6', 'c7', 'c8', 'a6', 'a7', 'a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a7" and piece_rn == '♚':
        tab_p = ['a8', 'a6', 'b6', 'b7', 'b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "h8" and piece_rn == '♚':
        tab_p = ['h7', 'g7', 'g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "g8" and piece_rn == '♚':
        tab_p = ['g7', 'h7', 'h8', 'f7', 'f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "f8" and piece_rn == '♚':
        tab_p = ['f7', 'g7', 'g8', 'e7', 'e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "e8" and piece_rn == '♚':
        tab_p = ['e7', 'f7', 'f8', 'd7', 'd8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "d8" and piece_rn == '♚':
        tab_p = ['d7', 'e7', 'e8', 'c7', 'c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "c8" and piece_rn == '♚':
        tab_p = ['c7', 'd7', 'd8', 'b7', 'b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "b8" and piece_rn == '♚':
        tab_p = ['b7', 'c7', 'c8', 'a7', 'a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_rn == "a8" and piece_rn == '♚':
        tab_p = ['a7', 'b7', 'b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p

#La dame | Déplacements de la dame
def dame_deplacement_blanc(coordo_db, piece_db):
    if coordo_db == "h1" and piece_db == '♕':
        tab_p = ['h2','h3','h4','h5','h6','h7','h8', 'g1','f1','e1','d1','c1','b1','a1','g2','f3','e4','d5','c6','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g1" and piece_db == '♕':
        tab_p = ['h1','h2','g2','g3','g4','g5','g6', 'g7','g8','f1','e1','d1','c1','b1','a1','f2','e3','d4','c5','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f1" and piece_db == '♕':
        tab_p = ['g1','h1','e1','d1','c1','b1','a1', 'g2','h3','f2','f3','f4','f5','f6','f7','f8','e2','d3','c4','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e1" and piece_db == '♕':
        tab_p = ['f1','g1','h1','d1','c1','b1','a1', 'f2','g3','h4','e2','e3','e4','e5','e6','e7','e8','d2','c3','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d1" and piece_db == '♕':
        tab_p = ['g1','h1','e1','f1','c1','b1','a1', 'c2','b3','a4','d2','d3','d4','d5','d6','d7','d8','e2','f3','g4','h5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c1" and piece_db == '♕':
        tab_p = ['g1','h1','e1','d1','f1','b1','a1', 'd2','e3','f4','g5','h6','b2','a3','c2','c3','c4','c5','c6','c7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b1" and piece_db == '♕':
        tab_p = ['g1','h1','e1','d1','c1','f1','a1', 'a2','b2','b3','b4','b5','b6','b7','b8','c2','d3','e4','f5','g6','h7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a1" and piece_db == '♕':
        tab_p = ['g1','h1','e1','d1','c1','b1','f1', 'a2','a3','a4','a5','a6','a7','a8','b2','c3','d4','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "h2" and piece_db == '♕':
        tab_p = ['g2','f2','e2','d2','c2','b2','a2', 'h1','h3','h4','h5','h6','h7','h8','g1','g3','f4','e5','d6','c7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g2" and piece_db == '♕':
        tab_p = ['h2','f2','e2','d2','c2','b2','a2', 'h1','f1','h3','g1','g3','g4','g5','g6','g7','g8','f3','e4','d5','c6','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f2" and piece_db == '♕':
        tab_p = ['g2','h2','e2','d2','c2','b2','a2', 'g1','g3','h4','f1','f3','f4','f5','f6','f7','f8','e3','d4','c5','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e2" and piece_db == '♕':
        tab_p = ['g2','h2','f2','d2','c2','b2','a2', 'f1','f3','g4','h5','d1','d3','c4','b5','a6','e1','e3','e4','e5','e6','e7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d2" and piece_db == '♕':
        tab_p = ['g2','h2','e2','f2','c2','b2','a2', 'e1','e3','f4','g5','h6','d1','d3','d4','d5','d6','d7','d8','c1','c3','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c2" and piece_db == '♕':
        tab_p = ['g2','h2','e2','f2','d2','b2','a2', 'd1','d3','e4','f5','g6','h7','b1','b3','a4','c1','c3','c4','c5','c6','c7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b2" and piece_db == '♕':
        tab_p = ['g2','h2','e2','f2','d2','c2','a2', 'c1','c3','d4','e5','f6','g7','h8','a1','a3','b1','b3','b4','b5','b6','b7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a2" and piece_db == '♕':
        tab_p = ['g2','h2','e2','f2','d2','c2','b2', 'a1','a3','a4','a5','a6','a7','a8','b1','b3','c4','d5','e6','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "h3" and piece_db == '♕':
        tab_p = ['g3','f3','e3','d3','c3','b3','a3', 'h1','h2','h4','h5','h6','h7','h8','g2','f1','g4','f5','e6','d7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g3" and piece_db == '♕':
        tab_p = ['h3','f3','e3','d3','c3','b3','a3', 'g2','g1','g4','g5','g6','g7','g8','h2','f4','e5','d6','c7','b8','f2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f3" and piece_db == '♕':
        tab_p = ['g3','h3','e3','d3','c3','b3','a3', 'g2','h1','e4','d5','c6','b7','a8','f2','f1','f4','f5','f6','f7','f8','e2','d1','g4','h5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e3" and piece_db == '♕':
        tab_p = ['g3','f3','h3','d3','c3','b3','a3', 'e1','e2','e4','e5','e6','e7','e8','f2','g1','d4','c5','b6','a7','d2','c1','f4','g5','h6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d3" and piece_db == '♕':
        tab_p = ['g3','f3','e3','h3','c3','b3','a3', 'd1','d2','d4','d5','d6','d7','d8','e2','f1','c4','b5','a6','d7','c2','b1','e4','f5','g6','h7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c3" and piece_db == '♕':
        tab_p = ['g3','f3','e3','d3','h3','b3','a3', 'c1','c2','c4','c5','c6','c7','c8','b2','a1','b4','a5','d2','e1','d4','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b3" and piece_db == '♕':
        tab_p = ['g3','f3','e3','d3','c3','h3','a3', 'b1','b2','b4','b5','b6','b7','b8','a2','a4','c2','d1','c4','d5','e6','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a3" and piece_db == '♕':
        tab_p = ['g3','f3','e3','d3','c3','h3','b3', 'a1','a2','a4','a5','a6','a7','a8','b4','c5','d6','e7','f8','b2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "h4" and piece_db == '♕':
        tab_p = ['g4','f4','e4','d4','c4','b4','a4', 'h1','h2','h3','h5','h6','h7','h8','g3','f2','e1','g5','f6','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g4" and piece_db == '♕':
        tab_p = ['h4','f4','e4','d4','c4','b4','a4', 'g1','g2','g3','g5','g6','g7','g8','h3','f5','e6','d7','c8','h5','f3','e2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f4" and piece_db == '♕':
        tab_p = ['h4','g4','e4','d4','c4','b4','a4', 'f1','f2','f3','f5','f6','f7','f8','e3','d2','c1','g5','h6','e5','d6','c7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e4" and piece_db == '♕':
        tab_p = ['h4','g4','f4','d4','c4','b4','a4', 'e1','e2','e3','e5','e6','e7','e8','f3','g2','h1','d5','c6','b7','a8','d3','c2','b1','f5','g6','h7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d4" and piece_db == '♕':
        tab_p = ['h4','g4','f4','e4','c4','b4','a4', 'd1','d2','d3','d5','d6','d7','d8','e3','f2','g1','c5','b6','a7','c3','b2','a1','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c4" and piece_db == '♕':
        tab_p = ['h4','g4','f4','e4','d4','b4','a4', 'c1','c2','c3','c5','c6','c7','c8','b3','a2','d5','e6','f7','g8','d3','e2','f1','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b4" and piece_db == '♕':
        tab_p = ['h4','g4','f4','e4','c4','d4','a4', 'b1','b2','b3','b5','b6','b7','b8','a3','c5','d6','e7','f8','c3','d2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a4" and piece_db == '♕':
        tab_p = ['h4','g4','f4','e4','c4','b4','d4', 'a1','a2','a3','a5','a6','a7','a8','b3','c2','d1','b5','c6','d7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "h5" and piece_db == '♕':
        tab_p = ['g5','f5','e5','d5','c5','b5','a5', 'h1','h2','h3','h4','h6','h7','h8','g4','f3','e2','d1','g6','f7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g5" and piece_db == '♕':
        tab_p = ['h5','f5','e5','d5','c5','b5','a5', 'g1','g2','g3','g4','g6','g7','g8','h4','f4','e3','d2','c1','f6','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f5" and piece_db == '♕':
        tab_p = ['h5','g5','e5','d5','c5','b5','a5', 'f1','f2','f3','f4','f6','f7','f8','g4','h3','e4','d3','c2','b1','e6','d7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e5" and piece_db == '♕':
        tab_p = ['h5','f5','g5','d5','c5','b5','a5', 'e1','e2','e3','e4','e6','e7','e8','f4','g3','h2','d6','c7','b8','d4','c3','b2','a1','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d5" and piece_db == '♕':
        tab_p = ['h5','f5','g5','e5','c5','b5','a5', 'd1','d2','d3','d4','d6','d7','d8','e4','f3','g2','h1','c6','b7','a8','c4','b3','a2','e6','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c5" and piece_db == '♕':
        tab_p = ['h5','f5','g5','d5','e5','b5','a5', 'c1','c2','c3','c4','c6','c7','c8','d4','e3','f2','g1','b6','a7','b4','a3','d6','e7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b5" and piece_db == '♕':
        tab_p = ['h5','f5','g5','d5','e5','c5','a5', 'b1','b2','b3','b4','b6','b7','b8','c4','d3','e2','f1','a6','a4','c6','d7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a5" and piece_db == '♕':
        tab_p = ['h5','f5','g5','d5','e5','b5','c5', 'a1','a2','a3','a4','a6','a7','a8','b4','c3','d2','e1','b6','c7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "h6" and piece_db == '♕':
        tab_p = ['g6','f6','e6','d6','c6','b6','a6', 'h1','h2','h3','h4','h5','h7','h8','g5','f4','e3','d2','c1','g7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g6" and piece_db == '♕':
        tab_p = ['h6','f6','e6','d6','c6','b6','a6', 'g1','g2','g3','g4','g5','g7','g8','h5','e4','d3','c2','b1','h7','f7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f6" and piece_db == '♕':
        tab_p = ['h6','g6','e6','d6','c6','b6','a6', 'f1','f2','f3','f4','f5','f7','f8','g5','h4','e5','d4','c3','b2','a1','h8','g7','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e6" and piece_db == '♕':
        tab_p = ['h6','g6','f6','d6','c6','b6','a6', 'e1','e2','e3','e4','e5','e7','e8','f5','g4','h3','d7','c8','d5','c4','b3','a2','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d6" and piece_db == '♕':
        tab_p = ['h6','g6','e6','f6','c6','b6','a6', 'd1','d2','d3','d4','d5','d7','d8','e5','f4','g3','h2','c7','b8','c5','b4','a3','e7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c6" and piece_db == '♕':
        tab_p = ['h6','g6','e6','f6','d6','b6','a6', 'c1','c2','c3','c4','c5','c7','c8','b5','a4','d7','e8','d5','e4','f3','g2','h1','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b6" and piece_db == '♕':
        tab_p = ['h6','g6','e6','f6','c6','d6','a6', 'b1','b2','b3','b4','b5','b7','b8','a5','c7','d8','a7','c5','d4','e3','f2','g1','e7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a6" and piece_db == '♕':
        tab_p = ['h6','g6','e6','f6','c6','b6','d6', 'a1','a2','a3','a4','a5','a7','a8','b7','c8','b5','c4','d3','e2','f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "h7" and piece_db == '♕':
        tab_p = ['g7','f7','e7','d7','c7','b7','a7', 'h1','h2','h3','h4','h5','h6','h8','g8','g6','f5','e4','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g7" and piece_db == '♕':
        tab_p = ['h7','f7','e7','d7','c7','b7','a7', 'g1','g2','g3','g4','g5','g6','g8','h6','f8','h8','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f7" and piece_db == '♕':
        tab_p = ['h7','g7','e7','d7','c7','b7','a7', 'f1','f2','f3','f4','f5','f6','f8','g6','h5','e8','g8','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e7" and piece_db == '♕':
        tab_p = ['h7','f7','g7','d7','c7','b7','a7', 'e1','e2','e3','e4','e5','e6','e8','f6','g5','h4','d8','f8','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d7" and piece_db == '♕':
        tab_p = ['h7','f7','e7','g7','c7','b7','a7', 'd1','d2','d3','d4','d5','d6','d8','c8','e6','f5','g4','h3','e8','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c7" and piece_db == '♕':
        tab_p = ['h7','f7','e7','d7','g7','b7','a7', 'c1','c2','c3','c4','c5','c6','c8','b8','d6','e5','f4','g3','h2','d8','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b7" and piece_db == '♕':
        tab_p = ['h7','f7','e7','d7','c7','g7','a7', 'b1','b2','b3','b4','b5','b6','b8','a6','c8','a8','c6','d5','e4','f3','g2','h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a7" and piece_db == '♕':
        tab_p = ['h7','f7','e7','d7','c7','b7','g7', 'a1','a2','a3','a4','a5','a6','a8','b8','b6','c5','d4','e3','f2','g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "h8" and piece_db == '♕':
        tab_p = ['g8','f8','e8','d8','c8','b8','a8', 'h1','h2','h3','h4','h5','h6','h7','g7','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "g8" and piece_db == '♕':
        tab_p = ['h8','f8','e8','d8','c8','b8','a8', 'g1','g2','g3','g4','g5','g6','g7','h7','f7','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "f8" and piece_db == '♕':
        tab_p = ['g8','h8','e8','d8','c8','b8','a8', 'f1','f2','f3','f4','f5','f6','f7','g7','h6','e7','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "e8" and piece_db == '♕':
        tab_p = ['g8','f8','h8','d8','c8','b8','a8', 'e1','e2','e3','e4','e5','e6','e7','f7','g6','h5','d7','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "d8" and piece_db == '♕':
        tab_p = ['g8','f8','e8','h8','c8','b8','a8', 'd1','d2','d3','d4','d5','d6','d7','e7','f6','g5','h4','c7','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "c8" and piece_db == '♕':
        tab_p = ['g8','f8','e8','d8','h8','b8','a8', 'c1','c2','c3','c4','c5','c6','c7','b7','a6','d7','e6','f5','g4','h3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "b8" and piece_db == '♕':
        tab_p = ['g8','f8','e8','d8','c8','h8','a8', 'b1','b2','b3','b4','b5','b6','b7','a7','c7','d6','e5','f4','g3','h2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_db == "a8" and piece_db == '♕':
        tab_p = ['g8','f8','e8','d8','c8','b8','h8', 'a1','a2','a3','a4','a5','a6','a7','b7','c6','d5','e4','f3','g2','h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    
def dame_deplacement_noir(coordo_dn, piece_dn):
    if coordo_dn == "h1" and piece_dn == '♛':
        tab_p = ['h2','h3','h4','h5','h6','h7','h8', 'g1','f1','e1','d1','c1','b1','a1','g2','f3','e4','d5','c6','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g1" and piece_dn == '♛':
        tab_p = ['h1','h2','g2','g3','g4','g5','g6', 'g7','g8','f1','e1','d1','c1','b1','a1','f2','e3','d4','c5','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f1" and piece_dn == '♛':
        tab_p = ['g1','h1','e1','d1','c1','b1','a1', 'g2','h3','f2','f3','f4','f5','f6','f7','f8','e2','d3','c4','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e1" and piece_dn == '♛':
        tab_p = ['f1','g1','h1','d1','c1','b1','a1', 'f2','g3','h4','e2','e3','e4','e5','e6','e7','e8','d2','c3','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d1" and piece_dn == '♛':
        tab_p = ['g1','h1','e1','f1','c1','b1','a1', 'c2','b3','a4','d2','d3','d4','d5','d6','d7','d8','e2','f3','g4','h5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c1" and piece_dn == '♛':
        tab_p = ['g1','h1','e1','d1','f1','b1','a1', 'd2','e3','f4','g5','h6','b2','a3','c2','c3','c4','c5','c6','c7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b1" and piece_dn == '♛':
        tab_p = ['g1','h1','e1','d1','c1','f1','a1', 'a2','b2','b3','b4','b5','b6','b7','b8','c2','d3','e4','f5','g6','h7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a1" and piece_dn == '♛':
        tab_p = ['g1','h1','e1','d1','c1','b1','f1', 'a2','a3','a4','a5','a6','a7','a8','b2','c3','d4','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "h2" and piece_dn == '♛':
        tab_p = ['g2','f2','e2','d2','c2','b2','a2', 'h1','h3','h4','h5','h6','h7','h8','g1','g3','f4','e5','d6','c7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g2" and piece_dn == '♛':
        tab_p = ['h2','f2','e2','d2','c2','b2','a2', 'h1','f1','h3','g1','g3','g4','g5','g6','g7','g8','f3','e4','d5','c6','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f2" and piece_dn == '♛':
        tab_p = ['g2','h2','e2','d2','c2','b2','a2', 'g1','g3','h4','f1','f3','f4','f5','f6','f7','f8','e3','d4','c5','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e2" and piece_dn == '♛':
        tab_p = ['g2','h2','f2','d2','c2','b2','a2', 'f1','f3','g4','h5','d1','d3','c4','b5','a6','e1','e3','e4','e5','e6','e7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d2" and piece_dn == '♛':
        tab_p = ['g2','h2','e2','f2','c2','b2','a2', 'e1','e3','f4','g5','h6','d1','d3','d4','d5','d6','d7','d8','c1','c3','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c2" and piece_dn == '♛':
        tab_p = ['g2','h2','e2','f2','d2','b2','a2', 'd1','d3','e4','f5','g6','h7','b1','b3','a4','c1','c3','c4','c5','c6','c7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b2" and piece_dn == '♛':
        tab_p = ['g2','h2','e2','f2','d2','c2','a2', 'c1','c3','d4','e5','f6','g7','h8','a1','a3','b1','b3','b4','b5','b6','b7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a2" and piece_dn == '♛':
        tab_p = ['g2','h2','e2','f2','d2','c2','b2', 'a1','a3','a4','a5','a6','a7','a8','b1','b3','c4','d5','e6','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "h3" and piece_dn == '♛':
        tab_p = ['g3','f3','e3','d3','c3','b3','a3', 'h1','h2','h4','h5','h6','h7','h8','g2','f1','g4','f5','e6','d7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g3" and piece_dn == '♛':
        tab_p = ['h3','f3','e3','d3','c3','b3','a3', 'g2','g1','g4','g5','g6','g7','g8','h2','f4','e5','d6','c7','b8','f2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f3" and piece_dn == '♛':
        tab_p = ['g3','h3','e3','d3','c3','b3','a3', 'g2','h1','e4','d5','c6','b7','a8','f2','f1','f4','f5','f6','f7','f8','e2','d1','g4','h5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e3" and piece_dn == '♛':
        tab_p = ['g3','f3','h3','d3','c3','b3','a3', 'e1','e2','e4','e5','e6','e7','e8','f2','g1','d4','c5','b6','a7','d2','c1','f4','g5','h6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d3" and piece_dn == '♛':
        tab_p = ['g3','f3','e3','h3','c3','b3','a3', 'd1','d2','d4','d5','d6','d7','d8','e2','f1','c4','b5','a6','d7','c2','b1','e4','f5','g6','h7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c3" and piece_dn == '♛':
        tab_p = ['g3','f3','e3','d3','h3','b3','a3', 'c1','c2','c4','c5','c6','c7','c8','b2','a1','b4','a5','d2','e1','d4','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b3" and piece_dn == '♛':
        tab_p = ['g3','f3','e3','d3','c3','h3','a3', 'b1','b2','b4','b5','b6','b7','b8','a2','a4','c2','d1','c4','d5','e6','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a3" and piece_dn == '♛':
        tab_p = ['g3','f3','e3','d3','c3','h3','b3', 'a1','a2','a4','a5','a6','a7','a8','b4','c5','d6','e7','f8','b2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "h4" and piece_dn == '♛':
        tab_p = ['g4','f4','e4','d4','c4','b4','a4', 'h1','h2','h3','h5','h6','h7','h8','g3','f2','e1','g5','f6','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g4" and piece_dn == '♛':
        tab_p = ['h4','f4','e4','d4','c4','b4','a4', 'g1','g2','g3','g5','g6','g7','g8','h3','f5','e6','d7','c8','h5','f3','e2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f4" and piece_dn == '♛':
        tab_p = ['h4','g4','e4','d4','c4','b4','a4', 'f1','f2','f3','f5','f6','f7','f8','e3','d2','c1','g5','h6','e5','d6','c7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e4" and piece_dn == '♛':
        tab_p = ['h4','g4','f4','d4','c4','b4','a4', 'e1','e2','e3','e5','e6','e7','e8','f3','g2','h1','d5','c6','b7','a8','d3','c2','b1','f5','g6','h7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d4" and piece_dn == '♛':
        tab_p = ['h4','g4','f4','e4','c4','b4','a4', 'd1','d2','d3','d5','d6','d7','d8','e3','f2','g1','c5','b6','a7','c3','b2','a1','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c4" and piece_dn == '♛':
        tab_p = ['h4','g4','f4','e4','d4','b4','a4', 'c1','c2','c3','c5','c6','c7','c8','b3','a2','d5','e6','f7','g8','d3','e2','f1','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b4" and piece_dn == '♛':
        tab_p = ['h4','g4','f4','e4','c4','d4','a4', 'b1','b2','b3','b5','b6','b7','b8','a3','c5','d6','e7','f8','c3','d2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a4" and piece_dn == '♛':
        tab_p = ['h4','g4','f4','e4','c4','b4','d4', 'a1','a2','a3','a5','a6','a7','a8','b3','c2','d1','b5','c6','d7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "h5" and piece_dn == '♛':
        tab_p = ['g5','f5','e5','d5','c5','b5','a5', 'h1','h2','h3','h4','h6','h7','h8','g4','f3','e2','d1','g6','f7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g5" and piece_dn == '♛':
        tab_p = ['h5','f5','e5','d5','c5','b5','a5', 'g1','g2','g3','g4','g6','g7','g8','h4','f4','e3','d2','c1','f6','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f5" and piece_dn == '♛':
        tab_p = ['h5','g5','e5','d5','c5','b5','a5', 'f1','f2','f3','f4','f6','f7','f8','g4','h3','e4','d3','c2','b1','e6','d7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e5" and piece_dn == '♛':
        tab_p = ['h5','f5','g5','d5','c5','b5','a5', 'e1','e2','e3','e4','e6','e7','e8','f4','g3','h2','d6','c7','b8','d4','c3','b2','a1','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d5" and piece_dn == '♛':
        tab_p = ['h5','f5','g5','e5','c5','b5','a5', 'd1','d2','d3','d4','d6','d7','d8','e4','f3','g2','h1','c6','b7','a8','c4','b3','a2','e6','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c5" and piece_dn == '♛':
        tab_p = ['h5','f5','g5','d5','e5','b5','a5', 'c1','c2','c3','c4','c6','c7','c8','d4','e3','f2','g1','b6','a7','b4','a3','d6','e7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b5" and piece_dn == '♛':
        tab_p = ['h5','f5','g5','d5','e5','c5','a5', 'b1','b2','b3','b4','b6','b7','b8','c4','d3','e2','f1','a6','a4','c6','d7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a5" and piece_dn == '♛':
        tab_p = ['h5','f5','g5','d5','e5','b5','c5', 'a1','a2','a3','a4','a6','a7','a8','b4','c3','d2','e1','b6','c7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "h6" and piece_dn == '♛':
        tab_p = ['g6','f6','e6','d6','c6','b6','a6', 'h1','h2','h3','h4','h5','h7','h8','g5','f4','e3','d2','c1','g7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g6" and piece_dn == '♛':
        tab_p = ['h6','f6','e6','d6','c6','b6','a6', 'g1','g2','g3','g4','g5','g7','g8','h5','e4','d3','c2','b1','h7','f7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f6" and piece_dn == '♛':
        tab_p = ['h6','g6','e6','d6','c6','b6','a6', 'f1','f2','f3','f4','f5','f7','f8','g5','h4','e5','d4','c3','b2','a1','h8','g7','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e6" and piece_dn == '♛':
        tab_p = ['h6','g6','f6','d6','c6','b6','a6', 'e1','e2','e3','e4','e5','e7','e8','f5','g4','h3','d7','c8','d5','c4','b3','a2','f7','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d6" and piece_dn == '♛':
        tab_p = ['h6','g6','e6','f6','c6','b6','a6', 'd1','d2','d3','d4','d5','d7','d8','e5','f4','g3','h2','c7','b8','c5','b4','a3','e7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c6" and piece_dn == '♛':
        tab_p = ['h6','g6','e6','f6','d6','b6','a6', 'c1','c2','c3','c4','c5','c7','c8','b5','a4','d7','e8','d5','e4','f3','g2','h1','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b6" and piece_dn == '♛':
        tab_p = ['h6','g6','e6','f6','c6','d6','a6', 'b1','b2','b3','b4','b5','b7','b8','a5','c7','d8','a7','c5','d4','e3','f2','g1','e7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a6" and piece_dn == '♛':
        tab_p = ['h6','g6','e6','f6','c6','b6','d6', 'a1','a2','a3','a4','a5','a7','a8','b7','c8','b5','c4','d3','e2','f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "h7" and piece_dn == '♛':
        tab_p = ['g7','f7','e7','d7','c7','b7','a7', 'h1','h2','h3','h4','h5','h6','h8','g8','g6','f5','e4','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g7" and piece_dn == '♛':
        tab_p = ['h7','f7','e7','d7','c7','b7','a7', 'g1','g2','g3','g4','g5','g6','g8','h6','f8','h8','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f7" and piece_dn == '♛':
        tab_p = ['h7','g7','e7','d7','c7','b7','a7', 'f1','f2','f3','f4','f5','f6','f8','g6','h5','e8','g8','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e7" and piece_dn == '♛':
        tab_p = ['h7','f7','g7','d7','c7','b7','a7', 'e1','e2','e3','e4','e5','e6','e8','f6','g5','h4','d8','f8','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d7" and piece_dn == '♛':
        tab_p = ['h7','f7','e7','g7','c7','b7','a7', 'd1','d2','d3','d4','d5','d6','d8','c8','e6','f5','g4','h3','e8','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c7" and piece_dn == '♛':
        tab_p = ['h7','f7','e7','d7','g7','b7','a7', 'c1','c2','c3','c4','c5','c6','c8','b8','d6','e5','f4','g3','h2','d8','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b7" and piece_dn == '♛':
        tab_p = ['h7','f7','e7','d7','c7','g7','a7', 'b1','b2','b3','b4','b5','b6','b8','a6','c8','a8','c6','d5','e4','f3','g2','h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a7" and piece_dn == '♛':
        tab_p = ['h7','f7','e7','d7','c7','b7','g7', 'a1','a2','a3','a4','a5','a6','a8','b8','b6','c5','d4','e3','f2','g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "h8" and piece_dn == '♛':
        tab_p = ['g8','f8','e8','d8','c8','b8','a8', 'h1','h2','h3','h4','h5','h6','h7','g7','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "g8" and piece_dn == '♛':
        tab_p = ['h8','f8','e8','d8','c8','b8','a8', 'g1','g2','g3','g4','g5','g6','g7','h7','f7','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "f8" and piece_dn == '♛':
        tab_p = ['g8','h8','e8','d8','c8','b8','a8', 'f1','f2','f3','f4','f5','f6','f7','g7','h6','e7','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "e8" and piece_dn == '♛':
        tab_p = ['g8','f8','h8','d8','c8','b8','a8', 'e1','e2','e3','e4','e5','e6','e7','f7','g6','h5','d7','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "d8" and piece_dn == '♛':
        tab_p = ['g8','f8','e8','h8','c8','b8','a8', 'd1','d2','d3','d4','d5','d6','d7','e7','f6','g5','h4','c7','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "c8" and piece_dn == '♛':
        tab_p = ['g8','f8','e8','d8','h8','b8','a8', 'c1','c2','c3','c4','c5','c6','c7','b7','a6','d7','e6','f5','g4','h3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "b8" and piece_dn == '♛':
        tab_p = ['g8','f8','e8','d8','c8','h8','a8', 'b1','b2','b3','b4','b5','b6','b7','a7','c7','d6','e5','f4','g3','h2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_dn == "a8" and piece_dn == '♛':
        tab_p = ['g8','f8','e8','d8','c8','b8','h8', 'a1','a2','a3','a4','a5','a6','a7','b7','c6','d5','e4','f3','g2','h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p

#Le fou | Déplacements du fou
def fou_deplacement_noir(coord_n,piece):
    if coord_n=="h8" and piece=='♗':
        tab_p = ['g7','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="h7" and piece=='♗':
        tab_p = ['g6','f5','e4','d3','c3','b1','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="h6" and piece=='♗':
        tab_p = ['g5','f4','e3','d2','c1','g7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="h5" and piece=='♗':
        tab_p = ['g4','f3','e2','d1','g6','f7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="h4" and piece=='♗':
        tab_p = ['g3','f2','e1','g5','f6','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="h3" and piece=='♗':
        tab_p = ['g2','f1','g4','f5','e6','d7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="h2" and piece=='♗':
        tab_p = ['g1','g3','f4','e5','d6','c7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="h1" and piece=='♗':
        tab_p = ['g2','f3','e4','d5','c6','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g8" and piece=='♗':
        tab_p = ['h7','f7','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g7" and piece=='♗':
        tab_p = ['h8','f8','h6','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g6" and piece=='♗':
        tab_p = ['h7','h5','f7','e8','f5','e4','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g5" and piece=='♗':
        tab_p = ['h6','h4','f6','e7','d8','f4','e3','d2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g4" and piece=='♗':
        tab_p = ['h5','h3','f5','e6','d7','c8','f3','e2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g3" and piece=='♗':
        tab_p = ['h4','h2','f4','e5','d6','c7','b8','f2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g2" and piece=='♗':
        tab_p = ['h3','h1','f3','e4','d5','c6','b7','a8','f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="g1" and piece=='♗':
        tab_p = ['h2','f2','e3','d4','c5','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f8" and piece=='♗':
        tab_p = ['g7','h6','e7','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f7" and piece=='♗':
        tab_p = ['g8','g6','h5','e8','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f6" and piece=='♗':
        tab_p = ['g7','g5','h8','h4','d8','e7','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f5" and piece=='♗':
        tab_p = ['g6','g4','h7','h3','d7','e6','c8','e4','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f4" and piece=='♗':
        tab_p = ['g5','g3','h6','h2','d6','e5','c7','b8','e3','d2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f3" and piece=='♗':
        tab_p = ['g4','g2','h5','h1','d5','e4','c6','b7','a8','e2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f2" and piece=='♗':
        tab_p = ['g3','g1','h4','h1','d4','e3','c5','b6','a7','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="f1" and piece=='♗':
        tab_p = ['g2','h3','d3','e2','c4','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e8" and piece=='♗':
        tab_p = ['f7','g6','h6','d7','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e7" and piece=='♗':
        tab_p = ['f8','f6','g5','h4','d8','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e6" and piece=='♗':
        tab_p = ['f7','f5','g8','h3','g4','d7','c8','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e5" and piece=='♗':
        tab_p = ['f6','f4','g7','h8','h2','g3','d6','c7','b8','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e4" and piece=='♗':
        tab_p = ['f5','f3','g6','h7','h1','g2','d5','c6','b7','a8','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e3" and piece=='♗':
        tab_p = ['f4','f2','g5','h6','g1','d4','c5','b6','a7','d2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e2" and piece=='♗':
        tab_p = ['f3','f1','g4','h5','g1','d3','c4','b5','a6','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="e1" and piece=='♗':
        tab_p = ['f2','g3','h4','d2','c3','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d8" and piece=='♗':
        tab_p = ['e7','f6','g5','h4','c7','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d7" and piece=='♗':
        tab_p = ['e6','f5','g4','h3','e8','c8','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d6" and piece=='♗':
        tab_p = ['e5','f4','g3','h2','e7','f8','c7','b8','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d5" and piece=='♗':
        tab_p = ['e4','f3','g2','h1','e6','f7','g8','c6','b7','a8','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d4" and piece=='♗':
        tab_p = ['e3','f2','g1','h8','e5','f6','g7','c5','b6','a7','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d3" and piece=='♗':
        tab_p = ['e2','f1','h7','e4','f5','g6','c4','b5','a6','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d2" and piece=='♗':
        tab_p = ['e1','h6','e3','f4','g5','c3','b4','a5','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="d1" and piece=='♗':
        tab_p = ['h5','e2','f3','g4','c2','b3','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c8" and piece=='♗':
        tab_p = ['d7','e6','f5','g4','h3','b7','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c7" and piece=='♗':
        tab_p = ['d8','d6','b8','e5','f4','g3','h2','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c6" and piece=='♗':
        tab_p = ['d7','d5','e8','e4','f3','g2','h1','b5','a4','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c5" and piece=='♗':
        tab_p = ['d6','d4','e7','f8','e3','f2','g1','b4','a3','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c4" and piece=='♗':
        tab_p = ['d5','d3','e6','f7','g8','e2','f1','b3','a2','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c3" and piece=='♗':
        tab_p = ['d4','d2','e5','f6','g7','h8','e1','b2','a1','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c2" and piece=='♗':
        tab_p = ['d3','d1','e4','f5','g6','h7','b1','b3','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="c1" and piece=='♗':
        tab_p = ['d2','e3','f4','g5','h6','b2','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b8" and piece=='♗':
        tab_p = ['c7','d6','e5','f4','g3','h2','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b7" and piece=='♗':
        tab_p = ['c6','c8','d5','e4','f3','g2','h1','a8','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b6" and piece=='♗':
        tab_p = ['c5','c7','d8','d4','e3','f2','g1','a7','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b5" and piece=='♗':
        tab_p = ['c4','c6','d7','e8','d3','e2','f1','a6','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b4" and piece=='♗':
        tab_p = ['c3','c5','d6','e7','f8','d2','e1','a5','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b3" and piece=='♗':
        tab_p = ['c2','c4','d5','e6','f7','g8','d1','a4','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b2" and piece=='♗':
        tab_p = ['c1','c3','d4','e5','f6','g7','h8','a3','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="b1" and piece=='♗':
        tab_p = ['c2','d3','e4','f5','g6','h7','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a8" and piece=='♗':
        tab_p = ['b7','c6','d5','e4','f3','g2','h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a7" and piece=='♗':
        tab_p = ['b8','b6','c5','d4','e3','f2','g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a6" and piece=='♗':
        tab_p = ['b7','c8','b5','c4','d3','e2','f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a5" and piece=='♗':
        tab_p = ['b6','c7','d8','b4','c3','d2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a4" and piece=='♗':
        tab_p = ['b5','c6','d7','e8','b3','c2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a3" and piece=='♗':
        tab_p = ['b4','c5','d6','e7','f8','b2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a2" and piece=='♗':
        tab_p = ['b3','c4','d5','e6','f7','g8','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_n=="a1" and piece=='♗':
        tab_p = ['b2','c3','d4','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p

def fou_deplacement_blanc(coord_b,piece):
    if coord_b=="h8" and piece=='♝':
        tab_p = ['g7','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="h7" and piece=='♝':
        tab_p = ['g6','f5','e4','d3','c3','b1','g8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="h6" and piece=='♝':
        tab_p = ['g5','f4','e3','d2','c1','g7','f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="h5" and piece=='♝':
        tab_p = ['g4','f3','e2','d1','g6','f7','e8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="h4" and piece=='♝':
        tab_p = ['g3','f2','e1','g5','f6','e7','d8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="h3" and piece=='♝':
        tab_p = ['g2','f1','g4','f5','e6','d7','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="h2" and piece=='♝':
        tab_p = ['g1','g3','f4','e5','d6','c7','b8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="h1" and piece=='♝':
        tab_p = ['g2','f3','e4','d5','c6','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g8" and piece=='♝':
        tab_p = ['h7','f7','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g7" and piece=='♝':
        tab_p = ['h8','f8','h6','f6','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g6" and piece=='♝':
        tab_p = ['h7','h5','f7','e8','f5','e4','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g5" and piece=='♝':
        tab_p = ['h6','h4','f6','e7','d8','f4','e3','d2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g4" and piece=='♝':
        tab_p = ['h5','h3','f5','e6','d7','c8','f3','e2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g3" and piece=='♝':
        tab_p = ['h4','h2','f4','e5','d6','c7','b8','f2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g2" and piece=='♝':
        tab_p = ['h3','h1','f3','e4','d5','c6','b7','a8','f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="g1" and piece=='♝':
        tab_p = ['h2','f2','e3','d4','c5','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f8" and piece=='♝':
        tab_p = ['g7','h6','e7','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f7" and piece=='♝':
        tab_p = ['g8','g6','h5','e8','e6','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f6" and piece=='♝':
        tab_p = ['g7','g5','h8','h4','d8','e7','e5','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f5" and piece=='♝':
        tab_p = ['g6','g4','h7','h3','d7','e6','c8','e4','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f4" and piece=='♝':
        tab_p = ['g5','g3','h6','h2','d6','e5','c7','b8','e3','d2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f3" and piece=='♝':
        tab_p = ['g4','g2','h5','h1','d5','e4','c6','b7','a8','e2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f2" and piece=='♝':
        tab_p = ['g3','g1','h4','h1','d4','e3','c5','b6','a7','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="f1" and piece=='♝':
        tab_p = ['g2','h3','d3','e2','c4','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e8" and piece=='♝':
        tab_p = ['f7','g6','h6','d7','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e7" and piece=='♝':
        tab_p = ['f8','f6','g5','h4','d8','d6','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e6" and piece=='♝':
        tab_p = ['f7','f5','g8','h3','g4','d7','c8','d5','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e5" and piece=='♝':
        tab_p = ['f6','f4','g7','h8','h2','g3','d6','c7','b8','d4','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e4" and piece=='♝':
        tab_p = ['f5','f3','g6','h7','h1','g2','d5','c6','b7','a8','d3','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e3" and piece=='♝':
        tab_p = ['f4','f2','g5','h6','g1','d4','c5','b6','a7','d2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e2" and piece=='♝':
        tab_p = ['f3','f1','g4','h5','g1','d3','c4','b5','a6','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="e1" and piece=='♝':
        tab_p = ['f2','g3','h4','d2','c3','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d8" and piece=='♝':
        tab_p = ['e7','f6','g5','h4','c7','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d7" and piece=='♝':
        tab_p = ['e6','f5','g4','h3','e8','c8','c6','b5','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d6" and piece=='♝':
        tab_p = ['e5','f4','g3','h2','e7','f8','c7','b8','c5','b4','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d5" and piece=='♝':
        tab_p = ['e4','f3','g2','h1','e6','f7','g8','c6','b7','a8','c4','b3','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d4" and piece=='♝':
        tab_p = ['e3','f2','g1','h8','e5','f6','g7','c5','b6','a7','c3','b2','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d3" and piece=='♝':
        tab_p = ['e2','f1','h7','e4','f5','g6','c4','b5','a6','c2','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d2" and piece=='♝':
        tab_p = ['e1','h6','e3','f4','g5','c3','b4','a5','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="d1" and piece=='♝':
        tab_p = ['h5','e2','f3','g4','c2','b3','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c8" and piece=='♝':
        tab_p = ['d7','e6','f5','g4','h3','b7','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c7" and piece=='♝':
        tab_p = ['d8','d6','b8','e5','f4','g3','h2','b6','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c6" and piece=='♝':
        tab_p = ['d7','d5','e8','e4','f3','g2','h1','b5','a4','b7','a8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c5" and piece=='♝':
        tab_p = ['d6','d4','e7','f8','e3','f2','g1','b4','a3','b6','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c4" and piece=='♝':
        tab_p = ['d5','d3','e6','f7','g8','e2','f1','b3','a2','b5','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c3" and piece=='♝':
        tab_p = ['d4','d2','e5','f6','g7','h8','e1','b2','a1','b4','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c2" and piece=='♝':
        tab_p = ['d3','d1','e4','f5','g6','h7','b1','b3','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="c1" and piece=='♝':
        tab_p = ['d2','e3','f4','g5','h6','b2','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b8" and piece=='♝':
        tab_p = ['c7','d6','e5','f4','g3','h2','a7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b7" and piece=='♝':
        tab_p = ['c6','c8','d5','e4','f3','g2','h1','a8','a6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b6" and piece=='♝':
        tab_p = ['c5','c7','d8','d4','e3','f2','g1','a7','a5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b5" and piece=='♝':
        tab_p = ['c4','c6','d7','e8','d3','e2','f1','a6','a4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b4" and piece=='♝':
        tab_p = ['c3','c5','d6','e7','f8','d2','e1','a5','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b3" and piece=='♝':
        tab_p = ['c2','c4','d5','e6','f7','g8','d1','a4','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b2" and piece=='♝':
        tab_p = ['c1','c3','d4','e5','f6','g7','h8','a3','a1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="b1" and piece=='♝':
        tab_p = ['c2','d3','e4','f5','g6','h7','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a8" and piece=='♝':
        tab_p = ['b7','c6','d5','e4','f3','g2','h1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a7" and piece=='♝':
        tab_p = ['b8','b6','c5','d4','e3','f2','g1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a6" and piece=='♝':
        tab_p = ['b7','c8','b5','c4','d3','e2','f1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a5" and piece=='♝':
        tab_p = ['b6','c7','d8','b4','c3','d2','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a4" and piece=='♝':
        tab_p = ['b5','c6','d7','e8','b3','c2','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a3" and piece=='♝':
        tab_p = ['b4','c5','d6','e7','f8','b2','c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a2" and piece=='♝':
        tab_p = ['b3','c4','d5','e6','f7','g8','b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coord_b=="a1" and piece=='♝':
        tab_p = ['b2','c3','d4','e5','f6','g7','h8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p

#Cavalier | Déplacements du cavalier
def cavalier_deplacement_blanc(coordo_cb, piece_cb):
    if coordo_cb == "h1" and piece_cb == '♘':
        tab_p = ['g3','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g1" and piece_cb == '♘':
        tab_p = ['h3','f3','e2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f1" and piece_cb == '♘':
        tab_p = ['g3','e3','h2','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e1" and piece_cb == '♘':
        tab_p = ['f3','d3','g2','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d1" and piece_cb == '♘':
        tab_p = ['e3','c3','b2','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c1" and piece_cb == '♘':
        tab_p = ['b3','d3','a2','e2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b1" and piece_cb == '♘':
        tab_p = ['a3','c3','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a1" and piece_cb == '♘':
        tab_p = ['b3','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "h2" and piece_cb == '♘':
        tab_p = ['g4','f1','f3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g2" and piece_cb == '♘':
        tab_p = ['h4','f4','e3','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f2" and piece_cb == '♘':
        tab_p = ['g4','e4','h3','h1','d3','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e2" and piece_cb == '♘':
        tab_p = ['f4', 'd4', 'g3', 'g1', 'c3', 'c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d2" and piece_cb == '♘':
        tab_p = ['f1', 'f3', 'b3', 'b1', 'c4', 'e4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c2" and piece_cb == '♘':
        tab_p = ['e1', 'e3', 'a3', 'a1', 'b4', 'd4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b2" and piece_cb == '♘':
        tab_p = ['a4', 'c4', 'b3', 'd1', 'd3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a2" and piece_cb == '♘':
        tab_p = ['b4', 'c1', 'c3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "h3" and piece_cb == '♘':
        tab_p = ['g1', 'f4', 'f2', 'g5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g3" and piece_cb == '♘':
        tab_p = ['f1','h1', 'e4', 'e2', 'h5','f5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f3" and piece_cb == '♘':
        tab_p = ['g5','e5', 'h4', 'h2', 'd4','d2','g1','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e3" and piece_cb == '♘':
        tab_p = ['f5','d5', 'g4', 'g2', 'c4','c2','f1','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d3" and piece_cb == '♘':
        tab_p = ['e5','c5', 'e1', 'c1', 'b4','b2','f4','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c3" and piece_cb == '♘':
        tab_p = ['b5','d5', 'b1', 'd1', 'e4','e2','a4','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b3" and piece_cb == '♘':
        tab_p = ['a5','c5', 'a1', 'c1', 'd4','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a3" and piece_cb == '♘':
        tab_p = ['b5','c2', 'c4', 'b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "h4" and piece_cb == '♘':
        tab_p = ['g2', 'g6', 'f3', 'f5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g4" and piece_cb == '♘':
        tab_p = ['h2', 'f2', 'g6', 'f6','e3','e5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f4" and piece_cb == '♘':
        tab_p = ['g6', 'f6', 'g2', 'e2','d3','d5','h3','h5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e4" and piece_cb == '♘':
        tab_p = ['f6', 'd6', 'g3', 'g5','c3','c5','d2','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d4" and piece_cb == '♘':
        tab_p = ['e6', 'c6', 'f3', 'f5','b3','b5','e2','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c4" and piece_cb == '♘':
        tab_p = ['b6', 'd6', 'e3', 'e5','a3','a5','b2','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b4" and piece_cb == '♘':
        tab_p = ['a6', 'c6', 'd3', 'd5','a2','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a4" and piece_cb == '♘':
        tab_p = ['b6', 'c3', 'c5', 'b5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "h5" and piece_cb == '♘':
        tab_p = ['g7', 'g3', 'f4', 'f6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g5" and piece_cb == '♘':
        tab_p = ['h7', 'f7', 'e4', 'e6','f3','h3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f5" and piece_cb == '♘':
        tab_p = ['g7', 'e7', 'h4', 'h6','d4','d6','e3','g3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e5" and piece_cb == '♘':
        tab_p = ['f7', 'd7', 'g4', 'g6','c4','c6','f3','d3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d5" and piece_cb == '♘':
        tab_p = ['e7', 'c7', 'f4', 'f6','b4','b6','e3','c3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c5" and piece_cb == '♘':
        tab_p = ['b7', 'd7', 'e4', 'e6','a4','a6','b3','d3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b5" and piece_cb == '♘':
        tab_p = ['a7', 'c7', 'd4', 'd6','a3','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a5" and piece_cb == '♘':
        tab_p = ['b7', 'b3', 'c4', 'c6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "h6" and piece_cb == '♘':
        tab_p = ['g8', 'g4', 'f5', 'f7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g6" and piece_cb == '♘':
        tab_p = ['h8', 'f8', 'e5', 'e7','h4','f4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f6" and piece_cb == '♘':
        tab_p = ['g8', 'e8', 'h5', 'h7','d5','d7','g4','e4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e6" and piece_cb == '♘':
        tab_p = ['f8', 'd8', 'g5', 'g7','c5','c7','f4','f4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d6" and piece_cb == '♘':
        tab_p = ['e8', 'c8', 'f5', 'f7','b5','b7','e4','c4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c6" and piece_cb == '♘':
        tab_p = ['b8', 'd8', 'e5', 'e7','a5','a7','b4','d4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b6" and piece_cb == '♘':
        tab_p = ['a8', 'c8', 'd5', 'd7','a4','c4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a6" and piece_cb == '♘':
        tab_p = ['b8','c5', 'c7','b4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "h7" and piece_cb == '♘':
        tab_p = ['g5','f6', 'f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g7" and piece_cb == '♘':
        tab_p = ['h5','f5', 'e8','e6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f7" and piece_cb == '♘':
        tab_p = ['g5','e5', 'h8','h6','d8','d6',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e7" and piece_cb == '♘':
        tab_p = ['f5','d5', 'g8','g6','c8','c6',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d7" and piece_cb == '♘':
        tab_p = ['f6','f8', 'e5','c5','b6','b8',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c7" and piece_cb == '♘':
        tab_p = ['a6','a8', 'b5','d5','e6','e8',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b7" and piece_cb == '♘':
        tab_p = ['a5','c5','d6','d8',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a7" and piece_cb == '♘':
        tab_p = ['b5','c6','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "h8" and piece_cb == '♘':
        tab_p = ['g6','f7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "g8" and piece_cb == '♘':
        tab_p = ['h6','f6','e7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "f8" and piece_cb == '♘':
        tab_p = ['h7','d7','g6','e6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "e8" and piece_cb == '♘':
        tab_p = ['d6','f6','g7','c7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "d8" and piece_cb == '♘':
        tab_p = ['e6','c6','f7','b7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "c8" and piece_cb == '♘':
        tab_p = ['d6','b6','a7','e7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "b8" and piece_cb == '♘':
        tab_p = ['a6','c6','d7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cb == "a8" and piece_cb == '♘':
        tab_p = ['b6','c7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p

def cavalier_deplacement_noir(coordo_cn, piece_cn):
    if coordo_cn == "h1" and piece_cn == '♞':
        tab_p = ['g3','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g1" and piece_cn == '♞':
        tab_p = ['h3','f3','e2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f1" and piece_cn == '♞':
        tab_p = ['g3','e3','h2','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e1" and piece_cn == '♞':
        tab_p = ['f3','d3','g2','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d1" and piece_cn == '♞':
        tab_p = ['e3','c3','b2','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c1" and piece_cn == '♞':
        tab_p = ['b3','d3','a2','e2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b1" and piece_cn == '♞':
        tab_p = ['a3','c3','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a1" and piece_cn == '♞':
        tab_p = ['b3','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "h2" and piece_cn == '♞':
        tab_p = ['g4','f1','f3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g2" and piece_cn == '♞':
        tab_p = ['h4','f4','e3','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f2" and piece_cn == '♞':
        tab_p = ['g4','e4','h3','h1','d3','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e2" and piece_cn == '♞':
        tab_p = ['f4', 'd4', 'g3', 'g1', 'c3', 'c1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d2" and piece_cn == '♞':
        tab_p = ['f1', 'f3', 'b3', 'b1', 'c4', 'e4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c2" and piece_cn == '♞':
        tab_p = ['e1', 'e3', 'a3', 'a1', 'b4', 'd4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b2" and piece_cn == '♞':
        tab_p = ['a4', 'c4', 'b3', 'd1', 'd3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a2" and piece_cn == '♞':
        tab_p = ['b4', 'c1', 'c3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "h3" and piece_cn == '♞':
        tab_p = ['g1', 'f4', 'f2', 'g5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g3" and piece_cn == '♞':
        tab_p = ['f1','h1', 'e4', 'e2', 'h5','f5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f3" and piece_cn == '♞':
        tab_p = ['g5','e5', 'h4', 'h2', 'd4','d2','g1','e1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e3" and piece_cn == '♞':
        tab_p = ['f5','d5', 'g4', 'g2', 'c4','c2','f1','d1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d3" and piece_cn == '♞':
        tab_p = ['e5','c5', 'e1', 'c1', 'b4','b2','f4','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c3" and piece_cn == '♞':
        tab_p = ['b5','d5', 'b1', 'd1', 'e4','e2','a4','a2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b3" and piece_cn == '♞':
        tab_p = ['a5','c5', 'a1', 'c1', 'd4','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a3" and piece_cn == '♞':
        tab_p = ['b5','c2', 'c4', 'b1']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "h4" and piece_cn == '♞':
        tab_p = ['g2', 'g6', 'f3', 'f5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g4" and piece_cn == '♞':
        tab_p = ['h2', 'f2', 'g6', 'f6','e3','e5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f4" and piece_cn == '♞':
        tab_p = ['g6', 'f6', 'g2', 'e2','d3','d5','h3','h5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e4" and piece_cn == '♞':
        tab_p = ['f6', 'd6', 'g3', 'g5','c3','c5','d2','f2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d4" and piece_cn == '♞':
        tab_p = ['e6', 'c6', 'f3', 'f5','b3','b5','e2','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c4" and piece_cn == '♞':
        tab_p = ['b6', 'd6', 'e3', 'e5','a3','a5','b2','d2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b4" and piece_cn == '♞':
        tab_p = ['a6', 'c6', 'd3', 'd5','a2','c2']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a4" and piece_cn == '♞':
        tab_p = ['b6', 'c3', 'c5', 'b5']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "h5" and piece_cn == '♞':
        tab_p = ['g7', 'g3', 'f4', 'f6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g5" and piece_cn == '♞':
        tab_p = ['h7', 'f7', 'e4', 'e6','f3','h3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f5" and piece_cn == '♞':
        tab_p = ['g7', 'e7', 'h4', 'h6','d4','d6','e3','g3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e5" and piece_cn == '♞':
        tab_p = ['f7', 'd7', 'g4', 'g6','c4','c6','f3','d3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d5" and piece_cn == '♞':
        tab_p = ['e7', 'c7', 'f4', 'f6','b4','b6','e3','c3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c5" and piece_cn == '♞':
        tab_p = ['b7', 'd7', 'e4', 'e6','a4','a6','b3','d3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b5" and piece_cn == '♞':
        tab_p = ['a7', 'c7', 'd4', 'd6','a3','a3']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a5" and piece_cn == '♞':
        tab_p = ['b7', 'b3', 'c4', 'c6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "h6" and piece_cn == '♞':
        tab_p = ['g8', 'g4', 'f5', 'f7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g6" and piece_cn == '♞':
        tab_p = ['h8', 'f8', 'e5', 'e7','h4','f4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f6" and piece_cn == '♞':
        tab_p = ['g8', 'e8', 'h5', 'h7','d5','d7','g4','e4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e6" and piece_cn == '♞':
        tab_p = ['f8', 'd8', 'g5', 'g7','c5','c7','f4','f4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d6" and piece_cn == '♞':
        tab_p = ['e8', 'c8', 'f5', 'f7','b5','b7','e4','c4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c6" and piece_cn == '♞':
        tab_p = ['b8', 'd8', 'e5', 'e7','a5','a7','b4','d4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b6" and piece_cn == '♞':
        tab_p = ['a8', 'c8', 'd5', 'd7','a4','c4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a6" and piece_cn == '♞':
        tab_p = ['b8','c5', 'c7','b4']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "h7" and piece_cn == '♞':
        tab_p = ['g5','f6', 'f8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g7" and piece_cn == '♞':
        tab_p = ['h5','f5', 'e8','e6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f7" and piece_cn == '♞':
        tab_p = ['g5','e5', 'h8','h6','d8','d6',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e7" and piece_cn == '♞':
        tab_p = ['f5','d5', 'g8','g6','c8','c6',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d7" and piece_cn == '♞':
        tab_p = ['f6','f8', 'e5','c5','b6','b8',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c7" and piece_cn == '♞':
        tab_p = ['a6','a8', 'b5','d5','e6','e8',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b7" and piece_cn == '♞':
        tab_p = ['a5','c5','d6','d8',]
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a7" and piece_cn == '♞':
        tab_p = ['b5','c6','c8']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "h8" and piece_cn == '♞':
        tab_p = ['g6','f7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "g8" and piece_cn == '♞':
        tab_p = ['h6','f6','e7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "f8" and piece_cn == '♞':
        tab_p = ['h7','d7','g6','e6']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "e8" and piece_cn == '♞':
        tab_p = ['d6','f6','g7','c7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "d8" and piece_cn == '♞':
        tab_p = ['e6','c6','f7','b7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "c8" and piece_cn == '♞':
        tab_p = ['d6','b6','a7','e7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "b8" and piece_cn == '♞':
        tab_p = ['a6','c6','d7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
    if coordo_cn == "a8" and piece_cn == '♞':
        tab_p = ['b6','c7']
        print(color + f"Allez en : {' ou '.join(tab_p)}" + reset)
        return tab_p
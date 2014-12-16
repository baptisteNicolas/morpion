global TCase
global tour
tour = 1
TCase = [[0,0,0],
         [0,0,0],
         [0,0,0]]
global x_ref
global y_ref
global largeur_ref
global hauteur_ref 

x_ref=100
y_ref=100
largeur_ref=100
hauteur_ref=100

def setup ():
    size(1000,800)

def draw ():
    background (255)
    bord()
    croixrond()
    
    
def VictoryScreen(joueur):
    texte = "Victoire "+str(joueur)
    print texte
    
    

def Victoire():
    global tour
    global TCase
    count = 0
    for i in range(3):
        countO = 0
        countX = 0
        for j in range(3):
            if TCase[i][j]==1:
                countX += 1
                count += 1
            elif TCase[i][j]==2:
                countO += 1
                count += 1
        if countO==3:
            VictoryScreen(2)
        elif countX==3:
            VictoryScreen(1)
    for j in range(3):
        countO = 0
        countX = 0
        
        for i in range(3):
            if TCase[i][j]==1:
                countX += 1
            elif TCase[i][j]==2:
                countO += 1
        if countO==3:
            VictoryScreen(2)
        elif countX==3:
            VictoryScreen(1)
    #Gestion des diagonales
    countLX = 0
    countLO = 0
    countRX = 0
    countRO = 0
    for a in range(3):
        if TCase[a][a]==1:
            countLX += 1
        elif TCase[a][a]==2:
            countLO += 1
        if TCase[a][2-a]==1:
            countRX += 1
        elif TCase[a][2-a]==2:
            countRO += 1
    if countLX==3 or countRX==3:
        VictoryScreen(1)
    elif countLO==3 or countRO==3:
        VictoryScreen(2)
    if count==9:
        VictoryScreen(0)
    if tour==1:
        tour = 2
    else:
        tour = 1
    print "A toi de Jouer"


def IA():
    global TCase
    RobotAJouer = False
    #analyse des lignes horizontales
    for i in range(3):
        countO = 0
        countX = 0
        for j in range(3):
            if TCase[i][j]==1:
                countX += 1
            elif TCase[i][j]==2:
                countO += 1
        if countO==2 or countX==2:
            for j in range(3):
                if TCase[i][j]==0 and RobotAJouer==False:
                    RobotAJouer = True
                    TCase[i][j] = 2
    #analyse des lignes verticales
    for j in range(3):
        countO = 0
        countX = 0
        for i in range(3):
            if TCase[i][j]==1:
                countX += 1
            elif TCase[i][j]==2:
                countO += 1
        if countO==2 or countX==2:
            for i in range(3):
                if TCase[i][j]==0 and RobotAJouer==False:
                    RobotAJouer = True
                    TCase[i][j] = 2
    #Gestion des diagonales
    countLX = 0
    countLO = 0
    countRX = 0
    countRO = 0
    for a in range(3):
        if TCase[a][a]==1:
            countLX += 1
        elif TCase[a][a]==2:
            countLO += 1
        if TCase[a][2-a]==1:
            countRX += 1
        elif TCase[a][2-a]==2:
            countRO += 1
    if countLX==2 or countLO==2:
        for a in range(3):
            if TCase[a][a]==0:
                TCase[a][a]==2
    if countRX==2 or countRO==2:
        for a in range(3):
            if TCase[a][a]==0:
                TCase[a][a]==2
    #Jeu au hasard
    if RobotAJouer==False:
        if TCase[1][1]==0:
            TCase[1][1] = 2
        else:
            option = []
            for i in range(3):
                for j in range (3):
                    if TCase[i][j]==0:
                        option.append(i+j)
            choix = floor(random(0,len(option)))
            print option[choix]
            choixI = floor(option[choix]/3)
            choixJ = floor(option[choix]-(option[choix]/3)*3)
            TCase[choixI][choixJ] = 2
    print TCase
    Victoire()
    

def mousePressed():
    global tour
    for i in range(3):
        for j in range(3):
            x = x_ref+largeur_ref*j
            y = y_ref+hauteur_ref*i
            xmax = x_ref+largeur_ref*(j+1)
            ymax = y_ref+hauteur_ref*(i+1)
            if mouseX>x and mouseX<xmax and mouseY>y and mouseY<ymax:
                if TCase[i][j]==0:
                    TCase[i][j] = tour
                    Victoire()
        
def Jeu ():
    test =0
def bord ():
    global x_ref
    global y_ref
    global largeur_ref
    global hauteur_ref 
    stroke (0)
    strokeWeight (1)
    fill(0)
    line (x_ref,y_ref,largeur_ref*3+x_ref,y_ref)
    line (x_ref,y_ref+hauteur_ref,largeur_ref*3+x_ref,y_ref+hauteur_ref)
    line (x_ref,y_ref+hauteur_ref*2,largeur_ref*3+x_ref,y_ref+hauteur_ref*2)
    line (x_ref,y_ref+hauteur_ref*3,largeur_ref*3+x_ref,y_ref+hauteur_ref*3)
    
    # verticale#
    
    line (x_ref,y_ref,x_ref,hauteur_ref*3+y_ref)
    line (x_ref+largeur_ref,y_ref,largeur_ref+x_ref,y_ref+hauteur_ref*3)
    line (x_ref+largeur_ref*2,y_ref,largeur_ref*2+x_ref,y_ref+hauteur_ref*3)
    line (x_ref+largeur_ref*3,y_ref,largeur_ref*3+x_ref,y_ref+hauteur_ref*3)
    
def croixrond():
    global x_ref
    global y_ref
    global largeur_ref
    global hauteur_ref 
    for i in range(3):
        for j in range(3):
            case = TCase[i][j]
            if case==1:
                rond(x_ref+j*largeur_ref,y_ref+i*hauteur_ref)
            if case==2:
                croix(x_ref+j*largeur_ref,y_ref+i*hauteur_ref)
            
    
def rond(x,y):
    global x_ref
    global y_ref
    global largeur_ref
    global hauteur_ref 
    ellipse(x+largeur_ref/2,y+largeur_ref/2,largeur_ref-10,hauteur_ref-10)
    
def croix(x,y):
    global x_ref
    global y_ref
    global largeur_ref
    global hauteur_ref 
    line (x+10,y+10, x+largeur_ref-10,y+hauteur_ref-10)
    line (x+largeur_ref-10,y+10,x+10,y+hauteur_ref-10)

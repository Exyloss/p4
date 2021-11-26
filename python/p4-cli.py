# Valeur ANSI des couleurs
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_yellow = "\033[0;93m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

dic= [[0 for i in range(7)] for i in range(7)]
inputColor = red
joueur = 1
colStat = [blue, "1", blue,"2", blue,"3", blue,"4", blue,"5", blue,"6", blue,"7"]
combGagnante=[]

def isWinning(dic):
    global combGagnante
    v = 0
    for i in range(0, 7): # Vérifie si le joueur gagne en horizontalité
        for j in range(0, 6):
            if v == 3:
                combGagnante.append([i,j])
                return True
            if dic[i][j] == dic[i][j+1] and dic[i][j] != 0:
                v += 1
                combGagnante.append([i,j])
            else:
                v = 0
                combGagnante = []
    v = 0
    combGagnante = []
    for i in range(0, 7): # Vérifie si le joueur gagne en verticalité
        for j in range(0, 6):
            if v == 3:
                return True
            if dic[j][i] == dic[j+1][i] and dic[j][i] != 0:
                v += 1
                combGagnante.append([j,i])
                combGagnante.append([j+1,i])
            else:
                v = 0
                combGagnante=[]
    v = 0
    combGagnante = []
    for i in range(6, 2, -1): # Vérifie si le joueur gagne en diagonale montante vers la droite
        for j in range(0, 3):
            for k in range(0, 4):
                if v == 3:
                    return True
                if dic[i-k][j+k] == dic[i-k-1][j+k+1] and dic[i-k][j+k] != 0:
                    v += 1
                    combGagnante.append([i-k,j+k])
                    combGagnante.append([i-k-1,j+k+1])
                else:
                    v = 0
                    combGagnante=[]
    v = 0
    combGagnante = []

    for i in range(0, 4): # Vérifie si le joueur gagne en diagonale montante vers la gauche
        for j in range(0, 4): # À faire
            for k in range(0, 3):
                if v == 3:
                    return True
                if dic[i+k][j+k] == dic[i+k+1][j+k+1] and dic[i+k][j+k] != 0:
                    v += 1
                    combGagnante.append([i+k,j+k])
                    combGagnante.append([i+k+1,j+k+1])
                else:
                    v = 0
                    combGagnante = []
    v = 0
    combGagnante = []

def isFull(col):
    return dic[0][col-1] == 0

def poserPion(col):
    for i in range(6,-1,-1):
        if dic[i][col-1] == 0:
            dic[i][col-1] = joueur
            break

def printTab(d):
    temp = " "
    for i in range(1, len(colStat), 2):
        if not isFull(int(colStat[i])):
            colStat[i-1] = bright_black
        temp += " "+colStat[i-1]+colStat[i]
    print(temp)
    for line in range(len(d)):
        temp=""
        temp+=blue+str(line+1)+" "
        for char in range(len(d)):
            if d[line][char] == 1:
                if [line, char] in combGagnante:
                    temp+=cyan+"0"
                else:
                    temp+=red+"0"
                temp+=" "
            elif d[line][char] == 2:
                if [line, char] in combGagnante:
                    temp+=cyan+"0"
                else:
                    temp+=yellow+"0"
                temp+=" "
            else:
                temp+=bright_white+"0"
                temp+=" "
        print(temp)
    


while True:
    printTab(dic)
    print(inputColor+"joueur "+str(joueur))
    rep=input(bright_white+':')
    if rep == "q":
        break
    elif rep == "h":
        print(green+"q: quitter le programmer\nnombres de 1 à 7: placer le pion sur une colonne")
    elif rep in [str(i) for i in range(1, 8)] and isFull(int(rep)):
        poserPion(int(rep))
        if isWinning(dic):
            printTab(dic)
            print(inputColor+"Joueur "+str(joueur)+" a gagné.")
            break
        if inputColor == red:
           inputColor = yellow
           joueur = 2
        else:
            inputColor = red
            joueur = 1

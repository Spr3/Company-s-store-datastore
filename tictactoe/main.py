import math
import random
import time
from tkinter import *
import random
root = Tk()
#first if row,second is the collumn and 3rd is to save the size
Boardsize = [3,3,2]
BoardArray = []
placmentRow, PLamentCollumn, Boardsizenumber,playerWon = StringVar(), StringVar(), IntVar(), StringVar()
LivingPlayers = 1
#Makes The UI
Topframe = Frame(root, width=335, height=110)
Topframe.grid(row=0, column=0)
Topframe.configure(bg='grey')
# Page1
Top1 = Label(Topframe, text="            TikTakToe            ", font=("Helvetica", 25))
Top1.grid(row=0, column=0)
Top1.configure(bg='black', fg='white')
#Send in X
global createdboard
createdboard = False
def playerhaswon1():
    for widgets in root.winfo_children():
        widgets.destroy()
    print(playerWon.get()," kefo")
    if playerWon.get() == "X":
        Top1 = Label(root, text="Player X has Won", font=("Helvetica", 25),width=20)
        Top1.grid(row=0, column=0)
        Top1.configure(bg='black', fg='white')
    elif playerWon.get() == "Y":
        Top1 = Label(root, text="Player Y has Won", font=("Helvetica", 25), width=20)
        Top1.grid(row=0, column=0)
        Top1.configure(bg='black', fg='white')
    elif playerWon.get() == "Draw":
        Top1 = Label(root, text="Draw!!", font=("Helvetica", 25), width=20)
        Top1.grid(row=0, column=0)
        Top1.configure(bg='black', fg='white')
def setbottom():
    Inputframe = Frame(root, width=335, height=110)
    Inputframe.grid(row=4223, column=0)
    Inputframe.configure(bg='grey')
    Top1 = Label(Inputframe, text="Row:", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')
    Top1 = Entry(Inputframe, textvariable = placmentRow, font=("Helvetica", 25),width=5)
    Top1.grid(row=0, column=1)
    Top1.configure(bg='black', fg='white')
    Top1 = Label(Inputframe, text="Collumn:", font=("Helvetica", 25))
    Top1.grid(row=0, column=3)
    Top1.configure(bg='black', fg='white')
    Top1 = Entry(Inputframe, textvariable = PLamentCollumn, font=("Helvetica", 25),width=5)
    Top1.grid(row=0, column=4)
    Top1.configure(bg='black', fg='white')
    Top1 = Button(Inputframe, text="Input", font=("Helvetica", 25), command=placeX)
    Top1.grid(row=0, column=5)
    Top1.configure(bg='black', fg='white')
    CreateBoard()
def placeY():
    if LivingPlayers == 1:
        while True:
            randomX = random.randint(0,Boardsize[2]-1)
            randomy = random.randint(0,Boardsize[2]-1)
            if BoardArray[randomX][randomy] == "  ":
                BoardArray[randomX][randomy] = "O"
                clear_screen()
                break
    else:
        if BoardArray[int(placmentRow.get()) - 1][int(PLamentCollumn.get()) - 1] == "  ":
            BoardArray[int(placmentRow.get()) - 1][int(PLamentCollumn.get()) - 1] = "O"
    endgame()
def placeX():
    if BoardArray[int(placmentRow.get()) - 1][int(PLamentCollumn.get()) - 1] == "  ":
        BoardArray[int(placmentRow.get()) - 1][int(PLamentCollumn.get()) - 1] = "X"
        placeY()
def endgame():
    stopgame = False
    for vertical in range(len(BoardArray)):
        if stopgame == True:
            break
        #this will get the values of the items
        XsandOs = [0,0]
        #check for horizontal
        for item in range(len(BoardArray[vertical])):
            Vertically = [0,0]
            #if there is nothing in the spot it will move onto the next line
            if BoardArray[vertical][item] == " ":
                break
            if BoardArray[vertical][item] == "X":
                XsandOs[0] += 1
            elif BoardArray[vertical][item] == "O":
                XsandOs[1] += 1
            if XsandOs[0] >= 1 and XsandOs[1] >= 1:
                break

            XsandOs1 = [0, 0]
            #checks verticly
            for hight in range(len(BoardArray)):
                if BoardArray[hight][item] == " ":
                    break
                if BoardArray[hight][item] == "X":
                    XsandOs1[0] += 1
                elif BoardArray[hight][item] == "O":
                    XsandOs1[1] += 1
                if XsandOs1[0] >= 1 and XsandOs1[1] >= 1:
                    break
            if XsandOs1[0] == len(BoardArray) or XsandOs1[1] == len(BoardArray):
                if XsandOs1[0] == len(BoardArray):
                    print("Player X has won")
                    playerWon = "X"
                    playerhaswon1()
                    return ("End")
                    stopgame = True
                else:
                    print("Player O has won")
                    playerWon = "Y"
                    playerhaswon1()
                    return ("End")
                    stopgame = True
        #checks if horizontal is done
        if XsandOs[0] == len(BoardArray[vertical]) or XsandOs[1] == len(BoardArray[vertical]):
            if XsandOs[0] == len(BoardArray[vertical]):
                print("Player X has won")
                playerWon = "X"
                playerhaswon1()
                return ("End")
                stopgame = True
            else:
                print("Player O has won")
                playerhaswon1()
                playerWon = "Y"
                return ("End")
                stopgame = True
        #diganal
        for hightdiaganle in range(len(BoardArray)):
            if stopgame == True:
                break
            if BoardArray[0][len(BoardArray[0])-1] == "X" and BoardArray[len(BoardArray)-1][0] == "X" or BoardArray[0][len(BoardArray[0])-1] == "O" and BoardArray[len(BoardArray)-1][0] == "O":
                winner = 1
                value = BoardArray[0][len(BoardArray[0])-1]
                for countingdown in range(len(BoardArray)):
                    if value == BoardArray[len(BoardArray[0])-countingdown-1][countingdown]:
                        if not winner == 0:
                            winner = 1
                    else:
                        winner = 0
                if winner == 1:
                    playerWon = BoardArray[len(BoardArray[0])-countingdown-1][countingdown]
                    playerhaswon1()
                    print("We have a winner and that is player", BoardArray[len(BoardArray[0])-countingdown-1][countingdown])
                    stopgame = True
                    return ("End")
                    break
            if BoardArray[0][0] == "X" and BoardArray[len(BoardArray)-1][len(BoardArray[0])-1] == "X" or BoardArray[0][0] == "O" and BoardArray[len(BoardArray)-1][len(BoardArray[0])-1] == "O":
                short = 0
                value = BoardArray[0][0]
                if len(BoardArray) >= len(BoardArray[0]):
                    short = len(BoardArray[0])
                else:
                    short = len(BoardArray)
                winner = 1
                for countingdown in range(short):
                    if value == BoardArray[countingdown][countingdown]:
                        if not winner == 0:
                            winner = 1
                    else:
                        winner = 0
                if winner == 1:
                    playerWon = BoardArray[0][0]
                    print("We have a winner and that is player", BoardArray[0][0])
                    playerhaswon1()
                    return ("End")
                    stopgame = True
                break
        draw = True
        for array in BoardArray:
            for item in array:
                if item == "  ":
                    draw = False
        if draw == True:
            print("It was a draw")
            playerWon = "Draw"
            playerhaswon1()
            stopgame = True
            return ("End")
    clear_screen()
def CreateBoard():
    global createdboard
    Boardsize[2] = Boardsizenumber.get()
    Boardsize[0] = Boardsize[2]
    Boardsize[1] = Boardsize[2]
    if createdboard == False:
        createdboard = True
        for i in range(Boardsize[2]):
            BoardArray.append([])
            for v in range(Boardsize[2]):
                BoardArray[i].append("  ")
    while Boardsize[0] >= 1:
        Topframe = Frame(root, width=335, height=110)
        Topframe.grid(row=Boardsize[2] - Boardsize[0]+1, column=0)
        while Boardsize[1] >= 1:
            print(Boardsize[2] - Boardsize[1])
            Top1 = Button(Topframe, text=BoardArray[Boardsize[2] - Boardsize[0]][Boardsize[2] - Boardsize[1]], font=("Helvetica", 25))
            Top1.grid(row=0, column=(Boardsize[1] - Boardsize[2])*-1)
            Top1.configure(bg='black', fg='white')
            Boardsize[1] -= 1
        Boardsize[0] -= 1
        Boardsize[1] = Boardsize[2]
def clear_screen():
    for widgets in root.winfo_children():
        widgets.destroy()
    setbottom()
def askforboardsize():
    Inputframe = Frame(root, width=335, height=110)
    Inputframe.grid(row=4223, column=0)
    Inputframe.configure(bg='grey')
    Top1 = Label(Inputframe, text="Size of Board:", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')
    Top1 = Entry(Inputframe, textvariable=Boardsizenumber, font=("Helvetica", 25), width=5)
    Top1.grid(row=0, column=1)
    Top1.configure(bg='black', fg='white')
    Top1.configure(bg='black', fg='white')
    Top1 = Button(Inputframe, text="Input", font=("Helvetica", 25), command=setbottom)
    Top1.grid(row=0, column=5)
    Top1.configure(bg='black', fg='white')
askforboardsize()
root.mainloop()
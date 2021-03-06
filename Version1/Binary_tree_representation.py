from tkinter import *
from BinaryTree import *

CanvasHeight = 650
CanvasWidth = 1000

X = int(CanvasHeight//1.5 + 30)
Y = 50
offset = 30


def clear_DrawBoard():
    inputEntry.delete(0,END)
    DrawBoard.delete('all')

def Circle(x,y,Value):
    DrawBoard.create_oval(x-offset,y-offset,x+offset,y+offset,width = 4,outline = 'blue')
    DrawBoard.create_text(x,y,text = str(Value))


def SlantLine(x,y,rol):
    if 1 == rol:
        #left slanted line
        DrawBoard.create_line(x,y+offset,x-100,y+offset+40,width = 3,fill = 'red')
    else:
        #right slanted line
        DrawBoard.create_line(x,y+offset,x+100,y+offset+40,width = 3,fill = 'red')

def printBinaryTree(Root):
    if Root:
        Circle(Root.x,Root.y,Root.data)
    if Root.left:
        SlantLine(Root.x,Root.y,1)
        printBinaryTree(Root.left)
    if Root.right:
        SlantLine(Root.x,Root.y,0)
        printBinaryTree(Root.right)

def BinTree(Data):
    #inialize points

    Data = list(map(int,Data))
    Root = Node(Data[0])
    Root.x = X
    Root.y = Y

    for i in range(1,len(Data)):
        Root.insert(Data[i])
        printBinaryTree(Root)


def get_Input():
    temp = inputEntry.get()
    if temp == '':
        return
    temp.strip()
    temp = temp.split(",")
    BinTree(temp)

master = Tk()

inputLabel = Label(master,text = "Enter Data\n(comma seperated)")
inputLabel.grid(row = 0 , column = 0,sticky = NW)

inputEntry = Entry(master,width = 125,bg = 'white')
inputEntry.grid(row = 0 , column = 1)

inputButton = Button(master,text = "Start",width = 10,command=lambda:get_Input())
inputButton.grid(row = 0,column = 2,columnspan = 2,sticky = E)

clearButton = Button(master,text= "Clear",width = 10 , command=lambda:clear_DrawBoard())
clearButton.grid(row = 0 , column = 5,sticky = E)

DrawBoard = Canvas(master, height = CanvasHeight, width = CanvasWidth,bg = 'white')
DrawBoard.grid(row = 1,rowspan = CanvasHeight,columnspan = CanvasWidth)

master.mainloop()

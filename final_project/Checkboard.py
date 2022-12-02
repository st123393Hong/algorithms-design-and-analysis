
import tkinter as tk
import tkinter.messagebox as message
from Jump import *
class Checkerboard:

    def __init__(self):
        self.solution = Jump()
        self.paths = []
        self.track = []
        self.num = 0
        self.boardData = [
            [2,5,1,6,1,4,1,2,1,2],
            [6,1,1,2,2,2,3,3,1,1],
            [4,2,3,2,1,3,1,5,4,1],
            [1,1,3,1,3,1,2,7,2,4],
            [4,1,2,3,4,1,2,3,2,5],
            [3,3,1,2,3,4,1,6,1,3],
            [1,5,2,5,4,2,1,2,1,3],
            [4,2,1,5,1,3,2,2,1,1],
            [1,2,4,1,2,3,1,1,2,3],
            [2,5,2,1,3,4,2,1,6,'end']]
        self.root_window =tk.Tk()
        self.canvas = tk.Canvas(self.root_window,
                        bg='#fff',
                        height=800,
                        width=600)

    
    def create(self):
        
        self.root_window.title('jumping game')
        self.root_window.geometry('800x500')
        #init color
        self.createColor()           
        
        B = tk.Button(self.root_window, text ="start",bg="#99ff33",relief="groove",width="40",height="25", command = self.startCallBack)
        next_button = tk.Button(self.root_window, text ="next",bg="#99ff33",relief="groove",width="40",height="25", command = self.nextCallBack)

        self.canvas.pack()
        B.place(x=620,y=237, width=60, height=30)
        next_button.place(x=620,y=290,width=60,height=30)
        self.root_window.mainloop()
    
    def createColor(self):
        x0,y0,x1,y1 = 0,0,50,50
       
        for j in range(0,10):
            flag = j%2
            for i in range(0,10):
                if i%2 ==flag:                    
                    self.canvas.create_rectangle((x0+50)*i,(y0+50)*j,x1*i+50,y1*j+50,fill='#B0E0E6',outline = '')
                    self.canvas.create_text((x0+50)*i+25,(y0+50)*j+25,text = self.boardData[j][i],font =(15))
                    
                else:                    
                    self.canvas.create_rectangle((x0+50)*i,(y0+50)*j,x1*i+50,y1*j+50,fill='#66ccff',outline = '') 
                    self.canvas.create_text((x0+50)*i+25,(y0+50)*j+25,text = self.boardData[j][i],font =(16))   
                                     
            self.canvas.create_rectangle(0,0,50,50,fill='#ccff99',outline = '') 
            self.canvas.create_text(25,25,text = self.boardData[0][0],font =(15))
                 
            self.canvas.create_rectangle(450,450,500,500,fill='#66ffcc',outline = '') 
            self.canvas.create_text(450+25,450+25,text = "end",font =('Times New Roman',16,'bold'),fill ='red') 


    def nextCallBack(self): 

        self.createColor()
        self.num = self.num+1
        temp = len(self.paths)-1
        if self.num <=temp:        
            for p in self.paths[self.num]:
                self.resultColor(p)
        else:
            self.num = temp
            for p in self.paths[self.num]:
                self.resultColor(p)    
            message.showinfo('tip','over',icon='warning')

    

    def startCallBack(self):
        
       self.solution.walk(self.boardData,0,0)
       self.paths = self.solution.paths   
       print(self.paths)    
       for p in self.paths[self.num]:
           self.resultColor(p)

    def resultColor(self,p):
        self.canvas.create_rectangle(50*p[0],50*p[1],50*p[0]+50,50*p[1]+50,fill='#ff6600',outline = '')
        self.canvas.create_text(50*p[0]+25,50*p[1]+25,text = self.boardData[p[0]][p[1]],font =(15))

board = Checkerboard()
board.create()


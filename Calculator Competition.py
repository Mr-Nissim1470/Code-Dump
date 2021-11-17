#Yosef Nahon
#Calcualtor Project

import tkinter
import tkinter.messagebox
import math

class Calculator:

    def __init__(self):
        #Main window
        self.main_window = tkinter.Tk()

        #Frames
        self.CALFrame = tkinter.Frame(self.main_window)
        self.ValFrameT1 = tkinter.Frame(self.main_window)
        self.ValFrameI1 = tkinter.Frame(self.main_window)
        self.ValFrameT2 = tkinter.Frame(self.main_window)
        self.ValFrameI2 = tkinter.Frame(self.main_window)
        self.OperationFrames = tkinter.Frame(self.main_window)
        self.Answers = tkinter.Frame(self.main_window)
        self.kill= tkinter.Frame(self.main_window)
        
        #in Frames
        self.ANS = tkinter.StringVar()
        
        self.header = tkinter.Label(self.CALFrame,
                                                       text = "Calculator")
        
        self.Val1T = tkinter.Label(self.ValFrameT1,
                                   text = "provide a Value (required)")
        self.Val1I = tkinter.Entry(self.ValFrameI1,
                                   width = 10)
        
        self.Val2T = tkinter.Label(self.ValFrameT2,
                                   text = "provide another Value (required for pretianing operations)")
        self.Val2I = tkinter.Entry(self.ValFrameI2,
                                   width = 10)

        self.Ans = tkinter.Label(self.Answers,
                                 textvariable = self.ANS)
        
        #operations
        self.Add = tkinter.Button(self.OperationFrames,
                                  text = "+",
                                  command = self.add)
        self.Subtract = tkinter.Button(self.OperationFrames,
                                  text = "-",
                                  command = self.sub)
        self.divide = tkinter.Button(self.OperationFrames,
                                  text ="/",
                                  command = self.div)
        self.multiply = tkinter.Button(self.OperationFrames,
                                  text = "X",
                                  command = self.mul)
        self.Mod = tkinter.Button(self.OperationFrames,
                                  text ="%",
                                  command = self.mod)
        self.SQRT = tkinter.Button(self.OperationFrames,
                                  text = "√",
                                  command = self.squ)
        self.Sin = tkinter.Button(self.OperationFrames,
                                  text ="Sin",
                                  command = self.sin)
        self.Cos = tkinter.Button(self.OperationFrames,
                                  text = "Cos",
                                  command = self.cos)
        self.Tan = tkinter.Button(self.OperationFrames,
                                  text = "Tan",
                                  command = self.tan)

        #quit
        self.Quit = tkinter.Button( self.kill,
                                    text = "End",
                                    command = self.main_window.destroy )

        #Packing
        self.header.pack(side = "top")
        self.Val1T.pack(side = "left")
        self.Val1I.pack(side = "right")
        self.Val2T.pack(side = "left")
        self.Val2I.pack(side = "right")
        self.Ans.pack(side = "top")
        self.Add.pack(side = "right")
        self.Subtract.pack(side = "right")
        self.divide.pack(side = "right")
        self.multiply.pack(side = "right")
        self.Mod.pack(side = "right")
        self.SQRT.pack(side = "left")
        self.Sin.pack(side = "left")
        self.Cos.pack(side = "left")
        self.Tan.pack(side = "left")
        self.Quit.pack()
        

        #main
        tkinter.mainloop()

        V1 = float(self.Val1I.get())
        V2 = float(self.Val2I.get())

    def add(self,V1,V2):
        Fin = (V1+V2)
        self.ANS.set(str(Fin))
        
    def sub(self,V1,V2):
        Fin = (V1-V2)
        self.ANS.set(str(Fin))
        
    def div(self,V1,V2):
        Fin = (V1/V2)
        self.ANS.set(str(Fin))    

    def mul(self,V1,V2):
        Fin = (V1*V2)
        self.ANS.set(str(Fin))

    def mod(self,V1,V2):
        Fin = (V1%V2)
        self.ANS.set(str(Fin))

    def squ(self,V1):
        Fin = (math.sqrt(V1))
        self.ANS.set(str(Fin))

    def sin(self,V1):
        Fin = (math.asin(V1))
        self.ANS.set(str(Fin))
        
    def cos(self,V1):
        Fin = (math.acos(V1))
        self.ANS.set(str(Fin))

    def tan(self,V1):
        Fin = (math.atan(V1))
        self.ANS.set(str(Fin))
    
        
        
Calculate = Calculator()
        

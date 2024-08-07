from tkinter import *
import random
import tkinter.messagebox as tmsg
import win32com.client

class GUI(Tk):
    def __init__(self):
        super().__init__()
        # GUI Appearance
        self.geometry("1000x600")
        self.title("Welcome To Ehshan Game")
        self.config(background="orange")

    # Game Function
    def user_choice(self):
        list=["Water","Gun","Snake"]
        if (var.get()=="Snake"):
            com=random.choice(list)
            if(com=="Snake"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"DRAW!{a.speak("Draw")}","Computer Choose Snake")
                # a.speak("Draw")
            if(com=="Water"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"YOU WIN!{a.speak("You Win")}","Computer Choose Water")
                # a.speak("You Win")
                
            if(com=="Gun"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"YOU LOSE!{a.speak("You Lose")}","Computer Choose Gun")
                # a.speak("You Lose")
                
        elif (var.get()=="Water"):
            com=random.choice(list)
            if(com=="Snake"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"YOU LOSE!{a.speak("You Lose")}","Computer Choose Snake")
                # a.speak("You Lose")
            if(com=="Water"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"DRAW!{a.speak("Draw")}","Computer Choose Water")
                # a.speak("Draw")
            if(com=="Gun"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"YOU WIN!{a.speak("You Win")}","Computer Choose Gun")
                # a.speak("You Win")
                

        elif(var.get()=="Gun"):
            com=random.choice(list)
            if(com=="Snake"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"YOU WIN!{a.speak("You Win")}","Computer Choose Snake")
                # a.speak("You Win")
                
            if(com=="Water"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"YOU LOSE!{a.speak("You Lose")}","Computer Choose Water")
                # a.speak("You Lose")
            if(com=="Gun"):
                a=win32com.client.Dispatch("SAPI.spVoice")
                tmsg.showinfo(f"DRAW!{a.speak("Draw")}","Computer Choose Gun")
                # a.speak("Draw")

        else:
            tmsg.showinfo("INVALID","No Input!")  

    def Score(self):
        if (tmsg.showinfo=="YOU WIN!"):
            for i in range(100):
                self.label2=Label(text=f"Score={i}",font="Comic 20 bold")
                self.label2.pack(side=TOP,anchor="e")

    # Choice Button
    def radiobutton(self):

        self.user1=Radiobutton(self,text="Snake",bg="orange",fg="green",variable=var,font="Lucida 20 bold",padx=100,value="Snake")
        self.user1.pack(anchor="w")

        self.user2=Radiobutton(self,text="Water",fg="blue",bg="orange",variable=var,font="Lucida 20 bold",padx=100,value="Water")
        self.user2.pack(anchor="w")
        
        self.user3=Radiobutton(self,text="Gun",fg="brown",bg="orange",variable=var,font="Lucida 20 bold",padx=100,value="Gun")
        self.user3.pack(anchor="w")

    # Play button
    def playbutton(self):
        self.enter=Button(text="Play",font="Helvatica 25",borderwidth=5,relief=RAISED,command=self.user_choice)
        self.enter.pack()
        self.enter=Button(text="Exit",bg="red",fg="white",font="Helvatica 10",borderwidth=5,relief=RAISED,command=quit)
        self.enter.pack(pady=100)

# Function Calling
if __name__=='__main__':
    window=GUI()
    var=StringVar()
    var.set("Radio")
    label1=Label(text="Snake Water Gun Game",fg="white",bg="orange", font="Helvatica 30 bold underline")
    label1.pack()
    label=Label(text="Your Choice!",fg="red",bg="orange",font="Lucida 25 bold").pack(pady=20)
    # window.Score()
    window.radiobutton()
    window.playbutton()
    window.mainloop()
    
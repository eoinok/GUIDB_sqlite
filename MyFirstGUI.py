from tkinter import *

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()
        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()
        self.entry2 = Entry()
        self.entry2.pack()
        
        self.helloButton = Button(master, text="Hello", command=self.sayhello)
        self.helloButton.pack()

        self.closeButton = Button(master, text="Close", command=self.close)
        self.closeButton.pack()

    def sayhello(self):    
        print("Hello " + self.entry1.get())

    def close(self):
        root.destroy()

root = Tk()
my_gui = MyFirstGUI(root)
root.dooneevent()

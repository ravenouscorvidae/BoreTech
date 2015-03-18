from Tkinter import *

class Base(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        
        self.initUI()
    
    def initUI(self):
      
        self.parent.title("The Menu Thing")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        remindMeInButton = Button(self, text="Remind Me In", command=pileODiags.remindMeInQ, width = 25)
        remindMeInButton.pack(padx=5, pady=1)

        testButton = Button(self, text="Test", command=pileODiags.printTest, width = 25)
        testButton.pack(padx=5, pady=1)

        quitButton = Button(self, text="Quit", command=self.quit, width = 25)
        quitButton.pack(padx=5, pady=1)

    def centerWindow(self):

        w = 200
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

class TestDialog(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)  
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Test Dialog")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        destroyButton = Button(self, text="OK", command=self.ok)
        destroyButton.place(x=50, y=70)

    def centerWindow(self):
        w = 290
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def ok(self):
        print "Button Prints"
        self.master.quit()
        self.master.destroy()
        print "and closes"

class RemindMeInQ(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.initUI()

    def initUI(self):

        self.parent.title("Remind Me In")
        self.pack(fill=BOTH, expand=1)
        
        rmi = Label(self, text = "Remind me in")
        rmi.pack()

        ## i want either a scale or an entry right here but...

        self.scale = Scale(self, from_=0, to=240, resolution=5, orient=HORIZONTAL, length=240, tickinterval=30)
        self.scale.pack()

        print self.scale.get()

        texMinutes = Label(self, text = "Minutes")
        texMinutes.pack()


        destroyButton = Button(self, text="cancel", command=self.ok)
        destroyButton.pack(side = BOTTOM)
        
        b=Button(self, text="get", command=self.scaleget)
        b.pack(side = BOTTOM)

    def scaleget(self):
        print self.scale.get()
        
    def ok(self):
        print "Button Prints"
        self.master.quit()
        self.master.destroy()
        print "and closes"

class pileODiags:
    
    @staticmethod
    def printTest():
        root = Tk()
        app = TestDialog(root)
        root.mainloop()

    @staticmethod
    def runMain():
        root = Tk()
        app = Base(root)
        root.mainloop()

    @staticmethod
    def remindMeInQ():
        root = Tk()
        app = RemindMeInQ(root)
        root.geometry("300x150+300+300")
        root.mainloop()
        
    
pileODiags.runMain()
 

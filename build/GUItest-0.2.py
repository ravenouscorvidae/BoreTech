from Tkinter import *
import time

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

        self.scale = Scale(self, from_=5, to=240, resolution=5, orient=HORIZONTAL, length=240, tickinterval=30)
        self.scale.pack()

        print self.scale.get()

        texMinutes = Label(self, text = "Minutes")
        texMinutes.pack()

        destroyButton = Button(self, text="cancel", command=self.ok)
        destroyButton.pack(side = BOTTOM)
        
        begButt = Button(self, text="Confirm", command = self.countdownStartPre)
        begButt.pack(side = BOTTOM)
        
        
        b=Button(self, text="get", command=self.scaleget)
        b.pack(side = BOTTOM)

    def scaleget(self):
        print self.scale.get()

    def printInt(self):
        print self.timeOrigScale

    def countdownStartPre(self):
        global timeOrigScale
        timeOrigScale = self.scale.get()
        print timeOrigScale
        self.ok()
        pileODiags.countdownStartDiag()
        
    def ok(self):
        print "Button Prints"
        self.master.quit()
        self.master.destroy()
        print "and closes"

class countdownStart(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        
        self.initUI()
    
    def initUI(self):
      
        self.parent.title("Reminding In...")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        timeNote = Label(self, text = "see console?")
        timeNote.pack()

        quitButton = Button(self, text="Quit", command=self.ok, width = 25)
        quitButton.pack(padx=5, pady=1)

        time.sleep(1)
        self.countdownProper()



    def centerWindow(self):

        w = 200
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def countdownProper(self):
        #Would very much like to interrupt this while loop
        global timeOrigScale
        timeCountScale = timeOrigScale * 60
        while timeCountScale > 0:
            print timeCountScale
            timeCountScale -=1
            time.sleep(1)

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
        root.mainloop()

    @staticmethod
    def countdownStartDiag():
        root = Tk()
        app = countdownStart(root)
        root.mainloop()
        
    
pileODiags.runMain()

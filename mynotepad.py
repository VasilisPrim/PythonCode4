from cProfile import label
from distutils import command
from json.tool import main
from pydoc import text
from tkinter import *
import tkinter
from tkinter.filedialog import Open
from turtle import color
from unicodedata import name
def donothing():
    filewin= Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
#Το about section του notepad
def aboutNotepad():
    filename = open("text.txt","r")
    aboutwin= Toplevel(root)
    aboutwin.title("About")
    text = Text(aboutwin,bg = "orange")
    text.insert(INSERT,filename.read())
    text.pack()
    filename.close()
#Αλλαγές χρωμάτων και γραμματοσειράς
def changeFontSize1():
    text.configure(font=("default",14-1,"normal"))

def changeFontSize2():
    text.configure(font=("default",14+4,"normal"))       

def changeFontSize3():
    text.configure(font=("default",14+7,"normal"))        
    
def changeFontSize4():
    text.configure(font=("default",14+11,"normal"))    
        
def changeFontSize5():
    text.configure(font=("default",14+14,"normal"))
def changeFontSize6():
    text.configure(font=("default",14,"normal"))
def changeColor1():
    text.config(fg = "red")
def changeColor2():
    text.config(fg = "yellow")            
def changeColor3():
    text.config(fg = "blue")
def changeColor4():
    text.config(fg = "green")

#Δημιουργία καινούργιου πλαισίου text στο notepad
def createNewtext():
    global text
    if (type(text) == Text):
            text.destroy()
    text = Text(root,xscrollcommand=scroll_barX.set,yscrollcommand=scroll_barY.set)        
    text.configure(font=("default",14,"normal"))
    text.pack(expand=True,fill="both")
#Εγγραφή αρχείου στο notepad για διάβασμα μετά το άνοιγμα    
def func(event):
    try:
        if (type(text) == Text):
            text.destroy()
        createNewtext()
        filename = open(entryText.get(),"r")
        text.insert(INSERT,filename.read())
        filename.close()
        filewin1.destroy()
    except:
        errorwin= Toplevel(root)
        errorwin.geometry("50x50")
        errorwin.title("ERROR MESSAGE")
        myleb = Label(errorwin,text = "File does not exist!",fg="red")  
        myleb.pack()
#Άνοιγμα καινούργιου φακέλου και γράψιμο των περιεχομένων του notepad
def func1(event):
    try:
        filename = open(entryText1.get(),"w")
        filename.write(text.get("1.0",END))
        filename.close()
        filewin2.destroy()
    except:
        errorwin= Toplevel(root)
        errorwin.geometry("50x50")
        errorwin.title("ERROR MESSAGE")
        myleb = Label(errorwin,text = "Could not save file!",fg="red")  
        myleb.pack()        
     
#Η συνάρτηση που χειρίζεται το άνοιγμα των αρχείων
def openFile():
    global filewin1
    filewin1= Toplevel(root)
    filewin1.title("Open")
    filewin1.geometry('250x100')
    myLabel = Label(filewin1, text="Enter a filename")
    myLabel.pack( side = LEFT)
    global entryText
    entryText = StringVar()
    myEntry = Entry(filewin1, bd =5,text = entryText )
    myEntry.bind("<Return>",func) # Η func θα γράψει το αρχείο στο notepad
    myEntry.pack(side = LEFT)
#Η συνάρτηση που χειρίζεται το 'σώσιμο' των αρχείων
def saveFile():
    global filewin2
    filewin2= Toplevel(root)
    filewin2.title("Save")
    filewin2.geometry('250x100')
    myLabel = Label(filewin2, text="Save as")
    myLabel.pack( side = LEFT) 
    global entryText1
    entryText1 = StringVar()
    myEntry = Entry(filewin2, bd =5,text = entryText1 )
    myEntry.bind("<Return>",func1) # Η func1 θα γράψει το αρχείο σε ένα φάκελο με όνομα entryText1
    myEntry.pack(side = LEFT)
    
    
    
if __name__ == "__main__":
    #Δημιουργία κυρίως παραθύρου    
    root = Tk()
    root.geometry("500x500")
    scroll_barY = Scrollbar(root)
    scroll_barX = Scrollbar(root,orient=HORIZONTAL)
    scroll_barY.pack( side = RIGHT,fill = Y )
    scroll_barX.pack( side = BOTTOM,fill = X )    
    root.title('Notepad')
    menubar= Menu(root)
    filemenu= Menu(menubar, tearoff=0)

    #Προσθήκη των menu και submenu
    filemenu.add_command(label="New", command=createNewtext)
    filemenu.add_command(label="Open", command=openFile)
    filemenu.add_command(label="Save as...", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    # --------end of file menu----------
    editmenu= Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    #-------start of font-size submenu--------
    fontSizeMenu= Menu(editmenu, tearoff=0)
    fontSizeMenu.add_command(label="-10%",command=changeFontSize1)
    fontSizeMenu.add_command(label="30%",command=changeFontSize2)
    fontSizeMenu.add_command(label="50%",command=changeFontSize3)
    fontSizeMenu.add_command(label="80%",command=changeFontSize4)
    fontSizeMenu.add_command(label="100%",command=changeFontSize5)
    fontSizeMenu.add_command(label="default",command=changeFontSize6)
    editmenu.add_cascade(label="Font-size", menu=fontSizeMenu)
    # --------end of font-size submenu----------
    textColor = Menu(editmenu,tearoff=0)
    textColor.add_command(label="red",command=changeColor1)
    textColor.add_command(label="yellow",command=changeColor2)
    textColor.add_command(label="blue",command=changeColor3)
    textColor.add_command(label="green",command=changeColor4)
    editmenu.add_cascade(label="Color", menu=textColor)
    #---------end of color submenu---------------
    # --------end of edit menu----------

    helpmenu= Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=aboutNotepad)
    menubar.add_cascade(label="Help", menu=helpmenu)
    # --------end of help menu----------
    root.config(menu=menubar)
    root.mainloop()
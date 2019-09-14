from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, askopenfilenames, askdirectory
import os.path
from subprocess import call

root = Tk()

global file_dir, final_dest

file_dir = ''
final_dest = ''
hasPassword = False

def choose_file():

    global file_dir
    
    file_dir = askopenfilename()
    
    print(file_dir)
    
    #check if file exists
    try:
        check = os.path.exists(file_dir)
        if check == False:
            raise ValueError('File does not exist')
    except(ValueError,IndexError):
        print("FILE NOT FOUND!")

def choose_files():

    global file_dir
    global long_string
    
    file_dir = askopenfilenames()

    file_dir = list(file_dir)
    
    long_string = ' '.join(file_dir)
    long_string = str(long_string)
    file_dir = long_string

    print(long_string)
    
    #check if file exists
##    try:
##        check = os.path.exists(file_dir)
##        if check == False:
##            raise ValueError('File does not exist')
##    except(ValueError,IndexError):
##        print("FILE NOT FOUND!")

def choose_dest():

    global final_dest

    final_dest = askdirectory(parent=root,initialdir="/home/pi",title='Please select a directory')
    
    print(final_dest)
    
    #check if directory exists
    try:
        check = os.path.exists(final_dest)
        if check == False:
            raise ValueError('False Path')
    except(ValueError,IndexError):
        print("PATH NOT FOUND")

def to_commandline():

    global file_dir, final_dest, hasPassword

    commander =   "sudo mv " + file_dir + " " + final_dest 

    os.system(commander)
    print(commander)
    call(str(commander), shell=True)  

Title = root.title( "SUDO extractor 1.0")

b1 = Button(root, text="SELECT A FILE", command=choose_file)
b1.pack()

b2 = Button(root, text="SELECT MULTIPLE FILES", command=choose_files)
b2.pack()

b3 = Button(root, text="SELECT DESTINATION", command=choose_dest)
b3.pack()

b4 = Button(root, text="EXTRACT", command=to_commandline)
b4.pack()

b5 = Button(root, text="EXIT", command=lambda:exit())
b5.pack()

root.mainloop()

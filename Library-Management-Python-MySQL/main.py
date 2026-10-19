from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# --- Database Connection ---
mypass = "Pratham@7972#"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

ROOT_BG = "#F0F8FF"      
HEADER_BG = "#0D47A1"   
HEADER_FG = "white"
BUTTON_BG ="#2196F3"    
BUTTON_FG = "white"
BUTTON_ACTIVE_BG = "#1976D2" 

HEADING_FONT = ('Arial', 16, 'bold')
SUBHEADING_FONT = ('Arial', 9, 'italic')
BUTTON_FONT = ('Arial', 11, 'bold')

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
root.config(bg=ROOT_BG) 

same=True
n=0.25

background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg=ROOT_BG, width=newImageSizeWidth, height=newImageSizeHeight, highlightthickness=0)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root, bg=HEADER_BG, bd=3, relief='ridge') 
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n DYP-Books Library", 
                     bg=HEADER_BG, fg=HEADER_FG, font=HEADING_FONT)
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.7)

subHeadingLabel = Label(headingFrame1, text="by: Prathmesh, Shrinivas, Anish & Abhay", 
                        bg=HEADER_BG, fg=HEADER_FG, font=SUBHEADING_FONT)
subHeadingLabel.place(relx=0,rely=0.7, relwidth=1, relheight=0.3)


button_options = {
    'bg': BUTTON_BG,
    'fg': BUTTON_FG,
    'font': BUTTON_FONT,
    'relief': 'raised',         
    'activebackground': BUTTON_ACTIVE_BG,
    'activeforeground': BUTTON_FG,
    'bd': 2
}

btn1 = Button(root,text="Add Book Details", command=addBook, **button_options)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book", command=delete, **button_options)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List", command=View, **button_options)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student", command = issueBook, **button_options)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book", command = returnBook, **button_options)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
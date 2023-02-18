from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.font as font
import runpy

#creating root after the teacher logs in
project=Tk()
project.configure(bg="white")
project.attributes("-fullscreen",True)

screen_width = project.winfo_screenwidth()
screen_height= project.winfo_screenheight()
#creating title bar
a=Frame(project,width=screen_width,height=35,bg="#57a1f8").place(x=0,y=0)
title=Label(a, text="AccuResult",font=("Comic Sans MS",15,"bold"), bg="#57a1f8").place(x=36,y=0)
img=Image.open(r"C:\Users\LENOVO\Documents\python_learning\sem_class\tkinter\logo.png") #image logo
img=img.resize((30,30))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=0,bg="#57a1f8").place(x=5,y=3)


#making maximize and minimize button manually
def min():
    project.iconify()
def on_enter(i):
    btn2['background']="red"
def on_leave(i):
    btn2['background']="#57a1f8"
def max():
    msg_box =messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?',icon='warning')
    if msg_box == 'yes':
        project.destroy()
label1=LabelFrame(project,height=35,fg="blue",bg="#57a1f8").place(x=0,y=0)
buttonFont = font.Font(size=14)

btn2=Button(a,text="✕", command=max,width=4,bg="#57a1f8",border=0,font=buttonFont)
btn2.pack(anchor="ne")
btn2.bind('<Enter>',on_enter)
btn2.bind('<Leave>',on_leave)

btn=Button(a,text="-", command=min,width=4,bg="#57a1f8",border=0,font=buttonFont)
btn.place(x=screen_width-100,y=0)
def enter(i):
    btn['background']="red"
def leave(i):
    btn['background']="#57a1f8"
btn.bind('<Enter>',enter)
btn.bind('<Leave>',leave)

#Inserting picture
img=ImageTk.PhotoImage(Image.open(r"AccuResult.png"))
image=Label(image=img,bg="white").place(x=50,y=(screen_height/4)+25)

#create frame
frame1=Frame(project,width=450,height=445,bg="white", highlightthickness=2,highlightbackground="black")
frame1.place(x=screen_width-550,y=screen_height/5)

heading=Label(frame1,text='AccuResult',fg="#57a1f8",bg="white",font=("Arial",30))
heading.place(x=121,y=25)
#defining function for taking username stdID after the "Check result" button has been clicked
des=Image.open(r"description.png") #image logo
des=des.resize((438,220))
des=ImageTk.PhotoImage(des)
detail=Label(frame1,image=des,border=0)
detail.place(x=5,y=90)
buttonFont1 = font.Font(size=13)
#defining function for creating result
def create():
    project.destroy()
    runpy.run_path(
        "final_login.py")
def check():
    frame2=Frame(project,width=450,height=445,bg="white", highlightthickness=2,highlightbackground="black")
    frame2.place(x=screen_width-550,y=screen_height/5)
    heading2=Label(frame2,text='Check Result',fg="#57a1f8",bg="white",font=("Arial",30))
    heading2.place(x=100,y=30)
    def on_enter(w):
        name=user.get()
        if name=="StudentName":
            user.delete(0,"end")
    def on_leave(w):
        name=user.get()
        if name=="":
            user.insert(0,"StudentName")
    user=Entry(frame2,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    user.place(x=50,y=130)
    user.insert(0,"StudentName")
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame2,width=340,height=2,bg="black").place(x=50,y=157)
    def on_enter(w):
        name=code.get()
        if name=="StudentID":
            code.delete(0,"end")
    def on_leave(w):
        name=code.get()
        if name=="":
            code.insert(0,"StudentID")  
    code=Entry(frame2,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    code.place(x=50,y=230)
    code.insert(0,"StudentID")
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    Frame(frame2,width=340,height=2,bg="black").place(x=50,y=257)
    def o_enter(a):
        c['background']='#7ab3f5'
    def o_leave(a):
        c['background']='#57a1f8'
    def result():
        messagebox.showerror("Error","No Result found")
    c=Button(frame2,width=40,pady=7,text="Fetch Result",bg="#57a1f8",fg="white",border=0,command=result,font=buttonFont1,activebackground="#57a1f8",activeforeground="white")
    c.place(x=38,y=305)
    c.bind('<Enter>',o_enter)
    c.bind('<Leave>',o_leave)

    def back():
        frame2.destroy()
        btn4.destroy()
    btn4=Button(project,text="<<",width=4,bg="#57a1f8",border=0,font=buttonFont,command=back)
    btn4.place(x=screen_width-150,y=0)
    def enter(i):
        btn4['background']="red"
    def leave(i):
        btn4['background']="#57a1f8"
    btn4.bind('<Enter>',enter)
    btn4.bind('<Leave>',leave)

des=Image.open(r"description.png") #image logo
des=des.resize((438,220))
des=ImageTk.PhotoImage(des)
detail=Label(frame1,image=des,border=0,bg="white")
detail.place(x=5,y=90)

#buttons for Checking and creating results
btn3=Button(frame1,text="Check Result",width=15,height=1,bg="light green",border=0,font=("Calibri",15,"bold"),command=check)
btn3.place(x=145,y=325)
btn4=Button(frame1,text="Create Result",width=15,height=1,bg="light green",border=0,font=("Calibri",15,"bold"),command=create)
btn4.place(x=145,y=380)

project.mainloop()
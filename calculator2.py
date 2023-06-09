import tkinter
import customtkinter
from PIL import Image, ImageTk

def b1act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"1")
    
def b2act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"2")
    
def b3act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"3")
    
def b4act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"4")
    
def b5act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"5")
    
def b6act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"6")
    
def b7act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"7")
    
def b8act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"8")
    
def b9act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"9")
    
def b00act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"00")
    
def b0act():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"0")
    
def bdotact():
    l=len(entrybox_variable.get())
    entrybox.insert(l,".")

def bdivact():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"/")
    
def bmulact():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"*")

def bsubact():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"-")

def baddact():
    l=len(entrybox_variable.get())
    entrybox.insert(l,"+")


def clear():
    l=len(entrybox_variable.get())
    entrybox.delete(0,l+1)
    
def answer():
    expression=entrybox_variable.get()
    try:
        result=eval(expression)
    except:
        result="Error! INVALID EXPRESSION"
    finally:
        l=len(entrybox_variable.get())
        entrybox.delete(0,l+1)
        entrybox.insert(0,result)

window=customtkinter.CTk()
window.title("Calculator")
window.geometry("550x700")

heading_label1=customtkinter.CTkLabel(master=window,text="Calculator",font=("Century Gothic",50))
heading_label1.pack()

heading_label2=customtkinter.CTkLabel(master=window,text="-----------------------------------------",font=("Century Gothic",36))
heading_label2.pack()

entrybox_variable=customtkinter.StringVar()
entrybox=customtkinter.CTkEntry(master=window,width=475,height=100,font=("Century Gothic",30),textvariable=entrybox_variable)
entrybox.pack()

button1=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="1",hover_color="green",command=b1act)
button1.place(x=38,y=225)

button2=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="2",hover_color="green",command=b2act)
button2.place(x=163,y=225)

button3=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="3",hover_color="green",command=b3act)
button3.place(x=288,y=225)

button_div=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="/",hover_color="green",command=bdivact)
button_div.place(x=413,y=225)

button4=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="4",hover_color="green",command=b4act)
button4.place(x=38,y=300)

button5=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="5",hover_color="green",command=b5act)
button5.place(x=163,y=300)

button6=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="6",hover_color="green",command=b6act)
button6.place(x=288,y=300)

button_mul=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="*",hover_color="green",command=bmulact)
button_mul.place(x=413,y=300)

button7=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="7",hover_color="green",command=b7act)
button7.place(x=38,y=375)

button8=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="8",hover_color="green",command=b8act)
button8.place(x=163,y=375)

button9=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="9",hover_color="green",command=b9act)
button9.place(x=288,y=375)

button_sub=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="-",hover_color="green",command=bsubact)
button_sub.place(x=413,y=375)

button00=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="00",hover_color="green",command=b00act)
button00.place(x=38,y=450)

button0=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="0",hover_color="green",command=b0act)
button0.place(x=163,y=450)

button_dot=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text=".",hover_color="green",command=bdotact)
button_dot.place(x=288,y=450)

button_add=customtkinter.CTkButton(master=window,width=100,height=50,corner_radius=5,font=("Century Gothic",30),text="+",hover_color="green",command=baddact)
button_add.place(x=413,y=450)

button_equal=customtkinter.CTkButton(master=window,width=475,height=50,corner_radius=5,font=("Century Gothic",30),text="Answer",hover_color="green",command=answer)
button_equal.place(x=38,y=525)

button_clear=customtkinter.CTkButton(master=window,width=475,height=50,corner_radius=5,font=("Century Gothic",30),text="Clear",hover_color="green",command=clear)
button_clear.place(x=38,y=600)

window.mainloop()
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("545x550")
root.configure(bg="#17161b")

label_result=Label(root,width=81,height=1,text="",font=("arial",30,"bold"))
label_result.pack()

equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

# Button creation and placeing on the screen

Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:clear()).place(x=5,y=65)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("/")).place(x=140,y=65)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("%")).place(x=275,y=65)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("*")).place(x=410,y=65)

Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("7")).place(x=5,y=160)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("8")).place(x=140,y=160)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("9")).place(x=275,y=160)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("-")).place(x=410,y=160)

Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("4")).place(x=5,y=255)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("5")).place(x=140,y=255)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("6")).place(x=275,y=255)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("+")).place(x=410,y=255)

Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("1")).place(x=5,y=350)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("2")).place(x=140,y=350)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("3")).place(x=275,y=350)

Button(root,text="0",width=10,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show("0")).place(x=5,y=442)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:show(".")).place(x=275,y=442)

Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),fg="#fff",bg="blue",command=lambda:calculate()).place(x=410,y=350)

root.mainloop()
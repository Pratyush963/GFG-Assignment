from tkinter import messagebox
window=Tk()
window.title("Simple interest calculator")
window.geometry("500x500")
def clicked():
 x=str(int(txt.get())*float(txt1.get())*int(txt2.get()))
 window.destroy()
 messagebox.showinfo("click","The simple interest is"+" "+x)
lbl1=Label(window,text="Simple interest calculator",font=("calibri",20),bg="b
lack",fg="violet")
lbl1.place(x=100,y=20)
lbl=Label(window,text="Principle",font=("comic sans ms",15),fg="blue",bg="bla
ck")
lbl.place(x=50,y=100)
lbl2=Label(window,text="Rate(in decimal)",font=("comic sans ms",15),fg="blue"
,bg="black")
lbl2.place(x=50,y=200)
lbl3=Label(window,text="Time",font=("comic sans ms",15),fg="blue",bg="black")
lbl3.place(x=50,y=300)
txt=Entry(window,bd=10,bg="black",fg="white")
txt.place(x=200,y=100)
txt1=Entry(window,bd=10,bg="black",fg="white")
txt1.place(x=200,y=200)
txt2=Entry(window,bd=10,bg="black",fg="white")
txt2.place(x=200,y=300)
butt=Button(window,text="calculate",fg="dark green",bg="black",command=clicke
d)
butt.place(x=250,y=400)
window.configure(background="black")
window.mainloop()
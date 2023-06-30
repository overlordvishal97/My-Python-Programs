from tkinter import *

window=Tk()

def kg_to_grams_pounds_ounces():
    print(e2_value.get())
    grams=float(e2_value.get())*1000
    pounds=float(e2_value.get())*2.205
    ounces=float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END,grams)
    t2.delete("1.0",END)
    t2.insert(END,pounds)
    t3.delete("1.0",END)
    t3.insert(END,ounces)

e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

b1=Button(window,text="Convert",command=kg_to_grams_pounds_ounces)
b1.grid(row=0,column=3)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=2)


t1=Text(window,height=1,width=25)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=25)
t2.grid(row=1,column=2)

t3=Text(window,height=1,width=25)
t3.grid(row=1,column=3)

window.mainloop()
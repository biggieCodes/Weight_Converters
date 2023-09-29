from tkinter import *
# Creating a GUI Window
window = Tk()
window.title("Weight Converter")

def from_kg():
    gram  = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    tonnes = float(e2_value.get())*2000
    
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
    t4.delete("1.0", END)
    t4.insert(END, tonnes)
    t5.delete("1.0", END)
    t5.insert(END, tonnes)
    t6.delete("1.0", END)
    t6.insert(END, tonnes)
    

    

e1 = Label(window, text="Input the weight in Kilogram")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")
e6 = Label(window,text="Tonne")

t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)
t4 = Text(window, height=5, width=30)
t5 = Text(window, height=5, width=30)
t6 = Text(window, height=5, width=30)


b1 = Button(window, text="Convert",width=10,activebackground= "blue",activeforeground= "grey", command=from_kg)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
e6.grid(row=1, column=3)

t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=2, column=3)
#t5.grid(row=2, column=4)
#t6.grid(row=2, column=5)

b1.grid(row=0, column=2)

window.mainloop()
from tkinter import *

tk = Tk()
tk.minsize(width=300, height=300)
def calculate():
    label1.config(text=float(entry.get())*1.6)

entry = Entry(width=10, font=(30))
entry.grid(row=0, column=1)

label = Label(text="Miles", font=(20)).grid(row=0, column=2)

label = Label(text="is equal to").grid(row=1, column=0)

label1 = Label(width=10, height=1)
label1.grid(row=1, column=1)

label = Label(text="Kms", font=20).grid(row=1, column=2)

button = Button(text="Calculate", command=calculate).grid(row=2, column=1)


tk.mainloop()
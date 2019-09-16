import tkinter as tk

def onclick():
    print ("Exit")
    root.distroy()

root = tk.Tk()

l1 = tk.Label(root,text = "Enter Name")
l1.pack()

e1 = tk.Entry(root)
e1.pack()

b1 = tk.Button(root,text = "Exit")
b1.pack()


root.mainloop()
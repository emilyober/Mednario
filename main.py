from customtkinter import *
from tkinter import *
import tkinter as tk

app = CTk()
app.geometry("900x600")
app.resizable(False,False)
set_appearance_mode("light")
app.title("Mednario")
app.attributes('-topmost',True)

canvas= tk.Canvas(app,width= 900, height=600, bg="grey92")
canvas.pack(fill=BOTH,expand=True)
canvas.create_oval(-10, -10, 100, 100, fill="", outline="#C4B7BB", width=10)
canvas.create_oval(830, 500, 940, 610, fill="", outline="#C4B7BB", width=10)
canvas.create_oval(40, 70, 140, 170, fill="", outline="#FAE0D8", width=10)
canvas.create_oval(950, 30, 1050, 130, fill="", outline="#FAE0D8", width=10)
canvas.create_oval(850, 570, 980, 700, fill="", outline="#DFE1BE", width=10)
canvas.create_oval(1000, -30, 1150, 120, fill="", outline="#DFE1BE", width=10)
canvas.create_oval(1000, 400, 1200, 600, fill="", outline="#F1DEEE", width=10)
canvas.create_oval(250, -150, 500, 100, fill="", outline="#F1DEEE", width=10)
main_label = CTkLabel(app, text="Mednario", font=('Fredoka One Regular', 45))
main_label.place(relx=0.5,rely=0.3, anchor="center")

app.mainloop()

from customtkinter import *
from tkinter import *
import tkinter as tk
import gspread

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
def game_screen():
    pass
def check_userandpass():
    if user_data_worksheet.find(username.get(0.0,'end'),in_column=1) != None:
        username_row = (user_data_worksheet.find(username.get(),in_column=1)).row
        if password.get(0.0,'end') in user_data_worksheet.row_values(username_row):
            game_screen()
        else:
            error_lab = CTkLabel(sign_in_win, text="Incorrect Password", font=('Fredoka One Regular', 20), text_color='red')
            error_lab.place(relx=0.5,rely=0.8, anchor="center")
    else:
        error_lab = CTkLabel(sign_in_win, text="Username Not Found", font=('Fredoka One Regular', 20), text_color='red')
        error_lab.place(relx=0.5,rely=0.9, anchor="center")

def sign_in():
    global username
    global password
    global sign_in_win
    sign_in_win = CTkToplevel()
    sign_in_win.title("Sign In")
    sign_in_win.geometry("500x300")
    sign_in_win.resizable(False,False)
    app.attributes('-topmost', False)
    sign_in_win.attributes('-topmost', True)
    username_lab = CTkLabel(sign_in_win, text="Username:", font=('Fredoka One Regular', 20))
    username_lab.place(relx=0.5,rely=0.15, anchor="center")
    username= CTkTextbox(sign_in_win, width= 300, height=30, font=('Fredoka One Regular', 15), wrap="none")
    username.place(relx=0.5,rely=0.3, anchor="center")
    password_lab = CTkLabel(sign_in_win, text="Password:", font=('Fredoka One Regular', 20))
    password_lab.place(relx=0.5,rely=0.45, anchor="center")
    password= CTkTextbox(sign_in_win, width= 300, height=30, font=('Fredoka One Regular', 15), wrap="none")
    password.place(relx=0.5,rely=0.6, anchor="center")
    enter_button = CTkButton(sign_in_win, text="Enter", font = ('Fredoka One Regular', 15), corner_radius=10, fg_color= "grey50", hover_color="#C4B7BB", command=check_userandpass)
    enter_button.place(relx=0.5,rely=0.75, anchor="center")
def sign_up():
    pass
sign_in_button = CTkButton(app,text="Sign In", font = ('Fredoka One Regular', 15), corner_radius=10, fg_color= "grey50", hover_color="#C4B7BB", command=sign_in)
sign_up_button = CTkButton(app,text="Sign Up", font = ('Fredoka One Regular', 15), corner_radius=10, fg_color= "grey50", hover_color="#C4B7BB", command=sign_up)
sign_in_button.place(relx=0.5,rely=0.47, anchor="center")
sign_up_button.place(relx=0.5,rely=0.53, anchor="center")
ud = gspread.service_account("user-data-mednario-612c17fd8e4f.json")
spreadsheet = ud.open('Mednario_User_Data')
user_data_worksheet = spreadsheet.get_worksheet(0)
scenario_posts_worksheet = spreadsheet.get_worksheet(1)

app.mainloop()

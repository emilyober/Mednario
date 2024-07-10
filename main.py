from customtkinter import *
from tkinter import *
import tkinter as tk
import gspread
from PIL import ImageTk, Image
import PIL as pillow

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
    main = CTkToplevel()  
    main.geometry("900x600")
    main.resizable(False,False)
    main.title("Mednario")
    main.attributes('-topmost',True)
    canvas= tk.Canvas(main,width= 900, height=600, bg="grey92")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_oval(-10, -10, 100, 100, fill="", outline="#C4B7BB", width=10)
    canvas.create_oval(830, 500, 940, 610, fill="", outline="#C4B7BB", width=10)
    canvas.create_oval(40, 70, 140, 170, fill="", outline="#FAE0D8", width=10)
    canvas.create_oval(950, 30, 1050, 130, fill="", outline="#FAE0D8", width=10)
    canvas.create_oval(850, 570, 980, 700, fill="", outline="#DFE1BE", width=10)
    canvas.create_oval(1000, -30, 1150, 120, fill="", outline="#DFE1BE", width=10)
    canvas.create_oval(1000, 400, 1200, 600, fill="", outline="#F1DEEE", width=10)
    canvas.create_oval(250, -150, 500, 100, fill="", outline="#F1DEEE", width=10)
    title_label = CTkLabel(main, text="Mednario", font=('Fredoka One Regular', 50))
    title_label.place(relx=0.5,rely=0.27, anchor="center")
    frame1 = CTkFrame(main,225,350,bg_color="grey92",fg_color="grey92")
    frame1.place(relx=0.5,rely=0.56,anchor="e")
    frame2 = CTkFrame(main,225,350,bg_color="grey92",fg_color="grey92")
    frame2.place(relx=0.5,rely=0.56,anchor="w")
    my_feed_but = CTkButton(frame1, width=215, height = 115, text="My Feed",font = ('Fredoka One Regular', 20),fg_color= "#D9A797", command=sign_in)
    my_feed_but.pack(anchor='nw',fill='both',padx=10,pady=10)
    daily_scenario_but = CTkButton(frame2,width=215, height = 115, text="Daily Scenario",font = ('Fredoka One Regular', 20),fg_color= "#D4A3CC", command=sign_in)
    daily_scenario_but.pack(anchor='ne',fill='both',padx=10,pady=10)
    timed_challenge_but = CTkButton(frame1,width=215, height = 115, text="Timed Challenge",font = ('Fredoka One Regular', 20),fg_color= "#AAAD74", command=sign_in)
    timed_challenge_but.pack(anchor='sw',fill='both',padx=10,pady=10)
    classic_scenarios_but = CTkButton(frame2,width=215, height = 115, text="Classic Scenarios",font = ('Fredoka One Regular', 20),fg_color= "#B78C99", command=sign_in)
    classic_scenarios_but.pack(anchor='se',fill='both',padx=10,pady=10)
    profile_but_pic = CTkImage(light_image=pillow.Image.open("Screenshot 2024-07-09 192127.png"), size=(100,100))
    profile_but = CTkButton(main,width=100,height=100,text="",image=profile_but_pic, bg_color="grey92",fg_color="grey92", hover_color="grey92")
    profile_but.place(relx=0.01,rely=0.99,anchor="sw")




def new_userandpass():
    if user_data_worksheet.find(username.get(0.0,'end'),in_column=1) == None:
        if len(password.get(0.0,'end'))>=8:
            user_data_worksheet.append_row([username.get(0.0,'end'),password.get(0.0,'end'),0,0,0])
            sign_up_win.destroy()
            game_screen()
        else:
            error_lab = CTkLabel(sign_up_win, text="Password is Too Short", font=('Fredoka One Regular', 15), text_color='red')
            error_lab.place(relx=0.5,rely=0.9, anchor="center")
    else:
        error_lab = CTkLabel(sign_up_win, text="Username Already Exists", font=('Fredoka One Regular', 15), text_color='red')
        error_lab.place(relx=0.5,rely=0.9, anchor="center")
def check_userandpass():
    if user_data_worksheet.find(username.get(0.0,'end'),in_column=1) != None:
        username_row = (user_data_worksheet.find(username.get(0.0,'end'),in_column=1)).row
        if password.get(0.0,'end') in user_data_worksheet.row_values(username_row):
            sign_in_win.destroy()
            game_screen()
        else:
            error_lab = CTkLabel(sign_in_win, text="Incorrect Password", font=('Fredoka One Regular', 15), text_color='red')
            error_lab.place(relx=0.5,rely=0.9, anchor="center")
    else:
        error_lab = CTkLabel(sign_in_win, text="Username Not Found", font=('Fredoka One Regular', 15), text_color='red')
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
    enter_button.place(relx=0.5,rely=0.76, anchor="center")
def sign_up():
    global username
    global password
    global sign_up_win
    sign_up_win = CTkToplevel()
    sign_up_win.title("Sign Up")
    sign_up_win.geometry("500x300")
    sign_up_win.resizable(False,False)
    app.attributes('-topmost', False)
    sign_up_win.attributes('-topmost', True)
    username_lab = CTkLabel(sign_up_win, text="Username:", font=('Fredoka One Regular', 20))
    username_lab.place(relx=0.5,rely=0.15, anchor="center")
    username= CTkTextbox(sign_up_win, width= 300, height=30, font=('Fredoka One Regular', 15), wrap="none")
    username.place(relx=0.5,rely=0.3, anchor="center")
    password_lab = CTkLabel(sign_up_win, text="Password:", font=('Fredoka One Regular', 20))
    password_lab.place(relx=0.5,rely=0.45, anchor="center")
    password_req = CTkLabel(sign_up_win, text="Password must be at least 8 characters", font=('Fredoka One Regular', 9), text_color='grey40')
    password_req.place(relx= 0.5, rely=0.68, anchor="center")
    password= CTkTextbox(sign_up_win, width= 300, height=30, font=('Fredoka One Regular', 15), wrap="none")
    password.place(relx=0.5,rely=0.6, anchor="center")
    enter_button = CTkButton(sign_up_win, text="Enter", font = ('Fredoka One Regular', 15), corner_radius=10, fg_color= "grey50", hover_color="#C4B7BB", command=new_userandpass)
    enter_button.place(relx=0.5,rely=0.77, anchor="center")


sign_in_button = CTkButton(app,text="Sign In", font = ('Fredoka One Regular', 15), corner_radius=10, fg_color= "grey50", hover_color="#C4B7BB", command=sign_in)
sign_up_button = CTkButton(app,text="Sign Up", font = ('Fredoka One Regular', 15), corner_radius=10, fg_color= "grey50", hover_color="#C4B7BB", command=sign_up)
sign_in_button.place(relx=0.5,rely=0.47, anchor="center")
sign_up_button.place(relx=0.5,rely=0.53, anchor="center")
ud = gspread.service_account("user-data-mednario-612c17fd8e4f.json")
spreadsheet = ud.open('Mednario_User_Data')
user_data_worksheet = spreadsheet.get_worksheet(0)
scenario_posts_worksheet = spreadsheet.get_worksheet(1)

app.mainloop()

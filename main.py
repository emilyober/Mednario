from customtkinter import *
from tkinter import *
import tkinter as tk
import gspread
from PIL import ImageTk, Image
import PIL as pillow
from datetime import date

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
def post_daily():
    global anon_post_check
    global scen_box
    global daily_scen_ans
    user_data_worksheet.update_cell(username_row,3,int(user_data_worksheet.cell(username_row,3).value)+10)
    try:
        daily_scen_ans = str(scen_box.get(0.0,'end'))
        daily_scen.destroy()
    except:
        grade_d.destroy()
    user_data_worksheet.update_cell(username_row,6,1)
    scenario_posts_worksheet.append_row([username_,anon_post_check.get(),scenario,daily_scen_ans,0,0,"",str(date.today())])
def grade_daily():
    global scen_box
    global grade_d
    global daily_scen_ans
    daily_scen_ans = str(scen_box.get(0.0,'end'))
    daily_scen.destroy()
    grade_d = CTkToplevel()
    grade_d.geometry("700x500")
    grade_d.resizable(False,False)
    grade_d.title("Auto Grader")
    grade_d.attributes('-topmost',True)
    canvas=tk.Canvas(grade_d,width=800,height=600,bg="#D4A3CC",highlightthickness=0)
    canvas.pack(expand=True,fill=BOTH)
    com_lab = CTkLabel(canvas, text="Computer Grade:",font=('Fredoka One Regular', 20),bg_color="#D4A3CC",fg_color="#D4A3CC")
    com_lab.place(relx=0.05,rely=0.05,anchor="nw")
    frame = CTkFrame(canvas, width=600,height=125,corner_radius= 10,bg_color="#D4A3CC",fg_color="grey87")
    frame.place(relx=0.5,rely=0.13,anchor="n")
    keyword_list = []
    keywords = (str(daily_scen_worksheet.cell(daily_scen_row,3).value)).split(',')
    for keyword in keywords:
        if keyword in daily_scen_ans.lower():
            keyword_list.append(keyword)
    if len(keyword_list) == 0:
        computer_message = "Incorrect. Your response does not reflect how this scenario would typically be answered by other medical professionals. If you believe your response is correct, please answer the question below to improve the automatic grading system."
    elif len(keyword_list) == 1:
        computer_message = "Correct! Other medical professionals used the word " + keyword_list[0] + " in their response."
    else:
        computer_message = "Correct! Other medical professionals used the words " + keyword_list[0] + " and " + keyword_list[1] + " in their response."
    com_grade = CTkLabel(frame, text=computer_message,font=('Fredoka One Regular', 15),bg_color="grey87",fg_color="grey87",wraplength=550)
    com_grade.place(relx=0.5,rely=0.5,anchor="center")
    auto_text = CTkLabel(grade_d, text="To help the auto grader become more accurate, please answer the following question: "+ str(daily_scen_worksheet.cell(daily_scen_row,4).value),font=('Fredoka One Regular', 15),bg_color="#D4A3CC",fg_color="#D4A3CC",wraplength=650)
    auto_text.place(relx=0.05,rely=0.45,anchor="nw")
    auto_textbox = CTkTextbox(grade_d,width=600,height=30,font=('Fredoka One Regular', 15),bg_color="#D4A3CC",fg_color="grey87",corner_radius=10)
    auto_textbox.place(relx=0.5,rely=0.58,anchor="n")
    def post_but():
        post_scen_but = CTkButton(grade_d,width=150,height=40,text="Post Scenario",font=('Fredoka One Regular', 18),bg_color="#D4A3CC",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=post_daily)
        post_scen_but.place(relx=0.5,rely=0.82,anchor="n")
    def enter_text():
        if (' ' not in str(auto_textbox.get(0.0,'end'))) and ((str(auto_textbox.get(0.0,'end'))).strip() not in str(daily_scen_worksheet.cell(daily_scen_row,3).value)):
            daily_scen_worksheet.update_cell(daily_scen_row,3,(str(daily_scen_worksheet.cell(daily_scen_row,3).value)).strip()+","+((str(auto_textbox.get(0.0,'end'))).strip()).lower())
        auto_textbox.delete(0.0,'end')
        auto_textbox.insert(0.0,'Thank you for your response!')
        post_but()
    enter_but = CTkButton(grade_d,width=100,height=30,text="Submit",font=('Fredoka One Regular', 15),bg_color="#D4A3CC",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=enter_text)
    enter_but.place(relx=0.35,rely=0.7,anchor="n")
    no_but = CTkButton(grade_d,width=100,height=30,text="No Thanks",font=('Fredoka One Regular', 15),bg_color="#D4A3CC",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=post_but)
    no_but.place(relx=0.65,rely=0.7,anchor="n")
def daily_scenario():
    global anon_post_check
    global scenario
    global daily_scen
    global daily_scen_row
    global scen_box
    if int(user_data_worksheet.cell(username_row,6).value) == int(0):
        daily_scen = CTkToplevel()  
        daily_scen.geometry("700x500")
        daily_scen.resizable(False,False)
        daily_scen.title("Daily Scenario")
        main.attributes("-topmost",False)
        daily_scen.attributes('-topmost',True)
        canvas10=tk.Canvas(daily_scen,width=800,height=600,bg="#D4A3CC",highlightthickness=0)
        canvas10.pack(expand=True,fill=BOTH)
        canvas10.create_line(0,30,1000,30,width=2)
        date_label= CTkLabel(canvas10, text=" "+str(date.today())+" ",font=('Fredoka One Regular', 15),bg_color="#D4A3CC",fg_color="#D4A3CC")
        date_label.place(relx=0.02,rely=0.018,anchor="nw")
        daily_scen_row = (daily_scen_worksheet.find(str(date.today()),in_column=1)).row 
        scenario_data = daily_scen_worksheet.row_values(daily_scen_row)
        scenario = str(scenario_data[1])
        daily_scen_lab = CTkLabel(canvas10, text="Scenario: "+scenario,font=('Fredoka One Regular', 20),bg_color="#D4A3CC",fg_color="#D4A3CC",wraplength=670)
        daily_scen_lab.place(relx=0.02,rely=0.08,anchor="nw")
        scen_box = CTkTextbox(daily_scen,width=650,height=250,font=('Fredoka One Regular', 15))
        scen_box.place(relx=0.5,rely=0.2,anchor="n")
        anon_post_check = CTkCheckBox(daily_scen,text="Post Anonymously",font=('Fredoka One Regular', 15),bg_color="#D4A3CC",fg_color="#D4A3CC")
        anon_post_check.place(relx=0.95,rely=0.72,anchor="ne")
        auto_grade_but = CTkButton(canvas10,width=100,height=30,text="Auto Grade",font=('Fredoka One Regular', 15),fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=grade_daily)
        auto_grade_but.place(relx=0.5,rely=0.83,anchor="center")
        post_scen_but = CTkButton(canvas10,width=100,height=30,text="Post Scenario",font=('Fredoka One Regular', 15),fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=post_daily)
        post_scen_but.place(relx=0.5,rely=0.92,anchor="center")
    else:
        daily_scen = CTkToplevel()  
        daily_scen.geometry("500x300")
        daily_scen.resizable(False,False)
        daily_scen.title("Daily Scenario")
        main.attributes("-topmost",False)
        daily_scen.attributes('-topmost',True)
        canvas=tk.Canvas(daily_scen,width=800,height=600,bg="#D4A3CC",highlightthickness=0)
        canvas.pack(expand=True,fill=BOTH)
        daily_scen_lab = CTkLabel(canvas, text='Already completed! Go to "My Posts" in the profile window to view your response and peer feedback.',font=('Fredoka One Regular', 20),bg_color="#D4A3CC",fg_color="#D4A3CC",wraplength=450)
        daily_scen_lab.place(relx=0.5,rely=0.5,anchor="center")

def profile_screen():
    global username_
    profile = CTkToplevel()  
    profile.geometry("700x500")
    profile.resizable(False,False)
    profile.title("Profile")
    main.attributes("-topmost",False)
    profile.attributes('-topmost',True)
    canvas1 = tk.Canvas(profile,width=800,height=600,bg="#FFDDA6",highlightthickness=0)
    canvas1.pack(expand=True,fill=BOTH)
    canvas2 = tk.Canvas(profile,width=700,height=575,bg="#E6B25E",highlightthickness=0)
    canvas2.place(relx=1,rely=1,anchor='se')
    username_label= CTkLabel(canvas1, text="Username: "+username_,font=('Fredoka One Regular', 15),bg_color="#FFDDA6",fg_color="#FFDDA6")
    username_label.place(relx=0.01,rely=0.02,anchor="nw")
    my_profile = CTkButton(canvas1,width=142,height=60,text="My Profile",font=('Fredoka One Regular', 15),corner_radius=0,fg_color= "#E6B25E",hover_color="#E6B25E",text_color="black")
    my_profile.place(relx=0,rely=0.08,anchor="nw")
    my_posts = CTkButton(canvas1,width=140,height=60,text="My Posts",font=('Fredoka One Regular', 15),corner_radius=0,border_color="black",border_width=1,fg_color= "#FFDDA6",hover_color="#FFDDA6",text_color="black")
    my_posts.place(relx=0,rely=0.2,anchor="nw")
    joined_lab = CTkLabel(canvas2,text="Joined "+str(user_data_worksheet.row_values(username_row)[5]),font=('Fredoka One Regular', 15),bg_color="#E6B25E",fg_color="#E6B25E")
    joined_lab.place(relx=0.02,rely=0.98,anchor="sw")
    canvas2.create_rectangle(60,30,610,50,outline="black")
    canvas2.create_rectangle(60,30,60+round(int(user_data_worksheet.row_values(username_row)[2])*1.83333),50,fill="#D4A3CC")
    canvas2.create_oval(40, 20, 80, 60, fill="#643715",outline="")
    canvas2.create_oval(223, 20, 263, 60, fill="#C0C0C0",outline="")
    canvas2.create_oval(427, 20, 467, 60, fill="#D4AF37",outline="")
    canvas2.create_oval(590, 20, 630, 60, fill="#CFE4EE",outline="")      
    current_rank_lab = CTkLabel(canvas2,text="Current Rank: "+ rank +" ("+ str(100-int(str((user_data_worksheet.row_values(username_row))[2])[-2:]))+" more points until next rank)",font=('Fredoka One Regular', 15),bg_color="#E6B25E",fg_color="#E6B25E")
    current_rank_lab.place(relx=0.02,rely=0.15,anchor="nw")
    daily_tasks_lab = CTkLabel(canvas2,text="Daily Tasks:",font=('Fredoka One Regular', 15),bg_color="#E6B25E",fg_color="#E6B25E")
    daily_tasks_lab.place(relx=0.02,rely=0.25, anchor="nw")
    tasks_frame=CTkFrame(canvas2,width=500,height=250,corner_radius=10,bg_color="#E6B25E",fg_color="#CC7000")
    tasks_frame.place(relx=0.02,rely=0.33, anchor="nw")
    task1_frame=CTkFrame(tasks_frame,width=450,height=70,corner_radius=10,bg_color="#CC7000",fg_color="white")
    task1_frame.place(relx=0.5,rely=0.05, anchor="n")
    if int((user_data_worksheet.row_values(username_row))[3]) >= 10:
        points1_lab = CTkLabel(task1_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="green",fg_color="#FFDDA6")
    else:
        points1_lab = CTkLabel(task1_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="#FFDDA6")
    points1_lab.place(relx=0.02,rely=0.5,anchor="w")
    task1_lab = CTkLabel(task1_frame,text="Comment on 10 other scenario posts",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task1_lab.place(relx=0.2,rely=0.5,anchor="w")
    task1_score = CTkLabel(task1_frame,text=str((user_data_worksheet.row_values(username_row))[3])+"/10",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task1_score.place(relx=0.9,rely=0.5,anchor="e")
    task2_frame=CTkFrame(tasks_frame,width=450,height=70,corner_radius=10,bg_color="#CC7000",fg_color="white")
    task2_frame.place(relx=0.5,rely=0.5, anchor="center")
    task2_lab = CTkLabel(task2_frame,text="Complete and post daily scenario",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task2_lab.place(relx=0.2,rely=0.5,anchor="w")
    if int((user_data_worksheet.row_values(username_row))[5]) == 1:
        points2_lab = CTkLabel(task2_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="green",fg_color="#FFDDA6")
    else:
        points2_lab = CTkLabel(task2_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="#FFDDA6")
    points2_lab.place(relx=0.02,rely=0.5,anchor="w")
    task2_score = CTkLabel(task2_frame,text=str((user_data_worksheet.row_values(username_row))[5])+"/1",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task2_score.place(relx=0.9,rely=0.5,anchor="e")
    task3_frame=CTkFrame(tasks_frame,width=450,height=70,corner_radius=10,bg_color="#CC7000",fg_color="white")
    task3_frame.place(relx=0.5,rely=0.95, anchor="s")
    task3_lab = CTkLabel(task3_frame,text="Complete all five timed scenarios correctly",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task3_lab.place(relx=0.2,rely=0.5,anchor="w")
    if int((user_data_worksheet.row_values(username_row))[8]) == 5:
        points3_lab = CTkLabel(task3_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="green",fg_color="#FFDDA6")
    else:
        points3_lab = CTkLabel(task3_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="#FFDDA6")
    points3_lab.place(relx=0.02,rely=0.5,anchor="w")
    task3_score = CTkLabel(task3_frame,text=str((user_data_worksheet.row_values(username_row))[8])+"/5",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task3_score.place(relx=0.9,rely=0.5,anchor="e")
def game_screen():
    global main
    global rank
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
    rank = ""
    if int(user_data_worksheet.row_values(username_row)[2]) < 100:
        rank = "Bronze"
    elif int(user_data_worksheet.row_values(username_row)[2]) < 200:
        rank = "Silver"
    elif int(user_data_worksheet.row_values(username_row)[2]) < 300:
        rank = "Gold"
    else:
        rank = "Platnum"
    title_label.place(relx=0.5,rely=0.24, anchor="center")
    frame1 = CTkFrame(main,225,350,bg_color="grey92",fg_color="grey92")
    frame1.place(relx=0.5,rely=0.56,anchor="e")
    frame2 = CTkFrame(main,225,350,bg_color="grey92",fg_color="grey92")
    frame2.place(relx=0.5,rely=0.56,anchor="w")
    my_feed_but = CTkButton(frame1, width=215, height = 115, text="My Feed",font = ('Fredoka One Regular', 20),fg_color= "#D9A797",hover_color="grey40", command=sign_in)
    my_feed_but.pack(anchor='nw',fill='both',padx=10,pady=10)
    daily_scenario_but = CTkButton(frame2,width=215, height = 115, text="Daily Scenario",font = ('Fredoka One Regular', 20),fg_color= "#D4A3CC",hover_color="grey40", command=daily_scenario)
    daily_scenario_but.pack(anchor='ne',fill='both',padx=10,pady=10)
    timed_challenge_but = CTkButton(frame1,width=215, height = 115, text="Timed Challenge",font = ('Fredoka One Regular', 20),fg_color= "#AAAD74",hover_color="grey40", command=sign_in)
    timed_challenge_but.pack(anchor='sw',fill='both',padx=10,pady=10)
    peer_review_scenarios_but = CTkButton(frame2,width=215, height = 115, text='Peer Review Scenarios',font = ('Fredoka One Regular', 20),fg_color= "#B78C99", hover_color="grey40",command=sign_in)
    peer_review_scenarios_but.pack(anchor='se',fill='both',padx=10,pady=10)
    profile_but_pic = CTkImage(light_image=pillow.Image.open("Screenshot 2024-07-09 192127.png"), size=(100,100))
    profile_but = CTkButton(main,width=100,height=100,text="",image=profile_but_pic, bg_color="grey92",fg_color="grey92", hover_color="grey92",command=profile_screen)
    profile_but.place(relx=0.01,rely=0.99,anchor="sw")
def new_userandpass():
    global username_
    global username_row
    username_ = username.get(0.0,'end')
    if user_data_worksheet.find(username_,in_column=1) == None:
        if len(password.get(0.0,'end'))>=8:
            user_data_worksheet.append_row([username_,password.get(0.0,'end'),0,0,str(date.today()),0,str(date.today()),str(date.today()),0,str(date.today())])
            username_row = (user_data_worksheet.find(username_,in_column=1)).row
            sign_up_win.destroy()
            game_screen()
        else:
            error_lab = CTkLabel(sign_up_win, text="Password is Too Short", font=('Fredoka One Regular', 15), text_color='red')
            error_lab.place(relx=0.5,rely=0.9, anchor="center")
    else:
        error_lab = CTkLabel(sign_up_win, text="Username Already Exists", font=('Fredoka One Regular', 15), text_color='red')
        error_lab.place(relx=0.5,rely=0.9, anchor="center")
def check_userandpass():
    global username_
    global username_row
    username_=username.get(0.0,'end')
    if user_data_worksheet.find(username_,in_column=1) != None:
        username_row = (user_data_worksheet.find(username_,in_column=1)).row
        if password.get(0.0,'end') in user_data_worksheet.row_values(username_row):
            if str(date.today()) not in user_data_worksheet.row_values(username_row):
                user_data_worksheet.update_cell(username_row,4,0)
                user_data_worksheet.update_cell(username_row,5,str(date.today()))
                user_data_worksheet.update_cell(username_row,6,0)
                user_data_worksheet.update_cell(username_row,7,str(date.today()))
                user_data_worksheet.update_cell(username_row,9,0)
                user_data_worksheet.update_cell(username_row,10,str(date.today()))
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
daily_scen_worksheet = spreadsheet.get_worksheet(2)

app.mainloop()

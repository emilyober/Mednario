from customtkinter import *
from tkinter import *
import tkinter as tk
import gspread
from PIL import ImageTk, Image
import PIL as pillow
from datetime import date
import random

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

def feed_display():
    peer_scen = CTkToplevel()  
    peer_scen.geometry("700x500")
    peer_scen.resizable(False,False)
    peer_scen.title("My Feed")
    main.attributes("-topmost",False)
    peer_scen.attributes('-topmost',True)
    canvas1 = tk.Canvas(peer_scen,width=800,height=600,bg="#D9A797",highlightthickness=0)
    canvas1.pack(expand=True,fill=BOTH)
    main_frame = CTkScrollableFrame(canvas1,width=600,height=450,corner_radius=10,border_width=2,bg_color="#D9A797",fg_color="#F2C7B9")
    main_frame.place(relx=0.5,rely=0.5,anchor="center")
    count = 0
    total_rows = len(scenario_posts_worksheet.col_values(1))
    posts = []
    while count > -5:
        try:
            posts.append(scenario_posts_worksheet.row_values(total_rows + count))
            count -= 1
        except:
            break
    try:
        post1_frame = CTkFrame(main_frame,width=550,corner_radius=10,bg_color="#F2C7B9",fg_color="#D9A797")
        post1_frame.pack(pady=10)
        post1username_row = (user_data_worksheet.find(posts[0][0],in_column=1)).row
        if int(user_data_worksheet.row_values(post1username_row)[2]) < 100:
            user_color = "#643715"
        elif int(user_data_worksheet.row_values(username_row)[2]) < 200:
            user_color = "#8E8C8C"
        elif int(user_data_worksheet.row_values(username_row)[2]) < 300:
            user_color = "#A48729"
        else:
            user_color = "#78A3B7"
        if posts[0][1] == 1:
            post1user = CTkLabel(post1_frame,width=550,height=25,text="anonymous",font=('Fredoka One Regular', 15),text_color=user_color)
        else:
            post1user = CTkLabel(post1_frame,width=550,height=25,text=posts[0][0],font=('Fredoka One Regular', 15),anchor="w",text_color=user_color)
        post1user.pack(ipadx=10)
        post1scen = CTkLabel(post1_frame,width=550,height=40,text="Scenario: " + posts[0][2],font=('Fredoka One Regular', 15),anchor="w",text_color="black")
        post1scen.pack(ipadx=10)
        post1_res_frame = CTkFrame(post1_frame,width=500,corner_radius=10,bg_color="#D9A797",fg_color="grey87")
        post1_res_frame.pack()
        post1_res = CTkLabel(post1_res_frame,text=posts[0][3],font=('Fredoka One Regular', 15),wraplength=500)
        post1_res.pack()

    except:
        pass
def peer_review_scen():
    peer_scen = CTkToplevel()  
    peer_scen.geometry("700x500")
    peer_scen.resizable(False,False)
    peer_scen.title("Peer Review Scenarios")
    main.attributes("-topmost",False)
    peer_scen.attributes('-topmost',True)
    canvas1 = tk.Canvas(peer_scen,width=800,height=600,bg="#B78C99",highlightthickness=0)
    canvas1.pack(expand=True,fill=BOTH)
    def post_peer():
        global anon_post_check
        global scen_box
        global scen_ans
        scen_ans = str(scen_box.get(0.0,'end'))
        scenario_posts_worksheet.append_row([username_,anon_post_check.get(),scenario,scen_ans,0,0,"",str(date.today())])
        peer_scen.destroy()
    def rand_scen():
        global anon_post_check
        global scen_box
        global scenario
        scenario_row = random.choice(r)
        r.remove(scenario_row)
        scenario_data = time_and_peer_ws.row_values(scenario_row)
        scenario = str(scenario_data[0])
        daily_scen_lab = CTkLabel(canvas1, text="Scenario: "+scenario,font=('Fredoka One Regular', 20),bg_color="#B78C99",fg_color="#B78C99",wraplength=670)
        daily_scen_lab.place(relx=0.02,rely=0.02,anchor="nw")
        scen_box = CTkTextbox(canvas1,width=650,height=250,font=('Fredoka One Regular', 15),corner_radius=10,bg_color="#B78C99",fg_color="grey87")
        scen_box.place(relx=0.5,rely=0.2,anchor="n")
        anon_post_check = CTkCheckBox(canvas1,text="Post Anonymously",font=('Fredoka One Regular', 15),bg_color="#B78C99",fg_color="#B78C99")
        anon_post_check.place(relx=0.95,rely=0.75,anchor="ne")
        post_scen_but = CTkButton(canvas1,width=120,height=40,text="Post Scenario",font=('Fredoka One Regular', 15),fg_color= "#E0BDC8",hover_color="#DB809B",text_color="black",command=post_peer)
        post_scen_but.place(relx=0.5,rely=0.87,anchor="center")
        generate_scen_but.configure(width=130,height=40,text="Generate New Scenario",font=('Fredoka One Regular', 15))
        generate_scen_but.place(relx=0.05,rely=0.87, anchor="w")
    generate_scen_but = CTkButton(canvas1,width=200,height=50,text="Generate Random Scenario",font=('Fredoka One Regular', 20),bg_color="#B78C99",corner_radius=10,fg_color= "#E0BDC8",hover_color="#DB809B",text_color="black",command=rand_scen)
    generate_scen_but.place(relx=0.5,rely=0.5,anchor="center")

def timed_challenge():
    global next_arrow
    global back_arrow
    global time_cha
    time_cha = CTkToplevel()  
    time_cha.geometry("700x500")
    time_cha.resizable(False,False)
    time_cha.title("Timed Challenge")
    main.attributes("-topmost",False)
    time_cha.attributes('-topmost',True)
    canvas1 = tk.Canvas(time_cha,width=800,height=600,bg="#AAAD74",highlightthickness=0)
    canvas1.pack(expand=True,fill=BOTH)
    back_arrow = CTkImage(light_image=pillow.Image.open("Screenshot 2024-07-13 182225.png"),size=(50,50))
    next_arrow = CTkImage(light_image=pillow.Image.open("Screenshot 2024-07-13 182146.png"),size=(50,50))
    def done_review():
        try:
            if (' ' not in str(scen1_add)) and ((scen1_add).strip() not in str(time_and_peer_ws.cell(scen_row1,2).value)):
                time_and_peer_ws.update_cell(scen_row1,2,(str(time_and_peer_ws.cell(scen_row1,2).value)).strip()+","+((str(scen1_add)).strip()).lower())
        except:
            pass
        try:
            if (' ' not in str(scen2_add)) and ((scen2_add).strip() not in str(time_and_peer_ws.cell(scen_row2,2).value)):
                time_and_peer_ws.update_cell(scen_row2,2,(str(time_and_peer_ws.cell(scen_row2,2).value)).strip()+","+((str(scen2_add)).strip()).lower())
        except:
            pass
        try:
            if (' ' not in str(scen3_add)) and ((scen3_add).strip() not in str(time_and_peer_ws.cell(scen_row3,2).value)):
                time_and_peer_ws.update_cell(scen_row3,2,(str(time_and_peer_ws.cell(scen_row3,2).value)).strip()+","+((str(scen3_add)).strip()).lower())
        except:
            pass
        try:
            if (' ' not in str(scen4_add)) and ((scen4_add).strip() not in str(time_and_peer_ws.cell(scen_row4,2).value)):
                time_and_peer_ws.update_cell(scen_row4,2,(str(time_and_peer_ws.cell(scen_row4,2).value)).strip()+","+((str(scen4_add)).strip()).lower())
        except:
            pass
        try:
            if (' ' not in str(scen5_add)) and ((scen5_add).strip() not in str(time_and_peer_ws.cell(scen_row5,2).value)):
                time_and_peer_ws.update_cell(scen_row5,2,(str(time_and_peer_ws.cell(scen_row5,2).value)).strip()+","+((str(scen5_add)).strip()).lower())
        except:
            pass
        time_cha.destroy()
    def review5():
        global scen5_add
        time_explain.configure(text="",font=("times",1),bg_color="grey87",fg_color="grey87")
        review_frame5 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        review_frame5.place(relx=0.5,rely=0.5,anchor="center")
        scen_title = CTkLabel(review_frame5, text="Scenario #5: "+str(time_and_peer_ws.cell(scen_row5,1).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=570)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        response_lab = CTkLabel(review_frame5, text="Your response:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        response_lab.place(relx=0.02,rely=0.16,anchor="nw")
        if scen_ans5:
            response5 = str(scen_ans5.get(0.0,'end')).strip()
        else:
            response5=""
        response_frame = CTkScrollableFrame(review_frame5,width = 300,height=20,corner_radius=10,fg_color="grey87",bg_color="#DFE1BE",label_fg_color="grey87",label_anchor="w",orientation="horizontal")
        response_frame.place(relx=0.22,rely=0.15,anchor="nw")
        responseinframe = CTkLabel(response_frame, text=response5,font=('Fredoka One Regular', 12),bg_color="grey87",fg_color="grey87")
        responseinframe.pack()
        com_lab = CTkLabel(review_frame5, text="Computer Grade:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        com_lab.place(relx=0.02,rely=0.27,anchor="nw")
        frame = CTkFrame(review_frame5, width=500,height=50,corner_radius= 10,bg_color="#DFE1BE",fg_color="grey87")
        frame.place(relx=0.5,rely=0.35,anchor="n")
        keyword_list = []
        keywords = (str(time_and_peer_ws.cell(scen_row5,2).value)).split(',')
        test_str = response5
        for char in r"[!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~]":
            test_str = (test_str).replace(char," ")
        for keyword in keywords:
            if (" " + keyword + " ") in (" " + test_str + " "):
                keyword_list.append(keyword)
        if len(keyword_list) == 0:
            computer_message = "Incorrect. Your response does not reflect how this scenario would typically be answered by other medical professionals."
        elif len(keyword_list) == 1:
            computer_message = "Correct! Other medical professionals used the word " + keyword_list[0] + " in their response."
        else:
            computer_message = "Correct! Other medical professionals used the words " + keyword_list[0] + " and " + keyword_list[1] + " in their response."
        com_grade = CTkLabel(frame, text=computer_message,font=('Fredoka One Regular', 15),bg_color="grey87",fg_color="grey87",wraplength=450)
        com_grade.place(relx=0.5,rely=0.5,anchor="center")
        auto_text = CTkLabel(review_frame5, text="To help the auto grader become more accurate, please answer the following question: "+ str(time_and_peer_ws.cell(scen_row5,3).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE",wraplength=550)
        auto_text.place(relx=0.5,rely=0.51,anchor="n")
        auto_textbox = CTkTextbox(review_frame5,width=500,height=20,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        auto_textbox.place(relx=0.5,rely=0.67,anchor="n")
        def enter_scen5():
            global scen5_add
            scen5_add = (str(auto_textbox.get(0.0,'end'))).strip()
            auto_textbox.delete(0.0,'end')
            auto_textbox.insert(0.0,'Thank you for your response!')
        enter_but = CTkButton(review_frame5,width=100,height=30,text="Enter",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=enter_scen5)
        enter_but.place(relx=0.5,rely=0.79,anchor="n")
        finish_review_but = CTkButton(review_frame5,width=50,height=50,text="Finish Review",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=done_review)
        finish_review_but.place(relx=0.98,rely=0.98,anchor="se")
        review_but= CTkButton(review_frame5,width=100,height=30,text="Review Page",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#C4B7BB",text_color="black",command=submit_screen)
        review_but.place(relx=0.5,rely=0.98,anchor="s")
        back_arrow_but = CTkButton(review_frame5,width=50,height=50,text="",image=back_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review4)
        back_arrow_but.place(relx=0.02,rely=0.98,anchor="sw")
    def review4():
        global scen4_add
        time_explain.configure(text="",font=("times",1),bg_color="grey87",fg_color="grey87")
        review_frame4 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        review_frame4.place(relx=0.5,rely=0.5,anchor="center")
        scen_title = CTkLabel(review_frame4, text="Scenario #4: "+str(time_and_peer_ws.cell(scen_row4,1).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=570)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        response_lab = CTkLabel(review_frame4, text="Your response:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        response_lab.place(relx=0.02,rely=0.16,anchor="nw")
        if scen_ans4:
            response4 = str(scen_ans4.get(0.0,'end')).strip()
        else:
            response4=""
        response_frame = CTkScrollableFrame(review_frame4,width = 300,height=20,corner_radius=10,fg_color="grey87",bg_color="#DFE1BE",label_fg_color="grey87",label_anchor="w",orientation="horizontal")
        response_frame.place(relx=0.22,rely=0.15,anchor="nw")
        responseinframe = CTkLabel(response_frame, text=response4,font=('Fredoka One Regular', 12),bg_color="grey87",fg_color="grey87")
        responseinframe.pack()
        com_lab = CTkLabel(review_frame4, text="Computer Grade:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        com_lab.place(relx=0.02,rely=0.27,anchor="nw")
        frame = CTkFrame(review_frame4, width=500,height=50,corner_radius= 10,bg_color="#DFE1BE",fg_color="grey87")
        frame.place(relx=0.5,rely=0.35,anchor="n")
        keyword_list = []
        keywords = (str(time_and_peer_ws.cell(scen_row4,2).value)).split(',')
        test_str = response4
        for char in r"[!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~]":
            test_str = (test_str).replace(char," ")
        for keyword in keywords:
            if (" " + keyword + " ") in (" " + test_str + " "):
                keyword_list.append(keyword)
        if len(keyword_list) == 0:
            computer_message = "Incorrect. Your response does not reflect how this scenario would typically be answered by other medical professionals."
        elif len(keyword_list) == 1:
            computer_message = "Correct! Other medical professionals used the word " + keyword_list[0] + " in their response."
        else:
            computer_message = "Correct! Other medical professionals used the words " + keyword_list[0] + " and " + keyword_list[1] + " in their response."
        com_grade = CTkLabel(frame, text=computer_message,font=('Fredoka One Regular', 15),bg_color="grey87",fg_color="grey87",wraplength=450)
        com_grade.place(relx=0.5,rely=0.5,anchor="center")
        auto_text = CTkLabel(review_frame4, text="To help the auto grader become more accurate, please answer the following question: "+ str(time_and_peer_ws.cell(scen_row4,3).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE",wraplength=550)
        auto_text.place(relx=0.5,rely=0.51,anchor="n")
        auto_textbox = CTkTextbox(review_frame4,width=500,height=20,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        auto_textbox.place(relx=0.5,rely=0.67,anchor="n")
        def enter_scen4():
            global scen4_add
            scen4_add = (str(auto_textbox.get(0.0,'end'))).strip()
            auto_textbox.delete(0.0,'end')
            auto_textbox.insert(0.0,'Thank you for your response!')
        enter_but = CTkButton(review_frame4,width=100,height=30,text="Enter",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=enter_scen4)
        enter_but.place(relx=0.5,rely=0.79,anchor="n")
        next_arrow_but = CTkButton(review_frame4,width=50,height=50,text="",image=next_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review5)
        next_arrow_but.place(relx=0.98,rely=0.98,anchor="se")
        review_but= CTkButton(review_frame4,width=100,height=30,text="Review Page",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#C4B7BB",text_color="black",command=submit_screen)
        review_but.place(relx=0.5,rely=0.98,anchor="s")
        back_arrow_but = CTkButton(review_frame4,width=50,height=50,text="",image=back_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review3)
        back_arrow_but.place(relx=0.02,rely=0.98,anchor="sw")
    def review3():
        global scen3_add
        time_explain.configure(text="",font=("times",1),bg_color="grey87",fg_color="grey87")
        review_frame3 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        review_frame3.place(relx=0.5,rely=0.5,anchor="center")
        scen_title = CTkLabel(review_frame3, text="Scenario #3: "+str(time_and_peer_ws.cell(scen_row3,1).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=570)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        response_lab = CTkLabel(review_frame3, text="Your response:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        response_lab.place(relx=0.02,rely=0.16,anchor="nw")
        if scen_ans3:
            response3 = str(scen_ans3.get(0.0,'end')).strip()
        else:
            response3=""
        response_frame = CTkScrollableFrame(review_frame3,width = 300,height=20,corner_radius=10,fg_color="grey87",bg_color="#DFE1BE",label_fg_color="grey87",label_anchor="w",orientation="horizontal")
        response_frame.place(relx=0.22,rely=0.15,anchor="nw")
        responseinframe = CTkLabel(response_frame, text=response3,font=('Fredoka One Regular', 12),bg_color="grey87",fg_color="grey87")
        responseinframe.pack()
        com_lab = CTkLabel(review_frame3, text="Computer Grade:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        com_lab.place(relx=0.02,rely=0.27,anchor="nw")
        frame = CTkFrame(review_frame3, width=500,height=50,corner_radius= 10,bg_color="#DFE1BE",fg_color="grey87")
        frame.place(relx=0.5,rely=0.35,anchor="n")
        keyword_list = []
        keywords = (str(time_and_peer_ws.cell(scen_row3,2).value)).split(',')
        test_str = response3
        for char in r"[!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~]":
            test_str = (test_str).replace(char," ")
        for keyword in keywords:
            if (" " + keyword + " ") in (" " + test_str + " "):
                keyword_list.append(keyword)
        if len(keyword_list) == 0:
            computer_message = "Incorrect. Your response does not reflect how this scenario would typically be answered by other medical professionals."
        elif len(keyword_list) == 1:
            computer_message = "Correct! Other medical professionals used the word " + keyword_list[0] + " in their response."
        else:
            computer_message = "Correct! Other medical professionals used the words " + keyword_list[0] + " and " + keyword_list[1] + " in their response."
        com_grade = CTkLabel(frame, text=computer_message,font=('Fredoka One Regular', 15),bg_color="grey87",fg_color="grey87",wraplength=450)
        com_grade.place(relx=0.5,rely=0.5,anchor="center")
        auto_text = CTkLabel(review_frame3, text="To help the auto grader become more accurate, please answer the following question: "+ str(time_and_peer_ws.cell(scen_row3,3).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE",wraplength=550)
        auto_text.place(relx=0.5,rely=0.51,anchor="n")
        auto_textbox = CTkTextbox(review_frame3,width=500,height=20,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        auto_textbox.place(relx=0.5,rely=0.67,anchor="n")
        def enter_scen3():
            global scen3_add
            scen3_add = (str(auto_textbox.get(0.0,'end'))).strip()
            auto_textbox.delete(0.0,'end')
            auto_textbox.insert(0.0,'Thank you for your response!')
        enter_but = CTkButton(review_frame3,width=100,height=30,text="Enter",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=enter_scen3)
        enter_but.place(relx=0.5,rely=0.79,anchor="n")
        next_arrow_but = CTkButton(review_frame3,width=50,height=50,text="",image=next_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review4)
        next_arrow_but.place(relx=0.98,rely=0.98,anchor="se")
        review_but= CTkButton(review_frame3,width=100,height=30,text="Review Page",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#C4B7BB",text_color="black",command=submit_screen)
        review_but.place(relx=0.5,rely=0.98,anchor="s")
        back_arrow_but = CTkButton(review_frame3,width=50,height=50,text="",image=back_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review2)
        back_arrow_but.place(relx=0.02,rely=0.98,anchor="sw")
    def review2():
        global scen2_add
        time_explain.configure(text="",font=("times",1),bg_color="grey87",fg_color="grey87")
        review_frame2 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        review_frame2.place(relx=0.5,rely=0.5,anchor="center")
        scen_title = CTkLabel(review_frame2, text="Scenario #2: "+str(time_and_peer_ws.cell(scen_row2,1).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=570)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        response_lab = CTkLabel(review_frame2, text="Your response:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        response_lab.place(relx=0.02,rely=0.16,anchor="nw")
        if scen_ans2:
            response2 = str(scen_ans2.get(0.0,'end')).strip()
        else:
            response2=""
        response_frame = CTkScrollableFrame(review_frame2,width = 300,height=20,corner_radius=10,fg_color="grey87",bg_color="#DFE1BE",label_fg_color="grey87",label_anchor="w",orientation="horizontal")
        response_frame.place(relx=0.22,rely=0.15,anchor="nw")
        responseinframe = CTkLabel(response_frame, text=response2,font=('Fredoka One Regular', 12),bg_color="grey87",fg_color="grey87")
        responseinframe.pack()
        com_lab = CTkLabel(review_frame2, text="Computer Grade:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        com_lab.place(relx=0.02,rely=0.27,anchor="nw")
        frame = CTkFrame(review_frame2, width=500,height=50,corner_radius= 10,bg_color="#DFE1BE",fg_color="grey87")
        frame.place(relx=0.5,rely=0.35,anchor="n")
        keyword_list = []
        keywords = (str(time_and_peer_ws.cell(scen_row2,2).value)).split(',')
        test_str = response2
        for char in r"[!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~]":
            test_str = (test_str).replace(char," ")
        for keyword in keywords:
            if (" " + keyword + " ") in (" " + test_str + " "):
                keyword_list.append(keyword)
        if len(keyword_list) == 0:
            computer_message = "Incorrect. Your response does not reflect how this scenario would typically be answered by other medical professionals."
        elif len(keyword_list) == 1:
            computer_message = "Correct! Other medical professionals used the word " + keyword_list[0] + " in their response."
        else:
            computer_message = "Correct! Other medical professionals used the words " + keyword_list[0] + " and " + keyword_list[1] + " in their response."
        com_grade = CTkLabel(frame, text=computer_message,font=('Fredoka One Regular', 15),bg_color="grey87",fg_color="grey87",wraplength=450)
        com_grade.place(relx=0.5,rely=0.5,anchor="center")
        auto_text = CTkLabel(review_frame2, text="To help the auto grader become more accurate, please answer the following question: "+ str(time_and_peer_ws.cell(scen_row2,3).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE",wraplength=550)
        auto_text.place(relx=0.5,rely=0.51,anchor="n")
        auto_textbox = CTkTextbox(review_frame2,width=500,height=20,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        auto_textbox.place(relx=0.5,rely=0.67,anchor="n")
        def enter_scen2():
            global scen2_add
            scen2_add = (str(auto_textbox.get(0.0,'end'))).strip()
            auto_textbox.delete(0.0,'end')
            auto_textbox.insert(0.0,'Thank you for your response!')
        enter_but = CTkButton(review_frame2,width=100,height=30,text="Enter",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=enter_scen2)
        enter_but.place(relx=0.5,rely=0.79,anchor="n")
        next_arrow_but = CTkButton(review_frame2,width=50,height=50,text="",image=next_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review3)
        next_arrow_but.place(relx=0.98,rely=0.98,anchor="se")
        review_but= CTkButton(review_frame2,width=100,height=30,text="Review Page",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#C4B7BB",text_color="black",command=submit_screen)
        review_but.place(relx=0.5,rely=0.98,anchor="s")
        back_arrow_but = CTkButton(review_frame2,width=50,height=50,text="",image=back_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review1)
        back_arrow_but.place(relx=0.02,rely=0.98,anchor="sw")
    def review1():
        global scen1_add
        time_explain.configure(text="",font=("times",1),bg_color="grey87",fg_color="grey87")
        review_frame1 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        review_frame1.place(relx=0.5,rely=0.5,anchor="center")
        scen_title = CTkLabel(review_frame1, text="Scenario #1: "+str(time_and_peer_ws.cell(scen_row1,1).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=570)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        response_lab = CTkLabel(review_frame1, text="Your response:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        response_lab.place(relx=0.02,rely=0.16,anchor="nw")
        if scen_ans1:
            response1 = str(scen_ans1.get(0.0,'end')).strip()
        else:
            response1=""
        response_frame = CTkScrollableFrame(review_frame1,width = 300,height=20,corner_radius=10,fg_color="grey87",bg_color="#DFE1BE",label_fg_color="grey87",label_anchor="w",orientation="horizontal")
        response_frame.place(relx=0.22,rely=0.15,anchor="nw")
        responseinframe = CTkLabel(response_frame, text=response1,font=('Fredoka One Regular', 12),bg_color="grey87",fg_color="grey87")
        responseinframe.pack()
        com_lab = CTkLabel(review_frame1, text="Computer Grade:",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE")
        com_lab.place(relx=0.02,rely=0.27,anchor="nw")
        frame = CTkFrame(review_frame1, width=500,height=50,corner_radius= 10,bg_color="#DFE1BE",fg_color="grey87")
        frame.place(relx=0.5,rely=0.35,anchor="n")
        keyword_list = []
        keywords = (str(time_and_peer_ws.cell(scen_row1,2).value)).split(',')
        test_str = response1
        for char in r"[!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~]":
            test_str = (test_str).replace(char," ")
        for keyword in keywords:
            if (" " + keyword + " ") in (" " + test_str + " "):
                keyword_list.append(keyword)
        if len(keyword_list) == 0:
            computer_message = "Incorrect. Your response does not reflect how this scenario would typically be answered by other medical professionals."
        elif len(keyword_list) == 1:
            computer_message = "Correct! Other medical professionals used the word " + keyword_list[0] + " in their response."
        else:
            computer_message = "Correct! Other medical professionals used the words " + keyword_list[0] + " and " + keyword_list[1] + " in their response."
        com_grade = CTkLabel(frame, text=computer_message,font=('Fredoka One Regular', 15),bg_color="grey87",fg_color="grey87",wraplength=450)
        com_grade.place(relx=0.5,rely=0.5,anchor="center")
        auto_text = CTkLabel(review_frame1, text="To help the auto grader become more accurate, please answer the following question: "+ str(time_and_peer_ws.cell(scen_row1,3).value),font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="#DFE1BE",wraplength=550)
        auto_text.place(relx=0.5,rely=0.51,anchor="n")
        auto_textbox = CTkTextbox(review_frame1,width=500,height=20,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        auto_textbox.place(relx=0.5,rely=0.67,anchor="n")
        def enter_scen1():
            global scen1_add
            scen1_add = (str(auto_textbox.get(0.0,'end'))).strip()
            auto_textbox.delete(0.0,'end')
            auto_textbox.insert(0.0,'Thank you for your response!')
        enter_but = CTkButton(review_frame1,width=100,height=30,text="Enter",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "grey50",hover_color="#C4B7BB",text_color="black",command=enter_scen1)
        enter_but.place(relx=0.5,rely=0.79,anchor="n")
        next_arrow_but = CTkButton(review_frame1,width=50,height=50,text="",image=next_arrow,bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#AAAD74",command=review2)
        next_arrow_but.place(relx=0.98,rely=0.98,anchor="se")
        review_but= CTkButton(review_frame1,width=100,height=30,text="Review Page",font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color= "#AAAD74",hover_color="#C4B7BB",text_color="black",command=submit_screen)
        review_but.place(relx=0.5,rely=0.98,anchor="s")
    def submit_screen():
        submit_frame = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        submit_frame.place(relx=0.5,rely=0.5,anchor="center")
        submit_title = CTkLabel(submit_frame, text='All timed scenarios have been answered. Review the auto graded score for each scenario.',font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=520)
        submit_title.place(relx=0.5,rely=0.02,anchor="n")
        review1_but = CTkButton(submit_frame,width=150,height=150,text="Scenario #1",font =('Fredoka One Regular', 20), fg_color= "#AAAD74", hover_color="#C4B7BB", command=review1)
        review1_but.place(relx=0.33,rely=0.36,anchor="e")
        review2_but = CTkButton(submit_frame,width=150,height=150,text="Scenario #2",font =('Fredoka One Regular', 20), fg_color= "#AAAD74", hover_color="#C4B7BB", command=review2)
        review2_but.place(relx=0.5,rely=0.36,anchor="center")
        review3_but = CTkButton(submit_frame,width=150,height=150,text="Scenario #3",font =('Fredoka One Regular', 20), fg_color= "#AAAD74", hover_color="#C4B7BB", command=review3)
        review3_but.place(relx=0.67,rely=0.36,anchor="w")
        review4_but = CTkButton(submit_frame,width=150,height=150,text="Scenario #4",font =('Fredoka One Regular', 20), fg_color= "#AAAD74", hover_color="#C4B7BB", command=review4)
        review4_but.place(relx=0.45,rely=0.78,anchor="e")
        review5_but = CTkButton(submit_frame,width=150,height=150,text="Scenario #5",font =('Fredoka One Regular', 20), fg_color= "#AAAD74", hover_color="#C4B7BB", command=review5)
        review5_but.place(relx=0.55,rely=0.78,anchor="w")
        time_explain.configure(text="",bg_color="#AAAD74",fg_color="#AAAD74")
    def submit():
        global submit_val
        submit_val = 1
        user_data_worksheet.update_cell(username_row,9,(user_data_worksheet.cell(username_row,9).value)+1)
        if user_data_worksheet.cell(username_row,9).value == 1:
            user_data_worksheet.update_cell(username_row,3,(user_data_worksheet.update_cell(username_row,3).value)+10)
        submit_screen()
    def time_scen5():
        global done4
        global submit_val
        global scen_ans5
        global scen_row5
        done4 = 1
        frame_s5 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        frame_s5.place(relx=0.5,rely=0.5,anchor="center")
        scen_row5 = random.choice(r)
        r.remove(scen_row5)
        scen_title = CTkLabel(frame_s5, text="Scenario #5: "+str(time_and_peer_ws.cell(scen_row5,1).value),font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=520)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        scen_ans5 = CTkTextbox(frame_s5,width=550,height=220,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        scen_ans5.place(relx=0.5,rely=0.28,anchor="n")
        submit_but = CTkButton(frame_s5,text="Submit",font =('Fredoka One Regular', 20), corner_radius=10, bg_color="#DFE1BE",fg_color= "grey50", hover_color="#C4B7BB", command=submit)
        submit_but.place(relx=0.5,rely=0.87,anchor="n")
        countdown_lab = CTkLabel(frame_s5, width=50,height=50,text="60",font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#AAAD74",corner_radius=25)
        countdown_lab.place(relx=0.98,rely=0.02,anchor="ne")
        countdown = 60
        submit_val = 0
        def count_down(countdown):
            countdown_lab.configure(text=str(countdown))
            if countdown == 0:
                submit()
                return
            elif submit_val == 1:
                return
            else:
                app.after(1000,count_down,(countdown - 1))
        app.after(1000,count_down,(countdown - 1))
    def time_scen4():
        global done3
        global done4
        global scen_ans4
        global scen_row4
        done3 = 1
        frame_s4 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        frame_s4.place(relx=0.5,rely=0.5,anchor="center")
        scen_row4 = random.choice(r)
        r.remove(scen_row4)
        scen_title = CTkLabel(frame_s4, text="Scenario #4: "+str(time_and_peer_ws.cell(scen_row4,1).value),font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=520)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        scen_ans4 = CTkTextbox(frame_s4,width=550,height=220,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        scen_ans4.place(relx=0.5,rely=0.28,anchor="n")
        done_but = CTkButton(frame_s4,text="Done",font =('Fredoka One Regular', 20), corner_radius=10, bg_color="#DFE1BE",fg_color= "grey50", hover_color="#C4B7BB", command=time_scen5)
        done_but.place(relx=0.5,rely=0.87,anchor="n")
        countdown_lab = CTkLabel(frame_s4, width=50,height=50,text="60",font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#AAAD74",corner_radius=25)
        countdown_lab.place(relx=0.98,rely=0.02,anchor="ne")
        countdown = 60
        done4 = 0
        def count_down(countdown):
            countdown_lab.configure(text=str(countdown))
            if countdown == 0:
                time_scen5()
                return
            elif done4 == 1:
                return
            else:
                app.after(1000,count_down,(countdown - 1))
        app.after(1000,count_down,(countdown - 1))
    def time_scen3():
        global done2
        global done3
        global scen_ans3
        global scen_row3
        done2 = 1
        frame_s3 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        frame_s3.place(relx=0.5,rely=0.5,anchor="center")
        scen_row3 = random.choice(r)
        r.remove(scen_row3)
        scen_title = CTkLabel(frame_s3, text="Scenario #3: "+str(time_and_peer_ws.cell(scen_row3,1).value),font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=520)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        scen_ans3 = CTkTextbox(frame_s3,width=550,height=220,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        scen_ans3.place(relx=0.5,rely=0.28,anchor="n")
        done_but = CTkButton(frame_s3,text="Done",font =('Fredoka One Regular', 20), corner_radius=10, bg_color="#DFE1BE",fg_color= "grey50", hover_color="#C4B7BB", command=time_scen4)
        done_but.place(relx=0.5,rely=0.87,anchor="n")
        countdown_lab = CTkLabel(frame_s3, width=50,height=50,text="60",font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#AAAD74",corner_radius=25)
        countdown_lab.place(relx=0.98,rely=0.02,anchor="ne")
        countdown = 60
        done3 = 0
        def count_down(countdown):
            countdown_lab.configure(text=str(countdown))
            if countdown == 0:
                time_scen4()
                return
            elif done3 == 1:
                return
            else:
                app.after(1000,count_down,(countdown - 1))
        app.after(1000,count_down,(countdown - 1))
    def time_scen2():
        global done1
        global done2
        global scen_ans2
        global scen_row2
        done1 = 1
        frame_s2 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        frame_s2.place(relx=0.5,rely=0.5,anchor="center")
        scen_row2 = random.choice(r)
        r.remove(scen_row2)
        scen_title = CTkLabel(frame_s2, text="Scenario #2: "+str(time_and_peer_ws.cell(scen_row2,1).value),font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=520)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        scen_ans2 = CTkTextbox(frame_s2,width=550,height=220,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        scen_ans2.place(relx=0.5,rely=0.28,anchor="n")
        done_but = CTkButton(frame_s2,text="Done",font =('Fredoka One Regular', 20), corner_radius=10, bg_color="#DFE1BE",fg_color= "grey50", hover_color="#C4B7BB", command=time_scen3)
        done_but.place(relx=0.5,rely=0.87,anchor="n")
        countdown_lab = CTkLabel(frame_s2, width=50,height=50,text="60",font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#AAAD74",corner_radius=25)
        countdown_lab.place(relx=0.98,rely=0.02,anchor="ne")
        countdown = 60
        done2 = 0
        def count_down(countdown):
            countdown_lab.configure(text=str(countdown))
            if countdown == 0:
                time_scen3()
                return
            elif done2 == 1:
                return
            else:
                app.after(1000,count_down,(countdown - 1))
        app.after(1000,count_down,(countdown - 1))
    def time_scen1():
        global done1
        global scen_ans1
        global scen_row1
        global time_cha
        time_cha.overrideredirect(True)
        time_explain.configure(text="",bg_color="grey87",fg_color="grey87")
        frame_s1 = CTkFrame(canvas1,width=600,height=400,corner_radius= 10,bg_color="#AAAD74",fg_color="#DFE1BE")
        frame_s1.place(relx=0.5,rely=0.5,anchor="center")
        scen_row1 = random.choice(r)
        r.remove(scen_row1)
        scen_title = CTkLabel(frame_s1, text="Scenario #1: "+str(time_and_peer_ws.cell(scen_row1,1).value),font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#DFE1BE", wraplength=520)
        scen_title.place(relx=0.02,rely=0.02,anchor="nw")
        scen_ans1 = CTkTextbox(frame_s1,width=550,height=220,font=('Fredoka One Regular', 15),bg_color="#DFE1BE",fg_color="grey87",corner_radius=10,border_width=2)
        scen_ans1.place(relx=0.5,rely=0.28,anchor="n")
        done_but = CTkButton(frame_s1,text="Done",font =('Fredoka One Regular', 20), corner_radius=10, bg_color="#DFE1BE",fg_color= "grey50", hover_color="#C4B7BB", command=time_scen2)
        done_but.place(relx=0.5,rely=0.87,anchor="n")
        countdown_lab = CTkLabel(frame_s1, width=50,height=50,text="60",font=('Fredoka One Regular', 20),bg_color="#DFE1BE",fg_color="#AAAD74",corner_radius=25)
        countdown_lab.place(relx=0.98,rely=0.02,anchor="ne")
        countdown = 60
        done1 = 0
        def count_down(countdown):
            countdown_lab.configure(text=str(countdown))
            if countdown == 0:
                time_scen2()
                return
            elif done1 == 1:
                return
            else:
                app.after(1000,count_down,(countdown - 1))
        app.after(1000,count_down,(countdown - 1))
    time_explain = CTkLabel(time_cha, text='You will have 1 minute to answer each scenario with a total of 5 minutes for 5 scenarios. This tests your ability to think fast and make good decisions under pressure. Your answers will graded based on previous responses from other medical professionals. Click the "Start" button when you are ready to begin.',font=('Fredoka One Regular', 15),bg_color="#AAAD74",fg_color="#AAAD74", wraplength=550)
    time_explain.place(relx=0.5,rely=0.4,anchor="center")
    start_but = CTkButton(canvas1,text="Start", font = ('Fredoka One Regular', 20), corner_radius=10, bg_color="#AAAD74", fg_color= "grey50", hover_color="#C4B7BB", command=time_scen1)
    start_but.place(relx=0.5,rely=0.6,anchor="center")
    
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
    if scen_box.get(0.0,'end'):
        daily_scen_ans = str(scen_box.get(0.0,'end'))
    else:
        daily_scen_ans = ""
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
    test_str = daily_scen_ans.lower()
    for char in r"[!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~]":
        test_str = (test_str).replace(char," ")
    for keyword in keywords:
        if (" " + keyword + " ") in (" " + test_str + " "):
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
        scen_box = CTkTextbox(daily_scen,width=650,height=250,font=('Fredoka One Regular', 15),corner_radius=10,bg_color="#D4A3CC",fg_color="grey87")
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
    joined_lab = CTkLabel(canvas2,text="Joined "+str(user_data_worksheet.row_values(username_row)[7]),font=('Fredoka One Regular', 15),bg_color="#E6B25E",fg_color="#E6B25E")
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
        points1_lab = CTkLabel(task1_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="green")
    else:
        points1_lab = CTkLabel(task1_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="#FFDDA6")
    points1_lab.place(relx=0.02,rely=0.5,anchor="w")
    task1_lab = CTkLabel(task1_frame,text="Comment on 5 other scenario posts",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task1_lab.place(relx=0.2,rely=0.5,anchor="w")
    task1_score = CTkLabel(task1_frame,text=str((user_data_worksheet.row_values(username_row))[3])+"/10",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task1_score.place(relx=0.9,rely=0.5,anchor="e")
    task2_frame=CTkFrame(tasks_frame,width=450,height=70,corner_radius=10,bg_color="#CC7000",fg_color="white")
    task2_frame.place(relx=0.5,rely=0.5, anchor="center")
    task2_lab = CTkLabel(task2_frame,text="Complete and post daily scenario",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task2_lab.place(relx=0.2,rely=0.5,anchor="w")
    if int((user_data_worksheet.row_values(username_row))[5]) == 1:
        points2_lab = CTkLabel(task2_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="green")
    else:
        points2_lab = CTkLabel(task2_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="#FFDDA6")
    points2_lab.place(relx=0.02,rely=0.5,anchor="w")
    task2_score = CTkLabel(task2_frame,text=str((user_data_worksheet.row_values(username_row))[5])+"/1",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task2_score.place(relx=0.9,rely=0.5,anchor="e")
    task3_frame=CTkFrame(tasks_frame,width=450,height=70,corner_radius=10,bg_color="#CC7000",fg_color="white")
    task3_frame.place(relx=0.5,rely=0.95, anchor="s")
    task3_lab = CTkLabel(task3_frame,text="Complete and grade all five timed scenarios",font=('Fredoka One Regular', 15),wraplength=300,bg_color="white",fg_color="white")
    task3_lab.place(relx=0.2,rely=0.5,anchor="w")
    if int((user_data_worksheet.row_values(username_row))[8]) == 1:
        points3_lab = CTkLabel(task3_frame,text="10 pts",font=('Fredoka One Regular', 15),corner_radius=100,bg_color="white",fg_color="green")
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
    my_feed_but = CTkButton(frame1, width=215, height = 115, text="My Feed",font = ('Fredoka One Regular', 20),fg_color= "#D9A797",hover_color="grey40", command=feed_display)
    my_feed_but.pack(anchor='nw',fill='both',padx=10,pady=10)
    daily_scenario_but = CTkButton(frame2,width=215, height = 115, text="Daily Scenario",font = ('Fredoka One Regular', 20),fg_color= "#D4A3CC",hover_color="grey40", command=daily_scenario)
    daily_scenario_but.pack(anchor='ne',fill='both',padx=10,pady=10)
    timed_challenge_but = CTkButton(frame1,width=215, height = 115, text="Timed Challenge",font = ('Fredoka One Regular', 20),fg_color= "#AAAD74",hover_color="grey40", command=timed_challenge)
    timed_challenge_but.pack(anchor='sw',fill='both',padx=10,pady=10)
    peer_review_scenarios_but = CTkButton(frame2,width=215, height = 115, text='Peer Review Scenarios',font = ('Fredoka One Regular', 20),fg_color= "#B78C99", hover_color="grey40",command=peer_review_scen)
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
time_and_peer_ws = spreadsheet.get_worksheet(3)
r = list(range(2,len(time_and_peer_ws.col_values(1))+1))

app.mainloop()

import random
import time
from datetime import datetime,timedelta,time
from time import *
from tkinter import ttk, StringVar
import customtkinter as ct
from verbindung import conn, zeit
import math


class kunde:
    def __init__(self,user,passwort,time,stein,holz,ftime,zufall):
        self.user = user
        self.passwort = passwort
        self.steine = stein
        self.time = time
        self.holz = holz
        self.ftime = ftime
        self.zufall = zufall



    def start_stein(self,now):

        self.time = datetime.today()
        self.user = self.user


        rest = timedelta(minutes=1)
        rest2 = datetime.today()

        window.update_idletasks()
        sleep(1)







        los = conn()
        los_c = los.cursor()
        los_c.execute("UPDATE spiel SET time = %s WHERE user = %s",(rest2,self.user))
        los.commit()
        los.close()

        info_text.configure(link3,text=f"Du bist jetzt {rest2} Arbeiten",text_color="red",font=("arial",15))







def log(user,passwort2):



    try:
         global l
         connect = conn()
         c = connect.cursor()
         c.execute("SELECT user,passwort,time,stein,holz,ftime,zufall FROM spiel WHERE user = %s",[user])
         user,passwort,time,stein,holz,ftime,zufall = c.fetchone()
         connect.close()

         if passwort == passwort2:

             name = kunde(user,passwort,time,stein,holz,ftime,zufall)
             frame.add(link1, text="Startseite",state="normal")
             frame.add(link2, text="Nachrichten", state="normal")
             frame.add(link3, text="Arbeiten", state="normal")
             frame.add(link4, text="Markt", state="normal")
             l.configure(text="")
             p.configure(text="")
             l_entry.destroy()
             p_entry.destroy()
             bl.destroy()

             zufall = random.randint(1,3)



             verb = conn()
             verb_c = verb.cursor()
             verb_c.execute("UPDATE spiel SET zufall = %s WHERE user = %s",(zufall,name.user))
             verb.commit()
             verb.close()

             if name.zufall == 1:
                 text =  "Es ist zur Zeit sehr schön"
             elif name.zufall == 2:
                 text = "Es ist zur Zeit sehr  bewölkt"
             elif name.zufall == 3:
                 text = "Es ist zur Zeit sehr kühl und Niesilig"
















             user_tag = ct.CTkLabel(link1,text=f"{zeit()} {name.user}, \n\n Wetter-Update:  {text},",font=("arial",16),text_color="black")
             user_tag.place(y=150,x=190)

             if name.time < timedelta(minutes=5) :
                ist = name.time + timedelta(minutes=5)
                info.configure(link1,text=f"Du bist noch bis {ist} Arbeiten",text_color="red",font=("arial",15))

             else:


                 up = conn()
                 up_c = up.cursor()
                 up_c.execute("UPDATE spiel SET stein = %s,time = %s WHERE user = %s",(1,0,name.user))
                 up.commit()
                 up.close()

                 info.configure(link1,text="Du bist fertig",text_color="red",font=("arial",15))






         else:

             info.configure(link1,text="Username oder Passwort Falsch",fg_color="red",font=("arial",18))


    except ValueError: print("")

    now  = StringVar(window)



    abfrage = conn()
    ab_c = abfrage.cursor()
    ab_c.execute("SELECT time FROM spiel WHERE user = %s",[name.user])
    time = ab_c.fetchone()
    abfrage.close()
    print(time)
    a1 = ct.CTkButton(link3, text="Steine Abbauen", text_color="black", bg_color="green", corner_radius=25,command= lambda : kunde.start_stein(name,now.get()))
    a1.place(y=200, x=300)

    a2 = ct.CTkButton(link3, text="Holz fällen", text_color="black", bg_color="green", corner_radius=25)
    a2.place(y=250, x=300)

    global info_text
    info_text = ct.CTkLabel(link3,text="")
    info_text.place(y=280,x=150)
















window = ct.CTk()
window.title("Spiel")
window.geometry("800x600")

global p,l, l_entry, p_entry, info,frame,link1,link2,link3,link4,bl

frame = ttk.Notebook(window)
frame.pack(expand=1,fill="both")


link1 = ttk.Frame(frame)
link2 = ttk.Frame(frame)
link3 = ttk.Frame(frame)
link4 = ttk.Frame(frame)

frame.add(link1,text="Startseite")
frame.add(link2,text="Nachrichten",state="disabled")
frame.add(link3,text="Steine Abbauen",state="disabled")
frame.add(link4,text="Holz Abbauen",state="disabled")




#Startseite-----------------------------

#Überschrift----------------------
u = ct.CTkLabel(link1,text="Spiel Kontakte",text_color="black",font=("arial",20))
u.place(y=25,x=320)


#login Entrys-----------------------
user = StringVar(window)
passwort = StringVar(window)
l = ct.CTkLabel(link1,text="Username :",text_color="black",font=("arial",13))
p = ct.CTkLabel(link1, text="Passwort :", text_color="black", font=("arial", 13))
l_entry = ct.CTkEntry(link1,width=200,corner_radius=25,textvariable=user)
p_entry = ct.CTkEntry(link1,width=200,corner_radius=25,textvariable=passwort)
bl = ct.CTkButton(link1, text="Login", text_color="black",
                  font=("arial", 15), corner_radius=25,command= lambda : log(user.get(),passwort.get()))
global info
info = ct.CTkLabel(link1,text="Du bist daheim",text_color="red",font=("arial",15))
info.place(y=50,x=350)




#Entry Kooardinaten----------------------
l.place(y=200,x=200)
p.place(y=250,x=200)
l_entry.place(y=200,x=350)
p_entry.place(y=250, x=350)
bl.place(y=300,x=360)
info.place(y=370,x=300)



#------------Arbeiten-----------































window.mainloop()









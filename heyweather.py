from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Hey Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

         #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c400f6043bf4fe0ff489aaba93bec5ee"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Hey Weather App","Invalid City Name!")

#search box
Search_image=PhotoImage(file="assets/img/searchbar.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=14,font=("poppins",25,"bold"),bg="white",border=0,fg="black")
textfield.place(x=75,y=38)
textfield.focus()

Search_icon=PhotoImage(file="assets/img/searchicon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="white",command=getWeather)
myimage_icon.place(x=343,y=38)

#heylogo
Logo_image=PhotoImage(file="assets/img/heylogo.png")
logo=Label(image=Logo_image)
logo.place(x=185,y=110)

#bottom box
Frame_image=PhotoImage(file="assets/img/bluebar.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=70,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=70,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="#ffff33",bg="#6699ff")
label1.place(x=130,y=395)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="#ffff33",bg="#6699ff")
label2.place(x=235,y=395)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="#ffff33",bg="#6699ff")
label3.place(x=410,y=395)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="#ffff33",bg="#6699ff")
label4.place(x=660,y=395)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=470,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=470,y=250)

w=Label(text="...",font=("arial",20,"bold"),fg="white",bg="#6699ff")
w.place(x=132,y=430)

h=Label(text="...",font=("arial",20,"bold"),fg="white",bg="#6699ff")
h.place(x=265,y=430)

d=Label(text="...",font=("arial",20,"bold"),fg="white",bg="#6699ff")
d.place(x=412,y=430)

p=Label(text="...",font=("arial",20,"bold"),fg="white",bg="#6699ff")
p.place(x=680,y=430)


root.mainloop()
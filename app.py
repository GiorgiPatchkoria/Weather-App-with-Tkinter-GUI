from encodings import search_function
import json
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image
from PIL import ImageTk



app = Tk()
app.title('Weather App')
app.configure(background='white')
icon = PhotoImage(file='main_logo.png')
app.iconphoto(True, icon)
app.geometry('1200x700')
app.resizable(False, False)

# getting time, weather, temperature and others

def getting_weather():
    try:
        # Determining location

        city = search_input.get()
        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        region = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        result = pytz.timezone(region)

        # Time

        local_time = datetime.now(result)
        current_time = local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        time.config(text='CURRENT TIME:')

        # Weather and other tools

        api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=646824f2b7b86caffec1d0b16ea77f79'
        json_data = requests.get(api).json()
        temperature = int(json_data['main']['temp']-273.15)
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        humidity = json_data['main']['humidity']
        pressure = json_data['main']['pressure']
        wind = json_data['wind']['speed']

        t.config(text=(temperature, '°'))
        c.config(text=(f'{condition} | FEELS LIKE {temperature}°'))
        w.config(text=wind)
        p.config(text=pressure)
        h.config(text=humidity)
        d.config(text=description)
    
        # changing images depended on weather

        if condition == 'Rain':
            rain_img = ImageTk.PhotoImage(Image.open('rain_weather.png'))
            panel.configure(image=rain_img)
            panel.image = rain_img
        elif condition == 'Clear':
            clear_img = ImageTk.PhotoImage(Image.open('clear_weather.png'))
            panel.configure(image=clear_img)
            panel.image = clear_img
        elif condition == 'Clouds': 
            cloudy_img = ImageTk.PhotoImage(Image.open('cloudy_weather.png'))
            panel.configure(image=cloudy_img)
            panel.image = cloudy_img
        elif condition == 'Haze':
            haze_img = ImageTk.PhotoImage(Image.open('haze_weather.png'))
            panel.configure(image=haze_img)
            panel.image = haze_img
        elif condition == 'Mist':
            mist_img = ImageTk.PhotoImage(Image.open('haze_weather.png'))
            panel.configure(image=mist_img)
            panel.image = mist_img
        elif condition == 'Thunderstorm':
            thunder_img = ImageTk.PhotoImage(Image.open('thunderstorm_weather.png'))
            panel.configure(image=thunder_img)
            panel.image = thunder_img
        elif condition == 'Snow':
            snow_img = ImageTk.PhotoImage(Image.open('snow_weather.png'))
            panel.configure(image=snow_img)
            panel.image = snow_img
        else:
            main_logo_img = ImageTk.PhotoImage(Image.open('main_logo.png'))
            panel.configure(image=main_logo_img)
            panel.image = main_logo_img

    except Exception as e:
        messagebox.showerror('weather app', 'City does not exist')
    

# Search Box

search_image = PhotoImage(file='search.png')
search_box = Label(image=search_image, bg='white')
search_box.place(x=10, y=10)

search_input = Entry(app, justify='center', width=20, font=('poppins',25), bg='#404040', border=0, fg='#ffffff')
search_input.place(x=40, y=30)
search_input.focus()

search_icon = PhotoImage(file='search_icon.png')
search_button = Button(image=search_icon, bg='#404040', activebackground='#404040', border=0, cursor='hand2', command=getting_weather)
search_button.place(x=390, y=23)

# Logo

logo_img = ImageTk.PhotoImage(Image.open('main_logo.png'))
panel = tk.Label(app, image=logo_img, bg='white')
panel.place(x=100, y=200)

# Time

time = Label(app, font=('arial', 15, 'bold'), bg='white', fg='#aeff00')
time.place(x=30,y=100)
clock = Label(app, font=('arial', 20), bg='white', fg='#de1818')
clock.place(x=30, y=130)

# right box and its values

box_image = Image.open('box.png')
box_image = box_image.resize((500,550))
bottom_image = ImageTk.PhotoImage(box_image)
bottom_box = Label(image=bottom_image, bg='white')
bottom_box.place(x=600, y=50)

label1 = Label(app, text='WIND', font=('Helvetica', 15, 'bold'), bg='#1ab5ef', fg='#ffffff')
label1.place(x=670, y=150)

label1 = Label(app, text='HUMIDITY', font=('Helvetica', 15, 'bold'), bg='#1ab5ef', fg='#ffffff')
label1.place(x=670, y=250)

label1 = Label(app, text='DESCRIPTION', font=('Helvetica', 15, 'bold'), bg='#1ab5ef', fg='#ffffff')
label1.place(x=670, y=350)

label1 = Label(app, text='PRESSURE', font=('Helvetica', 15, 'bold'), bg='#1ab5ef', fg='#ffffff')
label1.place(x=670, y=450)

t = Label(font=('arial',70,'bold'), bg='white',fg='#09006e')     # t stands for temperature
t.place(x=100, y=450)
c = Label(font=('arial',15,'bold'), bg='white',fg='#990505')     # c stand for condition
c.place(x=100, y=550)


w = Label(text='...', font=('arial', 15, 'bold'), bg='#1ab5ef')   # w stands for wind
w.place(x=920, y=150)
h = Label(text='...', font=('arial', 15, 'bold'), bg='#1ab5ef')     # h stands for humidity
h.place(x=920, y=250)
d = Label(text='...', font=('arial', 12, 'bold'), bg='#1ab5ef')     # d stands for descripiton
d.place(x=920, y=350)
p = Label(text='...', font=('arial', 15, 'bold'), bg='#1ab5ef')     # p stands for pressure
p.place(x=920, y=450)


app.mainloop()
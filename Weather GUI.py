from tkinter import *
import requests
import json
from configparser import  ConfigParser
from tkinter import messagebox
from PIL import ImageTk,Image

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_wether(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        #(city,country, temp_calsius
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        temp_fahrenheit = ((temp_kelvin-273.15)*(9/5)+(32))
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit,icon ,weather)
        return final
    else:
        return None

print(get_wether('hisar'))

def search():
    global imag,img,imga,image
    city = city_text.get()
    weather = get_wether(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0],weather[1])
        img = "{}".format(weather[4])
        imag = f"{img}.png"
        imga = ImageTk.PhotoImage(Image.open(f"{imag}"))
        image = Label(app, image=imga)
        image.pack(anchor=N)
        temp_lbl['text'] = '{:.2f}*C, {:.2f}*F'.format(weather[2],weather[3])
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror('Error','Cannot find city{}'.format(city))

app = Tk()
app.title("Weather App")
app.iconbitmap("x.ico")
app.geometry("700x350")

city_text = StringVar()
city_entry = Entry(app, textvariable= city_text)
city_entry.pack()

search_btn = Button(app, text='Search city Weather', width=20, command = search)
search_btn.pack()

location_lbl = Label(app, text='Location', font=('bold', 20))
location_lbl.pack()

temp_lbl = Label(app, text='temperature')
temp_lbl.pack()

weather_lbl = Label(app, text='weather')
weather_lbl.pack()




mainloop()

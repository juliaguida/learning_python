import tkinter as tk
import requests
import time
# Above package needed for the Going out? Check the weather!!!

def check_weather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=b479ea664562e6348931d28afef6d44c"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S',time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime('I%:%M:%S',time.gmtime(json_data['sys']['sunset']))

    final_info = condition + '\n' + str(temp) + '°C'
    final_data = '\n' + 'Max Temp: ' + str(max_temp) + '\n' + 'Min_temp: ' + str(min_temp) + '\n' + 'Pressure: ' + str(pressure) + '\n' + 'Humidity: ' + str(humidity) + '\n' + 'Wind: ' + str(wind) + '\n' + 'Sunrise: ' + str(sunrise) + '\n'+ 'Sunset: ' + str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)
    
# UI by importing tkinter 'web page to enter the city to get the weather.
canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('Going out? Check the weather!!!')

f = ('popping', 15, 'bold')
t = ('popping',35, 'bold')

textfield = tk.Entry(canvas, justify ='center', width = 20, font= t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', check_weather)

label1 = tk.Label(canvas, font =t)
label1.pack()
label2 = tk.Label(canvas, font =f)
label2.focus()
canvas.mainloop()

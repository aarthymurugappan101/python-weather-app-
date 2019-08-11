import tkinter as tk
import requests
HEIGHT = 500
WIDTH = 600

#09d08894b6194b49549816d73ab9cae2
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'city: %s \n conditions: %s\n Temprature (℃): %s' %(name, desc, temp)
    except:
        final_str = "error"    
    return final_str    

def get_weather(city):
    weather_key = "09d08894b6194b49549816d73ab9cae2"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key,"q": city,"units":'metric'}
    response = requests.get(url,params=params)
    weather = response.json()

    label['text'] = format_response(weather)



root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT,width = WIDTH)
canvas.pack()

background_img = tk.PhotoImage(file="C:\\Users\\gayat\\Desktop\\web dev PY\\weatherApp\\landscape.png")
background_label = tk.Label(root,image=background_img)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg="#80c1ff",bd=5)
frame.place (relx=0.5,rely=0.1,relwidth=0.75, relheight=0.1, anchor="n") #creates a responsive frame

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text="Get Weather",font=40,command= lambda: get_weather(entry.get())) 
# everytime the button is clicked it runs the lambda and exits the function instead of repeating itself
button.place(relx=0.7,relwidth=0.3,relheight=1)
# place helps us to place the guis with responsive resizeing

lowerFrame = tk.Frame(root,bg="#80c1ff",bd=10)
lowerFrame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')
# is the frame used to display the weather results

label = tk.Label(lowerFrame, font=("mordern",18),anchor='nw',justify='left',bd=4)
label.place(relwidth=1,relheight=1)

root.mainloop()

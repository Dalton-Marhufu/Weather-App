import tkinter
import requests

HEIGHT = 200
WIDTH = 300

# apikey Your apikey   api.openweathermap.org/data/2.5/forecast?

# organisied responce from weather api with exception handeling
def format_response(weather):
		try:
			name = (weather['name'])
			country = (weather['sys']['country'])
			desc = (weather['weather'][0]['description'])
			temp = ('Temp', weather['main']['temp'])
			humidity = ('Humidity', weather['main']['humidity'])
			return (str(name) + '\n' +str(country) + '\n' + str(desc) + '\n' + str(temp) + '\n' + str(humidity))
		except:
			print('There was a problem retrieving that information')

# weather api function
def get_weather(city):
	weather_key = 'Your apikey'
	url = 'http://api.openweathermap.org/data/2.5/weather?'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params=params)
	weather = response.json()
	label['text'] = format_response(weather)

# tkinter app	
root = tkinter.Tk()
root.title('WEATHER APP')
canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH,)

top_frame = tkinter.Frame(root)
top_frame.pack(side = 'top')

entry = tkinter.Entry(top_frame, bg='silver', width =15, font=50, justify='center')
entry.pack(side ='top')

button = tkinter.Button(top_frame, text='Get Weather', font=50, command=lambda: get_weather(entry.get()))
button.pack()

label = tkinter.Label(top_frame,text='WEATHER APP', font=50)
label.pack()

canvas.pack()
root.mainloop()

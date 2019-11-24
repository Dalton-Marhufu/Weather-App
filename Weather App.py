import tkinter
import requests


# apikey "Your API key"   api.openweathermap.org/data/2.5/forecast?

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
	weather_key = 'Your API key here'
	url = 'http://api.openweathermap.org/data/2.5/weather?'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params=params)
	weather = response.json()
	label['text'] = format_response(weather)

# tkinter app	
root = tkinter.Tk()

root.title('WEATHER APP')
root.geometry('300x300')
root.iconbitmap('apppic.jpg')

top_frame = tkinter.Frame(root)
top_frame.pack(side ='top')

entry = tkinter.Entry(top_frame, bg='silver', width =17, font=150, justify='center', borderwidth=5)
entry.pack(side ='top')
entry.insert(0, "Enter City")

button = tkinter.Button(top_frame, text='Get Weather', font=50, bg='#60edfc', command=lambda: get_weather(entry.get()))
button.pack()

label = tkinter.Label(top_frame,text='WEATHER APP', font=50, pady=50, fg='#002e85')
label.pack()

root.mainloop()

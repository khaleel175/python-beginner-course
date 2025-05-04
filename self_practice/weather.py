import requests

url = 'http://api.weatherapi.com/v1/current.json?key=4c6487c46ca04cdcab3161648250405&q=Hyderabad&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
desc = weather_json.get('current').get('condition').get('text')

print(f"Today's weather in hyderabad is: {desc} , And the temperature is: {temp} degrees celsius")
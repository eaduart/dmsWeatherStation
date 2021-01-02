# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 
import pprint
import sys

# Enter your API key here  - my key
api_key = "00712a93ba8f635ae5c08e11f8d1044b"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#list=[2514256,5810490]
#list=[sys.argv[1]]
def get_weather(id):
    # Give city name - Malaga and Silverdale 
    #for id in list(id):
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&id=" + str(id)
    #print(complete_url)

    # get method of requests module 
    # return response object 
    try:
        response = requests.get(complete_url) 
    except ConnectionError:
        return ("Networking problem", "None", 0, 0, 0, "networking issue") 
    #print(response)

    # json method of response object 
    # convert json format data into 
    # python format data 
    x = response.json() 

    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 

        # store the value of "main" 
        # key in variable y 
        y = x["main"] 

        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = round(( y["temp"] - 273.15 ) * 9/5 + 32, 2)

        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 

        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 

        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 

        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z 
        weather_description = z[0]["description"] 

        city_name = x["name"]
        country   = x["sys"]["country"]

        # print following values 
#        print("City Name: " + city_name + " in " + country +
#                "\nTemperature (in kelvin unit) = " +
#        				str(current_temperature) +
#        	"\n atmospheric pressure (in hPa unit) = " +
#        				str(current_pressure) +
#        	"\n humidity (in percentage) = " +
#        				str(current_humidiy) +
#        	"\n description = " +
#        				str(weather_description)) 

#    else: 
#        print(" City Not Found ") 

        return (city_name, country, current_temperature, current_pressure, current_humidiy, weather_description)

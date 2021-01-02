"""
    Dashboard using blocks of information.
    Copyright 2020 PySimpleGUI.org
"""

import PySimpleGUI as sg
import sys
import datetime
import time
from openweather_api_specific import get_weather

theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

# sg.theme_add_new('Dashboard', theme_dict)     # if using 4.20.0.1+
sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')

try:
    if sys.argv[1] == "demo":
        demo=True
except:
    demo=False


def get_weather_info(demo, id):
    '''get_weather_info will either get the weather using get_wather module or do a demo to not
       waste call to openweather.'''
    if demo:
        return "Testing", "SOMEWHERE", 100, 1000, 100, "Not cool"
    else:
        return get_weather(id)

def updatetime():
    '''updatetime - get the current date and time to be display.'''
    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))


top_banner = [[
               sg.Text(updatetime(), font='Any 20', justification='c', background_color=DARK_HEADER_COLOR, key='-clock-')]
             ]

top  = [[sg.Text('DM\'s super weather station', size=(50,1), justification='c', pad=BPAD_TOP, font='Any 20')],
           # [sg.T(f'{i*25}-{i*34}') for i in range(7)],]
        ]

city_name, country, temperature, pressure, humidity, descrption = get_weather_info(demo, 2514256)
Malaga = [[sg.Text(city_name, font='Any 20')],
            [sg.Text("Temp: " + str(temperature) + "F", key='-malagatemp-')],
            [sg.T("Humidity: " + str(humidity))],
            ]

city_name, country, temperature, pressure, humidity, descrption = get_weather_info(demo, 5810490)
Silverdale = [[sg.Text(city_name, font='Any 20')],
            [sg.Text("Temp: " + str(temperature) + "F",key='-silverdaletemp-')],
            [sg.T("Humidity: " + str(humidity))],
            ]


layout = [
          [sg.Column(top_banner, size=(900, 60), pad=(20,20), background_color=DARK_HEADER_COLOR)],
          [sg.Column(top, size=(900, 90), pad=BPAD_TOP)],
          [sg.Column(Malaga,size=(430, 120), pad=BPAD_TOP),
           sg.Column(Silverdale,size=(430, 120), pad=BPAD_TOP)]
         ]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, grab_anywhere=True)

start = time.perf_counter()
while True:             # Event Loop
    event, values = window.read(10)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window['-clock-'].update(updatetime())
    current = time.perf_counter()
    if current - start > 60:
        start = current
        city_name, country, temperature, pressure, humidity, descrption = get_weather_info(demo, 2514256)
        window['-malagatemp-'].update("Temp: " + str(temperature) + "F")
        city_name, country, temperature, pressure, humidity, descrption = get_weather_info(demo, 5810490)
        window['-silverdaletemp-'].update("Temp: " + str(temperature) + "F")
         
window.close()

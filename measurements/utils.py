import os
import requests

TOKEN = 'c9a3d9450858418edd708a73d631cb4b'
API_URL = 'http://api.openweathermap.org/data/2.5/find?appid={}'.format(TOKEN)

class DataCollector():
    def get_specific_data(latitude, longitude):
        location = '&lat={}&lon={}'.format(latitude, longitude)

        response = requests.get(API_URL + location)

        return response

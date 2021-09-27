import requests
from django.conf import settings

def get_geocode_response(address):
    URL = settings.GEOCODE_API_URL

    PARAMS = {'address':address, 'key': settings.GEOCODE_API_KEY}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']
    
    result_data = { "coordinates" : {'lat': latitude, 'lng':longitude}, "address": formatted_address}
    
    return result_data
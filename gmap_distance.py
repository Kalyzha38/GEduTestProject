from geopy.distance import geodesic
import requests
import json

from os import getenv

def gmap_distance(request):
    """origins:[float,float]
       destinations:[float,float]"""

    request_json = request.get_json()
    if request_json and 'origins' and 'destinations' in request_json:
        origins = request_json['origins']
        destinations = request_json['destinations']
        data = json.loads(requests.get(f'https://maps.googleapis.com/maps/api/distancematrix/json?'
                            f'origins={",".join(str(x) for x in origins)}'
                            f'&destinations={",".join(str(y) for y in destinations)}'
                            f'&key={getenv("API_KEY")}').content.decode())
        dist = geodesic(origins, destinations).kilometers
        drive_distance = data['rows'][0]['elements'][0]['distance']['text']
        drive_time = data['rows'][0]['elements'][0]['duration']['text']
        return f'Origin: {origins}\nDestination: {destinations}\nDistance: {dist}\nDriving distance: {drive_distance}\nDriving time: {drive_time}'
    else:
        return 'Invalid arguments'
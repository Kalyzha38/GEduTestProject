import requests
import json
import osmapi as osm
api = osm.OsmApi()

"""origins:[lat,lon]
   destinations:[lat,lon]"""
request_json = {"origins" : [50.42985, 30.51988],
                "destinations" : [50.42278, 30.51444]
                }
origins = request_json['origins']
destinations = request_json['destinations']
#d = {'routes': [{'geometry': 'kxwrHiidyD}@gJgB}LgEyS}@sNUyZ', 'legs': [{'annotation': {'nodes': [5315202312, 5315202313, 5315202314, 5315202315, 5315202624, 5315202317, 1674529518, 5315235934, 1028441920, 5315235930, 6486452783, 5315202629, 5315274098, 5315274097, 5315274096, 5315274095, 5315274094, 5315274093, 5315274092, 5315274091, 5315274082, 1224825127, 912455799, 1298346786, 3355420073, 804209422, 804207442, 248921431, 6375275448, 1298337426, 26546592, 1298337385, 6352091796, 1298337411, 2519039905, 306006478, 2841842416, 1379367173]}, 'summary': '', 'weight': 292.4, 'duration': 255.8, 'steps': [], 'distance': 1060.4}], 'weight_name': 'routability', 'weight': 292.4, 'duration': 255.8, 'distance': 1060.4}], 'waypoints': [{'hint': 'hFzegKc8Vol1AAAAAAAAAF0AAABMAAAAI5cPQgAAAACm8-JBxiLDQnUAAAAAAAAAXQAAAEwAAAA8pgAAbmrRAd9vAQN8atEByG8BAwIArwQpPcUz', 'distance': 2.7450963806760007, 'name': 'Протасів Яр вулиця', 'location': [30.501486, 50.425823]}, {'hint': 'etMfgP___3-mAQAAawEAACsAAAApAAAAVy4NQ2RpsUDbp2NBCw-FQaYBAAC2AAAAKwAAABUAAAA8pgAAWaLRAaJ4AQNYotEBxHgBAwEAjwUpPcUz', 'distance': 3.782743509784986, 'name': 'Івана Федорова вулиця', 'location': [30.515801, 50.428066]}], 'code': 'Ok'}

data = json.loads(requests.get(f'http://router.project-osrm.org/route/v1/driving/'
                               f'{",".join(str(x) for x in reversed(origins))}'
                               f';{",".join(str(y) for y in reversed(destinations))}'
                               f'?alternatives=false&annotations=nodes').content.decode())
nodes = data['routes'][0]['legs'][0]['annotation']['nodes']
for n in nodes:
    print(f'{api.NodeGet(n).get("lat")}, {api.NodeGet(n).get("lon")}')
for n in nodes:
    print(f'node({n})')

import folium
import geocoder
import json


def read_json(file_name):
    """
    (str) -> dict
    Returns json file as dictionary.
    """
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_user_friends(user_id):
    """
    (str) -> list
    Sends request to Twitter and returns user's friends list.
    """
    response = read_json('list.json')
    return response['users']


def get_location(user):
    """
    (dict) -> str
    Returns location of the user.
    """
    return user['location']


def get_coordinates(location):
    """
    (str) -> list(lat, long)
    Returns coordinates of the given location.
    """
    geo = geocoder.osm(location)
    return geo.latlng


def locations_layer(locations):
    """
    (list) -> FeatureGroup
    Creates layer with locations in the list and returns it.
    """
    fg_loc = folium.FeatureGroup(name="Friend's_locations")
    for location in locations:
        fg_loc.add_child(folium.Marker(location=[location[0], location[1]],
                                       popup=location[2], icon=folium.Icon()))
    return fg_loc


def create_map(user_id, path):
    """
    (str) ->  str
    Returns map with all user's friends' locations as html file.
    """
    user_friends_map = folium.Map()
    friends_list = get_user_friends(user_id)
    locations = []
    for friend in friends_list:
        location = get_location(friend)
        lat, long = get_coordinates(location)
        locations.append([lat, long, friend['screen_name']])
    fg_loc = locations_layer(locations)
    user_friends_map.add_child(fg_loc)
    user_friends_map.add_child(folium.LayerControl())
    map_name = 'friends_map.html'
    user_friends_map.save(path + map_name)
    return map_name


if __name__ == "__main__":
    user_id = ''
    create_map(user_id)

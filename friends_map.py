import folium
import geocoder
from twitter import friends_list


def get_user_friends(user_id):
    """
    (str) -> list
    Returns user's friends list.
    """
    return friends_list(user_id)


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
    user_friends_list = get_user_friends(user_id)
    locations = []
    for friend in user_friends_list:
        location = get_location(friend)
        coordinates = get_coordinates(location)
        if coordinates:
            locations.append([coordinates[0], coordinates[1], friend['screen_name']])
    fg_loc = locations_layer(locations)
    user_friends_map.add_child(fg_loc)
    user_friends_map.add_child(folium.LayerControl())
    map_name = 'friends_map.html'
    user_friends_map.save(path + map_name)
    return map_name


if __name__ == "__main__":
    user_id = ''
    create_map(user_id)

# Sue Ji 33337876

import urllib.parse
import urllib.request
import json

direction_url="http://open.mapquestapi.com/directions/v2/route?"
elevation_url="http://open.mapquestapi.com/elevation/v1/profile?"
mapquest_api_key="9LA00n6aop1cmV4Uopi5fwFMdrEOHUoG"



def build_locations_url(destinations:list) -> str:
    '''
    This function takes all the destinations during the trip,
    and builds and returns a URL that can be used to ask the
    mapquest API key for information about directions matching the search
    request.
    '''
    query_parameters = [
        ('key', mapquest_api_key), ('from', destinations[0])]
    for location in range (1,len(destinations),1):
        query_parameters.append(("to",destinations[location]))

    return direction_url  + urllib.parse.urlencode(query_parameters)



def build_LatLong_url(LatLong:str) -> str:
    '''
    This function takes a string of latitude and longitude,
    and builds and returns a URL that can be used to ask the
    mapquest for information about the elevation of each specified location.
    '''
    query_parameters = [
        ('key', mapquest_api_key), ('latLngCollection', LatLong)]

    return elevation_url + urllib.parse.urlencode(query_parameters)



def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None

    response = urllib.request.urlopen(url)
    json_text = response.read().decode(encoding = 'utf-8')
    if response != None:
        response.close()
    
    return json.loads(json_text)


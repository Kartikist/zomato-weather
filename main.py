import requests

api_key = "your-api-key"

# localit_Id = 'ZWL003027'
# ZWL003027 - ameerpet
# ZWL005963 - masab tank

def zom_weather(local_ids):
    
    url = f'https://weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id={local_ids}'
    headers = {'x-zomato-api-key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()
    # print(jsonData)
    # if jsonData["message"] == 'temporarily unavailable':
        # print (jsonData["message"])
        # print (jsonData)
        # print("hello")
        # return 'temporarily unavailable'
    # else:
        # temperature = jsonData["locality_weather_data"]['temperature']
        # rainIntensity = jsonData["locality_weather_data"]['rain_intensity']
        # rainAccum = jsonData["locality_weather_data"]['rain_accumulation']
        # temperature = print(f'Temperature = {main_data}')
        # print (jsonData)
    return jsonData



meow = zom_weather('ZWL005963')
print (meow)

if __name__ == "__main__":
    # print(get_data(place= "tokyo",days=3,kind="Temperature"))
    zom_weather('ZWL005963')

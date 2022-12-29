import requests
import json

url_for_request = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-01-21&api_key=7vzKtU7epj1KA7XWjMfmHm1v52XpvLzGouhRGt6X"

"""Get запрос Mars Rover Photos, Querying by Earth date на дату 21.01.2022"""
r = requests.get(url_for_request)
r.raise_for_status()
data = r.json()  # do not create the result file until json is parsed
with open('response.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

"""Открыть запрос хранящий json файл запроса request """
with open('response.json', 'r') as file:
    data = json.load(file)
    for photo in data:
        id_photo = data['photos'][1]
        print(id_photo)

        jstr = json.dumps(id_photo, ensure_ascii=False, indent=4)
        print(jstr)

        with open('id-922929.json', 'w') as file:
            json.dump(id_photo, file, indent=4)

c = id_photo['img_src']
print(c)




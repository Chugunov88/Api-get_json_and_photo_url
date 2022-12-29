# Тестовое задание выполняется на площадке open api NASA - https://api.nasa.gov/
# Задание выполнять в Postman
# Задача:
#
# Необходимо найти запросы Mars Rover Photos
# Выполнить запрос по Querying by Earth date на дату 21.01.2022
# Передать в переменную окружения id второй фотографии, распарсив json
# Ответ на задание прислать в следующем виде:
#
# URL получившегося запроса
# Код js для передачи переменной

import requests
import json

url_for_request = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-01-21&api_key=7vzKtU7epj1KA7XWjMfmHm1v52XpvLzGouhRGt6X"

"""Get запрос Mars Rover Photos, Querying by Earth date на дату 21.01.2022"""
r = requests.get(url_for_request)
r.raise_for_status()

data = r.json()
for photo in data:
    id_photo = data['photos'][1]
    print(id_photo)

"""Сохранить json запроса всех фото: GET Mars Rover Photos, Querying by Earth date на дату 21.01.2022"""
with open('response.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

jstr = json.dumps(id_photo, ensure_ascii=False, indent=4)
print(jstr)

with open('id-922929.json', 'w') as file:
    json.dump(id_photo, file, indent=4)

c = id_photo['img_src']
print(c)

#URL получившегося запроса GET: https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-01-21&api_key=7vzKtU7epj1KA7XWjMfmHm1v52XpvLzGouhRGt6X

#Фото с марса: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03363/opgs/edr/fcam/FRB_696038660EDR_F0922864FHAZ00304M_.JPG
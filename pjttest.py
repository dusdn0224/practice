import requests

# url = 'https://fakestoreapi.com/carts'
# data = requests.get(url).json()
# print(data)

# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97
# API key
key = "f784f99c6ad5e3197507f5d64741ae9c"
# 검색 조건
city = "Seoul,KR"

# API 요청 url (위도, 경도)
url_1 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
# API 요청 url (도시 이름)
url_2 = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

data = requests.get(url_1).json()
# print(data)

temp = data['main']['temp']
print(f'캘빈 온도: {temp}K')
print(f'섭씨 온도: {temp - 273.15:.2f}℃')
description = data['weather'][0]['description']
print(f"'날씨 설명: {description}'")

# import json

# json_data = '''
# {
#     "name": "dldusdn",
#     "age": 29,
#     "city": "seoul",
#     "hobbies": [
#         "game",
#         "bed"
#     ],
#     "isStudent": true
# }
# '''
# data = json.loads(json_data)
# print(data)
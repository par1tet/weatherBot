import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_weat(city):
    ua = UserAgent()
    request_headers = {
    'user-agent': ua.random
    }
    # city = str(input())
    # link_wiki = f'https://www.accuweather.com/ru/search-locations?query={city}'
    # request_wiki = requests.get(link_wiki, headers= request_headers)
    # print(request_wiki.status_code)
    # soup_coords_of_city = BeautifulSoup(request_wiki.text, 'lxml')
        
    # with open('wiki.html', 'w') as file:
    #     file.write(soup_coords_of_city.text)
    
    # #<a class="mw-kartographer-maplink mw-kartographer-link" data-mw-kartographer="maplink" data-style="osm-intl" href="#/maplink/1" data-zoom="12" data-lat="56.5" data-lon="31.63333" data-lang="ru" data-overlays="[&quot;_9a8d7be2afad966d65ced4a7f602a15e9db11ce1&quot;]">56°30′00″&nbsp;с.&nbsp;ш. 31°38′00″&nbsp;в.&nbsp;д.</a>
    
    # coordsLat = soup_coords_of_city.find('a', {'class': 'mw-kartographer-maplink'}).get('data-lat')
    # coordsLon = soup_coords_of_city.find('a', {'class': 'mw-kartographer-maplink'}).get('data-lon')
    # print(f'{coordsLat}, {coordsLon}')
    
    # link_weathersite = f'https://yandex.com.am/weather?lat={coordsLat}&lon={coordsLon}&via=srp'
    # request_weather = requests.get(link_weathersite, headers= request_headers)
    # print(request_weather.status_code)
    # soup_weather = BeautifulSoup(request_weather.text, 'lxml')
    
    # with open('weather.html', 'w') as file:
    #     file.write(soup_weather.text)
        
    # temparature = soup_weather.find('span', {'class': 'temp__value temp__value_with-unit'})
    # print(f'Температура: {temparature}°')
    
    link_weather = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    request_weather = requests.get(link_weather, headers = request_headers)
    print(request_weather.status_code)
    soup_coords_of_city = BeautifulSoup(request_weather.text, 'lxml')
    data = json.loads(request_weather.text)
    with open('app/weather.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(request_weather.text)
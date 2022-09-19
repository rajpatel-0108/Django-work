import requests
import key
from bs4 import BeautifulSoup

url = f'https://pixabay.com/api/videos/?key={key.api_key}&q=nature&category=nature&pretty=true'
r = requests.get(url)
# print(r.json())
# large = []
json_data = r.json()
for video in json_data['hits']:
    # print(video)
    name= video['id']
    video_url = video['videos']
    # print("video url wala: ", video_url)
    large_url = video_url['large']['url']
    print("large url: ", video_url['large']['url'])
    r = requests.get(large_url,stream=True)
    
    with open(str(name) + '.mp4', 'wb') as f:
        f.write(r.content)   
# print(large[0])


# import requests
# import key

# url = f'https://www.pexels.com/video/?key={key.pexel_key}&q=nature&category=nature&pretty=true'
# print(url)
# r = requests.get(url)
# print(r.json())
# large = []
# json_data = r.json()

# for video in json_data['hits']:
#     # print(video)
#     name= video['id']
#     video_url = video['videos']
#     # print("video url wala: ", video_url)
#     large_url = video_url['large']['url']
#     print("large url: ", video_url['large']['url'])
#     r = requests.get(large_url,stream=True)
    
#     with open(str(name) + '.mp4', 'wb') as f:
#         f.write(r.content)   
# print(large[0])

import requests


class Pexels():

    api_key = '563492ad6f91700001000001f3e523d39e564cb8956b679c45df1f28'
    base_endpoint = ''
    video_endpoint = ''
    headers = ''

    def __init__(self, api_key):
        self.base_endpoint = 'https://api.pexels.com/v1/'
        self.video_endpoint = 'https://api.pexels.com/videos/'
        self.api_key = api_key
        self.headers = {"Authorization": self.api_key}

    def search_photos(self, query='ocean', orientation='', size='', color='', locale='', page=1, per_page=15):
        term = 'search'
        query = {'query': query, 'orientation': orientation, 'size': size,
                 'color': color, 'page': page, 'per_page': per_page}
        photos = self.fetch_pexels(term, query, 'photo')
        return photos

    def curated_photos(self, page=1, per_page=15):
        term = 'curated'
        query = {'page': page, 'per_page': per_page}
        curated = self.fetch_pexels(term, query, 'photo')
        return curated

    def get_photo(self, get_id):
        term = 'photos'
        query = {}
        curated = self.fetch_pexels(term, query, 'photo', get_id)
        return curated

    def search_videos(self, query='ocean', orientation='', size='', color='', locale='', page=1, per_page=15):
        term = 'search'
        query = {'query': query, 'orientation': orientation, 'size': size,
                 'color': color, 'page': page, 'per_page': per_page}
        videos = self.fetch_pexels(term, query, 'video')
        return videos

    def popular_videos(self, min_width='', min_height='', min_duration='', max_duration='', page=1, per_page=15):
        term = 'popular'
        query = {'min_width': min_width, 'min_height': min_height, 'min_duration': min_duration,
                 'max_duration': max_duration, 'page': page, 'per_page': per_page}
        videos = self.fetch_pexels(term, query, 'video')
        return videos

    def get_video(self, get_id):
        term = 'videos'
        query = {}
        curated = self.fetch_pexels(term, query, 'video', get_id)
        return curated

    def fetch_pexels(self, term, query, search_type, get_id=0):
        endpoint = ''
        if search_type == 'photo':
            endpoint = self.base_endpoint
        elif search_type == 'video':
            endpoint = self.video_endpoint

        if get_id > 0:
            response = requests.get(format('%s%s/%s' % (endpoint, term, get_id)),
                                    headers=self.headers)
        else:
            response = requests.get(format('%s%s' % (endpoint, term)),
                                    headers=self.headers, params=query)
        return response.json()


import requests


user_agent = 'api-access-homework +https://github.com/VasilyLupuleac/discogs-api'
with open('keys.txt', 'r') as key_file:
    key, secret = key_file.readline().split()
headers = {'User-Agent': user_agent, 'Authorization': f'Discogs key={key}, secret={secret}'}

base_url = 'https://api.discogs.com/'
search_base_url = base_url + 'database/search?'

def find_album(title, artist=None):
    search_query = search_base_url + f'release_title={title}'
    if artist:
        search_query += f'&artist={artist}'
    response = requests.get(search_query, headers=headers)
    if not response.status_code == 200:
        print('Could not access the API. Status code: ', response.status_code)
        return
    match = response.json()['results'][0]
    print('Title:', match['title'])
    print('Country:', match['country'])
    print('Release year:', match['year'])
    print('Genre:', ', '.join(match['genre']))
    print('Style:', ', '.join(match['style']))

find_album(title='relayer', artist='yes')
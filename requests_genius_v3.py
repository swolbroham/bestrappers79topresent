import auth
import json
from urllib.parse import urlencode
from requests_html import AsyncHTMLSession
import asyncio
import unicodedata

with open("best_rappers.txt") as f:
    li = f.readlines()
    li = list(map(lambda x: x[:-1], li))

class url:
    def __init__(self, access_token = auth.access_token, q = None, artist_id = None, song_id = None):
        self.default_params  = {
            "access_token": access_token,
            "redirect_uri": "https://httpbin.org/anything",
            "response_type": "token"
        }
        if q:
            self.default_params["q"] = q
            self.endpoint = "/search?" +  urlencode(self.default_params)
        elif artist_id:
            self.default_params["id"] = artist_id
            self.endpoint = "/artists?" + urlencode(self.default_params)
        elif song_id:
            self.default_params["id"] = song_id
            self.endpoint = "/songs/"+urlencode(self.default_params)
        return None

async def get_resp(url, client):
    r = await client.get(url)
    return r

async def get_contents(resp):
    return resp.html

async def main(urls):
    # async with AsyncHTMLSession() as client:
    client = AsyncHTMLSession()
    responses = await asyncio.gather(*[get_resp(url, client) for url in urls])
    responses = await asyncio.gather(*[get_contents(url) for url in responses])

    return responses

base_url = "https://api.genius.com"
search_urls = list(map(lambda x: base_url+url(q = x).endpoint, li))

responses = asyncio.run(main(search_urls))

print([(x.text.encode("utf-8")) for x in responses])

# genius_response(search_url)



# class build_params:
#     def __init__(self):
#         self.base_params ={
#         "access_token" : auth.access_token,
#         "redirect_uri": "https://httpbin.org/anything",
#         "response_type": "token"
#         }

#     def search(self, q):
#         self.base_params["q"] = q
#         return urlencode(self.base_params)

#     def artist(self, id):
#         self.base_params["id"] = id
#         return urlencode(self.base_params)


# class build_url:
#     def __init__(self, params):
#         self.base_url = "https://api.genius.com"
#         self.front_url = "https://www.genius.com"
#         self.params = params

#     def search(self):
#         url = self.base_url + "/search" + "?" + self.params
#         return url

#     def artists_songs(self):
#         url = self.base_url + "/artists" + id + "/songs"
#         return url

# s = "Nicki Minaj"
# search_artist = build_params().search(s)



# results = S.get(build_url(search_artist).search()).json()["response"]["hits"]

# id_results = list(map(lambda x: x["result"]["primary_artist"]["id"], results))

# most_likely = max(id_results, key = id_results.count)

# songs_param = build_params().artist(most_likely)


# print(build_url(songs_param).artists_songs())

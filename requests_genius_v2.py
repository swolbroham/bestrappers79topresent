import json
import auth
import unicodedata
from requests_html import HTMLSession
from urllib.parse import urlencode



class g_params:

    def __init__(self,access_token):
        self.access_token = access_token
        self.params = {
            "access_token": self.access_token,
            "redirect_uri": "https://httpbin.org/anything",
            "response_type": "token"
        }
        return None

    def get(self):
        return self.params

    def update(self, key, value):
        assert [key, value], "no values given"
        self.params[key] = value
        return None

    def delete (self, key):
        assert key, "no key given"
        del self.params[key]
        return None

# params = g_params(123)
# print(params.get())
# params.update(key = "q",value =  "Mac Miller")
# print(params.get())
# params.delete(key = "q")
# print(params.get())

class g_requests:
    def __init__(self, access_token):
        self.base_url = "https://api.genius.com"
        self.session = HTMLSession()
        self.params = g_params(access_token)
        return None

    def search_artists(self,artist):
        self.params.update("q", artist)
        endpoint = self.get_url("/search", self.params.get())
        resp = self.session.get(endpoint).html.text
        _suff = json.loads(resp)['response']["hits"][0]['result']['primary_artist']["api_path"]
        self.params.delete("q")
        return _suff

    def get_songs(self, artist):
        artist_endpoint = self.search_artists(artist)
        self.params.update("per_page", 20)
        self.params.update("sort", "popularity")
        songs = self.get_url(artist_endpoint+"/songs", self.params.get())
        resp = self.session.get(songs).html.text
        song_json = json.loads(unicodedata.normalize("NFKC",resp))
        [self.get_lyrics(x["url"]) for x in song_json["response"]["songs"]]
        self.params.delete("per_page")
        self.params.delete("sort")
        # print([x["title"] for x in song_json["response"]["songs"]])

    def get_lyrics(self, song_path):
        if song_path == None:
            return None
        lyrics = self.session.get(song_path).html.find("div#lyrics-root", first=True).text
        print(unicodedata.normalize("NFKD",lyrics))
        # return unicodedata.normalize("NFKC", lyrics)

    def get_url(self, endpoint, params):
        return self.base_url + endpoint + "?" +urlencode(params)



S = g_requests(auth.access_token)
S.get_songs("Grandmaster caz")

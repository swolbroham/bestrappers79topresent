import json, requests
import unicodedata
import auth
from requests_html import HTMLSession
from urllib.parse import urlencode





redirect_uri = "https://httpbin.org/headers"
params = {
    "access_token": auth.access_token,
    "redirect_uri": redirect_uri,
    "response_type": "token",
    "q":"Grandmaster Caz"
}

endpoint = "https://api.genius.com/search"
endpoint += "?"+urlencode(params)

S = HTMLSession()
r = S.get(endpoint)
response = r.html.text
response = unicodedata.normalize("NFKD", response)
# release_dates = [x["result"]["release_date_components"] for x in json.loads(response)["response"]["hits"]]
# print([x["result"]["full_title"] for x in json.loads(response)["response"]["hits"]])

# for x in json.loads(response)["response"]["hits"]:
#     print(x["result"]["primary_artist"]["api_path"])

artists_suff = json.loads(response)["response"]["hits"][0]["result"]["primary_artist"]["api_path"]

base_url = "https://api.genius.com"

songs = base_url+artists_suff+"/songs"
del params["q"]
# params["per_page"] = 20
# params["page"] = 1
songs+="?"+urlencode(params)
discography = S.get(songs)
print(discography.html.text)

# lyrics = S.get("https://genius.com/Mac-miller-self-care-lyrics")
# print(lyrics)
# # print(unicodedata.normalize("NFKD",str(lyrics.text.encode("utf-8"))))
# print(lyrics.html.find("div#lyrics-root", first = True).text)

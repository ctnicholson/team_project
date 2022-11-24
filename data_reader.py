import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "95545dabcc3cfa791d8e0f5198ff71b1"
    }

conn.request("GET", "/leagues/?id=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))













# url = "https://soccer.sportmonks.com/api/v2.0/leagues"

# response = requests.get(
#     'https://soccer.sportmonks.com/api/v2.0/leagues',
#     params={'api_token': API_KEY}
# )

# response_data = json.loads(response.text)
# print(response_data)
# print(get_data(f"teams/search/USA",{}))


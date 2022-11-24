import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "95545dabcc3cfa791d8e0f5198ff71b1"
    }

conn.request("GET", "/fixtures/?league=1&season=2022", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
import requests
from requests.exceptions import HTTPError

with open('devKEY.txt') as f:
    KEY = f.readline()

gameName = input ("Summoner's name: ")    

try:
    response = requests.get('https://la2.api.riotgames.com/tft/summoner/v1/summoners/by-name/' + gameName + '?api_key=' + KEY)
except HTTPError as http_err:
    print(f'HTTP error ocurred: {http_err}')
except Exception as err:
    print(f'Other error ocurred: {err}')
else:
    summonerData = response.json()

summonerID = summonerData['id']

rankedRequest = requests.get('https://la2.api.riotgames.com/tft/league/v1/entries/by-summoner/' + summonerID + '?api_key=' + KEY)
rankData = rankedRequest.json()

tier = rankData[0]['tier']
rank = rankData[0]['rank']
leaguePoints = str(rankData[0]['leaguePoints'])

print(gameName + '\n' + 'Rank: ' + tier + ' ' + rank + '\n' + 'LP: ' + leaguePoints)
import requests
from requests.exceptions import HTTPError
import os

with open('devKEY.txt') as f:
    KEY = f.readline()

def request_data(summonerName, region):    
    try:
        response = requests.get('https://la2.api.riotgames.com/tft/summoner/v1/summoners/by-name/' + summonerName + '?api_key=' + KEY)
    except HTTPError as http_err:
        print(f'HTTP error ocurred: {http_err}')
    except Exception as err:
        print(f'Other error ocurred: {err}')
    else:
        summonerData = response.json()

        summonerID = summonerData['id']

        rankedRequest = requests.get('https://la2.api.riotgames.com/tft/league/v1/entries/by-summoner/' + summonerID + '?api_key=' + KEY)
        rankData = rankedRequest.json()

        return rankData,summonerData

def get_league_rank(rankData):    
    tier = rankData[0]['tier']
    rank = rankData[0]['rank']
    leaguePoints = str(rankData[0]['leaguePoints'])

    return [tier,rank,leaguePoints]



def get_match_history(puuid):
    matchList = requests.get('https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/'+puuid+'/ids?count=3&api_key=' + KEY)
    matchIds = matchList.json()
    matchPlacements = []
    for match in matchIds:
        matchRequest = requests.get("https://americas.api.riotgames.com/tft/match/v1/matches/" + match +"?api_key=" + KEY)
        matchData = matchRequest.json()
        foundSummoner = False
        j=0
        while (not foundSummoner and j<8):
            playerTemp = matchData["info"]["participants"]
            if (playerTemp[j]["puuid"] == puuid):
                matchPlacements.append(playerTemp[j]["placement"])
                foundSummoner = True
            else:
                j+=1        

    return matchPlacements
    
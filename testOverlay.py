import rankedData
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests
from requests.exceptions import HTTPError
import os


class overlayGUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("overlay.ui",self)

summonerName = "MrFaso"
region = "LA2"

rawData, summonerData = rankedData.request_data(summonerName, region)
parsedData = rankedData.get_league_rank(rawData)
puuid = summonerData["puuid"]
matchPlacements = rankedData.get_match_history(puuid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = overlayGUI()
    overlay.leagueText.setText(parsedData[0]+ " " + parsedData[1] + "\n" + parsedData[2] + " LP")
    overlay.leaguePhoto.setPixmap(QtGui.QPixmap('media/' + parsedData[0] + '.png'))
    overlay.placementText.setText(str(matchPlacements[0]) + "\n" + str(matchPlacements[1]) + "\n" + str(matchPlacements[2]) )
    overlay.show()
    sys.exit(app.exec_())


import rankedData
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

class overlayGUI(QMainWindow):
    def __init__(self):
        super().__init__()    
        uic.loadUi("overlay.ui",self)
    

class loginGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("guiAlpha.ui", self)

        self.searchSummonerButton.clicked.connect(self.button_activate)

        regionListStr = ['Select Region','LA1','LA2','BR1','EUN1','EUW1','JP1','KR','NA1','OC1','RU1','TR1']
        self.regionList.addItems(regionListStr)

        self.overlay = overlayGUI()

    def button_activate(self):

        summonerName = self.summonerEntry.text()
        region = str(self.regionList.currentText())

        rawData, summonerData = rankedData.request_data(summonerName,region)
        parsedData = rankedData.get_league_rank(rawData)
        puuid = summonerData["puuid"]
        matchPlacements = rankedData.get_match_history(puuid)

        print(rawData)
        print(summonerData)
        print("puuid: " + puuid)
        print(matchPlacements)

        self.overlay.leagueText.setText(parsedData[0]+ " " + parsedData[1] + "\n" + parsedData[2] + " LP")
        self.overlay.leaguePhoto.setPixmap(QtGui.QPixmap('media/' + parsedData[0] + '.png'))
        self.overlay.placementText.setText(str(matchPlacements[0]) + "\n" + str(matchPlacements[1]) + "\n" + str(matchPlacements[2]) )
        self.overlay.show()



        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = loginGUI()
    GUI.show()
    sys.exit(app.exec_())
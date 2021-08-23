import rankedData
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

class overlay_GUI(QMainWindow):
    def __init__(self):
        super().__init__()    
        uic.loadUi("overlay.ui",self)
    

class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("guiAlpha.ui", self)
        self.searchSummonerButton.clicked.connect(self.button_activate)
        regionListStr = ['LA1','LA2','BR1','EUN1','EUW1','JP1','KR','NA1','OC1','RU1','TR1']
        self.regionList.addItems(regionListStr)

        self.overlay = overlay_GUI()

    def button_activate(self):
        var = self.summonerEntry.text()
        region = str(self.regionList.currentText())
        rawData = rankedData.gather_data(var,region)
        parsedData = rankedData.get_league_rank(rawData)
        self.overlay.leagueText.setText(parsedData[0] + "\n" + parsedData[1])
        photoPath = rankedData.get_photo_path(parsedData[0])
        self.overlay.leaguePhoto.setPixmap(QtGui.QPixmap('media/' + parsedData[0] + '.png'))
        self.overlay.show()

            








if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
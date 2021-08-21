import rankedData
import sys
from PyQt5 import uic
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

        self.overlay = overlay_GUI()

    def button_activate(self):
        var = self.summonerEntry.text()
        print(var)
        rawData = rankedData.gather_data(var,"LA2")
        parsedData = rankedData.get_league_rank(rawData)
        print(parsedData)
        self.overlay.leagueText.setText(parsedData[0] + "\n" + parsedData[1])
        self.overlay.show()

            








if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
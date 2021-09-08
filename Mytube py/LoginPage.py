from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QGraphicsOpacityEffect,QApplication
import sys

import MytubeUi
import PlaylistPage

class LoginLogic:

    def __init__(self):
        ui.LoginBtn.clicked.connect(self.goPlaylistPage)
        ui.backBtn.clicked.connect (self.logout)
        ui.RegisterBtn.clicked.connect (self.goRegisterPage)
    
    def goPlaylistPage(self):
        idvalue = ui.idTypeLine.text()
        self.playlist = PlaylistPage.PlaylistLogic(ui,idvalue)
        currentpage = ui.stackedWidget.currentIndex()
        ui.stackedWidget.setCurrentIndex(currentpage+2)

    def logout(self):
        currentpage = ui.stackedWidget.currentIndex()
        ui.stackedWidget.setCurrentIndex(currentpage-1)

    def goRegisterPage(self):
        currentpage = ui.stackedWidget.currentIndex()
        ui.stackedWidget.setCurrentIndex(currentpage+1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = MytubeUi.MainUi()

    Lg = LoginLogic()
    
    sys.exit(app.exec_())
from RegisterPage import RegisterLogic
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QGraphicsOpacityEffect,QApplication
import sys

import MytubeUi
import MytubeDbLogic
import PlaylistPage,RegisterPage

class LoginLogic:

    def __init__(self):
        self.db = MytubeDbLogic.DbLogic(ui)
        ui.LoginBtn.clicked.connect(self.loginCheck)
        ui.RegisterBtn.clicked.connect(self.goRegisterPage)

    def loginCheck(self):
        self.msgBox = QtWidgets.QMessageBox()

        idValue = ui.idTypeLine.text()
        pwValue = ui.pwTypeLine.text()
        self.db.login(idValue,pwValue)
        if idValue == "":
            self.msgBox.setInformativeText("아이디를 입력해주세요.")
            self.loginWarning() 
        elif pwValue == "":
            self.msgBox.setInformativeText("비밀번호를 입력해주세요.")
            self.loginWarning() 
        elif self.db.loginState == False :
            self.msgBox.setInformativeText("아이디 또는 비밀번호를 다시 확인해주세요.")
            self.loginWarning()
        else :
            id = ui.idTypeLine.text()
            self.playlist = PlaylistPage.PlaylistLogic(ui,id)

            self.loginPageClear()
            currentpage = ui.stackedWidget.currentIndex()
            ui.stackedWidget.setCurrentIndex(currentpage+2)

    def loginWarning(self):
        self.msgBox.setWindowTitle("로그인 오류")  
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.msgBox.exec_()

    def loginPageClear(self):
        ui.idTypeLine.setText("")
        ui.pwTypeLine.setText("")

    def goRegisterPage(self):
        self.loginPageClear()
        self.register = RegisterPage.RegisterLogic(ui)
        currentpage = ui.stackedWidget.currentIndex()
        ui.stackedWidget.setCurrentIndex(currentpage+1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = MytubeUi.MainUi()

    Lg = LoginLogic()
    
    sys.exit(app.exec_())
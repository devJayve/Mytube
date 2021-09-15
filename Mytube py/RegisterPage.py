from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QGraphicsOpacityEffect,QApplication
import sys
import re

import MytubeDbLogic

class RegisterLogic:

    def __init__(self,ui):
        self.db = MytubeDbLogic.DbLogic(ui)
        self.ui = ui
        self.idState = False
        self.pwState = False
        self.pwOverlapState = False
        self.phoneNumState = False
        self.infoAgreeState = True
        self.idBtn = False
        self.ui.overlapCheck.clicked.connect(self.idOverlap)
        self.ui.rgIdLine.textChanged.connect(self.idCheck)
        self.ui.rgPwLine.textChanged.connect(self.pwCheck)
        self.ui.rgPwLine.textChanged.connect(self.pwOverlap)
        self.ui.rgPwLine2.textChanged.connect(self.pwOverlap)
        self.ui.rgFinishBtn.clicked.connect(self.registerApprove)
        self.ui.rgPhoneNumber.textChanged.connect(self.phoneNumberCheck)
        self.ui.personalInfoY.toggled.connect(self.InfoAgreeCheck)


    def idCheck(self):
        self.idBtn = False
        self.idState = False
        idValue = self.ui.rgIdLine.text()
        if idValue == " ":
            self.ui.rgIdCheckLabel.setText("아이디를 입력해주세요.")
            self.ui.overlapCheck.setDisabled(True)

        elif len(idValue) < 8:
            self.ui.rgIdCheckLabel.setText("8자 이상 입력해주세요.")
            self.ui.overlapCheck.setDisabled(True)
        
        elif len(idValue) >20:
            self.ui.rgIdCheckLabel.setText("20자 이하로 입력해주세요.")
            self.ui.overlapCheck.setDisabled(True)
        else :
            self.ui.rgIdCheckLabel.setText("")
            self.ui.overlapCheck.setDisabled(False)
            self.idBtn = True
        
    def idOverlap(self):
        id = self.ui.rgIdLine.text()
        self.db.bringOverlapIdValue(id)
        self.idState = False
        if self.db.overlapState == True:
            self.ui.rgIdCheckLabel.setText("중복된 아이디입니다.")
        
        else :
            self.ui.rgIdCheckLabel.setText("사용가능한 아이디 입니다.")
            self.ui.rgIdCheckLabel.setStyleSheet("color:rgb(0, 0, 255);")
            self.idState = True

    def pwCheck(self):
        self.ui.rgPwCheckLabel.show()
        self.pwSate = False
        pwValue = self.ui.rgPwLine.text()
        if len(pwValue) < 8 :
            self.ui.rgPwCheckLabel.setText("8자 이상으로 입력해주세요.")

        elif re.search('[0-9]+',pwValue) is None:
            self.ui.rgPwCheckLabel.setText("최소 1개 이상의 숫자를 포함해주세요.")
        
        elif re.search('[a-zA-Z]+', pwValue) is None:
            self.ui.rgPwCheckLabel.setText("최소 1개 이상의 영문 대소문자를 포함해주세요.")

        elif re.search('[~!@#$%^&*(),<.>/?]+',pwValue) is None:
            self.ui.rgPwCheckLabel.setText("최소 1개 이상의 특수문자를 포함해주세요.")

        elif len(pwValue) > 20 :
            self.ui.rgPwCheckLabel.setText("20자 이하로 입력해주세요.")
        else :
            self.ui.rgPwCheckLabel.hide()
            self.pwState = True

    def pwOverlap(self):
        self.pwOverlapState = False
        if self.ui.rgPwLine.text() != self.ui.rgPwLine2.text():
            self.ui.rgPwCheckLabel2.setText("비밀번호가 일치하지 않습니다.")
        else :
            self.ui.rgPwCheckLabel2.setText("비밀번호가 일치합니다.")
            self.ui.rgPwCheckLabel2.setStyleSheet("color:rgb(0, 0, 255);")
            self.pwOverlapState = True

    def InfoAgreeCheck(self):
        if self.ui.personalInfoY.isChecked():
            self.infoAgreeState = True
        else :
            self.infoAgreeSTate = False

    def phoneNumberCheck(self):
        if len(self.ui.rgPhoneNumber.text()) == 11:
            self.phoneNumState = True
        else :
            self.phoneNumState = False

    def registerApprove(self):
        self.msgBox = QtWidgets.QMessageBox()
        if self.idState == False:
            self.msgBox.setInformativeText("아이디를 다시 확인해주세요.")
            self.registerWarning()
        elif self.pwState == False:
            self.msgBox.setInformativeText("비밀번호를 다시 확인해주세요.")
            self.registerWarning()
        elif self.pwOverlapState == False:
            self.msgBox.setInformativeText("입력된 비밀번호가 서로 일치하지 않습니다.")
            self.registerWarning()
        elif self.phoneNumState == False:
            self.msgBox.setInformativeText("전화번호를 다시 확인해주세요.")
            self.registerWarning()
        elif self.infoAgreeState == False:
            self.msgBox.setInformativeText("개인정보 수집에 동의해주세요.")
            self.registerWarning()
        
        else :
            self.db.newUser()
            self.registerClear()
            currentpage = self.ui.stackedWidget.currentIndex()
            self.ui.stackedWidget.setCurrentIndex(currentpage-1)
            

    def registerWarning(self):
        self.msgBox.setWindowTitle("회원가입 오류")  
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.msgBox.exec_()

    def registerClear(self):
        self.ui.rgIdLine.setText("")
        self.ui.rgPwLine.setText("")
        self.ui.rgPwLine2.setText("")
        self.ui.rgPhoneNumber.setText("")

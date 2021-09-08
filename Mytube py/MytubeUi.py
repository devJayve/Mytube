from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIcon
import sys

class MainUi(object):

    def __init__(self):
        
        # MainWindow
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1600,900)
        self.mainWindow.setWindowIcon(QIcon('Mytube photo/youtube-logo.png'))
        self.mainWindow.setWindowTitle("Mytube")
        self.mainWindow.setFixedSize(1600, 900)
        
        #centralWidget
        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))

        #stackWidgetS
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.stackedWidget.setObjectName("stackedWidget")
        
        #Image
        self.logoImage = (QtGui.QPixmap("Mytube photo/MainLogo.png")).scaled(670, 300, QtCore.Qt.KeepAspectRatio)
        self.registerLogoImage = (QtGui.QPixmap("Mytube photo/Register.png")).scaled(401, 1000, QtCore.Qt.KeepAspectRatio)
        self.whiteLabel = (QtGui.QPixmap("Mytube photo/whiteLine.png")).scaled(1500, 110, QtCore.Qt.KeepAspectRatio)
        self.whiteLabel2 = (QtGui.QPixmap("Mytube photo/whiteLine2.png")).scaled(1080,150, QtCore.Qt.KeepAspectRatio)
        self.backIcon = (QtGui.QPixmap("Mytube photo/backBtnImage.png")).scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.addIcon = (QtGui.QPixmap("Mytube photo/addIcon.png")).scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.userIcon = (QtGui.QPixmap("Mytube photo/userIcon.png")).scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.nonePlayList = (QtGui.QPixmap("Mytube photo/NonePlaylistIcon.png")).scaled(540, 370, QtCore.Qt.KeepAspectRatio)
        self.tinyLogoImg = (QtGui.QPixmap("Mytube photo/MainLogo.png")).scaled(140, 90, QtCore.Qt.KeepAspectRatio)

        #font
        self.font1 = QtGui.QFont()
        self.font1.setFamily("에스코어 드림 3 Light")
        self.font1.setPointSize(10)
        self.font2 = QtGui.QFont()
        self.font2.setFamily("에스코어 드림 4 Regular")
        self.font2.setPointSize(10)
        self.font3 = QtGui.QFont()
        self.font3.setFamily("에스코어 드림 5 Medium")
        self.font3.setPointSize(11)
        self.font4 = QtGui.QFont()
        self.font4.setFamily("에스코어 드림 6 Bold")
        self.font4.setPointSize(15)
    

        #BtnList
        self.LoginPageBtnList = []
        self.RegisterPageBtnList = []
        self.rgTypeObject = []

        self.LoginPageUi()
        self.RegisterPageUi()
        self.PlaylistPageUi()
        self.VideoPageUi()
        self.retranslateUi(self.mainWindow)
        self.stackedWidget.setCurrentIndex(3)

        self.mainWindow.show()
        
    def LoginPageUi(self):
        self.LoginPage = QtWidgets.QWidget()
        self.LoginPage.setObjectName("LoginPage")
        self.LoginPage.setStyleSheet(
            "background-color: black;"
        )

        self.MainLogo = QtWidgets.QLabel(self.LoginPage)
        self.MainLogo.setGeometry(QtCore.QRect(460, 130, 671, 300))
        self.MainLogo.setPixmap(self.logoImage)

        self.idTypeLine = QtWidgets.QLineEdit(self.LoginPage)
        self.idTypeLine.setGeometry(510,460,411,51)
        self.idTypeLine.setStyleSheet("background-color: white;")
        self.idTypeLine.setFont(self.font2)

        self.pwTypeLine = QtWidgets.QLineEdit(self.LoginPage)
        self.pwTypeLine.setGeometry(510,550,411,51)
        self.pwTypeLine.setStyleSheet("background-color: white;")
        self.pwTypeLine.setEchoMode(QLineEdit.Password)
        self.pwTypeLine.setFont(self.font2)

        self.LoginBtn = QtWidgets.QPushButton(self.LoginPage)
        self.LoginBtn.setGeometry(QtCore.QRect(960,460,110,140))
        self.LoginBtn.setFont(self.font3)
        self.LoginBtn.setText("로그인")
        self.LoginBtn.setStyleSheet(
            "background-color: rgb(219, 32, 44);"
            "color:white;"
            )

        self.RegisterBtn = QtWidgets.QPushButton(self.LoginPage)
        self.RegisterBtn.setGeometry(QtCore.QRect(620,630,260,50))
        self.RegisterBtn.setFont(self.font3)
        self.RegisterBtn.setText("회원가입")
        self.RegisterBtn.setStyleSheet(
            "background-color: rgb(219, 32, 44);"
            "color:white;"
            )
        self.stackedWidget.addWidget(self.LoginPage)

    def RegisterPageUi(self):
        self.RegisterPage = QtWidgets.QWidget()
        self.RegisterPage.setObjectName("LoginPage")
        self.RegisterPage.setStyleSheet(
            "background-color: rgb(242, 242, 242);"
        )

        self.RegisterLogo = QtWidgets.QLabel(self.RegisterPage)
        self.RegisterLogo.setStyleSheet("background-color: black;")
        self.RegisterLogo.setGeometry(QtCore.QRect(0, 0, 400, 1000))
        self.RegisterLogo.setPixmap(self.registerLogoImage)

        self.registerLabelList = ['아이디','비밀번호','비밀번호\n재확인','연락처','생년월일']
        for i in range(0,5):
            registerLabel = QtWidgets.QLabel(self.RegisterPage)
            registerLabel.setGeometry(QtCore.QRect(450, 60+100*i, 90, 55))
            registerLabel.setText(self.registerLabelList[i])
            registerLabel.setFont(self.font3)
            registerLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        self.rgIdLine = QtWidgets.QLineEdit(self.RegisterPage)
        self.rgIdLine.setGeometry(QtCore.QRect(570, 70, 441, 41))
        self.rgTypeObject.append(self.rgIdLine)

        self.overlapCheck = QtWidgets.QPushButton(self.RegisterPage)
        self.overlapCheck.setGeometry(QtCore.QRect(1050, 70, 100, 40))
        self.overlapCheck.setFont(self.font2)
        self.overlapCheck.setText("중복확인")
        self.RegisterPageBtnList.append(self.overlapCheck)

        self.rgPwLine = QtWidgets.QLineEdit(self.RegisterPage)
        self.rgPwLine.setGeometry(QtCore.QRect(570, 170, 441, 41))
        self.rgTypeObject.append(self.rgPwLine)

        self.rgPwLine2 = QtWidgets.QLineEdit(self.RegisterPage)
        self.rgPwLine2.setGeometry(QtCore.QRect(570, 270, 441, 41))
        self.rgTypeObject.append(self.rgPwLine2)

        self.rgCountryNumCmb = QtWidgets.QComboBox(self.RegisterPage)
        self.rgCountryNumCmb.setGeometry(QtCore.QRect(570, 370, 81, 41))
        self.rgCountryNumCmb.addItem("82+")
        self.rgTypeObject.append(self.rgCountryNumCmb)

        self.rgPhoneNumber = QtWidgets.QLineEdit(self.RegisterPage)
        self.rgPhoneNumber.setGeometry(670,370,331,41)
        self.rgTypeObject.append(self.rgPhoneNumber)

        self.yearCmb = QtWidgets.QComboBox(self.RegisterPage)
        self.yearCmb.setGeometry(QtCore.QRect(570, 470, 140, 41))
        for i in range(0,30):
            self.yearCmb.addItem(str(1990+i))
        self.rgTypeObject.append(self.yearCmb)

        self.monthCmb = QtWidgets.QComboBox(self.RegisterPage)
        self.monthCmb.setGeometry(QtCore.QRect(740, 470, 80, 41))
        for i in range(0,12):
            self.monthCmb.addItem(str(1+i))
        self.rgTypeObject.append(self.monthCmb)

        self.dayCmb = QtWidgets.QComboBox(self.RegisterPage)
        self.dayCmb.setGeometry(QtCore.QRect(850, 470, 80, 41))
        for i in range(0,31):
            self.dayCmb.addItem(str(1+i)) 
        self.rgTypeObject.append(self.dayCmb) 

        self.personalInfo = QtWidgets.QTextBrowser(self.RegisterPage)
        self.personalInfo.setGeometry(QtCore.QRect(460, 560, 1060, 150))
        self.personalInfo.setObjectName("personalInfo")
        self.rgTypeObject.append(self.personalInfo)

        self.personalInfoY = QtWidgets.QRadioButton(self.RegisterPage)
        self.personalInfoY.setGeometry(QtCore.QRect(1250, 730, 130, 25))
        self.personalInfoY.setFont(self.font3)
        self.personalInfoY.setText("동의")

        self.personalInfoN = QtWidgets.QRadioButton(self.RegisterPage)
        self.personalInfoN.setGeometry(QtCore.QRect(1400, 730, 130, 25))
        self.personalInfoN.setFont(self.font3)
        self.personalInfoN.setText("비동의")

        for i in range(0,9):
            self.rgTypeObject[i].setStyleSheet(
                "background-color: white;"
                "border: 2px solid black;"
                )
            self.rgTypeObject[i].setFont(self.font2)

        self.rgFinishrBtn = QtWidgets.QPushButton(self.RegisterPage)
        self.rgFinishrBtn.setGeometry(QtCore.QRect(820,820,260,50))
        self.rgFinishrBtn.setFont(self.font3)
        self.rgFinishrBtn.setText("회원가입")
        self.rgFinishrBtn.setStyleSheet(
            "background-color: rgb(219, 32, 44);"
            "color:white;"
            )
        self.RegisterPageBtnList.append(self.rgFinishrBtn)
        
        for i in range(0,2):
            self.RegisterPageBtnList[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.stackedWidget.addWidget(self.RegisterPage)                                                                

    def PlaylistPageUi(self):
        self.PlaylistPage = QtWidgets.QWidget()
        self.PlaylistPage.setObjectName("PlaylistPage")
        self.PlaylistPage.setStyleSheet(
            "background-color: black;"
        )
        whiteLabel = QtWidgets.QLabel(self.PlaylistPage)
        whiteLabel.setGeometry(QtCore.QRect(70,60,1430,110))
        whiteLabel.setPixmap(self.whiteLabel)

        self.backBtn = QtWidgets.QPushButton(self.PlaylistPage) 
        self.backBtn.setGeometry(QtCore.QRect(150,80,151,61))
        self.backBtn.setText("뒤로가기")
        self.backBtn.setFont(self.font3)
        self.backBtn.setStyleSheet(
            "color:white;"
            "background-color:black;")
        self.backBtn.setIcon(QtGui.QIcon(self.backIcon))
        self.backBtn.setIconSize(QtCore.QSize(50,50))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.addPlaylistBtn = QtWidgets.QPushButton(self.PlaylistPage)
        self.addPlaylistBtn.setGeometry(QtCore.QRect(320,80,200,61))  
        self.addPlaylistBtn.setText("재생목록 추가")
        self.addPlaylistBtn.setFont(self.font3)
        self.addPlaylistBtn.setStyleSheet(
            "color:white;"
            "background-color:black;")
        self.addPlaylistBtn.setIcon(QtGui.QIcon(self.addIcon))
        self.addPlaylistBtn.setIconSize(QtCore.QSize(50,50))
        self.addPlaylistBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.userInfoBtn = QtWidgets.QPushButton(self.PlaylistPage)
        self.userInfoBtn.setGeometry(QtCore.QRect(900,80,451,61))
        self.userInfoBtn.setText("김주영님의 플레이리스트")
        self.userInfoBtn.setFont(self.font4)
        self.userInfoBtn.setStyleSheet(
            "color:white;"
            "background-color:black;")
        self.userInfoBtn.setIcon(QtGui.QIcon(self.userIcon))
        self.userInfoBtn.setIconSize(QtCore.QSize(50,50))
        self.userInfoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 

        self.nonePlayListLabel = QtWidgets.QLabel(self.PlaylistPage)
        self.nonePlayListLabel.setGeometry(QtCore.QRect(500,310,540,370))  
        self.nonePlayListLabel.setPixmap(self.nonePlayList)


        self.stackedWidget.addWidget(self.PlaylistPage)  

    def VideoPageUi (self):
        self.VideoPage = QtWidgets.QWidget()
        self.VideoPage.setObjectName("VideoPage")
        self.VideoPage.setStyleSheet(
            "background-color: black;"
        )

        self.rightDesign = QtWidgets.QScrollArea(self.VideoPage)
        self.rightDesign.setStyleSheet("background-color:rgb(242,242,242);")
        self.rightDesign.setGeometry(QtCore.QRect(1100, 0, 500, 900))

        self.topLabel = QtWidgets.QLabel(self.VideoPage)
        self.topLabel.setGeometry(QtCore.QRect(0, 30, 1100, 150))
        #self.topLabel.setStyleSheet("background-color:black;")
        self.topLabel.setPixmap(self.whiteLabel2)

        self.Mytubelogo = QtWidgets.QLabel(self.VideoPage)
        self.Mytubelogo.setGeometry(QtCore.QRect(50, 55, 140, 90))
        self.Mytubelogo.setPixmap(self.tinyLogoImg)

        self.backBtn2 = QtWidgets.QPushButton(self.VideoPage) 
        self.backBtn2.setGeometry(QtCore.QRect(850,60,150,80))
        self.backBtn2.setText("뒤로가기")
        self.backBtn2.setFont(self.font3)
        self.backBtn2.setStyleSheet(
            "color:white;"
            "background-color:black;")
        self.backBtn2.setIcon(QtGui.QIcon(self.backIcon))
        self.backBtn2.setIconSize(QtCore.QSize(50,50))
        self.backBtn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.videoName = QtWidgets.QPushButton(self.VideoPage) 
        self.videoName.setGeometry(QtCore.QRect(220,60,300,80))
        self.videoName.setFont(self.font4)
        self.videoName.setText("영상 제목입니다.")
        self.videoName.setStyleSheet("color:white;")



        self.stackedWidget.addWidget(self.VideoPage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.personalInfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'나눔고딕\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:70%;\"><span style=\" font-family:\'HY중고딕\'; font-size:7pt; font-weight:600;\">&lt; 개인정보 수집 및 이용 &gt;</span></p>\n"
        "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:110%;\"><span style=\" font-family:\'Gulim\'; font-size:7pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'HY중고딕\'; font-size:7pt;\">○ 개인정보 수집·이용의 목적: 제안서 심의·연구자 선정, 연구 참여 제한여부 확인, 연구과제 관리 </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'HY중고딕\'; font-size:7pt;\">○ 수집하려는 개인정보의 항목: 인적사항(생년월일, 성명, 핸드폰번호, 이메일 등), 학력, 경력, 연구업적 등</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'HY중고딕\'; font-size:7pt;\">○ 개인정보의 보유 및 이용 기간 : 제안서를 접수하는 시점부터 선정·심의, 참여제한 여부, 과제관리 종료 시점까지 보유, 보유기간 종료 시 재생이 불가능한 방법으로 즉시 파기</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Gulim\'; font-size:7pt;\"><br /></p></body></html>"))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    mu = MainUi()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QDialog, QGraphicsOpacityEffect,QApplication, QMessageBox
from PyQt5.QtCore import Qt 
import sys
import pafy
import urllib.request
from youtubesearchpython import VideosSearch

import MytubeDbLogic,VideoPage

class PlaylistLogic:

    def __init__(self,ui,id):
        self.db = MytubeDbLogic.DbLogic(ui)
        self.ui = ui
        self.id = id
        self.clickNum = 0
        self.myPlaylist = []

        self.db.bringPlList(self.id)

        self.ui.addPlaylistBtn.clicked.connect(self.PlaylistaddWindow)
        self.ui.userInfoBtn.clicked.connect(self.modifyPIWindow)
        self.ui.backBtn.clicked.connect(self.logout)
        self.ui.searchBtn.clicked.connect(self.addVideo)

        for index in range(0,9):
            self.ui.plWidgetList[index].mousePressEvent = lambda event, i = index : self.plPressEvent(event,i)

    def createVideo(self):
        url = "https://www.youtube.com/watch?v=get7Pxsh7WA"
        video = pafy.new(url)
        print(f"영상제목: {video.title}")

    def PlaylistaddWindow(self):
        self.ui.typeListLine.setText("")
        self.ui.addDialog.show()
        self.ui.btnDialog.clicked.connect(self.addPlaylist)

    def addPlaylist(self):
        self.msgBox = QtWidgets.QMessageBox()
        playlistName = self.ui.typeListLine.text()
        if len(playlistName) == 0:
            self.msgBox.setInformativeText("플레이리스트 이름을 입력해주세요.")
        elif len(playlistName) > 20:
            self.msgBox.setInformativeText("이름은 20자 이하로 입력해주세요.")
        else :
            self.ui.addDialog.close()
            self.db.addPlaylist(self.id,playlistName)
            self.ui.typeListLine.clear()

    def plAddWarning(self):
        self.msgBox.setWindowTitle("플레이리스트 오류")  
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.msgBox.exec_()

    def logout(self):
        logoutMsg = QtWidgets.QMessageBox()
        logoutMsg.setWindowTitle("로그아웃")
        logoutMsg.setInformativeText("로그아웃 하시겠습니까?")  
        btnYes = logoutMsg.addButton("예",QMessageBox.ActionRole)
        btnNo = logoutMsg.addButton("아니오",QMessageBox.ActionRole)
        logoutMsg.exec_()
        if logoutMsg.clickedButton() == btnYes:
            print("로그아웃")
            currentpage = self.ui.stackedWidget.currentIndex()
            self.ui.stackedWidget.setCurrentIndex(currentpage-2)
        else :
            pass

    def modifyPIWindow(self):
        self.ui.idLine.setText("{}님".format(self.id))
        self.ui.modifyDialog.show()
        self.ui.modifyFinishBtn.clicked.connect(self.modifyPI)

    def modifyPI(self):
        self.ui.modifyDialog.close()

    def searchVideo(self):
        pass

    def plPressEvent(self,event,widgetNum):
        self.clickNum = widgetNum

        if event.buttons() & Qt.LeftButton:
            self.db.plNameCheck(self.id,widgetNum)
            if self.db.videoExist == True:
                self.video = VideoPage.VideoLogic(self.ui)
                currentpage = self.ui.stackedWidget.currentIndex()
                self.ui.stackedWidget.setCurrentIndex(currentpage+1)
            else :
                self.noVideoMsg = QtWidgets.QMessageBox()
                self.noVideoMsg.setWindowTitle("비디오 오류")  
                self.noVideoMsg.setInformativeText("플레이리스트에 비디오를 추가해주세요.")
                self.noVideoMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.noVideoMsg.setDefaultButton(QtWidgets.QMessageBox.Ok)
                self.noVideoMsg.exec_()
        if event.buttons() & Qt.RightButton:
            self.plEdit(widgetNum)
    
    def plEdit(self,widgetNum):
        plEditMsg = QtWidgets.QMessageBox()
        plEditMsg.setWindowTitle("재생목록 편집") 
        addBtn = plEditMsg.addButton("영상추가",QMessageBox.ActionRole)
        removeBtn = plEditMsg.addButton("재생목록 삭제",QMessageBox.ActionRole)
        plEditMsg.exec_()
        if plEditMsg.clickedButton() == addBtn:
            self.ui.searchDialog.show()
        elif plEditMsg.clickedButton() == removeBtn: 
            self.db.plNameCheck2(self.id,widgetNum)

    def addVideo(self):
        self.msgBox = QtWidgets.QMessageBox()
        videoName = self.ui.typeVideoLine.text()
        if videoName == "":
            self.msgBox.setInformativeText("비디오 이름을 입력해주세요.")
        else :
            videosSearch = VideosSearch(videoName, limit = 1)
            videoResult = videosSearch.result()
            url = ((videoResult['result'])[0])['link']
            video = pafy.new(url)
            self.ui.videoNameShow.setText("{}".format(video.title))
            print("{}".format(video.title))

            thumbnail = (((videoResult['result'])[0])['thumbnails'][0])['url']
            imageFromWeb = urllib.request.urlopen(thumbnail).read()
            qPixmapVar = QtGui.QPixmap()
            qPixmapVar.loadFromData(imageFromWeb)
            self.ui.videoShow.setPixmap(qPixmapVar)
        
        self.ui.videoAddBtn.clicked.connect(lambda : self.myVideo(url))

    def myVideo(self,url):
        self.db.plNameCheck3(self.id,self.clickNum,url)
        



            
            



        




    



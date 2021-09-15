import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class DbLogic:

    def __init__(self,ui):
        self.ui = ui
        self.plList = []
        self.plNum = 0
        self.overlapState = False
        self.loginState = False
        self.videoExist = False

    def bringOverlapIdValue(self,id):
        connection = sqlite3.connect("Mytubedb.db") 
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user WHERE id='" + str(id) + "';")
        data = cursor.fetchall()
        
        if len(data)==1:
            self.overlapState = True
        else :
            self.overlapState = False

    def login(self,id,pw):
        self.loginState = False
        connection = sqlite3.connect("Mytubedb.db") 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE id='" + id + "' AND password='" + pw + "';")
        data = cursor.fetchall()

        if len(data) == 1:
            self.loginState = True
        else :
            pass

    def addPlaylist(self,id,listName):
        connection = sqlite3.connect("Mytubedb.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO playlist VALUES('" + str(id) + "','" + listName + "');")

        connection.commit()
        connection.close()
        self.bringPlList(id)

    def plNameCheck(self,id,widgetNum):
        connection = sqlite3.connect("Mytubedb.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM playlist WHERE id='" + str(id) + "';")
        data = cursor.fetchall()

        playlistName = data[widgetNum][1]

        self.videoCheck(id,playlistName)

    def plNameCheck2(self,id,widgetNum):
        connection = sqlite3.connect("Mytubedb.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM playlist WHERE id='" + str(id) + "';")
        data = cursor.fetchall()

        playlistName = data[widgetNum][1]

        self.deletePl(id,playlistName)

    def plNameCheck3(self,id,widgetNum,url):
        connection = sqlite3.connect("Mytubedb.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM playlist WHERE id='" + str(id) + "';")
        data = cursor.fetchall()

        playlistName = data[widgetNum][1]

        self.videoAdd(id,playlistName,url)

    def videoCheck(self,id,playlistName):
        connection = sqlite3.connect("Mytubedb.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM video WHERE id='" + str(id) + "' AND listname ='" + playlistName + "';")
        data = cursor.fetchall()
        if len(data) > 0:
            self.videoExist = True
        else :
            self.videoExist = False

    def deletePl(self,id,playlistName):
        connection = sqlite3.connect("Mytubedb.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM playlist WHERE id='" + str(id) + "' AND listname='"+playlistName+"';")
        cursor.execute("DELETE FROM video WHERE id='" + str(id) + "' AND listname='"+playlistName+"';")

        connection.commit()
        connection.close()
        self.bringPlList(id)

    def bringPlList(self,id):
        for i in range(0,9):
            self.ui.plWidgetList[i].hide()
            self.ui.plNameList[i].hide()
        
        connection = sqlite3.connect("Mytubedb.db")
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM playlist WHERE id='" + str(id) + "';")
        data = cursor.fetchall()
        self.plNum = len(data)

        if self.plNum == 0:
            self.ui.nonePlayListLabel.show()
        else :
            self.ui.nonePlayListLabel.hide()
            for i in range(0,self.plNum):
                self.ui.plWidgetList[i].show()
                self.ui.plNameList[i].show()
                self.ui.plNameList[i].setText(data[i][1])

    def newUser(self):
        connection = sqlite3.connect("Mytubedb.db") 
        cursor = connection.cursor()
        idValue = self.ui.rgIdLine.text()
        pwValue = self.ui.rgPwLine.text()
        yearValue = self.ui.yearCmb.currentText()
        monthValue = self.ui.monthCmb.currentText()
        dayValue = self.ui.dayCmb.currentText()
        phoneNumValue = self.ui.rgPhoneNumber.text()
        dateValue = yearValue+"-"+monthValue+"-"+dayValue
        cursor.execute("INSERT INTO user VALUES('" + idValue + "','" + pwValue + "','" + phoneNumValue + "','" + dateValue + "');")
        connection.commit()
        connection.close()
    
    def videoAdd(self,id,listName,url):
        connection = sqlite3.connect("Mytubedb.db") 
        cursor = connection.cursor()
        cursor.execute("INSERT INTO video VALUES('" + str(id) + "','" + listName + "','" + url + "');")
        connection.commit()
        connection.close()



    def recordPoint(self,ID,point):
        connection = sqlite3.connect("RPSdb.db") 
        cursor = connection.cursor()
        cursor.execute("UPDATE gameInfo SET point = "+str(point)+" WHERE id = '" + ID + "';")
        connection.commit()
        connection.close()

    def changeRank(self):
        connection = sqlite3.connect("RPSdb.db") 
        cursor = connection.cursor()
        cursor.execute("SELECT * from gameInfo ORDER BY point DESC;")
        cursor.execute("SELECT * FROM gameInfo;")
        data = cursor.fetchall()
        for i in range(0,len(data)):
            self.ui.userNameList[i].setText(str(data[i][0]))
            self.ui.pointList[i].setText(str(data[i][1]))
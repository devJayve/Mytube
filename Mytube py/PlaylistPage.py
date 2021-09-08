from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QGraphicsOpacityEffect,QApplication
import sys
import pafy

import MytubeUi

class PlaylistLogic:

    def __init__(self,ui,id):
        self.ui = ui
        self.id = id

    def createVideo(self):
        url = "https://www.youtube.com/watch?v=get7Pxsh7WA"
        video = pafy.new(url)
        print(f"영상제목: {video.title}")

    



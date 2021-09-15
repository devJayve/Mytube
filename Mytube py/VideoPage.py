from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QDialog, QGraphicsOpacityEffect,QApplication, QMessageBox
from PyQt5.QtCore import Qt 
import sys
import pafy
import requests

import MytubeDbLogic

class VideoLogic:

    def __init__(self,ui):
        self.ui = ui

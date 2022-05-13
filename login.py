
import json
import sys
from tkinter import Widget
from PyQt5 import uic, QtWidgets
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
# import login_page




class Login(QMainWindow):
    
    user_name = ""

    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('ui/login_page.ui', self)
        self.login_login_page.clicked.connect(self.login)
        self.quit_login_page.clicked.connect(self.quit)
        self.show()


    def login(self):
        # login methode
        self.user_name = self.username_login_page.text()

        if not os.path.isfile('user/'+self.user_name+'.json'):
            self.signup()

        else:
            pass
    
    def signup(self):
        # signup methode
        self.user_info = {
                'username': self.user_name,
                # 'password': self.password,
                'level': 1,
                'time': 0
        }

 
        
        js_file_name = 'user/'+self.user_name+'.json'
        with open(js_file_name, 'w') as jsFile:
            jsFile.write(json.dumps(self.user_info, indent=4))


    def quit(self):
        self.close()

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
# window = Ui_MainWindow()
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
app.exec_()



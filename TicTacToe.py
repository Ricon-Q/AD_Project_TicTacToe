import sys
from random import randint

from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.Main.show()
        self.Mode.hide()
        self.comVsplay.hide()
        self.Game.hide()
        self.Result.hide()

        self.StartBtn.clicked.connect(self.funtion)

    def funtion(self):
        self.Main.hide()
        self.Mode.show()
        self.comVsplay.hide()
        self.Game.hide()
        self.Result.hide()

        self.play1.clicked.connect(self.playName)

    def playName(self):
        self.Mode.hide()
        self.Game.hide()
        self.Main.hide()
        self.Result.hide()
        self.comVsplay.show()
        self.playButton.clicked.connect(self.gamedef)


    def gamedef(self):
        self.Main.hide()
        self.comVsplay.hide()
        self.Game.show()
        self.Mode.hide()
        self.Result.hide()

        self.player1name = self.PlayLabel1.text()
        self.P1.setText(self.player1name)

        self.btn_array = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        for i in range(9):
            self.btn_array[i].clicked.connect(self.btnclick)
        self.btn_chk = {self.btn1 : '1', self.btn2 : '2', self.btn3 : '3', self.btn4 : '4', self.btn5 : '5', self.btn6 : '6', self.btn7 : '7', self.btn8: '8',self.btn9: '9'}

    def btnclick(self):

        self.sender().setText("X")
        self.btn_chk[self.sender()] = "X"
        self.btn_array.remove(self.sender())
        if(self.btn_array != []):
            self.randbtn = self.btn_array[randint(0, len(self.btn_array)-1)]
            self.randbtn.setText("O")
            self.btn_chk[self.randbtn] = "O"
            self.btn_array.remove(self.randbtn)
        else:
            self.winner = "draw"
            self.winFunc()

        self.chkwin()

    def chkwin(self):
        self.btn_final = [self.btn_chk[self.btn1], self.btn_chk[self.btn2], self.btn_chk[self.btn3], self.btn_chk[self.btn4], self.btn_chk[self.btn5], self.btn_chk[self.btn6], self.btn_chk[self.btn7], self.btn_chk[self.btn8], self.btn_chk[self.btn9]]
        if((self.btn_final[0] == self.btn_final[1]) and (self.btn_final[1] == self.btn_final[2])):
            self.winner = self.btn_final[0]
            self.winFunc()
        elif((self.btn_final[3] == self.btn_final[4]) and (self.btn_final[4] == self.btn_final[5])):
            self.winner = self.btn_final[3]
            self.winFunc()
        elif((self.btn_final[6] == self.btn_final[7]) and (self.btn_final[7] == self.btn_final[8])):
            self.winner = self.btn_final[6]
            self.winFunc()
        elif((self.btn_final[0] == self.btn_final[3]) and (self.btn_final[3] == self.btn_final[6])):
            self.winner = self.btn_final[0]
            self.winFunc()
        elif((self.btn_final[1] == self.btn_final[4]) and (self.btn_final[4] == self.btn_final[7])):
            self.winner = self.btn_final[1]
            self.winFunc()
        elif((self.btn_final[2] == self.btn_final[5]) and (self.btn_final[5] == self.btn_final[8])):
            self.winner = self.btn_final[2]
            self.winFunc()
        elif((self.btn_final[0] == self.btn_final[4]) and (self.btn_final[4] == self.btn_final[8])):
            self.winner = self.btn_final[0]
            self.winFunc()
        elif((self.btn_final[2] == self.btn_final[4]) and (self.btn_final[4] == self.btn_final[6])):
            self.winner = self.btn_final[2]
            self.winFunc()


    def winFunc(self):
        self.Main.hide()
        self.Mode.hide()
        self.comVsplay.hide()
        self.Game.hide()
        self.Result.show()

        if(self.winner == "X"):
            self.winText.setText(self.player1name + " WIN!")
        elif(self.winner == "O"):
            self.winText.setText("Computer WIN!")
        elif(self.winner == "draw"):
            self.winText.setText("DRAW!")

        self.exit.clicked.connect(self.resultfunc)
    def resultfunc(self):
         sys.exit()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
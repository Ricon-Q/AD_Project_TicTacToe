import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QStackedWidget,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class TicTacToe(QWidget):

    def __init__(self):
        super().__init__()
        self.MainWindow()
        # self.MainMenu()

    def MainWindow(self):
        self.MainMenu()
        self.setGeometry(700, 300, 550, 550)
        self.setWindowTitle('Tic Tac Toe Game')
        self.show()

    def MainMenu(self):
        self.TicTacToeFont()
        self.StartButton = QPushButton("Start", self)
        self.StartButton.move(205, 400)
        self.StartButton.resize(150, 70)
        self.StartButton.setStyleSheet("font-size:20px")

        self.StartButton.clicked.connect(self.Gamemode)

    def TicTacToeFont(self):
        self.Tic = QLabel("Tic", self)
        self.Tac = QLabel("Tac", self)
        self.Toe = QLabel("Toe", self)

        self.Tic.move(205, 50)
        self.Tac.move(190, 150)
        self.Toe.move(190, 250)

        TicFont = self.Tic.font()
        TacFont = self.Tac.font()
        ToeFont = self.Toe.font()

        TicFont.setPointSize(72)
        TacFont.setPointSize(72)
        ToeFont.setPointSize(72)

        TicFont.setBold(True)
        TacFont.setBold(True)
        ToeFont.setBold(True)

        self.Tic.setFont(TicFont)
        self.Tac.setFont(TacFont)
        self.Toe.setFont(ToeFont)

    def Gamemode(self):
        self.Tic.close()
        self.Tac.close()
        self.Toe.close()
        self.StartButton.close()

        self.modeSelect = QLabel("##Select GameMode##", self)
        self.modeSelect.move(35, 50)
        modeFont = self.modeSelect.font()
        modeFont.setPointSize(30)
        modeFont.setBold(True)
        self.modeSelect.setFont(modeFont)
        self.modeSelect.setVisible(True)

        self.ComVSPer = QPushButton("COM VS Player", self)
        self.ComVSPer.move(180, 200)
        self.ComVSPer.resize(200, 70)
        self.ComVSPer.setStyleSheet("font-size:20px")
        self.ComVSPer.setVisible(True)
        self.ComVSPer.clicked.connect(self.PlayerName)

        self.PerVSPer = QPushButton("Player VS Player", self)
        self.PerVSPer.move(180, 300)
        self.PerVSPer.resize(200, 70)
        self.PerVSPer.setStyleSheet("font-size:20px")
        self.PerVSPer.setVisible(True)
        self.PerVSPer.clicked.connect(self.PlayerName)

    def PlayerName(self):

        self.modeSelect.close()
        self.ComVSPer.close()
        self.PerVSPer.close()

        self.inputName = QLabel("Input Player Name", self)
        self.inputName.move(105, 100)
        inputFont = self.inputName.font()
        inputFont.setPointSize(30)
        self.inputName.setFont(inputFont)
        self.inputName.setVisible(True)

        if(self.sender()==self.ComVSPer):
            self.Player2 = "COM"
            self.player2bool = False

            self.inputPlayer1()
        else:
            self.player2bool = True
            self.inputPlayer1()

            self.Player2 = QLineEdit("Input Player2 Name", self)
            self.Player2.move(180, 280)
            self.Player2.resize(200, 50)
            self.Player2.setStyleSheet("font-size:20px")
            self.Player2.setVisible(True)

        self.PlayGame = QPushButton("PLAY GAME", self)
        self.PlayGame.move(360, 470)
        self.PlayGame.resize(150, 50)
        self.PlayGame.setStyleSheet("font-size:20px")
        self.PlayGame.setVisible(True)
        self.PlayGame.clicked.connect(self.GameScreen)

    def inputPlayer1(self):
        self.Player1 = QLineEdit("Input Player1 Name", self)
        self.Player1.move(180, 200)
        self.Player1.resize(200, 50)
        self.Player1.setStyleSheet("font-size:20px")
        self.Player1.setVisible(True)

    def GameScreen(self):
        self.inputName.close()
        self.Player1.close()
        if(self.player2bool == True):
            self.Player2.close()
        self.PlayGame.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec_())

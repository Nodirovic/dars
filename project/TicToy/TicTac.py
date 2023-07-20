from PyQt5.QtWidgets import *
from os import system as sys

sys("cls")

class Button(QPushButton):
    def __init__(self, btn):
        super().__init__(btn)
        self.style = """
            background-color: cyan;
            font-size: 60px;
        """
        self.setFixedSize(111, 100)
        self.setStyleSheet(self.style)

    def addStyle(self, st):
        self.setStyleSheet(self.style + st)
        


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score_x = 0
        self.score_o = 0
        self.design()
        self.restart_btn.clicked.connect(self.restart_function)

        

        self.buttons[0][0].clicked.connect(lambda: self.bosildi(0, 0))
        self.buttons[0][1].clicked.connect(lambda: self.bosildi(0, 1))
        self.buttons[0][2].clicked.connect(lambda: self.bosildi(0, 2))
        self.buttons[1][0].clicked.connect(lambda: self.bosildi(1, 0))
        self.buttons[1][1].clicked.connect(lambda: self.bosildi(1, 1))
        self.buttons[1][2].clicked.connect(lambda: self.bosildi(1, 2))
        self.buttons[2][0].clicked.connect(lambda: self.bosildi(2, 0))
        self.buttons[2][1].clicked.connect(lambda: self.bosildi(2, 1))
        self.buttons[2][2].clicked.connect(lambda: self.bosildi(2, 2))

        self.show()

    def restart_function(self):
        for i in range(len(self.buttons)):
            for k in range(len(self.buttons[i])):
                self.buttons[i][k].setText("")
        self.turn = 0
        self.turn_label.setText("X ni navbati")
        self.score_x = 0
        self.score_o = 0
        self.X_score_label.setText("X: "+ str(self.score_x))
        self.O_score_label.setText("O: "+ str(self.score_o))

    def checked_win_function(self, txt):
        for i in range(len(self.buttons)):
            for k in range(len(self.buttons[i])):
                self.buttons[i][k].setText("")
        self.turn = 0
        self.turn_label.setText("X ni navbati")
        if txt == "X":
            self.score_x += 1 
        else: self.score_o += 1
        self.X_score_label.setText("X: "+ str(self.score_x))
        self.O_score_label.setText("O: "+ str(self.score_o))




    def design(self):
        self.main_layout = QVBoxLayout(self)
        self.setStyleSheet("""
            background-color: white;
            font-size: 20px;
            font-family: Calibri;
        """)

        self.setWindowTitle("TicTacToe")
        self.setFixedSize(450, 470)
        score_layout = QVBoxLayout()

        self.X_score_label = QLabel(self)
        self.X_score_label.setText("X: 0")
        self.X_score_label.adjustSize()

        self.O_score_label = QLabel(self)
        self.O_score_label.setText("O: 0")
        self.O_score_label.adjustSize()

        score_layout.addWidget(self.X_score_label)
        score_layout.addWidget(self.O_score_label)

        self.turn_label = QLabel(self)
        self.turn_label.setText("X ni navbati")

        header_layout = QHBoxLayout()
        header_layout.addLayout(score_layout)
        header_layout.addStretch(1)
        header_layout.addWidget(self.turn_label)
        header_layout.addStretch(2)

        self.buttons = list()
        buttons_layout = QVBoxLayout()
        for i in range(3):
            button_h_layout = QHBoxLayout()
            qator = list()
            for k in range(3):
                btn = Button(self)
                qator.append(btn)
                button_h_layout.addWidget(btn)
                button_h_layout.addStretch()
            buttons_layout.addLayout(button_h_layout)
            self.buttons.append(qator)
            buttons_layout.addStretch()
                
        self.restart_btn = Button(self)
        self.restart_btn.setFixedSize(200, 35)
        self.restart_btn.setText("restart")
        self.restart_btn.addStyle("font-size: 18px; bg-color: ")

        self.restart_layout = QHBoxLayout()
        self.restart_layout.addStretch(20)
        self.restart_layout.addWidget(self.restart_btn)
        self.restart_layout.addStretch(25)

        self.main_layout.addLayout(header_layout)
        self.main_layout.addLayout(buttons_layout)
        self.main_layout.addLayout(self.restart_layout)

    def bosildi(self, s: int, q: int):
        print(self.buttons[s][q].text())
        if len(self.buttons[s][q].text()) > 0:
            return 0
        self.buttons[s][q].setText('X' if self.turn % 2 == 0 else 'O')
        self.turn_label.setText('O ni navbati' if self.turn % 2 == 0 else 'X ni navbati')
        self.turn += 1
        self.checked(self.buttons)
    def checked(self, buttons):
        if buttons[0][0].text() == buttons[1][0].text() and buttons[0][0].text() == buttons[2][0].text() and buttons[1][0].text() == buttons[2][0].text() and buttons[0][0].text() != "" and buttons[1][0].text() != "" and buttons[2][0].text() != "":
            self.checked_win_function(buttons[0][0].text())
        elif buttons[0][1].text() == buttons[1][1].text() and buttons[0][1].text() == buttons[2][1].text() and buttons[1][1].text() == buttons[2][1].text() and buttons[0][1].text() != "" and buttons[1][1].text() != "" and buttons[2][1].text() != "":
            self.checked_win_function(buttons[0][1].text())
        elif buttons[0][2].text() == buttons[1][2].text() and buttons[0][2].text() == buttons[2][2].text() and buttons[1][2].text() == buttons[2][2].text() and buttons[0][2].text() != "" and buttons[1][2].text() != "" and buttons[2][2].text() != "":
            self.checked_win_function(buttons[0][2].text())
        elif buttons[0][0].text() == buttons[0][1].text() and buttons[0][1].text() == buttons[0][2].text() and buttons[0][0].text() == buttons[0][2].text() and buttons[0][0].text() != "" and buttons[0][1].text() != "" and buttons[0][2].text() != "":
            self.checked_win_function(buttons[0][0].text())
        elif buttons[1][0].text() == buttons[1][1].text() and buttons[1][1].text() == buttons[1][2].text() and buttons[1][0].text() == buttons[1][2].text() and buttons[1][0].text() != "" and buttons[1][1].text() != "" and buttons[1][2].text() != "":
            self.checked_win_function(buttons[1][0].text())
        elif buttons[2][0].text() == buttons[2][1].text() and buttons[2][1].text() == buttons[2][2].text() and buttons[2][0].text() == buttons[2][2].text() and buttons[2][0].text() != "" and buttons[2][1].text() != "" and buttons[2][2].text() != "":
            self.checked_win_function(buttons[2][0].text())
        elif buttons[0][0].text() == buttons[1][1].text() and buttons[1][1].text() == buttons[2][2].text() and buttons[0][0].text() == buttons[2][2].text() and buttons[0][0].text() != "" and buttons[1][1].text() != "" and buttons[2][2].text() != "":
            self.checked_win_function(buttons[0][0].text())
        elif buttons[0][2].text() == buttons[1][1].text() and buttons[1][1].text() == buttons[2][0].text() and buttons[2][0].text() == buttons[0][2].text() and buttons[0][2].text() != "" and buttons[1][1].text() != "" and buttons[2][0].text() != "":
            self.checked_win_function(buttons[0][2].text())
        

app = QApplication([])

window = Window()

app.exec_()
# Form implementation generated from reading ui file 'Poker_inter.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 683)
        MainWindow.setStyleSheet("background-color: rgb(186, 231, 226);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 183, 176);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 40, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 183, 176);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 183, 176);")
        self.label_3.setObjectName("label_3")
        self.card_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_5.setGeometry(QtCore.QRect(390, 110, 101, 31))
        self.card_5.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_5.setIndent(-1)
        self.card_5.setObjectName("card_5")
        self.card_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_4.setGeometry(QtCore.QRect(290, 110, 101, 31))
        self.card_4.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_4.setIndent(-1)
        self.card_4.setObjectName("card_4")
        self.card_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_2.setGeometry(QtCore.QRect(100, 110, 101, 31))
        self.card_2.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_2.setIndent(-1)
        self.card_2.setObjectName("card_2")
        self.card_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_3.setGeometry(QtCore.QRect(200, 110, 91, 31))
        self.card_3.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_3.setIndent(-1)
        self.card_3.setObjectName("card_3")
        self.card_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_1.setGeometry(QtCore.QRect(0, 110, 101, 31))
        self.card_1.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_1.setIndent(-1)
        self.card_1.setObjectName("card_1")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 0, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(181, 255, 175);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 80, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(181, 255, 175);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 0, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 0, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.card_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_6.setGeometry(QtCore.QRect(0, 150, 91, 121))
        self.card_6.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_6.setText("")
        self.card_6.setIndent(-1)
        self.card_6.setObjectName("card_6")
        self.card_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_7.setGeometry(QtCore.QRect(100, 150, 91, 121))
        self.card_7.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_7.setText("")
        self.card_7.setIndent(-1)
        self.card_7.setObjectName("card_7")
        self.card_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_8.setGeometry(QtCore.QRect(200, 150, 91, 121))
        self.card_8.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_8.setText("")
        self.card_8.setIndent(-1)
        self.card_8.setObjectName("card_8")
        self.card_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_9.setGeometry(QtCore.QRect(300, 150, 91, 121))
        self.card_9.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_9.setText("")
        self.card_9.setIndent(-1)
        self.card_9.setObjectName("card_9")
        self.card_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_10.setGeometry(QtCore.QRect(400, 150, 91, 121))
        self.card_10.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_10.setText("")
        self.card_10.setIndent(-1)
        self.card_10.setObjectName("card_10")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 281, 91, 31))
        self.label_6.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.card_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_11.setGeometry(QtCore.QRect(0, 331, 91, 121))
        self.card_11.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_11.setText("")
        self.card_11.setIndent(-1)
        self.card_11.setObjectName("card_11")
        self.card_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_12.setGeometry(QtCore.QRect(100, 331, 91, 121))
        self.card_12.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_12.setText("")
        self.card_12.setIndent(-1)
        self.card_12.setObjectName("card_12")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 331, 91, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 361, 91, 23))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 391, 91, 23))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 420, 91, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 281, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 301, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 280, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 300, 91, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(500, 299, 91, 16))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 280, 91, 31))
        self.label_10.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 300, 91, 16))
        self.label_13.setObjectName("label_13")
        self.card_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_13.setGeometry(QtCore.QRect(300, 330, 91, 121))
        self.card_13.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_13.setText("")
        self.card_13.setIndent(-1)
        self.card_13.setObjectName("card_13")
        self.card_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_14.setGeometry(QtCore.QRect(400, 330, 91, 121))
        self.card_14.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_14.setText("")
        self.card_14.setIndent(-1)
        self.card_14.setObjectName("card_14")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(500, 279, 91, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(400, 280, 91, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(200, 479, 91, 16))
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(100, 480, 91, 16))
        self.label_18.setObjectName("label_18")
        self.card_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_15.setGeometry(QtCore.QRect(0, 510, 91, 121))
        self.card_15.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_15.setText("")
        self.card_15.setIndent(-1)
        self.card_15.setObjectName("card_15")
        self.card_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_16.setGeometry(QtCore.QRect(100, 510, 91, 121))
        self.card_16.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_16.setText("")
        self.card_16.setIndent(-1)
        self.card_16.setObjectName("card_16")
        self.label_19 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(200, 459, 91, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(100, 460, 91, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(500, 479, 91, 16))
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(400, 480, 91, 16))
        self.label_23.setObjectName("label_23")
        self.card_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_17.setGeometry(QtCore.QRect(300, 510, 91, 121))
        self.card_17.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_17.setText("")
        self.card_17.setIndent(-1)
        self.card_17.setObjectName("card_17")
        self.card_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_18.setGeometry(QtCore.QRect(400, 510, 91, 121))
        self.card_18.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"color: rgb(255, 255, 255);")
        self.card_18.setText("")
        self.card_18.setIndent(-1)
        self.card_18.setObjectName("card_18")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(500, 459, 91, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(400, 460, 91, 16))
        self.label_25.setObjectName("label_25")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 390, 91, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 419, 91, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(500, 330, 91, 23))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 360, 91, 23))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 570, 91, 23))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 599, 91, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 510, 91, 23))
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(200, 540, 91, 23))
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(500, 570, 91, 23))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 599, 91, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(500, 510, 91, 23))
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(500, 540, 91, 23))
        self.pushButton_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 460, 91, 31))
        self.label_17.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(300, 460, 91, 31))
        self.label_22.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_22.setObjectName("label_22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poker"))
        self.label.setText(_translate("MainWindow", "Flop"))
        self.label_2.setText(_translate("MainWindow", "Turn"))
        self.label_3.setText(_translate("MainWindow", "River"))
        self.card_5.setText(_translate("MainWindow", "Card 5"))
        self.card_4.setText(_translate("MainWindow", "Card 4"))
        self.card_2.setText(_translate("MainWindow", "Card 2"))
        self.card_3.setText(_translate("MainWindow", "Card 3"))
        self.card_1.setText(_translate("MainWindow", "Card 1"))
        self.label_4.setText(_translate("MainWindow", "Bank"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.pushButton_2.setText(_translate("MainWindow", "Game rules"))
        self.pushButton_3.setText(_translate("MainWindow", "Restart game"))
        self.label_6.setText(_translate("MainWindow", "Player 1"))
        self.pushButton_4.setText(_translate("MainWindow", "Check"))
        self.pushButton_5.setText(_translate("MainWindow", "Fold"))
        self.pushButton_6.setText(_translate("MainWindow", "Raise"))
        self.label_7.setText(_translate("MainWindow", "Players bet:"))
        self.label_8.setText(_translate("MainWindow", "Players bank:"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "1000"))
        self.label_12.setText(_translate("MainWindow", "1000"))
        self.label_10.setText(_translate("MainWindow", "Player 2"))
        self.label_13.setText(_translate("MainWindow", "Players bank:"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "Players bet:"))
        self.label_16.setText(_translate("MainWindow", "1000"))
        self.label_18.setText(_translate("MainWindow", "Players bank:"))
        self.label_19.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "Players bet:"))
        self.label_21.setText(_translate("MainWindow", "1000"))
        self.label_23.setText(_translate("MainWindow", "Players bank:"))
        self.label_24.setText(_translate("MainWindow", "0"))
        self.label_25.setText(_translate("MainWindow", "Players bet:"))
        self.pushButton_7.setText(_translate("MainWindow", "Raise"))
        self.pushButton_8.setText(_translate("MainWindow", "Check"))
        self.pushButton_9.setText(_translate("MainWindow", "Fold"))
        self.pushButton_10.setText(_translate("MainWindow", "Raise"))
        self.pushButton_11.setText(_translate("MainWindow", "Check"))
        self.pushButton_12.setText(_translate("MainWindow", "Fold"))
        self.pushButton_13.setText(_translate("MainWindow", "Raise"))
        self.pushButton_14.setText(_translate("MainWindow", "Check"))
        self.pushButton_15.setText(_translate("MainWindow", "Fold"))
        self.label_17.setText(_translate("MainWindow", "Player 3"))
        self.label_22.setText(_translate("MainWindow", "Player 4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
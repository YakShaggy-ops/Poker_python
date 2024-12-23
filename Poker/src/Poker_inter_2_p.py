# Form implementation generated from reading ui file 'Poker_inter.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

import time
from turtledemo.clock import setup

from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from classes import *
from output_functoins import *
#from main import restart



class Ui_MainWindow(QMainWindow):

    # def player_wins_2(self):
    #     self.Player_1_console.setText('You win round')
    #     self.Player_1_console.update()  # Обновление интерфейса

    def update_inf(self):
        self.update_bets()
        self.whose_turn()
        self.Bank_numb.setText(str(self.bank))


    def isbetsame_i(self):
        players = get_players()
        for i in range(len(players)):
            if players[i].n_bet != players[(i + 1) % len(players)].n_bet:
                return False
        return True

    def text_console(self, turn, text):
        #print('text_console')
        self.Player_1_console.clear()
        self.Player_2_console.clear()
        if turn == 0:
            self.Player_1_console.setText(text)
        elif turn == 1:
            self.Player_2_console.setText(text)

    # def push_last_bet_main(self):
    #     return last_bet

    def create_win_label(self, height=50):
        self.Player_1_console.setText('')
        self.Player_2_console.setText('')

        # label = QtWidgets.QLabel("You Win!", parent)
        # label.setStyleSheet("color: red; font-size: 24px;")  # Установка цвета и размера шрифта
        # label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Выравнивание по центру
        # label.setFixedHeight(height)  # Регулировка высоты QLabel

        # self.Bank_text = QtWidgets.QLabel(parent=self.centralwidget)
        # self.Bank_text.setGeometry(QtCore.QRect(490, 0, 231, 81))
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # font.setBold(True)
        # font.setWeight(75)
        # self.Bank_text.setFont(font)
        # self.Bank_text.setStyleSheet("background-color: rgb(181, 255, 175);")
        # self.Bank_text.setObjectName("Bank_text")

        # print('create_win_label')
        #return label
        pass

    def player_wins(self, player):
        players = get_players()
        turn = player.index(player)
        self.final_player(turn)

    def end_programm(self):
        self.bank = 0
        self.Bank_numb.clear()
        self.Bank_numb.setText(str(0))
        self.Bank_numb.repaint()
        players = get_players()
        #print('updated')
        time.sleep(10)
        for pla in players:
            pla.player_money = 1000
        pass
        # self.update_inf()
        # self.create_win_label()
        # time.sleep(3)
        # sys.exit(app.exec())


    def second_player_wins(self):
        turn = get_turn()
        players = get_players()
        self.final_player(turn)


    def final_player(self, turn):
        players = get_players()
        #print('final', turn)
        #self.text_console(turn, 'You win round!')
        if turn == 0:
            a = self.Player_1_bet_numb.text()
            b = self.Player_2_bet_numb.text()
            a, b = int(a), int(b)
            #print(a, b)
            new_p_bank = a + b + int(self.Player_2_bank_numb.text())
            #print(new_p_bank, a, b)
            self.Player_2_bank_numb.setText(str(new_p_bank))
            players[1].player_money = new_p_bank

            players[1].player_money = new_p_bank + self.bank
            #print(players[1].player_money, players[0].n_bet, players[1].n_bet)
            self.bank = 0
            self.Bank_numb.setText(str(0))
            self.Bank_numb.repaint()

            self.Player_1_bank_numb.setText(str(players[0].player_money))
            self.Player_1_bank_numb.repaint()

            self.Player_2_bank_numb.setText(str(players[1].player_money))
            self.Player_2_bank_numb.repaint()

            if players[0].n_bet + players[0].player_money == 0:
                self.Player_2_bank_numb.setText(str(players[1].player_money))
                self.Player_2_bank_numb.repaint()


                self.end_programm()

            self.restart_win()
        elif turn == 1:
            a = self.Player_1_bet_numb.text()
            b = self.Player_2_bet_numb.text()
            a, b = int(a), int(b)
            #print(a, b)
            new_p_bank = a + b + int(self.Player_1_bank_numb.text())
            #print(new_p_bank, a, b)
            self.Player_1_bank_numb.setText(str(new_p_bank))
            players[0].player_money = new_p_bank

            if players[1].n_bet + players[1].player_money == 0:
                self.Player_1_bank_numb.setText(str(players[0].player_money))
                self.Player_1_bank_numb.repaint()

                self.end_programm()

            players[0].player_money = new_p_bank + self.bank
            self.bank = 0
            self.Bank_numb.setText(str(0))
            self.Bank_numb.repaint()

            self.Player_1_bank_numb.setText(str(players[0].player_money))
            self.Player_1_bank_numb.repaint()

            self.Player_2_bank_numb.setText(str(players[1].player_money))
            self.Player_2_bank_numb.repaint()

            self.restart_win()

        #print(players[turn].player_name, 'wins')


    def update_bets(self):
        players = get_players()
        self.Player_1_bet_numb.setText(str(players[0].n_bet))
        self.Player_2_bet_numb.setText(str(players[1].n_bet))
        self.Player_1_bet_numb.repaint()
        self.Player_2_bet_numb.repaint()
        self.Player_1_bank_numb.setText(str(players[0].player_money))
        self.Player_2_bank_numb.setText(str(players[1].player_money))
        self.Player_1_bank_numb.repaint()
        self.Player_2_bank_numb.repaint()

    def whose_turn(self):
        turn = get_turn()
        players = get_players()
        self.text_console(turn, 'Your turn')

    def player_answer(self, ans, number, bet = '0', bet_o = '0'):
        # print(2)
        turn = get_turn()
        players = get_players()
        if number == turn + 1:
            if ans == 'c':
                #print(12)
                if number == 1:
                    bet_o = self.Player_1_bet_numb.text()
                elif number == 2:
                    bet_o = self.Player_2_bet_numb.text()
                main_player_answer('c', bet, bet_o)
                #self.player_bets_counter += 1
            if ans == 'f':
                self.second_player_wins()
            if ans == 'r':
                try:
                    bet = int(bet)
                    main_player_answer('r', bet, bet_o)
                except ValueError:
                    self.text_console(turn, 'Please enter a number')
                    self.player_bets_counter -= 1

            tim_len = len(players)
            self.player_bets_counter += 1
            #print(tim_len, self.player_bets_counter)
            if self.isbetsame_i() and self.player_bets_counter >= tim_len:
                self.bank += players[0].n_bet
                self.bank += players[1].n_bet
                self.Player_1_bet_numb.setText(str(0))
                self.Player_2_bet_numb.setText(str(0))
                self.Player_1_bet_numb.repaint()
                self.Player_2_bet_numb.repaint()
                for pla in players:
                    pla.n_bet = 0

                if self.game_pos == 0:
                    flop_i()
                    table = get_table_i()
                    self.pixmap = QPixmap(show_cards_way(table[0]))
                    self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
                    self.card_6.setPixmap(self.pixmap)
                    if self.pixmap.isNull():
                        print("Ошибка загрузки изображения для карты 0")

                    self.pixmap = QPixmap(show_cards_way(table[1]))
                    self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
                    self.card_7.setPixmap(self.pixmap)

                    self.pixmap = QPixmap(show_cards_way(table[2]))
                    self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
                    self.card_8.setPixmap(self.pixmap)

                    self.game_pos += 1
                    push_last_bet_i(0)
                    self.player_bets_counter = 0

                elif self.game_pos == 1:
                    turn_i()
                    table = get_table_i()
                    self.pixmap = QPixmap(show_cards_way(table[3]))
                    self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
                    self.card_9.setPixmap(self.pixmap)
                    push_last_bet_i(0)
                    self.player_bets_counter = 0
                    self.game_pos += 1

                elif self.game_pos == 2:
                    river_i()
                    table = get_table_i()
                    self.pixmap = QPixmap(show_cards_way(table[4]))
                    self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
                    self.card_10.setPixmap(self.pixmap)
                    push_last_bet_i(0)
                    self.player_bets_counter = 0
                    self.game_pos += 1

                elif self.game_pos == 3:
                    final_i()
                    pla = get_wins_player_i()
                    if len(pla) == 1:
                        #print('P_I', pla[0].player_name)
                        turn = players.index(pla[0])
                        players = get_players()
                        if turn == 1:
                            a = self.Player_1_bet_numb.text()
                            b = self.Player_2_bet_numb.text()
                            a, b = int(a), int(b)
                            new_p_bank = a + b + int(self.Player_2_bank_numb.text())
                            self.Player_2_bank_numb.setText(str(new_p_bank))
                            players[1].player_money = new_p_bank
                            players[1].player_money = new_p_bank + self.bank
                            self.bank = 0
                            self.Bank_numb.setText(str(0))
                            self.Bank_numb.repaint()

                            self.Player_1_bank_numb.setText(str(players[0].player_money))
                            self.Player_1_bank_numb.repaint()

                            self.Player_2_bank_numb.setText(str(players[1].player_money))
                            self.Player_2_bank_numb.repaint()

                            if players[0].n_bet + players[0].player_money == 0:
                                self.Player_2_bank_numb.setText(str(players[1].player_money))
                                self.Player_2_bank_numb.repaint()

                                self.end_programm()

                            self.restart_win()
                        elif turn == 0:
                            a = self.Player_1_bet_numb.text()
                            b = self.Player_2_bet_numb.text()
                            a, b = int(a), int(b)
                            new_p_bank = a + b + int(self.Player_2_bank_numb.text())
                            self.Player_1_bank_numb.setText(str(new_p_bank))
                            players[0].player_money = new_p_bank

                            players[0].player_money = new_p_bank + self.bank
                            self.bank = 0
                            self.Bank_numb.setText(str(0))
                            self.Bank_numb.repaint()

                            self.Player_1_bank_numb.setText(str(players[0].player_money))
                            self.Player_1_bank_numb.repaint()

                            self.Player_2_bank_numb.setText(str(players[1].player_money))
                            self.Player_2_bank_numb.repaint()

                            if players[1].n_bet + players[1].player_money == 0:
                                self.Player_1_bank_numb.setText(str(players[0].player_money))
                                self.Player_1_bank_numb.repaint()

                                self.end_programm()

                            self.restart_win()
                    else:
                        a = self.Player_1_bet_numb.text()
                        b = self.Player_2_bet_numb.text()
                        a, b = int(a), int(b)
                        # print(a, b)
                        new_p_bank = a + b + self.bank
                        p1 = new_p_bank // 2
                        p2 = new_p_bank - p1
                        pla[0].player_money += p1
                        pla[1].player_money += p2
                        self.bank = 0
                        self.Bank_numb.setText(str(0))

                        self.Player_1_bank_numb.setText(str(players[0].player_money))
                        self.Player_1_bank_numb.repaint()

                        self.Player_2_bank_numb.setText(str(players[1].player_money))
                        self.Player_2_bank_numb.repaint()

                        self.restart_win()

            self.update_inf()


    def restart_win(self, t=3):
        time.sleep(t)
        self.card_update()
        self.update_inf()
        self.player_bets_counter = 0
        self.game_pos = 0
        self.clean_table_cards()
        start_game()
        #MainWindow.show()

    def card_update(self):
        self.pixmap = QPixmap(show_cards_way(get_players()[0].player_deck[0]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_1_card_1.setPixmap(self.pixmap)

        self.pixmap = QPixmap(show_cards_way(get_players()[0].player_deck[1]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_1_card_2.setPixmap(self.pixmap)

        self.pixmap = QPixmap(show_cards_way(get_players()[1].player_deck[0]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_2_card_1.setPixmap(self.pixmap)

        self.pixmap = QPixmap(show_cards_way(get_players()[1].player_deck[1]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_2_card_2.setPixmap(self.pixmap)

    def card_update_not_time(self):
        self.pixmap = QPixmap(show_cards_way(get_players()[0].player_deck[0]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_1_card_1.setPixmap(self.pixmap)

        self.pixmap = QPixmap(show_cards_way(get_players()[0].player_deck[1]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_1_card_2.setPixmap(self.pixmap)

        self.pixmap = QPixmap(show_cards_way(get_players()[1].player_deck[0]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_2_card_1.setPixmap(self.pixmap)

        self.pixmap = QPixmap(show_cards_way(get_players()[1].player_deck[1]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_2_card_2.setPixmap(self.pixmap)


    def clean_table_cards(self):
        pass
        self.card_6.clear()
        self.card_7.clear()
        self.card_8.clear()
        self.card_9.clear()
        self.card_10.clear()



    def raise_command(self, number):
        # print(1)
        # global last_bet
        turn = get_turn()
        players = get_players()
        # command = self.line_edit.text()
        l = ''
        l_2 = ''
        if number == 1:
            l = self.Player_1_r_lineEdit.text()
            self.Player_1_r_lineEdit.clear()
            l_2 = self.Player_1_bet_numb.text()
        elif number == 2:
            l = self.Player_2_r_lineEdit.text()
            self.Player_2_r_lineEdit.clear()
            l_2 = self.Player_1_bet_numb.text()
        self.player_answer('r', number, str(l), str(l_2))

        # self.Player_1_fold_button.clear()
        # last_bet = get_last_bet()
        # m_bet = get_m_bet()
        # while True:
        #     try:
        #         command = int(command)
        #         if command < last_bet:
        #             self.text_console(turn, 'Enter a raise bet')
        #             continue
        #         break
        #     except ValueError:
        #         self.text_console(turn, 'Enter a numder')
        # for pla in players:
        #     if pla.player_money < command:
        #         command = pla.player_money
        # last_bet = command - (command % m_bet)
        # players[turn].n_bet = last_bet

    def restart_button(self):
        players = get_players()
        #self.Player_1_bet_numb
        players[0].player_money = 1000
        players[1].player_money = 1000
        self.Player_1_bank_numb.setText(str(1000))
        self.Player_2_bank_numb.setText(str(1000))
        self.Player_1_bank_numb.repaint()
        self.Player_2_bank_numb.repaint()
        players[0].n_bet, players[1].n_bet = 0, 0
        self.bank = 0
        self.Bank_numb.setText(str(0))
        self.Bank_numb.repaint()
        self.clean_table_cards()
        zero_last_bets()
        self.restart_win(t=0)


        # time.sleep(1)
        # #print(players[1].player_money)
        # MainWindow = QtWidgets.QMainWindow()
        # start_game()
        # ui = Ui_MainWindow()
        # ui.setupUi(MainWindow)
        # self.card_update()
        # ui.update_inf()
        # self.player_bets_counter = 0
        # self.game_pos = 0
        # self.clean_table_cards()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.Player_1_pos = ''
        self.Player_2_pos = ''

        self.player_bets_counter = 0
        self.bank = 0
        self.game_pos = 0
        self.time_sleep = 5

        MainWindow.resize(688, 500)
        self.new_width, self.new_height = 80, 120
        MainWindow.setStyleSheet("background-color: rgb(186, 231, 226);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Flop_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Flop_text.setGeometry(QtCore.QRect(0, 40, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Flop_text.setFont(font)
        self.Flop_text.setStyleSheet("background-color: rgb(255, 183, 176);")
        self.Flop_text.setObjectName("Flop_text")
        self.Turn_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Turn_text.setGeometry(QtCore.QRect(290, 40, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Turn_text.setFont(font)
        self.Turn_text.setStyleSheet("background-color: rgb(255, 183, 176);")
        self.Turn_text.setObjectName("Turn_text")
        self.River_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.River_text.setGeometry(QtCore.QRect(400, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.River_text.setFont(font)
        self.River_text.setStyleSheet("background-color: rgb(255, 183, 176);")
        self.River_text.setObjectName("River_text")
        self.card_5_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_5_text.setGeometry(QtCore.QRect(390, 110, 101, 31))
        self.card_5_text.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                       "color: rgb(255, 255, 255);")
        self.card_5_text.setIndent(-1)
        self.card_5_text.setObjectName("card_5_text")
        self.card_4_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_4_text.setGeometry(QtCore.QRect(290, 110, 101, 31))
        self.card_4_text.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                       "color: rgb(255, 255, 255);")
        self.card_4_text.setIndent(-1)
        self.card_4_text.setObjectName("card_4_text")
        self.card_2_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_2_text.setGeometry(QtCore.QRect(100, 110, 101, 31))
        self.card_2_text.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                       "color: rgb(255, 255, 255);")
        self.card_2_text.setIndent(-1)
        self.card_2_text.setObjectName("card_2_text")
        self.card_3_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_3_text.setGeometry(QtCore.QRect(200, 110, 91, 31))
        self.card_3_text.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                       "color: rgb(255, 255, 255);")
        self.card_3_text.setIndent(-1)
        self.card_3_text.setObjectName("card_3_text")
        self.card_1_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_1_text.setGeometry(QtCore.QRect(0, 110, 101, 31))
        self.card_1_text.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                       "color: rgb(255, 255, 255);")
        self.card_1_text.setIndent(-1)
        self.card_1_text.setObjectName("card_1_text")
        self.Bank_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Bank_text.setGeometry(QtCore.QRect(490, 0, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Bank_text.setFont(font)
        self.Bank_text.setStyleSheet("background-color: rgb(181, 255, 175);")
        self.Bank_text.setObjectName("Bank_text")
        self.Bank_numb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Bank_numb.setGeometry(QtCore.QRect(490, 80, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Bank_numb.setFont(font)
        self.Bank_numb.setStyleSheet("background-color: rgb(181, 255, 175);")
        self.Bank_numb.setObjectName("Bank_numb")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.restart_button)

        self.card_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_6.setGeometry(QtCore.QRect(0, 150, self.new_width, self.new_height))
        # self.card_6.setPixmap(self.pixmap)

        self.card_6.setStyleSheet("background-color: rgb(181, 181, 181);""color: rgb(255, 255, 255);")
        self.card_6.setText("")
        self.card_6.setIndent(-1)

        self.card_6.setObjectName("card_6")
        self.card_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_7.setGeometry(QtCore.QRect(100, 150, self.new_width, self.new_height))
        self.card_7.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                  "color: rgb(255, 255, 255);")
        self.card_7.setText("")
        self.card_7.setIndent(-1)
        self.card_7.setObjectName("card_7")
        self.card_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_8.setGeometry(QtCore.QRect(200, 150, self.new_width, self.new_height))
        self.card_8.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                  "color: rgb(255, 255, 255);")
        self.card_8.setText("")
        self.card_8.setIndent(-1)
        self.card_8.setObjectName("card_8")
        self.card_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_9.setGeometry(QtCore.QRect(300, 150, self.new_width, self.new_height))
        self.card_9.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                  "color: rgb(255, 255, 255);")
        self.card_9.setText("")
        self.card_9.setIndent(-1)
        self.card_9.setObjectName("card_9")
        self.card_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_10.setGeometry(QtCore.QRect(400, 150, self.new_width, self.new_height))
        self.card_10.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                   "color: rgb(255, 255, 255);")
        self.card_10.setText("")
        self.card_10.setIndent(-1)
        self.card_10.setObjectName("card_10")
        self.Player_1_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_text.setGeometry(QtCore.QRect(0, 281, 91, 31))
        self.Player_1_text.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Player_1_text.setObjectName("Player_1_text")

        self.Player_1_card_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_card_1.setGeometry(QtCore.QRect(0, 331, self.new_width, self.new_height))
        self.Player_1_card_1.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                           "color: rgb(255, 255, 255);")
        self.pixmap = QPixmap(show_cards_way(get_players()[0].player_deck[0]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_1_card_1.setPixmap(self.pixmap)
        self.Player_1_card_1.setText("")
        self.Player_1_card_1.setIndent(-1)
        self.Player_1_card_1.setObjectName("Player_1_card_1")

        self.Player_1_card_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_card_2.setGeometry(QtCore.QRect(100, 331, self.new_width, self.new_height))
        self.Player_1_card_2.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                           "color: rgb(255, 255, 255);")
        self.pixmap = QPixmap(show_cards_way(get_players()[0].player_deck[1]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_1_card_2.setPixmap(self.pixmap)
        self.Player_1_card_2.setText("")
        self.Player_1_card_2.setIndent(-1)
        self.Player_1_card_2.setObjectName("Player_1_card_2")

        self.Player_1_check_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Player_1_check_button.setGeometry(QtCore.QRect(200, 331, 91, 23))
        self.Player_1_check_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Player_1_check_button.setObjectName("Player_1_check_button")

        self.Player_1_check_button.clicked.connect(lambda: self.player_answer('c', 1))

        self.Player_1_fold_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Player_1_fold_button.setGeometry(QtCore.QRect(200, 361, 91, 23))
        self.Player_1_fold_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Player_1_fold_button.setObjectName("Player_1_fold_button")

        self.Player_1_fold_button.clicked.connect(lambda: self.player_answer('f', 1))


        self.Player_1_r_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Player_1_r_lineEdit.setGeometry(QtCore.QRect(200, 420, 91, 31))
        self.Player_1_r_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Player_1_r_lineEdit.setObjectName("Player_1_r_lineEdit")

        self.Player_1_r_lineEdit.returnPressed.connect(lambda: self.raise_command(1))

        self.Player_1_bet_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_bet_text.setGeometry(QtCore.QRect(100, 281, 61, 16))
        self.Player_1_bet_text.setObjectName("Player_1_bet_text")
        self.Player_1_bank_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_bank_text.setGeometry(QtCore.QRect(100, 301, 71, 16))
        self.Player_1_bank_text.setObjectName("Players_1_bank_text")
        self.Player_1_bet_numb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_bet_numb.setGeometry(QtCore.QRect(170, 281, 51, 16))
        self.Player_1_bet_numb.setObjectName("Player_1_bet_numb")
        self.Player_1_bank_numb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_bank_numb.setGeometry(QtCore.QRect(170, 301, 51, 16))
        self.Player_1_bank_numb.setObjectName("Players_1_bank_numb")
        self.Player_2_bank_numb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_bank_numb.setGeometry(QtCore.QRect(470, 300, 51, 16))
        self.Player_2_bank_numb.setObjectName("Players_2_bank_numb")
        self.Player_2_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_text.setGeometry(QtCore.QRect(300, 280, 91, 31))
        self.Player_2_text.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Player_2_text.setObjectName("Player_2_text")
        self.Player_2_bank_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_bank_text.setGeometry(QtCore.QRect(400, 300, 71, 16))
        self.Player_2_bank_text.setObjectName("Players_2_bank_text")

        self.raise_1_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.raise_1_text.setGeometry(QtCore.QRect(530, 400, 80, 20))
        self.raise_1_text.setObjectName("Players_2_bank_text")

        self.raise_2_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.raise_2_text.setGeometry(QtCore.QRect(230, 400, 80, 20))
        self.raise_2_text.setObjectName("Players_2_bank_text")

        self.Player_2_card_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_card_1.setGeometry(QtCore.QRect(300, 330, self.new_width, self.new_height))
        self.Player_2_card_1.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                           "color: rgb(255, 255, 255);")
        self.pixmap = QPixmap(show_cards_way(get_players()[1].player_deck[0]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_2_card_1.setPixmap(self.pixmap)
        self.Player_2_card_1.setText("")
        self.Player_2_card_1.setIndent(-1)
        self.Player_2_card_1.setObjectName("Player_2_card_1")

        self.Player_2_card_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_card_2.setGeometry(QtCore.QRect(400, 330, self.new_width, self.new_height))
        self.Player_2_card_2.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                           "color: rgb(255, 255, 255);")
        self.pixmap = QPixmap(show_cards_way(get_players()[1].player_deck[1]))
        self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
        self.Player_2_card_2.setPixmap(self.pixmap)
        self.Player_2_card_2.setText("")
        self.Player_2_card_2.setIndent(-1)
        self.Player_2_card_2.setObjectName("Player_2_card_2")

        self.Player_2_bet_numb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_bet_numb.setGeometry(QtCore.QRect(470, 280, 51, 16))
        self.Player_2_bet_numb.setObjectName("Player_2_bet_numb")
        self.Player_2_bet_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_bet_text.setGeometry(QtCore.QRect(400, 280, 61, 16))
        self.Player_2_bet_text.setObjectName("Player_2_bet_text")


        self.Player_2_r_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Player_2_r_lineEdit.setGeometry(QtCore.QRect(500, 419, 91, 31))
        self.Player_2_r_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Player_2_r_lineEdit.setObjectName("Player_2_r_lineEdit")

        self.Player_2_r_lineEdit.returnPressed.connect(lambda: self.raise_command(2))

        self.Player_2_check_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Player_2_check_button.setGeometry(QtCore.QRect(500, 330, 91, 23))
        self.Player_2_check_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Player_2_check_button.setObjectName("Player_2_check_button")
        self.Player_2_check_button.clicked.connect(lambda: self.player_answer('c', 2))

        self.Player_2_fold_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Player_2_fold_button.setGeometry(QtCore.QRect(500, 360, 91, 23))
        self.Player_2_fold_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Player_2_fold_button.setObjectName("Player_2_fold_button")
        self.Player_2_fold_button.clicked.connect(lambda: self.player_answer('f', 2))
        _translate = QtCore.QCoreApplication.translate



        self.card_5_text_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_5_text_2.setGeometry(QtCore.QRect(500, 150, 110, 31))
        self.card_5_text_2.setStyleSheet("")
        self.card_5_text_2.setIndent(-1)
        self.card_5_text_2.setObjectName("card_5_text_2")
        self.card_5_text_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.card_5_text_3.setGeometry(QtCore.QRect(500, 180, 110, 31))
        self.card_5_text_3.setStyleSheet("")
        self.card_5_text_3.setIndent(-1)
        self.card_5_text_3.setObjectName("card_5_text_3")
        self.Player_1_console = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_1_console.setGeometry(QtCore.QRect(220, 300, 71, 20))
        self.Player_1_console.setStyleSheet("color: rgb(255, 0, 0);")
        self.Player_1_console.setObjectName("Player_1_console")
        self.Player_2_console = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player_2_console.setGeometry(QtCore.QRect(520, 300, 71, 20))
        self.Player_2_console.setStyleSheet("color: rgb(255, 0, 0);")
        self.Player_2_console.setObjectName("Player_2_console")

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
        self.Flop_text.setText(_translate("MainWindow", "<b>Flop</b>"))
        self.Turn_text.setText(_translate("MainWindow", "<b>Turn</b>"))
        self.River_text.setText(_translate("MainWindow", "<b>River</b>"))
        self.card_5_text.setText(_translate("MainWindow", "Card 5"))
        self.card_4_text.setText(_translate("MainWindow", "Card 4"))
        self.card_2_text.setText(_translate("MainWindow", "Card 2"))
        self.card_3_text.setText(_translate("MainWindow", "Card 3"))
        self.card_1_text.setText(_translate("MainWindow", "Card 1"))
        self.Bank_text.setText(_translate("MainWindow", "<b>Bank</b>"))
        #self.Bank_text.setStyleSheet("padding: 5px;")
        self.Bank_numb.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Restart game"))
        self.Player_1_text.setText(_translate("MainWindow", "Player 1"))
        self.Player_1_check_button.setText(_translate("MainWindow", "Check"))
        self.Player_1_fold_button.setText(_translate("MainWindow", "Fold"))
        # self.Player_1_raise_button.setText(_translate("MainWindow", "Raise"))
        self.Player_1_bet_text.setText(_translate("MainWindow", "Players bet:"))
        self.Player_1_bank_text.setText(_translate("MainWindow", "Players bank:"))
        self.Player_1_bet_numb.setText(_translate("MainWindow", "0"))
        self.Player_1_bank_numb.setText(_translate("MainWindow", "1000"))
        self.Player_2_bank_numb.setText(_translate("MainWindow", "1000"))
        self.Player_2_text.setText(_translate("MainWindow", "Player 2"))
        self.Player_2_bank_text.setText(_translate("MainWindow", "Players bank:"))
        self.raise_1_text.setText(_translate("MainWindow", "Raise:"))
        self.raise_2_text.setText(_translate("MainWindow", "Raise:"))


        self.Player_2_bet_numb.setText(_translate("MainWindow", "0"))
        self.Player_2_bet_text.setText(_translate("MainWindow", "Players bet:"))

        # self.Player_2_raise_button.setText(_translate("MainWindow", "Raise"))
        self.Player_2_check_button.setText(_translate("MainWindow", "Check"))
        self.Player_2_fold_button.setText(_translate("MainWindow", "Fold"))
        # self.Player_3_raise_button.setText(_translate("MainWindow", "Raise"))
        self.card_5_text_2.setText(_translate("MainWindow", "Minimal bet: 10"))
        self.card_5_text_3.setText(_translate("MainWindow", "Minimal bet step: 5"))
        self.Player_1_console.setText(_translate("MainWindow", "Er"))
        self.Player_2_console.setText(_translate("MainWindow", "Er"))


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#
#     MainWindow = QtWidgets.QMainWindow()
#     start_game()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#
#     ui.update_inf()
#
#     MainWindow.show()
#
#     # main_game()
#     sys.exit(app.exec())

def inter_2():
    MainWindow = QtWidgets.QMainWindow()
    start_game()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_inf()

    MainWindow.show()


def inter():
    import sys
    #global app
    app = QtWidgets.QApplication(sys.argv)
    # inter_2()
    MainWindow = QtWidgets.QMainWindow()
    start_game()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_inf()
    MainWindow.show()
    sys.exit(app.exec())


    # main_game()


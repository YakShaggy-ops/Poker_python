import random


class Player: #Игрок
    def __init__(self, player_name, player_num, player_money = 1000, n_bet = 0, player_combination = ''):
        self.player_name = player_name
        self.player_num = player_num
        self.player_money = player_money
        self.n_bet = n_bet
        self.main_deck = []
        self.player_combination = player_combination
        self.player_deck = []

    def get_deck(self, card1, card2):
        self.player_deck = [card1, card2]

    def show_deck(self):
        for el in self.player_deck:
            el.show()


class Card: #Описывает одну карту как объект
    def __init__ (self,suit,value):
      self.suit=suit
      self.value=value
    def show(self):
        print(self.value, self.suit)

def gen(): #Генерирует колоду карт
    global deck
    for val in values:
        for su in suits:
            deck.append(Card(su,val)) #Добавляем в колоду по карте


def mix_deck(): #Тасуем карты
    random.shuffle(deck)

def card_draw():
    global deck
    global players
    for pla in players:
        pla.get_deck(deck[0],deck[1])
        deck.pop(0)
        deck.pop(0)
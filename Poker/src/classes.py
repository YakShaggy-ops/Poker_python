class Player: #Игрок
    def __init__(self, player_name, player_money = 1000, n_bet = 0, player_combination_name = 'top_cards'):
        self.player_name = player_name
        self.player_money = player_money
        self.n_bet = n_bet
        self.player_combination_name = player_combination_name
        self.player_combination = []
        self.player_deck = []
        self.player_answer = ''
        self.player_bank_win = 0
        self.all_in = False

    def get_deck(self, card1, card2):
        self.player_deck = [card1, card2]

    def show_deck(self):
        pass
        # for el in self.player_deck:
        #     el.show()

class Card: #Описывает одну карту как объект
    def __init__ (self,suit,value):
      self.suit=suit
      self.value=value
    def show(self):
        pass
        # print(self.value, self.suit)
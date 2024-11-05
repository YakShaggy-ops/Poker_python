import random

class Player: #Игрок
    def __init__(self, player_name, player_num, player_money = 1000, n_bet = 0):
        self.player_name = player_name
        self.player_num = player_num
        self.player_money = player_money
        self.n_bet = n_bet

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

def blind():
    print('blind')
    global players
    global next_turn
    global base_bet
    global last_bet
    players[next_turn].n_bet = base_bet // 2
    next_player()
    players[next_turn].n_bet = base_bet
    last_bet = base_bet
    next_player()

def preflop():
    global last_bet
    print('preflop')
    for pla in players:
        pla.show_deck()
        print('')
    bets_round()
    print('')
    for pla in players:
        print(pla.player_name)
        print(pla.n_bet)


def flop(): #Выдаём 3 карты и делаем круг ставок
    global deck, last_bet, prelast_bet
    global table
    global players
    global next_turn
    for i in range (3):
        table.append(deck[0])
        deck.pop(0)
    print('')
    for el in table:
        el.show()
    print('')
    zeroing_bets()
    # print('')
    for pla in players:
        print(pla.player_name)
        print(pla.n_bet)
    print('')
    bets_round()

def turn(): #Выдаём 1 карту
    global deck, table
    print('')
    print('turn')
    print('')
    table.append(deck[0])
    deck.pop(0)
    for el in table:
        el.show()
    print('')
    zeroing_bets()
    for pla in players:
        print(pla.player_name)
        print(pla.n_bet)
    print('')
    bets_round()

def river(): #Выдаём 1 карту
    global deck, table
    print('')
    print('river')
    print('')
    table.append(deck[0])
    deck.pop(0)
    for el in table:
        el.show()
    print('')
    zeroing_bets()
    for pla in players:
        print(pla.player_name)
        print(pla.n_bet)
    print('')
    bets_round()

def bets_round():
    tim_len = len(players)
    blind_counter = 0
    while True:
        blind_counter += 1
        player_bet()
        del_players()
        next_player()
        # print(players[next_turn].n_bet, last_bet, prelast_bet)
        if isbetsame() and blind_counter >= tim_len:
            break

def isbetsame():
    global players
    for i in range (len(players)):
        if players[i].n_bet != players[(i + 1) % len(players)].n_bet:
            return False
    return True

def next_player():
    global next_turn
    global players
    next_turn = next_turn + 1
    next_turn = next_turn % len(players)

def out_cards(n):
    global deck
    global out
    for i in range(n):
        out.append(deck[0])
        deck.pop(0)

def player_bet():
    global next_turn, players, last_bet, prelast_bet
    print(players[next_turn].player_name, ':', sep='')
    ans = input('your bet (f, c, r): ')
    if ans == 'f':
        check_player()
    elif ans == 'c':
        prelast_bet = last_bet
        players[next_turn].n_bet = last_bet
    elif ans == 'r':
        prelast_bet = last_bet
        last_bet = int(input('your bet: '))
        players[next_turn].n_bet = last_bet
    else:
        print('invalid input')

def check_player():
    global players
    global next_turn
    global check_players
    check_players.append(players[next_turn])

def zeroing_bets():
    global players, last_bet, prelast_bet, bank
    for pla in players:
        bank += pla.n_bet
        pla.n_bet = 0
        # print(pla.player_name, ': ', pla.n_bet, sep='')
    last_bet = 0

def del_players():
    global players
    global next_turn
    global check_players
    number_of_players = len(players)
    for pla in players:
        if pla in check_players:
            players.remove(pla)
            break
    if number_of_players != len(players):
        if next_turn == 0:
            next_turn = len(players) - 1
        else:
            next_turn = next_turn - 1

# def pop_player():
#     global players
#     global next_turn
#     players.pop(next_turn)
#     next_turn = next_turn % len(players)

def players_input(): #Набор игроков
    global players
    for i in range (int(input('how many players?: '))):
        players.append(Player(input('player_name: '), i))

def show_desk(): #Показать колоду
    global deck
    for el in deck:
        el.show()


player_1 = Player('Player 1', 0)
player_2 = Player('Player 2', 1)
player_3 = Player('Player 3', 2)
player_4 = Player('Player 4', 3)

#Переменные
prelast_bet = 0
base_bet = 10
m_bet = 5
last_bet = 0
next_turn = 0
players = [player_1, player_2, player_3, player_4]
check_players = []
bank = 0
out = [] #Сброс
table = [] #Стол
deck=[] #Наша колода
values=['2','3','4','5','6','7','8','9','10','J','Q','K','A'] #Задаем масти и достонство карт
suits=['Буби','Червы','Пики','Крести']

#Ход игры
def main_game():
    gen()
    mix_deck()
    card_draw()
    out_cards(1)
    blind()
    preflop()
    flop()
    out_cards(1)
    turn()
    out_cards(1)
    river()



main_game()
# for pla in players:
#     print(pla.player_name)
#     print(pla.n_bet)








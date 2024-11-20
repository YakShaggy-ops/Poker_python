player_1 = Player('Player 1', 0)
player_2 = Player('Player 2', 1)
player_3 = Player('Player 3', 2)
player_4 = Player('Player 4', 3)

#Переменные
prelast_bet = 0
poker_combinations = ['hight_cards', 'pair', 'two_pairs', 'three_cards', 'straight',
                'flush', 'full_house', 'four_cards', 'straight_flush', 'royal_flush']
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
    global deck, table, player_1, player_2, player_3, player_4
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
    table = [Card('Буби', 'K'), Card('Буби', 'K'), Card('Буби', 'K'), Card('Буби', '7'), Card('Буби', '8')]
    final()
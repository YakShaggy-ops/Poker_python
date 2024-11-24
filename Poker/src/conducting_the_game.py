
#from src.main import players

poker_combinations = ['top_cards', 'pair', 'two_pairs', 'three_cards', 'straight',
                'flush', 'full_house', 'four_cards', 'straight_flush', 'royal_flush']
values=['2','3','4','5','6','7','8','9','10','J','Q','K','A'] #Задаем масти и достонство карт
suits=['Буби','Червы','Пики','Крести']
deck = []


def gen_d(): #Генерирует колоду карт
    global deck
    for val in values:
        for su in suits:
            deck.append(Card(su,val))
        #return deck

 #Добавляем в колоду по карте

def mix_deck(): #Тасуем карты
    random.shuffle(deck)


def card_draw():
    global deck
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
    global last_bet, players
    # for pla in players:
    #     pla.player_combination_name = ''
    #     pla.player_combination = []
    print('preflop')
    for pla in players:
        pla.show_deck()
        print('')
    bets_round()
    print('')
    # for pla in players:
    #     print(pla.player_name)
    #     print(pla.n_bet)


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
    # print('')
    for pla in players:
        print(pla.player_name)
        print(pla.n_bet)
    zeroing_bets()
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
    for pla in players:
        print(pla.player_name)
        print(pla.n_bet)
    zeroing_bets()
    print('')
    bets_round()

def river(): #Выдаём 1 карту
    global deck, table, bank
    print('')
    print('river')
    print('')
    table.append(deck[0])
    deck.pop(0)
    for el in table:
        el.show()
    print('')

    for pla in players:
        print(pla.player_name)
        print(pla.n_bet)
    zeroing_bets()
    print('')
    bets_round()

def final():
    global table

    for pla in players:
        print()
        cards = table.copy()
        for el in pla.player_deck:
            cards.append(el)
        best_card_combination(pla.player_deck, pla)
        print(pla.player_combination_name)
        print(pla.player_combination)
        print('cards:')
        for el in cards:
            el.show()
    compare_cards()
    print()
    print('bank:', bank)


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
            print()
            print('bank:', bank)
            break

def isbetsame():
    global players
    for i in range (len(players)):
        if players[i].n_bet != players[(i + 1) % len(players)].n_bet:
            return False
    return True

def next_player():
    global next_turn, players
    next_turn = next_turn + 1
    next_turn = next_turn % len(players)

def out_cards(n):
    global deck
    global out
    for i in range(n):
        out.append(deck[0])
        deck.pop(0)

def player_bet():
    global next_turn, players, last_bet, prelast_bet, m_bet
    print(players[next_turn].player_name, ':', sep='')
    ans = input('your bet (f, c, r): ')
    if ans == 'f':
        check_player()
    elif ans == 'c':
        prelast_bet = last_bet
        players[next_turn].n_bet = last_bet
    elif ans == 'r':
        prelast_bet = last_bet
        while True:
            try:
                try_last_bet = int(input('your bet: '))
                if try_last_bet < last_bet:
                    print('your bet is less than last_bet')
                    continue
                break
            except ValueError:
                print('please enter a number')
        last_bet = try_last_bet - (try_last_bet % m_bet)
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

def best_card_combination(player_cards, player):
    global table, values, suits
    cards = table.copy()
    for el in player_cards:
        cards.append(el)
    top_five_cards = top_five_cards_func(cards)
    player.player_combination = top_five_cards
    player.player_combination_name = 'top_cards'
    if pair(player_cards)[0]:
        player.player_combination = pair(player_cards)[1]
        player.player_combination_name = 'pair'
    if two_pairs(player_cards)[0]:
        player.player_combination = two_pairs(player_cards)[1]
        player.player_combination_name = 'two_pairs'
    if three_cards(player_cards)[0]:
        player.player_combination = three_cards(player_cards)[1]
        player.player_combination_name = 'three_cards'
    if has_straight(player_cards)[0]:
        player.player_combination = has_straight(player_cards)[1]
        player.player_combination_name = 'straight'
    if flush(player_cards)[0]:
        player.player_combination = flush(player_cards)[1]
        player.player_combination_name = 'flush'
    if full_house(player_cards)[0]:
        player.player_combination = full_house(player_cards)[1]
        player.player_combination_name = 'full_house'
    if four_cards(player_cards)[0]:
        player.player_combination = four_cards(player_cards)[1]
        player.player_combination_name = 'four_cards'
    if straight_flush(player_cards)[0]:
        player.player_combination = straight_flush(player_cards)[1]
        player.player_combination_name = 'straight_flush'
    if royal_flush(player_cards)[0]:
        player.player_combination = royal_flush(player_cards)[1]
        player.player_combination_name = 'royal_flush'

def compare_cards():
    global players
    player_win = []
    player_sort = players.copy()
    player_sort = sorted(player_sort, key=lambda comb: poker_combinations.index(comb.player_combination_name), reverse=True)
    print([pla.player_combination_name for pla in player_sort])
    for el in player_sort:
        if el.player_combination_name == player_sort[0].player_combination_name:
            player_win.append(el)
    print([pla.player_combination_name for pla in player_win])
    wins_combination_players = [player_win[0]]
    for i in range(1, len(player_win)):
        for q in range(len(player_win[0].player_combination)):
            if wins_combination_players[0] == player_win[i]:
                continue
            p_1 = values.index(wins_combination_players[0].player_combination[q])
            p_2 = values.index(player_win[i].player_combination[q])
            #print(wins_combination_players[0].player_name)
            #print(player_win[i].player_name)
            #print(p_1, p_2)
            if p_1 < p_2:
                wins_combination_players[0] = player_win[i]
            elif p_1 == p_2:
                if q == len(player_win[0].player_combination) - 1:
                    wins_combination_players.append(player_win[i])
    wins_combination = wins_combination_players.copy()
    for i in range(1, len(wins_combination_players)):
        if wins_combination_players[0].player_combination != wins_combination_players[i].player_combination:
            wins_combination.remove(wins_combination_players[i])
    #print(wins_combination_players[0].player_name)
    print()
    for pla in wins_combination:
        print(pla.player_name)


def main_game():
    gen_d()
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
    #table = [Card('Буби', '9'), Card('Буби', 'K'), Card('Буби', 'Q'), Card('Буби', 'J'), Card('Буби', '10')]
    #table = [Card('Буби', '8'), Card('Крести', '8'), Card('Буби', '8'), Card('Крести', '8'), Card('Буби', '5')]
    #table = [Card('Буби', 'K'), Card('Буби', 'A'), Card('Буби', '2'), Card('Буби', '3'), Card('Буби', '4')]
    final()
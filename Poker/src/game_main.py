import random
from output_functoins import *
from classes import *
#from Poker_inter import *
from Poker_inter_2_p import *


def ret_players(): return players, next_turn

def last_bet_main(): return last_bet

def m_bet_main(): return m_bet

def get_table():
    #print(table[0].value, 'value')
    return table

def push_last_bet(a):
    global last_bet
    last_bet = a

def gen_d(): #Генерирует колоду карт
    global deck
    deck = []
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
    #print('blind')
    global players
    global next_turn
    global base_bet
    global last_bet
    players[next_turn].n_bet = base_bet // 2
    players[next_turn].player_money -= players[next_turn].n_bet
    #print(players[next_turn].n_bet)
    next_player()
    players[next_turn].n_bet = base_bet
    players[next_turn].player_money -= players[next_turn].n_bet
    last_bet = base_bet
    #print(players[next_turn].n_bet)
    next_player()

def preflop():
    global last_bet, players
    # for pla in players:
    #     pla.player_combination_name = ''
    #     pla.player_combination = []
    #print('preflop')
    # for pla in players:
    #     pla.show_deck()
        #print('')
    #bets_round()
    #print('')
    # for pla in players:
    #     print(pla.player_name)
    #     print(pla.n_bet)


def flop(): #Выдаём 3 карты и делаем круг ставок
    global deck, last_bet, prelast_bet
    global table
    global players
    global next_turn
    #print('flop')
    table = []
    for i in range (3):
        table.append(deck[0])
        deck.pop(0)

    #print('')
    #show_table_cards(table)
    # print('')
    #for pla in players:
        #show_player_cards(pla)
    #zeroing_bets()
    #print('')
    #bets_round()

def turn(): #Выдаём 1 карту
    global deck, table
    #print('')
    #print('turn')
    #print('')
    table.append(deck[0])
    deck.pop(0)
    #show_table_cards(table)
    # for pla in players:
    #     show_player_cards(pla)
    #zeroing_bets()
    #print('')
    #bets_round()

def river(): #Выдаём 1 карту
    global deck, table, bank
    table.append(deck[0])
    deck.pop(0)

def final():
    global table

    for pla in players:
        #print('final')
        cards = table.copy()
        for el in pla.player_deck:
            cards.append(el)
        best_card_combination(pla.player_deck, pla)
        #print(pla.player_combination_name)
        #print(pla.player_combination)
        #print('cards:')
        for el in cards:
            el.show()
    compare_cards()
    # print()
    # print('bank:', bank)

def zer_last_bet_2():
    last_bet = 0
    pre_last_bet = 0

def bets_round():
    tim_len = len(players)
    blind_counter = 0
    while True:
        blind_counter += 1
        #player_bet()
        del_players()
        next_player()
        #print(players[next_turn].n_bet, last_bet, prelast_bet)
        if isbetsame() and blind_counter >= tim_len:
            # print()
            # print('bank:', bank)
            break

def next_player_round():
    global blind_counter, last_bet
    tim_len = len(players)
    blind_counter += 1
    next_player()
    #print(players[next_turn].n_bet, last_bet, prelast_bet)
    if isbetsame() and blind_counter >= tim_len:
        last_bet = 0

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

def player_bet(ans, bet, bet_o):
    global next_turn, players, last_bet, prelast_bet, m_bet
    #print(players[next_turn].player_name, ':', sep='')
    #ans = input('your bet (f, c, r): ')
    if ans == 'f':
        fold_player()
        players[next_turn].player_answer = 'f'
        #ui.second_player_wins()
        next_player_round()
    elif ans == 'c':
        prelast_bet = last_bet + int(bet_o)
        players[next_turn].n_bet = last_bet
        players[next_turn].player_money -= last_bet - int(bet_o)
        players[next_turn].player_answer = 'c'
        next_player_round()
    elif ans == 'r':
        prelast_bet = last_bet
        while True:
            try:
                try_last_bet = int(bet) + int(bet_o)
                if try_last_bet <= last_bet:
                    pass
                else:
                    if try_last_bet > (players[0].n_bet + players[0].player_money) or try_last_bet > (players[1].n_bet + players[1].player_money):
                        try_last_bet = min(players[0].n_bet + players[0].player_money, players[1].n_bet + players[1].player_money)# + bet
                    #next_player()
                    players[next_turn].player_answer = 'r'
                    last_bet = try_last_bet - (try_last_bet % m_bet)
                    players[next_turn].n_bet = last_bet
                    players[next_turn].player_money -= last_bet - int(bet_o)
                    next_player_round()
                break
            except ValueError:
                break
    else:
        print('invalid input')


def fold_player():
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

def top_five_cards_func(cards):
    global deck, values
    top_five_cards = sorted(card.value for card in cards)#[:5]
    top_five_cards.reverse()
    top_five_cards = sorted(top_five_cards, key=lambda card: values.index(card), reverse=True)[:5]
    return top_five_cards

def has_straight(player_cards, five_cards_bool = True):
    global table, values
    if five_cards_bool:
        cards = table.copy()
        for el in player_cards:
            cards.append(el)
        set_card_values = [card.value for card in cards]
        cards = sorted(cards, key=lambda card: values.index(card.value), reverse=True)
    else:
        cards = player_cards.copy()
        set_card_values = player_cards.copy()
    # Получаем уникальные значения карт и сортируем их
    unique_values = sorted(set(set_card_values))

    #print(1, [card.value for card in cards])
    index_values = []
    for s_card in unique_values:
        index_values.append(values.index(s_card))
    index_values.sort()
    length = len(index_values)
    if five_cards_bool:
        top_five_cards = top_five_cards_func(cards)
    else:
        top_five_cards = player_cards.copy()
    # Проверяем последовательности
    ans = []
    for i in range(length):
        if ((int(index_values[i]) + 4) % 13 == (int(index_values[(i + 1) % length]) + 3) % 13 == (int(index_values[(i + 2) % length]) + 2) % 13
                == (int(index_values[(i + 3) % length]) + 1) % 13 == int(index_values[(i + 4) % length])):
            straight_value = max(int(index_values[i]), int(index_values[(i + 1) % length]), int(index_values[(i + 2) % length]),
                                 int(index_values[(i + 3) % length]), int(index_values[(i + 4) % length]))
            straight_value = values[straight_value]
            return True, straight_value
    return False, top_five_cards

def pair(player_cards):
    global table, values
    cards = table.copy()
    for el in player_cards:
        cards.append(el)

    pair_values = sorted(card.value for card in cards)
    pair_values = sorted(pair_values, key=lambda card: values.index(card), reverse=True)
    top_five_cards = top_five_cards_func(cards).copy()
    if len(pair_values) >= len(set(pair_values)) + 1:
        for i in range(len(pair_values) - 1):
            if pair_values[i] == pair_values[i + 1]:
                for q in range(2):
                    if pair_values[i] in top_five_cards:
                        top_five_cards.remove(pair_values[i])
                return True, [pair_values[i], pair_values[i + 1], top_five_cards[0], top_five_cards[1], top_five_cards[2]]
    else:
        return False, top_five_cards

def three_cards(player_cards):
    global table, values
    cards = table.copy()
    for el in player_cards:
        cards.append(el)
    three_values = sorted(card.value for card in cards)
    three_values = sorted(three_values, key=lambda card: values.index(card), reverse=True)
    top_five_cards = top_five_cards_func(cards)
    if len(three_values) >= len(set(three_values)) + 2:
        for i in range(len(three_values) - 2):
            if three_values[i] == three_values[i + 1] == three_values[i + 2]:
                for q in range(3):
                    if three_values[i] in top_five_cards:
                        top_five_cards.remove(three_values[i])
                return True, [three_values[i], three_values[i + 1], three_values[i + 2], top_five_cards[0], top_five_cards[1]]
        else:
            return False, top_five_cards
    else:
        return False, top_five_cards

def two_pairs(player_cards):
    global table, values
    cards = table.copy()
    for el in player_cards:
        cards.append(el)
    pair_pair_values = sorted(card.value for card in cards)
    set_pair_pair_values = set(pair_pair_values)
    top_five_cards = top_five_cards_func(cards)
    ans_top_five_cards = []
    del_l_pair_values = pair_pair_values.copy()
    ans_two_pairs = []
    for el in set_pair_pair_values:
        del_l_pair_values.remove(el)
    con = True
    for i in range(len(pair_pair_values) - 1):
        for j in range(i + 1, len(pair_pair_values)):
            if pair_pair_values[i] == pair_pair_values[j]:
                for q in range(j + 1, len(pair_pair_values) - 1):
                    for w in range(q + 1, len(pair_pair_values)):
                        if pair_pair_values[q] == pair_pair_values[w]:
                            ans_two_pairs.append(pair_pair_values[q])
                            ans_two_pairs.append(pair_pair_values[w])
                            ans_two_pairs.append(pair_pair_values[i])
                            ans_two_pairs.append(pair_pair_values[j])
                            #print('ans_two_pairs:', ans_two_pairs)
                            con = False
                            break
                    if con == False:
                        break
            if con == False:
                break
        if con == False:
            break
    if len(pair_pair_values) >= len(set(pair_pair_values)) + 2 and len(del_l_pair_values) >= 2 and len(del_l_pair_values) == len(set(del_l_pair_values)):
        if len(del_l_pair_values) == 3:
            del_l_pair_values = sorted(del_l_pair_values, key=lambda card: values.index(card), reverse=True)
            #print(del_l_pair_values)
            top_five_cards = sorted(card.value for card in cards)
            top_five_cards.reverse()
            del_l_pair_values.pop(-1)
            #print(del_l_pair_values)
            for i in range(2):
                ans_top_five_cards.append(del_l_pair_values[0])
                ans_top_five_cards.append(del_l_pair_values[1])
            #print(ans_top_five_cards)
            top_seven_cards = sorted(top_five_cards, key=lambda card: values.index(card), reverse=True)
            while top_seven_cards[0] in del_l_pair_values:
                top_seven_cards.remove(top_seven_cards[0])
                if len(top_seven_cards) == 0:
                    return False, top_seven_cards

            ans_top_five_cards = sorted(ans_top_five_cards, key=lambda card: values.index(card), reverse=True)
            ans_top_five_cards.append(top_seven_cards[0])
            return True, ans_top_five_cards
        else:
            top_five_cards = sorted(card.value for card in cards)  # [:5]
            top_five_cards.reverse()
            top_seven_cards = sorted(top_five_cards, key=lambda card: values.index(card), reverse=True)
            while top_seven_cards[0] in del_l_pair_values:
                top_seven_cards.remove(top_seven_cards[0])
                if len(top_seven_cards) == 0:
                    return False, top_seven_cards
            if values.index(ans_two_pairs[0]) < values.index(ans_two_pairs[3]):
                ans_two_pairs.reverse()
            ans_two_pairs.append(top_seven_cards[0])
            return True, ans_two_pairs
    return False, top_five_cards

def four_cards(player_cards):
    global table, values
    cards = table.copy()
    for el in player_cards:
        cards.append(el)
    four_values = sorted(card.value for card in cards)
    four_values = sorted(four_values, key=lambda card: values.index(card), reverse=True)
    top_five_cards = top_five_cards_func(cards)
    if len(four_values) >= len(set(four_values)) + 3:
        for i in range(len(four_values) - 3):
            if four_values[i] == four_values[i + 1] == four_values[i + 2] == four_values[i + 3]:
                for q in range(4):
                    if four_values[i] in top_five_cards:
                        top_five_cards.remove(four_values[i])
                return True, [four_values[i], four_values[i + 1], four_values[i + 2], four_values[i + 3],top_five_cards[0]]
        return False, top_five_cards
    else:
        # top_five_cards = sorted(cards, key=lambda card: card.value, reverse=True)[:5]
        return False, top_five_cards

def full_house(player_cards):
    global table, values
    cards = table.copy()
    for el in player_cards:
        cards.append(el)
    full_values = sorted(card.value for card in cards)
    ans_top_five_cards = []
    del_l_full_values = full_values.copy()
    top_five_cards = top_five_cards_func(cards)
    set_full_pair_values = set(full_values)
    for el in set_full_pair_values:
        del_l_full_values.remove(el)
    del_l_full_values.sort()
    if (len(full_values) == len(set(full_values)) + 3 and four_cards(player_cards)[0] == False
            and len(set(del_l_full_values)) == 2):
        for i in range(2):
            ans_top_five_cards.append(del_l_full_values[0])
            ans_top_five_cards.append(del_l_full_values[2])
        ans_top_five_cards.append(del_l_full_values[1])
        ans_top_five_cards = sorted(ans_top_five_cards, key=lambda card: values.index(card), reverse=True)
        return True, ans_top_five_cards
    return False, top_five_cards

def flush(player_cards, five_cards_bool = True):
    global table, values, suits
    if five_cards_bool:
        cards = table.copy()
        for el in player_cards:
            cards.append(el)
    else:
        cards = player_cards
    card_suits = sorted(card.suit for card in cards)
    n_card_suits = sorted(cards, key=lambda card: suits.index(card.suit), reverse=True)
    for i in range(len(card_suits) - 4):
        if n_card_suits[i].suit == n_card_suits[i + 4].suit:

            ans_n_card_suits = n_card_suits.copy()
            for el in n_card_suits:
                if el.suit != n_card_suits[i].suit:
                    ans_n_card_suits.remove(el)
            ans_n_card_suits = sorted(ans_n_card_suits, key=lambda card: values.index(card.value), reverse=True)
            ans_n_card_suits = n_card_suits.copy()
            ans_n_card_suits = sorted(ans_n_card_suits, key=lambda card: values.index(card.value), reverse=True)
            return True, [card.value for card in ans_n_card_suits if card.suit == n_card_suits[i].suit], n_card_suits[i].suit
    return False, card_suits

def straight_flush(player_cards):
    global table, values
    cards = table.copy()
    for el in player_cards:
        cards.append(el)
    top_five_cards = top_five_cards_func(cards)
    if has_straight(player_cards)[0]:
        cards = has_straight(player_cards)[1]
        if flush(player_cards)[0]:
            if has_straight(flush(player_cards)[1], False)[0]:
                return True, has_straight(flush(player_cards)[1], False)[1]
    return False, top_five_cards

def royal_flush(player_cards):
    global table, values
    cards = table.copy()
    for el in player_cards:
        cards.append(el)
    top_five_cards = top_five_cards_func(cards)
    r_f_cards_b = [Card('Буби', 'A'), Card('Буби', 'K'), Card('Буби', 'Q'),
                   Card('Буби', 'J'), Card('Буби', '10')]
    for su in suits:
        c = 0
        for el in r_f_cards_b:
            for le in cards:
                if el.value == le.value and su == le.suit: c += 1
        if c == 5: return True, [card.value for card in r_f_cards_b], su
    return False, top_five_cards

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
    for el in player_sort:
        if el.player_combination_name == player_sort[0].player_combination_name:
            player_win.append(el)
    wins_combination_players = player_win.copy()

    for i in range(len(player_win) - 1):
        for q in range(len(player_win[0].player_combination)):
            if (values.index(wins_combination_players[i].player_combination[q]) >
                    values.index(wins_combination_players[i + 1].player_combination[q])):
                wins_combination_players[i], wins_combination_players[i + 1] =\
                    wins_combination_players[i + 1], wins_combination_players[i]
                break
            elif (values.index(wins_combination_players[i].player_combination[q]) <= values.index(wins_combination_players[i + 1].player_combination[q])):
                continue
    wins_combination_players.reverse()
    wins_combination = [wins_combination_players[0]]
    for i in range(1, len(wins_combination_players)):
        if wins_combination_players[i-1].player_combination != wins_combination_players[i].player_combination:
            break
        else:
            wins_combination.append(wins_combination_players[i])
    bank_separation(wins_combination)

def bank_separation(wins_combination):
    global bank
    if len(wins_combination) == 1:
        wins_combination[0].player_bank_win = bank
    else:
        #print()
        players_procent = 1 / len(wins_combination)
        bank_pl_proc = int(bank * players_procent)
        for pla in wins_combination:
            pla.player_bank_win = bank_pl_proc
            bank -= bank_pl_proc
            if bank < bank_pl_proc:
                pla.player_bank_win += bank

def compare_cards_i():
    global players
    player_win = []
    player_sort = players.copy()
    player_sort = sorted(player_sort, key=lambda comb: poker_combinations.index(comb.player_combination_name), reverse=True)
    #print([pla.player_combination_name for pla in player_sort])
    for el in player_sort:
        if el.player_combination_name == player_sort[0].player_combination_name:
            player_win.append(el)
    #print([pla.player_combination_name for pla in player_win])
    wins_combination_players = player_win.copy()

    for i in range(len(player_win) - 1):
        for q in range(len(player_win[0].player_combination)):
            if (values.index(wins_combination_players[i].player_combination[q]) >
                    values.index(wins_combination_players[i + 1].player_combination[q])):
                wins_combination_players[i], wins_combination_players[i + 1] =\
                    wins_combination_players[i + 1], wins_combination_players[i]
                break
            elif (values.index(wins_combination_players[i].player_combination[q]) <= values.index(wins_combination_players[i + 1].player_combination[q])):
                continue
    wins_combination_players.reverse()
    wins_combination = [wins_combination_players[0]]
    for i in range(1, len(wins_combination_players)):
        if wins_combination_players[i-1].player_combination != wins_combination_players[i].player_combination:
            break
        else:
            wins_combination.append(wins_combination_players[i])
    return wins_combination


def main_game():
    #print('main_game started')
    gen_d()
    mix_deck()
    card_draw()
    out_cards(1)
    blind()
    preflop()
    # flop()
    # out_cards(1)
    # turn()
    # out_cards(1)
    # river()
    # final()


player_1 = Player('Player 1')
player_2 = Player('Player 2')
player_3 = Player('Player 3')
player_4 = Player('Player 4')


#Переменные
prelast_bet = 0
poker_combinations = ['top_cards', 'pair', 'two_pairs', 'three_cards', 'straight',
                'flush', 'full_house', 'four_cards', 'straight_flush', 'royal_flush']
deck = []
base_bet = 10
m_bet = 5
last_bet = 0
next_turn = 0
#players = [player_1, player_2, player_3, player_4]
players = [player_1, player_2]
check_players = []
bank = 0
out = [] #Сброс
table = [] #Стол
values=['2','3','4','5','6','7','8','9','10','J','Q','K','A'] #Задаем масти и достонство карт
suits=['Буби','Червы','Пики','Крести']
blind_counter = 0



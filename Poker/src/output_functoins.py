from classes import *
from game_main import *
#from main import restart


def start_game(): main_game()

def show_table_cards(table):
    # for el in table:
    #     el.show()
    # print()
    pass

def show_player_cards(pla):
    # print(pla.player_name)
    # print(pla.n_bet)
    pass

def show_table_cards_1(table): return table

def show_cards_way(card):
    ans_c_i = '../data/'
    if card.suit == 'Буби':
        ans_c_i += '/images_b/card_'
    elif card.suit == 'Червы':
        ans_c_i += '/images_ch/card_'
    elif card.suit == 'Пики':
        ans_c_i += '/images_p/card_'
    elif card.suit == 'Крести':
        ans_c_i += '/images_k/card_'
    ans_c_i += card.value
    return ans_c_i

def get_players():
    players, next_turn = ret_players()
    return players

def get_turn():
    players, next_turn = ret_players()
    return next_turn

def get_last_bet(): return last_bet_main()

def push_last_bet_i(a): push_last_bet(a)

def get_m_bet(): return m_bet_main()

def main_player_answer(ans, bet = '0', bet_o = 0):
    player_bet(ans, bet, bet_o)

def flop_i(): flop()

def turn_i(): turn()

def river_i(): river()

def final_i(): final()

def get_wins_player_i(): return compare_cards_i()

def get_table_i(): return get_table()
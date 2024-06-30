import random

from GameState import GameState
from Deck import Deck
from Row import Row
from Human import Human


class GameInteractions:
    MAX_PLAYERS = 4
    COUNT_ROWS = 3

    @staticmethod
    def run():
        count_players = 0
        while not 1 < count_players <= GameInteractions.MAX_PLAYERS:
            count_players = int(input(f'Введите количество игрогов (2 =< n =< {GameInteractions.MAX_PLAYERS}): '))

        players = []
        for i in range(count_players):
            name = input(f'Введите имя {i + 1}-го игрока: ')
            players.append(Human(name))

        current_player = 0
        deck = Deck()
        deck.shuffle()

        rows = []
        for i in range(GameInteractions.COUNT_ROWS):
            rows.append(Row([deck.draw_card()]))
        rows[1].add_card(deck.draw_card())

        gs = GameState(players, rows, current_player, deck)

        total_moves = 53 // (count_players * GameInteractions.COUNT_ROWS) + 2
        for move in range(total_moves):
            print('-------------------------')
            print(f'Ход {move + 1}')
            for i in range(count_players):
                print('Колоды:')
                GameInteractions.print_rows(gs.rows)
                current_mover = gs.players[gs.current_player]
                current_mover.choose_row(gs.rows, gs.players)
                gs.add_cards()
                gs.current_player = (gs.current_player + 1) % count_players

                gs.save()

        for p in gs.players:
            print(f'Игрок {p} набрал - {p.hand.score()} очков')
            # print(f'Карты: {p.hand.get_dictionary()}')

        max_score = 0
        winner = ''
        for p in gs.players:
            cur_score = p.hand.score()
            if cur_score > max_score:
                winner = p
                max_score = cur_score

        print(f'Победитель - {winner}')

    @staticmethod
    def print_rows(row: list[Row]):
        for j in range(3):
            print(f'{j + 1}: {row[j]}')

    # @staticmethod
    # def print_player():

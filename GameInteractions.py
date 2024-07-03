from GameState import GameState
from Deck import Deck
from Player import Player
from Row import Row


class GameInteractions:
    MAX_PLAYERS = 4
    COUNT_ROWS = 3
    SAVE_FILE = 'save-file.json'

    @staticmethod
    def run():
        exist_last_game = GameInteractions.is_exist_last_game()

        gs = GameState([], [])
        if exist_last_game:
            last_gs = GameState.load(GameInteractions.SAVE_FILE)
            print(f'Найдена игра: {last_gs}')
            ans = input('Введите "да" чтобы начать новую игру: ')
            if ans.lower() == 'да':
                gs = GameInteractions.start_new_game()
            else:
                gs = last_gs
                print('Игра загружена')
        else:
            gs = GameInteractions.start_new_game()

        # Расчет общего количества ходов в игре
        # за один ход каждый игрок выбирает колоду
        total_moves = gs.deck.remaining_cards() // (len(gs.players) * GameInteractions.COUNT_ROWS)
        for move in range(total_moves):
            print('-------------------------')
            print(f'Ход {move + 1}')
            for i in range(len(gs.players)):
                print('Колоды:')
                GameInteractions.print_rows(gs.rows)
                current_mover = gs.players[gs.current_player]
                current_mover.choose_row(gs.rows, gs.players)

                # Добавление карт в колоды
                gs.add_cards()

                # Обновление номера текущего игрока
                gs.current_player = (gs.current_player + 1) % len(gs.players)

                gs.save()

        # Вывод очков у каждого игрока
        for p in gs.players:
            print(f'Игрок {p} набрал - {p.hand.score()} очков')

        max_score = 0
        winner = ''
        # Поиск игрока с наибольшим количеством очков
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

    @staticmethod
    def is_exist_last_game():
        try:
            GameState.load(GameInteractions.SAVE_FILE)
        except Exception:
            return False
        return True

    @staticmethod
    def start_new_game():
        # Подготовка к новой игре
        # Ввод количества игроков
        # количества людей
        # подготовка колоды
        # раздача карт

        count_players = 0
        while not 1 < count_players <= GameInteractions.MAX_PLAYERS:
            count_players = int(input(f'Введите количество игроков (2 =< n =< {GameInteractions.MAX_PLAYERS}): '))

        count_humans = -1
        while not 0 <= count_humans <= count_humans:
            count_humans = int(input(f'Введите число людей (0 =< n =< {count_players}): '))

        players = []
        for i in range(count_humans):
            name = input(f'Введите имя {i + 1}-го игрока: ')
            players.append(Player(name, None, True))

        for i in range(count_players - count_humans):
            name = f'AI{i}'
            players.append(Player(name, None, False))

        current_player = 0
        deck = Deck()
        deck.shuffle()

        rows = []
        for i in range(GameInteractions.COUNT_ROWS):
            rows.append(Row([deck.draw_card()]))
        rows[1].add_card(deck.draw_card())

        return GameState(players, rows, current_player, deck)
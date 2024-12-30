import random

# Implement a 2 players version of tictactoe
PLAYER_1 = "X"
PLAYER_2 = "O"
GRID = [str(n) for n in range(1, 10)]


def choose_sides():
    global PLAYER_1
    global PLAYER_2
    if random.choice([0, 1]) == 0:
        PLAYER_1 = "O"
        PLAYER_2 = "X"


def check_game_over():
    global GRID
    positive_results = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for result in positive_results:
        a, b, c = result
        v1, v2, v3 = GRID[a], GRID[b], GRID[c]
        for i in ["X", "O"]:
            if (v1, v2, v3) == (i, i, i):
                return True, f"{i} WON!"

    if all(not e.isnumeric() for e in GRID):
        return True, "DRAW"
    return False, ""


def show_grid_status():
    print(
        f"""
GRID: 
{GRID[0:3]}
{GRID[3:6]}
{GRID[6:9]}
"""
    )


def start_game():
    global GRID
    choose_sides()
    print(
        f"""PLAYER 1: {PLAYER_1}
PLAYER 2: {PLAYER_2}
"""
    )
    show_grid_status()
    while True:
        is_game_over, message = check_game_over()
        if is_game_over:
            print(f"Game has ended, {message}")
            break

        player_input = ask_for_player_input("1", PLAYER_1)
        GRID[int(player_input) - 1] = PLAYER_1
        show_grid_status()

        is_game_over, message = check_game_over()
        if is_game_over:
            print(f"Game has ended, {message}")
            break

        player_input = ask_for_player_input("2", PLAYER_2)
        GRID[int(player_input) - 1] = PLAYER_2
        show_grid_status()


def ask_for_player_input(player: str, symbol: str):
    player_input = input(
        f"Player {player}, select a number on the GRID to put the {symbol}: "
    )
    while (
        not player_input.isnumeric() and int(player_input) > 9 and int(player_input) < 1
    ):
        player_input = input(
            f"Invalid input. Player {player}, select a number on the GRID to put the '{symbol}': "
        )
    return player_input


start_game()

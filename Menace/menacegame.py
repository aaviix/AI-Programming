import json
import random

TOTAL_POSITIONS = 8


# Function to select a position based on weighted probability

def sel_weight_position(position_weights):
    # Calculate cumulative weights
    cumulative_wg = []
    total = 0
    for wg in position_weights:
        total += wg
        cumulative_wg.append(total)

    # Select position based on cumulative weights
    random_roll = random.randint(1, total)
    for i, cumulative_weight in enumerate(cumulative_wg):
        if random_roll <= cumulative_weight:
            return i

        random_roll -= position_weights[i]


# Function to check if the game has reached an end state

def game_over(game_state):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_combinations:
        if game_state[a] == game_state[b] == game_state[c] != '-':
            return True, game_state[a]
    if '-' not in game_state:
        return True, None
    return False, None


def make_move(game_state, move, player):
    new_game_state = list(game_state)
    new_game_state[move] = player
    return ''.join(new_game_state)


def the_legal_moves(game_state):
    return [i for i, spot in enumerate(game_state) if spot == '-']


def print_board(game_state):
    print("Board positions:")
    for i in range(1, 10, 3):
        print(f"{i} {i+1} {i+2}")
    print("\nCurrent board:")
    for i in range(0, 9, 3):
        print(' '.join(game_state[i:i+3]))


def man_move(game_state):
    print_board(game_state)
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in the_legal_moves(game_state):
                return move
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a number.")


def save_menace_game_state(menace):
    with open('menace_game_state.json', 'w') as file:
        json.dump(menace, file)


def load_menace_game_state():
    try:
        with open('menace_game_state.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def one_game(menace, human_player=False, self_play=False):
    game_state = "---------"
    history = []
    game_end, winner = game_over(game_state)
    while not game_end:
        player = 'X' if game_state.count('X') == game_state.count('O') else 'O'
        if human_player and player == 'O':
            move = man_move(game_state)
        else:
            if self_play or game_state not in menace:
                num_holes = game_state.count('-')
                menace[game_state] = [TOTAL_POSITIONS for _ in range(num_holes)]
            move_position_weights = menace[game_state]
            legal_moves = the_legal_moves(game_state)
            chosen_index = sel_weight_position(move_position_weights)
            move = legal_moves[chosen_index]

        history.append((game_state, move))
        game_state = make_move(game_state, move, player)
        game_end, winner = game_over(game_state)
    if human_player:
        print_board(game_state)
        if winner:
            print(f"Game ended, winner: {winner}")
        else:
            print("Game ended, draw")
    update_board(menace, history, winner)
    return winner


def update_board(menace, history, winner):
    reward = 10
    penalty = 1
    for game_state, move in reversed(history):
        if game_state in menace:
            index = the_legal_moves(game_state).index(move)
            if (winner == 'X' and game_state.count('X') == game_state.count('O')) or \
                    (winner == 'O' and game_state.count('X') > game_state.count('O')):
                menace[game_state][index] += reward
            else:
                menace[game_state][index] = max(1, menace[game_state][index] - penalty)


def play_again():
    choice = input("Play again? (y/n): ").lower()
    return choice == 'y'


def train_menace_self_play(menace, games):
    for i in range(games):
        one_game(menace, human_player=False, self_play=True)
        if i % 1000 == 0 or i == games - 1:
            print(
                f"Self-Play Training Progress: {i / games * 100:.1f}%", end="\r")
    print()


menace = load_menace_game_state()

# Training MENACE
train_menace_self_play(menace, 10000)

save_menace_game_state(menace)

# Playing against MENACE
while True:
    one_game(menace, human_player=True)
    if play_again():
        continue
    else:
        break

save_menace_game_state(menace)

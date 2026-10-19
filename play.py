from data_loader import load_data
from game import Game

path_len_2 = "./data/words_len_2.csv"
path_len_5 = "./data/words_len_5_cleaned.csv"

data = load_data(path_len_5)

game = Game(data, verbose=True)

while not game.finished:
    prompt = "Enter word (" + str(game.get_remaining_attempts()) + " attempts remaining): "
    inp = input(prompt)
    game.eval_word(inp)
    
from data_loader import load_data
from game import Game
from agent import Result
from agent_random import RandomAgent
#from agent_bandit import BanditAgent
#from agent_nn import NNAgent

path_len_2 = "./data/words_len_2.csv"
path_len_5 = "./data/words_len_5_cleaned.csv"

data = load_data(path_len_2)
vocab_size = len(data)

NUM_GAMES = 10000
PRINT_RATE = 500

agent = RandomAgent(data)
#agent = BanditAgent(data)
#agent = NNAgent(data, vocab_size)

success_rate = 0
avg_steps = 0

for i in range(NUM_GAMES):
    game = Game(data, verbose=False)
    agent.start_game()
    #print("New Game with solution:", game.solution)
    
    while not game.finished:
        action = agent.take_action()
        valid, colors = game.eval_word(action)
        if valid:
            #print(action, Back.RED, n_red, Back.YELLOW, n_yellow, Back.GREEN, n_green, Style.RESET_ALL)
            result = Result(action, colors, game.success, game.finished and not game.success)
            agent.rcv_result(result)

    success_rate += game.success
    avg_steps += game.attempts

    if i % PRINT_RATE == PRINT_RATE - 1:
        print(f"Game {i+1}, Success Rate: {success_rate / PRINT_RATE:.2f}, Avg Steps: {avg_steps / PRINT_RATE:.2f}")
        avg_steps = 0
        success_rate = 0



    
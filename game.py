from enum import Enum
from colorama import Back, Style
from data_loader import sample_word

MAX_ATTEMPTS = 6

class Color(Enum):
    GREY = 0
    YELLOW = 1
    GREEN = 2

class Game:
    def __init__(self, data, verbose=True):
        self.verbose = verbose
        self.words = data
        self.solution = sample_word(data)
        self.word_len = len(self.solution)
        self.attempts = 0
        self.finished = False
        self.success = False

    def get_remaining_attempts(self):
        return MAX_ATTEMPTS - self.attempts

    def eval_word(self, word):
        if len(word) != self.word_len:
            print("Error: Word length mismatch:", word)
            return False, []
        if self.finished:
            print("Error: Word evaluated after game has ended.")
            return False, []

        word = word.lower()
        if word not in self.words:
            print("Error: Word unknown:", word)
            return False, []
        
        self.attempts += 1
        if self.attempts == MAX_ATTEMPTS:
            self.finished = True

        colors = [Color.GREY] * self.word_len
        
        solution_matched = [False] * self.word_len
        word_matched = [False] * self.word_len

        for i in range(self.word_len):
            if word[i] == self.solution[i]:
                colors[i] = Color.GREEN
                solution_matched[i] = True
                word_matched[i] = True

        for i in range(len(word)):
            if word_matched[i]:
                continue
    
            for j in range(len(self.solution)):
                if not solution_matched[j] and self.solution[j] == word[i]:
                    solution_matched[j] = True
                    colors[i] = Color.YELLOW
                    break

        if all(x == Color.GREEN for x in colors):
            self.finished = True
            self.success = True

        if self.verbose:                    
            for i in range(len(colors)):
                color = ""
                if colors[i] == Color.GREEN:
                    color = Back.GREEN
                elif colors[i] == Color.YELLOW:
                    color = Back.YELLOW
                print(color, end="")
                print(word[i], end="")
                print(Style.RESET_ALL, end="")
            print(Style.RESET_ALL)

            if self.success:
                print("Game solved in", self.attempts, "steps! Solution was:", self.solution)
            elif self.finished:
                print("Game lost! Solution was:", self.solution)

        return True, colors
        
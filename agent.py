from game import Color


class Result:
    def __init__(self, word: str, colors: list[Color], solved: bool, failed: bool):
        self.word = word
        self.colors = colors
        self.solved = solved
        self.failed = failed


class State:
    def __init__(self):
        self.results: list[Result] = []
        self.attempts = 0

    def add_result(self, result: Result):
        self.results.append(result)
        self.attempts += 1


class Agent:
    def __init__(self, action_space: list[str]):
        self.action_space = action_space
        self.state = State()

    def start_game(self):
        self.state = State()

    def take_action(self) -> str:
        return ""

    def calc_reward(self, result: Result) -> float:
        if result.solved:
            return 10
        if result.failed:
            return -10
        return -1

    def rcv_result(self, result: Result):
        pass

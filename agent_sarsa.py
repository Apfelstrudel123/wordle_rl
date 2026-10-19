import random
import agent


class SarsaAgent(agent.Agent):
    def __init__(self, action_space: list[str]):
        super(SarsaAgent, self).__init__(action_space)
        self.action_space = action_space
        self.word_len = len(action_space[0])
        # self.state_space =

    def start_game(self):

        return super().start_game()

    def take_action(self) -> str:
        return random.choice(self.action_space)

    def rcv_result(self, result: agent.Result):
        pass

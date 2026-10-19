import random
import agent

class RandomAgent(agent.Agent):
    def __init__(self, action_space: list[str]):
        super(RandomAgent, self).__init__(action_space)
        
    def take_action(self) -> str:
        return random.choice(self.action_space)

    def rcv_result(self, result: agent.Result):
        pass
import random
from multi_agent_bandits.core.agent import Agent

class RandomAgent(Agent):
    def choose_arm(self):
        return random.randrange(self.n_arms)

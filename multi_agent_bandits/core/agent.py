import random

class Agent:
    """
    Class interface for a bandit agent.
    """

    def __init__(self, n_arms):
        self.n_arms = n_arms

    def choose_arm(self):
        raise NotImplementedError

    def update(self, reward):
        pass

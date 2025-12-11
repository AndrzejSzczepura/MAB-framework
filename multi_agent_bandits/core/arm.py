import random

class Arm:
    def __init__(self, mean, sd=1.0, reward_fn=None):
        self.mean = mean
        self.sd = sd
        self.reward_fn = reward_fn or self._gaussian

    def _gaussian(self):
        return random.gauss(self.mean, self.sd)

    def sample(self):
        return self.reward_fn()

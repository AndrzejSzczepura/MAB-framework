import random
from multi_agent_bandits.core.reward_sharing import linear_share

class Environment:
    """
    Extendable multi-agent bandit environment.
    Agents choose arms -> collisions are handled -> generate rewards.
    """

    def __init__(self, n_agents, n_arms, reward_means, collision_policy=linear_share):
        self.n_agents = n_agents
        self.n_arms = n_arms
        self.reward_means = reward_means
        self.collision_policy = collision_policy

    def sample_reward(self, arm):
        """Gaussian reward with mean arm value (placeholder)."""
        return random.gauss(self.reward_means[arm], 1.0)

    def step(self, agents):
        """
        One timestep:
        1. each agent selects an arm
        2. environment evaluates collisions and rewards
        3. agents receive reward
        """
        choices = [agent.choose_arm() for agent in agents]

        #group agents by th chosen arm
        collisions = {}
        for i, arm in enumerate(choices):
            collisions.setdefault(arm, []).append(i)

        rewards = [0.0] * len(agents)
        for arm, agent_ids in collisions.items():
            raw_reward = self.sample_reward(arm)

            if len(agent_ids) == 1:
                #if no collision
                rewards[agent_ids[0]] = raw_reward
            else:
                shares = self.collision_policy(raw_reward, len(agent_ids))
                for idx, aid in enumerate(agent_ids):
                    rewards[aid] = shares[idx]

        #update agents with rewards.
        for agent, reward in zip(agents, rewards):
            agent.update(reward)

        return choices, rewards

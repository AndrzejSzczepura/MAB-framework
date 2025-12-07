import os
import csv
import matplotlib.pyplot as plt

class ExperimentRunner:
    """
    Runs agents in an environment with metric logging.
    Feel free to extend to your needs (class MyRunner(ExperimentRunner):...)
    Optional exporting of logs to disk (if save_dir provided)
    """

    def __init__(self, env, agents, timestep_limit=100, save_dir=None):
        self.env = env
        self.agents = agents
        self.T = timestep_limit

        #logs
        self.choices_log = []
        self.rewards_log = []
        self.total_rewards = [0.0] * len(agents)

        #saving option
        self.save_dir = save_dir
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)

    def run(self):
        """Run T steps and record metrics."""
        for t in range(self.T):
            choices, rewards = self.env.step(self.agents)

            self.choices_log.append(choices)
            self.rewards_log.append(rewards)

            for i, r in enumerate(rewards):
                self.total_rewards[i] += r

        if self.save_dir:
            self.save_logs()

        return self.choices_log, self.rewards_log

    def save_logs(self):
        #save choices
        choices_path = os.path.join(self.save_dir, "choices.csv")
        with open(choices_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([f"agent_{i}" for i in range(len(self.agents))])
            writer.writerows(self.choices_log)

        #save rewards
        rewards_path = os.path.join(self.save_dir, "rewards.csv")
        with open(rewards_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([f"agent_{i}" for i in range(len(self.agents))])
            writer.writerows(self.rewards_log)

        #save summary
        summary_path = os.path.join(self.save_dir, "summary.txt")
        with open(summary_path, "w") as f:
            f.write("Experiment Summary\n")
            for i, total in enumerate(self.total_rewards):
                f.write(f"Agent {i} total reward: {total:.2f}\n")

    def print_summary(self):
        print("Experiment Summary")
        for i, total in enumerate(self.total_rewards):
            print(f"Agent {i} total reward: {total:.2f}")
        print("--------------")

    def plot_reward_trajectories(self):
        for agent_idx in range(len(self.agents)):
            plt.plot([step[agent_idx] for step in self.rewards_log],
                     label=f"Agent {agent_idx}")

        plt.title("Reward per timestep")
        plt.xlabel("Time")
        plt.ylabel("Reward")
        plt.legend()
        plt.show()

    def plot_arm_frequencies(self):
        n_agents = len(self.agents)
        n_arms = self.env.n_arms

        counts = [[0]*n_arms for _ in range(n_agents)]

        for step in self.choices_log:
            for agent_idx, arm in enumerate(step):
                counts[agent_idx][arm] += 1

        for agent_idx in range(n_agents):
            plt.bar(range(n_arms), counts[agent_idx],
                    alpha=0.6, label=f"Agent {agent_idx}")

        plt.title("Arm selection frequencies")
        plt.xlabel("Arm")
        plt.ylabel("Count")
        plt.legend()
        plt.show()

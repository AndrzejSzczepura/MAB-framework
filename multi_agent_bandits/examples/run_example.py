from multi_agent_bandits.core.environment import Environment
from multi_agent_bandits.core.experiment_runner import ExperimentRunner

from multi_agent_bandits.strategies.random import RandomAgent
from multi_agent_bandits.strategies.ucb_baseline import UCB_BaselineAgent

def main():
    n_agents = 3
    n_arms = 3
    reward_means = [1.0, 2.0, 1.5]
    steps = 1000

    env = Environment(
        n_agents=n_agents,
        n_arms=n_arms,
        reward_means=reward_means)


    # agents = [RandomAgent(n_arms) for _ in range(n_agents)]
    agents = [UCB_BaselineAgent(n_arms) for _ in range(n_agents)]



    runner = ExperimentRunner(
        env,
        agents,
        timestep_limit=steps,
        save_dir="results/example_run")


    runner.run()
    runner.print_summary()
    runner.plot_reward_trajectories()
    runner.plot_arm_frequencies()

if __name__ == "__main__":
    main()

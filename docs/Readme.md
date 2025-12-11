# Multi-Agent-Bandits

*Andrzej Szczepura*

This repository contains the framework for running the Multi-Agent-Bandit simulations.

If you're writing a thesis supervised by me (A. Szczepura), you're in the right place.

Below you'll find some general guidelines and tips for the project.

## Contact
Best way of contacting me is through email - a.szczepura@vu.nl  
Add *MAB* at the beginning of the mail topic, please - I get quite a lot of mail, it'd be helpful (e.g. "[MAB] - Problem with repository access").  
I aim to reply to every message as soon as possible, within a 48h window.

We will have regular supervision meetings - you should be always aware of when the next one is, as we'll end every meeting with scheduling a new one.  
The meetings will be by default online, unless we've specified otherwise beforehand.

## Repository
The repository is designed in a highly modular way, so that you can easily modify or extend any part of the simulation.

For certain thesis topics (e.g., adding memory, noise, social learning, communication networks, new collision logic), you will need to work inside the core package.  
For others (e.g., designing new strategies or experiments), you will only edit the strategies/ or experiments/ folders.

Before writing any code, read the following files in order:
- environment.md
- core/environment.py
- core/agent.py, core/arm.py, core/reward_sharing.py
- experiments/example.py
- core/experiment_runner.py

Then create your own experiment script based on the example, run it, and play with the system.

### GitHub
To use the repository you must:

1. Fork the repository on GitHub  
Go to https://github.com/AndrzejSzczepura/MAB-framework  
Click Fork (top right)

This creates your own GitHub-hosted copy.

2. Clone your fork to your local machine  
From your fork page on GitHub:  
Click Code → copy the HTTPS/SSH link.

On your terminal:  
`git clone https://github.com/YOUR_USERNAME/MAB-framework.git`

Now you have a local working copy of your fork.

Note:  
- a fork is a GitHub copy of a repo; we need it so that I can easily access your code.  
- a clone is a physical copy of a repo on a machine. You'll clone your fork to work on it locally.

All your work, commits, and experiments should be pushed to your fork, not the main repository.

### Package Installation

After cloning your fork:

```
cd MAB-framework
pip install -e .
```

This installs the framework in editable mode, which gives you:

- the Python module multi_agent_bandits  
- the command-line tool mab

Note: Editable mode also creates an .egg-info folder — this is expected and ignored by git.  
More about the mab tool usage can be found in environment.md

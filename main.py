import random
import matplotlib.pyplot as plt
import numpy as np
import sys

class Slider:
    """
    This class implements RL environment.

    Our environment setting: [0,0,0,0,0,G], where G represents Goal state.

    Paramteres:
    ===========
    env_size: int
        --> size of the environment; default is 7.
    """
    def __init__(self, env_size=7):
        self.env_size = env_size
        self.env = [0]*self.env_size
        self.env[0] = 1
        self.action_space = [-1,1]
        self.observation_space=list(range(7))
        self.alpha = 0.01
        self.epsilon = 0.2

        # Initialize Q-table with random values
        self.q_table = np.zeros((self.env_size, 2))
     
    def reset(self):
        self.env = [0]*self.env_size
        self.env[0] = 1

    def get_action(self, state):
        p = random.random()
        if p < self.epsilon:
            return random.choice(self.action_space)
        else:
            if self.q_table[state][0] <= self.q_table[state][1]:
                return -1
            return 1

    def get_reward(self, state):
        if state == 6:
            return 10
        return 1

    def step(self, state, action):
        if state == 0 and action == -1:
            new_state = state
            reward = -10
        else:
            new_state = state+action
            self.env[state] = 0
            self.env[new_state] = 1
            reward = 10 if new_state == 6 else 1
        return new_state, reward
    
    def show_functions(self):
        print('{:^3}|{:^6}|{:^6}|'.format('S', '<-', '->'))
        for state, values in enumerate(self.q_table):
            print('{:^3}|{:^6.2f}|{:^6.2f}|'.format(state,values[0],values[1]))
        print('Policy: [',end='')
        for state in self.q_table:
            if state[0] > state[1]:
                print('<-',end=',')
            else:
                print('->',end=',')
        print(']')

    def __repr__(self):
        return "Easy example for understanding Reinforcement Learning."

def run_exp(num_iterations=100):
    game = Slider()
    reward_graph = []
    episode_graph = []

    game.reset()
    for episode in range(num_iterations):
        # Used to count the number of moves in a single iteration
        state = 0
        moves = 0
        episodic_reward = 0
        while state != 6 and moves < 20:
            action = game.get_action(state)
            #print(f'{state=}, {action=}')
            new_state, reward = game.step(state, action)
            #print(f'{new_state=}')
            # Temporal Difference
            temp_diff = reward + max(game.q_table[new_state]) - game.q_table[state][action]
            # Q_learning
            game.q_table[state][action] += game.alpha * temp_diff
            state = new_state
            moves += 1
            episodic_reward += reward
        episode_graph.append(moves)
        reward_graph.append(episodic_reward)
        game.reset()
    
    game.show_functions()
    plot_graphs(reward_graph, episode_graph)
    return 0

def plot_graphs(reward_graph, episode_graph):
    # Plot useful information
    fig, axs = plt.subplots(1,2, figsize=(5,2.7), layout='constrained')
    axs[0].plot(range(len(reward_graph)), reward_graph, label='reward')
    axs[0].set_title("Reward per episode")
    axs[0].set_xlabel("Episode")
    axs[0].set_ylabel("Reward")
    axs[1].plot(range(len(episode_graph)), episode_graph, label='ep_length')
    axs[1].set_title("Episode lengths")
    axs[1].set_xlabel("Episode")
    axs[1].set_ylabel("Legth")
    plt.show()
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        run_exp(100)
    else:
        run_exp(int(sys.argv[1]))
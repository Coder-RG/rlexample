import random
import matplotlib.pyplot as plt

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
        self.env = [0]*env_size
        self.action_space = [-1,1]
        self.observation_space=list(range(7))
        self.alpha = 0.01
        self.epsilon = 0.2

        # Initialize Q-table with random values
        self.q_table = [
            [random.random() for _ in range(2)] for _ in range(env_size)
        ]

    def get_action(self, state):
        p = random.random()
        if p < self.epsilon:
            return random.choice(self.action_space)
        else:
            if self.q_table[state][0] <= self.q_table[state][1]:
                return -1
            return 1

    def get_state(self):
        try:
            state = self.env.index(1)
        except ValueError:
            state = -1
        return state
    
    def get_reward(self, state):
        if state == 6:
            return 10
        return 1

    def step(self, state, action):
        if state == 0:
            new_state = state
            reward = -10
        else:
            new_state = state+action
            self.env[state] = 0
            self.env[new_state] = 1
            reward = 10 if new_state == 6 else 0
        return new_state, reward

    def __repr__(self):
        return "Easy example for understanding Reinforcement Learning."

def run_exp(num_iterations=100):
    game = Slider()
    reward_graph = []
    episode_graph = []

    for episode in range(num_iterations):
        # Used to count the number of moves in a single iteration
        game = Slider()
        state = 0
        moves = 0
        episodic_reward = 0
        while state != 6 and moves <= 100:
            action = game.get_action(state)
            new_state, reward = game.step(state, action)
            temp_diff = reward + max(game.q_table[new_state]) - game.q_table[state][action]
            game.q_table[state][action] += game.alpha * temp_diff
            state = new_state
            moves += 1
            episodic_reward += reward
        print(f'{episode=}, {moves=}')
        episode_graph.append(moves)
        reward_graph.append(episodic_reward)
    plt.plot(range(len(reward_graph), reward_graph))
    plt.plot(range(len(episode_graph), episode_graph))
    plt.show()
    return 0

if __name__ == "__main__":
    run_exp()
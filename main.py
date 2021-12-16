import random

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
        self.q_table = 0

    def get_action(self):
        return random.choice(self.action_space)

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
            reward = 10 if state == 6 else 0
        return new_state, reward

    def __repr__(self):
        return "Easy example for understanding Reinforcement Learning."

def run_exp():
    exp = Slider()
    return 0

if __name__ == "__main__":
    run_exp()
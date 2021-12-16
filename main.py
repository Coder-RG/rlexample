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

    def get_action(self, state):
        return random.choice(self.action_space)
    
    def get_state(self):
        return self.env.index(1)
    
    def get_reward(self, state):
        if state == 7:
            return 5
        return 0

    def step(self, action):
        return

    def __repr__(self):
        return "Easy example for understanding Reinforcement Learning."

if __name__ == "__main__":
    game = Slider()
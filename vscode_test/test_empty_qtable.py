import numpy as np
from time import sleep
import gym
from IPython.display import clear_output
import random
import time


env = gym.make("Taxi-v2").env
q_table = np.zeros([env.observation_space.n, env.action_space.n])

"""Evaluate agent's performance after Q-learning"""

total_epochs, total_penalties = 0, 0
episodes = 100

for i in range(episodes):
    clear_output(wait=True)
    print(f"Episode: {i}")
    state = env.reset()
    epochs, penalties, reward = 0, 0, 0
    
    done = False
    
    while not done:
        action = np.argmax(q_table[state])
        print("Action :", action, " State: ", state)
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print(f"Results after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")
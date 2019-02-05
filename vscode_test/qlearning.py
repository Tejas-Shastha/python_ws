import numpy as np
from time import sleep
import gym
from IPython.display import clear_output
import random
import time

start = time.time()
"""Training the agent"""

env = gym.make("Taxi-v2").env

q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1

# For plotting metrics
all_epochs = []
all_penalties = []

for i in range(1, 100001):
    state = env.reset()

    epochs, penalties, reward, = 0, 0, 0
    done = False

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Explore action space
        else:
            action = np.argmax(q_table[state])  # Exploit learned values

        next_state, reward, done, info = env.step(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * \
            (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1

    if i % 100 == 0:
        clear_output(wait=True)
        print("Episode: {}".format(i))

print("Training finished.\n")
end = time.time()
print("Time elapesed : ",  end-start)


total_epochs, total_penalties = 0, 0
episodes = 100

for i in range(episodes):
    state = env.reset()
    epochs, penalties, reward = 0, 0, 0
    if (q_table[state] == [0,0,0,0,0,0]).all() :
        #clear_output(wait=True)
        print("Skipped iteration : ", i)
        continue
    else:
        print("Computing iteration : ", i)
    done = False
    trials=0
    while not done:
        action = np.argmax(q_table[state])
        #clear_output(wait=True)
        #print("i : ", i,  "Action : ", action, " State : ", state)
        new_state, reward, done, info = env.step(action)
        
        if reward == -10:
            penalties += 1

        epochs += 1
        print("Iteration : ", i , " Epoch : ", epochs)
        #if epochs > 200:
        #    print("Iteration : ", i , " Epoch : ", epochs, " Skipped")
        #    break

    total_penalties += penalties
    total_epochs += epochs

print("Results after {episodes} episodes:")
print("Average timesteps per episode: {total_epochs / episodes}")
print("Average penalties per episode: {total_penalties / episodes}")

print("Final q table :", q_table)

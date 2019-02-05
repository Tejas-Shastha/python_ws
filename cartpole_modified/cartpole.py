import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import model_from_json

from scores.score_logger import ScoreLogger

ENV_NAME = "CartPole-v1"

GAMMA = 0.95
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995


class DQNSolver:

    def __init__(self, observation_space, action_space):
        self.exploration_rate = EXPLORATION_MAX

        self.action_space = action_space
        self.memory = deque(maxlen=MEMORY_SIZE)
        self.observation_space = observation_space

        # self.model = Sequential()
        # self.model.add(Dense(24, input_shape=(observation_space,), activation="relu"))
        # self.model.add(Dense(24, activation="relu"))
        # self.model.add(Dense(self.action_space, activation="linear"))
        # self.model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE))
    
    def build_fresh(self):
        self.model = Sequential()
        self.model.add(Dense(24, input_shape=(self.observation_space,), activation="relu"))
        self.model.add(Dense(24, activation="relu"))
        self.model.add(Dense(self.action_space, activation="linear"))
        self.model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE))
        self.train_mode = True

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() < self.exploration_rate and self.train_mode:
            return random.randrange(self.action_space)
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])

    def experience_replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(list(self.memory), BATCH_SIZE)
        for state, action, reward, state_next, terminal in batch:
            q_update = reward
            if not terminal:
                q_update = (reward + GAMMA * np.amax(self.model.predict(state_next)[0]))
            q_values = self.model.predict(state)
            q_values[0][action] = q_update
            self.model.fit(state, q_values, verbose=0)
        self.exploration_rate *= EXPLORATION_DECAY
        self.exploration_rate = max(EXPLORATION_MIN, self.exploration_rate)

    def save_model(self):
        model_json = self.model.to_json()
        with open("cartpole_model.json","w") as json_file:
            json_file.write(model_json)
        self.model.save_weights("cartpole_model.h5")
        print("Saved model and weights")

    def load_model(self):
        json_file = open('cartpole_model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("cartpole_model.h5")
        print("Loaded model from disk")
        self.model = loaded_model
        self.model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE))
        self.train_mode = False
        return loaded_model



def cartpole():
    env = gym.make("CartPole-v1")
    score_logger = ScoreLogger(ENV_NAME)
    observation_space = env.observation_space.shape[0]
    action_space = env.action_space.n
    dqn_solver = DQNSolver(observation_space, action_space)
    dqn_solver.build_fresh()
    # dqn_solver.load_model()
    run = 0
    while True:
        run += 1
        state = env.reset()
        state = np.reshape(state, [1, observation_space])
        step = 0
        while True:
            step += 1
            env.render()
            action = dqn_solver.act(state)
            state_next, reward, terminal, info = env.step(action)
            reward = reward if not terminal else -reward
            state_next = np.reshape(state_next, [1, observation_space])
            if dqn_solver.train_mode:
                dqn_solver.remember(state, action, reward, state_next, terminal)
            state = state_next
            if terminal:
                print("Run: " + str(run) + ", exploration: " + str(dqn_solver.exploration_rate) + ", score: " + str(step))
                is_solved = score_logger.add_score(step, run)
                if is_solved and dqn_solver.train_mode:
                    dqn_solver.save_model()
                    exit()
                break
            if dqn_solver.train_mode:
                dqn_solver.experience_replay()
            


if __name__ == "__main__":
    cartpole()

import os
import pickle
import time

import gymnasium as gym
import hi_env

gym.register_envs(hi_env)

env = gym.make("hi-standup-v0")
configs: list = []
filename: str = env.unwrapped.get_initial_config_filename()

if os.path.exists(filename):
    configs = pickle.load(open(filename, "rb"))

try:
    while True:
        env.reset(options={"use_cache": False})
        configs.append([env.unwrapped.sim.data.qpos.copy(), env.unwrapped.sim.data.ctrl.copy()])

        if len(configs) % 100 == 0:
            print(f"Generated {len(configs)} initial in the file {filename}")
            pickle.dump(configs, open(filename, "wb"))
except KeyboardInterrupt:
    print("Saving...")
    pickle.dump(configs, open(filename, "wb"))

import numpy as np

# 兼容旧代码，临时添加 np.bool
if not hasattr(np, "bool"):
    np.bool = bool  # 让 np.bool 指向 Python 的 bool
    
import soccer_twos
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env

# Wrap soccer_twos in a vectorized environment for efficient training
def make_env():
    return soccer_twos.make(render=False, worker_id=1)

env = make_vec_env(make_env, n_envs=4)  # Parallel environments

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_soccer/")

model.learn(total_timesteps=1_000_000)

model.save("ppo_soccer_twos")

model = PPO.load("ppo_soccer_twos")

obs = env.reset()
while True:
    action, _ = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()

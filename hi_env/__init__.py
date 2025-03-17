from gymnasium.envs.registration import register

register(
    id="hi-standup-v0",
    entry_point="hi_env.env:FRASAEnv",
)

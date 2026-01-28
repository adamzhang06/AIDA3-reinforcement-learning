import gymnasium as gym

# ! Create the FrozenLake environment with custom parameters
env = gym.make(
    'FrozenLake-v1',
    desc=None,
    map_name="4x4",
    is_slippery=True,
    success_rate=1.0/3.0,
    reward_schedule=(1, 0, 0),
    render_mode="human",
)

# ! Reset the environment to start a new episode
env.reset()
env.render()


# This just keeps the window open until you press Enter
input("Press Enter to close the window")



# ! Close the environment when done
env.close()
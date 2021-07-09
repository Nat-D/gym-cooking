import gym
import gym_cooking
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser("Overcooked 2 argument parser")

    # Environment
    parser.add_argument("--level", type=str, required=True)
    parser.add_argument("--num-agents", type=int, required=True)

    return parser.parse_args()

arglist = parse_arguments()
env = gym.make('overcookedEnv-v0', arglist=arglist)


obs = env.reset()
obs = env.step(action_dict={
	'agent-1': (0,0),
	'agent-2': (1,0)
	})
obs = env.step(action_dict={
    'agent-1': (0,1),
    'agent-2': (0,-1)
    })
obs = env.step(action_dict={
    'agent-1': (0,1),
    'agent-2': (0,0)
    })
obs = env.step(action_dict={
    'agent-1': (0,1),
    'agent-2': (0,0)
    })





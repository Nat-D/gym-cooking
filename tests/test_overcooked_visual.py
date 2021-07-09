import gym_cooking
import gym

import numpy as np
import cv2 
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser("Overcooked 2 argument parser")

    # Environment
    parser.add_argument("--level", type=str, default='open-divider_salad')
    parser.add_argument("--num-agents", type=int, default=2)
    
    return parser.parse_args()

arglist = parse_arguments()
env = gym.make('overcookedVisual-v0', arglist=arglist)


"""
img = cv2.cvtColor(obs, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (500, 500))
cv2.imshow('img', img) 
cv2.waitKey(100000)
"""

action_list = [(0,0), (1,0), (0,1), (-1,0), (0, -1)]
action_idx_list = [0, 1, 2, 3, 4]
done = False
obs = env.reset()

while not done:
     
    # display observation
    img = cv2.cvtColor(obs, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (500, 500))
    cv2.imshow('img', img) 
    cv2.waitKey(1)

    # select actions
    agent_1 = action_list[np.random.choice(action_idx_list)]
    agent_2 = action_list[np.random.choice(action_idx_list)]


    #take a step 
    obs, reward, done, info = env.step(action_dict={
                                        'agent-1':agent_1,
                                        'agent-2':agent_2
                                       })




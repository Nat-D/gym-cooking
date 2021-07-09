import pygame
import os
import numpy as np
from PIL import Image
from gym_cooking.misc.game.game import Game
import cv2

class GameImage(Game):
    def __init__(self, filename, world, sim_agents, record=False):
        Game.__init__(self, world, sim_agents)
        self.game_record_dir = 'misc/game/record/{}/'.format(filename)
        self.record = record


    def on_init(self):
        super().on_init()

        if self.record:
            # Make game_record folder if doesn't already exist
            if not os.path.exists(self.game_record_dir):
                os.makedirs(self.game_record_dir)

            # Clear game_record folder
            for f in os.listdir(self.game_record_dir):
                os.remove(os.path.join(self.game_record_dir, f))

    def get_image_obs(self, resize=False):
        self.on_render()
        img_int = pygame.PixelArray(self.screen)

        img_rgb = np.zeros([img_int.shape[1], img_int.shape[0], 3], dtype=np.uint8)
        for i in range(img_int.shape[0]):
            for j in range(img_int.shape[1]):
                color = pygame.Color(img_int[i][j])
                img_rgb[j, i, 0] = color[1]
                img_rgb[j, i, 1] = color[2]
                img_rgb[j, i, 2] = color[3]

        if resize:
            img_rgb = cv2.resize(img_rgb, (84,84), interpolation=cv2.INTER_LINEAR)

        return img_rgb

    def save_image_obs(self, t):
        self.on_render()
        pygame.image.save(self.screen, '{}/t={:03d}.png'.format(self.game_record_dir, t))

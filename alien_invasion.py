# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:08:53 2019

@author: tianyang.wen
"""


import pygame

from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象，窗口尺寸1200*800像素
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(ai_settings, screen)
    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        #每次循环时都重绘屏幕，用背景色填充屏幕
        gf.update_screen(ai_settings, screen, ship)
        
run_game()
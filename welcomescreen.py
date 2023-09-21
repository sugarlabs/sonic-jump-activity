#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sonic Jump
# Copyright (C) 2015  Utkarsh Tiwari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com


import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pickle
import pygame
import sys

from math import *

from random import *


'''
     
pygame.init()
sound=True
        
try:
    pygame.mixer.init()
except Exception, err:
    sound=False
    print 'error with sound', error
            
black=(0,0,0)
white=(255,255,255)
clock=pygame.time.Clock()
timer=pygame.time.Clock()
            
crashed=False   
disp_width = 600
disp_height = 600
            
press=0    
            
gameDisplay=pygame.display.get_surface()
        
if not(gameDisplay):
    info=pygame.display.Info()
    gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
    pygame.display.set_caption("Make Them Fall")
    #gameicon=pygame.image.load('data/images/icon.png')
    #pygame.display.set_icon(gameicon)

#back=pygame.image.load('background/back6.jpg')
fruitscore=0
'''


class welcomescreen:

    def __init__(self):
        self.step = 0
        self.showing_help = False

    def run(self, gameDisplay):

        pygame.init()
        sound = True

        try:
            pygame.mixer.init()
        except Exception as err:
            sound = False
            print('error with sound', err)

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        crashed = False
        press = 0

        info = pygame.display.Info()
        gameDisplay = pygame.display.get_surface()

        if not(gameDisplay):

            gameDisplay = pygame.display.set_mode(
                (info.current_w, info.current_h))

            pygame.display.set_caption("Sonic Jump")
            # gameicon=pygame.image.load('data/images/icon.png')
            # pygame.display.set_icon(gameicon)
        width = 490
        startx = (info.current_w - width) // 2
        endx = (info.current_w + width) // 2
        background = pygame.image.load("images/home-bg.jpg")
        background = pygame.transform.scale(background,
                                            (width, width * (800 // 480)))

        pillar_width = width // 5
        pillar_height = info.current_h // 3
        pillar = pygame.Rect(startx + width // 2 - pillar_width // 2,
                             info.current_h - pillar_height,
                             pillar_width, pillar_height)
        # fruit=pygame.transform.scale(fruit,(40,40))

        # scoreplate.set_alpha(100)

        sonic = pygame.image.load("images/sonic.png")

        font_path = "fonts/sans.ttf"
        font_size = 80
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/sans.ttf", 20)
        font3 = pygame.font.Font("fonts/sans.ttf", 40)
        font4 = pygame.font.Font("fonts/sans.ttf", 20)

        play = pygame.transform.scale(
            pygame.image.load("images/play.png"), (160, 60))

        help_btn_radius = (width * 13) // 100
        help_btn_color = (225, 225, 235)
        help_btn_text = font3.render("?", True, black)
        help_btn = pygame.Rect(startx + 13, 13,
                               help_btn_radius,
                               help_btn_radius)

        howtoplay = pygame.image.load("images/howtoplay.png")
        howtoplay = pygame.transform.scale(howtoplay, (width, info.current_h))

        buttonsound = pygame.mixer.Sound("sound/sound-button.ogg")

        sonic1 = pygame.image.load("images/sonic.png")
        sonic1_rect = sonic1.get_rect()
        sonic1 = pygame.transform.scale(sonic1,
                                        (50, 50 * (sonic1_rect.height // sonic1_rect.width)))
        sonic1 = pygame.transform.flip(sonic1, True, False)

        def get_sonic_pos():
            if abs(self.step) < width // 8:
                self.step += 3
            elif abs(self.step) < width // 4:
                self.step += 4
            else:
                self.step += 5
            if self.step < -width // 2 or self.step > width // 2:
                self.step = -width // 2
            x = startx + width // 2 + self.step - sonic1.get_rect().width // 2
            y = info.current_h - pillar.height - (abs(self.step) * 100) ** 0.5 - sonic1.get_rect().height
            return (x, y)

        while not crashed:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed = True

            mos_x, mos_y = pygame.mouse.get_pos()

            # print event

            gameDisplay.fill(white)
            gameDisplay.blit(background,
                             (startx, info.current_h - background.get_rect().height))

            pygame.draw.rect(gameDisplay, (61, 104, 255), pillar)

            gameDisplay.blit(sonic1, get_sonic_pos())

            scale_fac = info.current_h // 768
            gameDisplay.blit(pygame.transform.scale(
                sonic, (100, 150)), (startx + 70, 80 * scale_fac))

            gameDisplay.blit(play, (startx + 170, 280*scale_fac))

            head1 = font1.render("SONIC", 1, (black))
            gameDisplay.blit(head1, (startx + 170, 60*scale_fac))

            head2 = font1.render("JUMP", 1, (black))
            gameDisplay.blit(head2, (startx + 170, 130*scale_fac))

            # left and right black background patches
            pygame.draw.rect(gameDisplay, black, (0, 0, startx, info.current_h))
            pygame.draw.rect(gameDisplay, black, (endx, 0, startx, info.current_h))

            # Help Button
            hover_scaleup = 1.1 if help_btn.collidepoint(mos_x, mos_y) else 1
            help_text_rect = help_btn_text.get_rect()

            pygame.draw.circle(gameDisplay, help_btn_color,
                               help_btn.center,
                               int(help_btn.w * hover_scaleup // 2))

            help_txt_draw = pygame.transform.scale(help_btn_text,
                                                   (int(help_text_rect.w * hover_scaleup),
                                                    int(help_text_rect.h * hover_scaleup))) # if hovered, grow '?'

            help_text_rect = help_txt_draw.get_rect()
            gameDisplay.blit(help_txt_draw,
                            (help_btn.centerx - help_text_rect.w // 2,
                             help_btn.centery - help_text_rect.h // 2))

            # Hide help
            if self.showing_help and (pygame.mouse.get_pressed())[0] == 1 and press == 0:
                self.showing_help = False

            # Help Button Action
            if help_btn.collidepoint(mos_x, mos_y) and \
                    (pygame.mouse.get_pressed())[0] == 1 and \
                    press == 0 and not self.showing_help:
                self.showing_help = True

            # Play Button

            if play.get_rect(center=(startx + 170 + (play.get_width() // 2),
                                     280*scale_fac + (play.get_height() // 2))).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(play, (play.get_width() + 4, play.get_height() + 4)),
                                                        (startx + 170 - 2, 280*scale_fac - 2))
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0 and not self.showing_help:
                    buttonsound.play(0)
                    return

            # Show Help
            if self.showing_help:
                gameDisplay.blit(howtoplay, (startx, 0))

            pygame.display.update()
            clock.tick(60)

            if crashed == True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()


'''

if __name__ == "__main__":
    g = welcomescreen()
    g.make(gameDisplay)         
'''

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
import gtk
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
            
    #pygame.display.set_caption("Make Them Fall")
    #gameicon=pygame.image.load('data/images/icon.png')
    #pygame.display.set_icon(gameicon)

#back=pygame.image.load('background/back6.jpg')
fruitscore=0
score=0

'''






class scorescreen:

    def run(self,gameDisplay,score,scoreflag):
        
        pygame.init()
        sound=True
        
        try:
            pygame.mixer.init()
        except Exception, err:
            sound=False
            print 'error with sound', err
            
        black=(0,0,0)
        white=(255,255,255)
        clock=pygame.time.Clock()
        timer=pygame.time.Clock()
            
        crashed=False   
        disp_width = 600
        disp_height = 600
            
        press=0    
        
        info=pygame.display.Info()
        gameDisplay=pygame.display.get_surface()
        
        
        if not(gameDisplay):
            
            gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
            
            
        
        back=pygame.image.load("images/over.png")
        home=pygame.transform.scale(pygame.image.load("images/home.png"),(160,60))
        play=pygame.transform.scale(pygame.image.load("images/play.png"),(160,60))
        
        #herotr=hero
        
        
        #herotr=pygame.transform.scale(hero,(30,26))
        
        
        #hero1=pygame.image.load("images/hero1.png")
        
        font_path = "fonts/sans.ttf"
        font_size = 55
        font1= pygame.font.Font(font_path, font_size)
        font2=pygame.font.Font("fonts/sans.ttf",30)
        font3=pygame.font.Font("fonts/sans.ttf",30)
        font4=pygame.font.Font("fonts/sans.ttf",20)
        
        down=1
        bounce=0
        i=0
        red=(255,0,0)
        
        keypressflag=0
        
        
        maxscore=0
        
        
        
        with open('score.pkl', 'rb') as input:    #REading
            maxscore = pickle.load(input)
            
        
        
        buttonsound=pygame.mixer.Sound("sound/sound-button.ogg")
        
        
        
        
        
        
        
        # GAME LOOP BEGINS !!!
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            for event in pygame.event.get():
                #totaltime+=timer.tick()
                if event.type==pygame.KEYDOWN:
                    return 1
                if event.type == pygame.QUIT:
                    crashed=True
                    
                
                    
                
            #print "help"
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            #print event
            
            
                
            gameDisplay.fill(white)
            gameDisplay.blit(pygame.transform.scale(back,(490,768)),(350,0))
            
            
            
            
            
            
            
            
            scores=font2.render(str(score),1,black)
            
            
            
            gameDisplay.blit(scores,(560,250))
            
            if(scoreflag==1):
                maxscores=font2.render(str(maxscore)+"  NEW!",1,red)
            else:
                maxscores=font2.render(str(maxscore),1,black)
            
            
            gameDisplay.blit(maxscores,(560,325))
            
            
            
            gameDisplay.blit(home,(430,450))
            
            gameDisplay.blit(play,(620,450))
            
            
            
            # GAME START
            
            
            
            
            # Home button
            
            if home.get_rect(center=(430+(home.get_width()/2),450+(home.get_height()/2))).collidepoint(mos_x,mos_y):
                gameDisplay.blit(pygame.transform.scale(home,(home.get_width()+4,home.get_height()+4)),(430-2,450-2))
                
                if(pygame.mouse.get_pressed())[0]==1 and press==0:
                    buttonsound.play(0)
                    return 0
                
                
                
            
            
            # Play Button
            
            if play.get_rect(center=(620+(play.get_width()/2),450+(play.get_height()/2))).collidepoint(mos_x,mos_y):
                gameDisplay.blit(pygame.transform.scale(play,(play.get_width()+4,play.get_height()+4)),(620-2,450-2))
                
                if(pygame.mouse.get_pressed())[0]==1 and press==0:
                    
                    buttonsound.play(0)
                    return 1
                
                
                 
            
            
            
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==273 :
                    buttonsound.play(0)
                    return 1
            
            
            #left and right black background patches
                      
            pygame.draw.rect(gameDisplay,black,(0,0,350,768))    
                    
            pygame.draw.rect(gameDisplay,black,(840,0,693,768))
            
            
            
            
            
            
            
            
            
            pygame.display.update()
            clock.tick(60)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
     
     
     
     
        # Just a window exception check condition

        event1=pygame.event.get()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()



'''


if __name__ == "__main__":
    g = scorescreen()
    g.make(gameDisplay,score)         

'''

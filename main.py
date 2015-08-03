#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Stick Hero
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


from pygame.locals import *












class game:

    def make(self):
        
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
            
            
            pygame.display.set_caption("Stick Hero")
            #gameicon=pygame.image.load('images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        sprite=pygame.image.load("images/sprite.png")
        
        #herotr=hero
        #herotr=pygame.transform.scale(hero,(30,26))
        
        
        
        
        
        
        #pillarlist=[alpha,beta,gamma,delta]
        
        
        # Sound loads
        
        
        
        #pop1=pygame.mixer.Sound("sound/pop_1.ogg")
        
        
        
        
        font_path = "fonts/comicsans.ttf"
        font_size = 40
        font1= pygame.font.Font(font_path, font_size)
        font2=pygame.font.Font("fonts/sans.ttf",25)
        font3=pygame.font.Font("fonts/sans.ttf",40)
        font4=pygame.font.Font("fonts/sans.ttf",20)
        
        
        
        
        
        # VARIABLE INITIALIZATION
        
        
        herod=33
        
        fruitscore=0
        score=0
        
        
        #running  7 sprites
        
        running=[[8,11],[50,7],[93,9],[137,9]]
        
        runningwd=[[40,33],[41,37],[39,36],[40,33]]
        
        
        stop=[[184,10],[215,8],[249,10]]
        stopwd=[[27,34],[27,35],[24,32]]
        
        
        #jumping 15 sprites
        
        jumping=[[10,55],[39,59],[64,54],[95,58],[122,57],[156,57],[187,57],[218,58],[249,57],[284,54],[321,51],[355,51],[390,63],[427,65],[473,67]]
        
        jumpingwd=[[23,38],[23,22],[26,32],[24,25],\
            [29,26],[26,27],[26,29],[24,24],[30,26],[26,32],[26,37],[30,37],[29,32],[28,29],[24,26]]
        
        
    
                    
        
        
        
        
        
        
        
        
        
        
        if os.path.getsize("score.pkl") == 0:
            
            with open('score.pkl', 'wb') as output:
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)
        
        
        with open('score.pkl', 'rb') as input:    #REading
            fruitscore = pickle.load(input)
            fruitscore=pickle.load(input)
        
        
        i=0
        
        j=0
        k=0
        
        
        
        
        #lastpillardist=pillar2x-457
        
        
        # GAME LOOP BEGINS !!!
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            for event in pygame.event.get():
            #totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed=True
                
            
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            #print "hello"
            
                
            gameDisplay.fill(white)
            
                    
            #gameDisplay.blit(sprite,(350,50))
            
            
            
            
            
            i+=1
            
            if(i>50):
                i=0
                
                
            if(i%5==0):
                k+=1
                if(k>=4):
                    k=0
                
            
            
            

            SPRT_RECT_X=4 
            SPRT_RECT_Y=67  
            #This is where the sprite is found on the sheet

            LEN_SPRT_X=24
            LEN_SPRT_Y=33
            #This is the length of the sprite

            #screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y)) #Create the screen
            
            sprite.set_clip(pygame.Rect(running[k][0], running[k][1],runningwd[k][0], runningwd[k][1])) #Locate the sprite you want
            draw_me = sprite.subsurface(sprite.get_clip()) #Extract the sprite you want

            #backdrop = pygame.Rect(0,0,350,768) #Create the whole screen so you can draw on it

            gameDisplay.blit(draw_me,(355,422)) #'Blit' on the backdrop
            #pygame.display.flip()
            
            
            
            
            
            
            
            
            
            
                      
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
            

if __name__ == "__main__":
    g = game()
    g.make()         

            
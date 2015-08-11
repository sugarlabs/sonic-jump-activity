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






class welcomescreen:

    def make(self,gameDisplay):
        
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
            
            
            pygame.display.set_caption("Sonic Jump")
            #gameicon=pygame.image.load('data/images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        back=pygame.image.load("images/welcome.png")
        #fruit=pygame.transform.scale(fruit,(40,40))
        
       
        #scoreplate.set_alpha(100)
        
        
        
        
        
        
        
        
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
            
            #print event
            
            
                
            
                
            gameDisplay.fill(white)
            #gameDisplay.blit(back,(350,0))
            
            
            
            
            
            
            '''
           
            
            if fruit.get_rect(center=(790+20,20+20)).collidepoint(mos_x,mos_y):
                if(pygame.mouse.get_pressed())[0]==1 and press==0:
                    
                    gameDisplay.blit(scoreplate,(780,40))
                    #gameDisplay.blit(scoreplate,(780,60))
                    
                    head1=font2.render(str(fruitmaxscore),1,(white)) 
                    gameDisplay.blit(head1,(785,60))
                        
                      
                
                
                
                if event.type==pygame.MOUSEBUTTONUP:
                    press=0
            
            
            
            # GAME START
            
            if play.get_rect(center=(510+85,200+bounce+85)).collidepoint(mos_x,mos_y):
                if(pygame.mouse.get_pressed())[0]==1 and press==0:
                    
                    return 2
                
                
              
            
            
            
            '''
            
            #gameDisplay.blit(fruit,(780,20))
            
            #head1=font1.render("SONIC",1,(black)) 
            #gameDisplay.blit(head1,(500,20))
            
            
            #head2=font1.render("JUMP",1,(black)) 
            #gameDisplay.blit(head2,(510,80))
            
            
            
            
            
            #left and right black background patches
                      
            pygame.draw.rect(gameDisplay,black,(0,0,350,768))    
                    
            pygame.draw.rect(gameDisplay,black,(840,0,693,768))
            
            
            #print "hello"
            
            
            
            
            
            
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
    g = welcomescreen()
    g.make(gameDisplay)         

            
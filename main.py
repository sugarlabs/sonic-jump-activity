#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sonic Thief
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
        
        
        
        color=[(153,50,204),(255,105,180),(255,215,0),(0,255,127),(30,144,255),(255,69,0)]
        
        
        
        
        # VARIABLE INITIALIZATION
        
        
        herod=33
        
        fruitscore=0
        score=0
        
        
        #running  7 sprites
        
        running=[[8,11],[50,7],[93,9],[137,9]]
        
        runningwd=[[40,33],[41,37],[39,36],[40,33]]
        
        
        stops=   [10,55]
        stopwd= [23,38]
        
        
        #jumping 15 sprites
        
        jumping=[[39,59],[64,54],[95,58],[122,57],[156,57],[187,57],\
            [218,58],[249,57]]
        
        jumpingwd=[[23,22],[26,32],[24,25],\
            [29,26],[26,27],[26,29],[24,24],[30,26]]
        
        falls=[[284,54],[321,51],[355,51]]
        
        fallswd=[[26,32],[26,37],[30,37]]
        
        touchs=[[390,63],[427,65],[473,67]]
        touchswd=[[29,32],[28,29],[24,26]]
        
        
        
    
                    
        
        
        
        
        
        
        
        
        
        
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
        
        keyinit=0
        
        
        run=1
        jump=stop=0
        
        fall=touch=0
        
        r=s=j=0
        
        frame=5     # FRame rate
        
        
        sonicy=410
        
        inity=410
        velocity=0
        distance=150
        
        time=0
        fall=0
        down=0
        flag1=0
        
        
        f=t=0
        
        
        
        
        jumpf=fallf=stopf=0   
        
        accf=10
        
        
        
        initialvelocity=10
        
        #distance=(initialvelocity**2)/(2*10)
        
        timefactor=0.03
        
        step=0
        
        velocity=10
        
        
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
                
            
            
            
                
            if(run==1):
                if(i%frame==0):    
                    r+=1
                    if(r>=4):
                        r=0
            
            
                
            elif(jump==1):
                if(i%frame==0):
                    j+=1
                    if(j>=8):
                        j=0
                        
                        
            elif(fall==1):
                if(i%frame==0):
                    if(f<2):
                        f+=1
                        
                        
            elif(touch==1):
                if(i%frame==0):
                    if(t<2):
                        t+=1
                    
                        
                        
                        
                        
                        
            
            
            
            
            
            if(stopf==1 or jumpf==1):
                time+=1
                if(time>2):
                    jump=1
                    stop=0
                    #keyinit=0
                
                velocity=initialvelocity-(accf*(time/18))
                
                #print (accf*(time/100))
                sonicy-=velocity
                
                
            
            if(fallf==1):
                
                time+=1
                if(time>5):
                    fall=1
                    jump=0
                velocity=accf*(time/18)
                sonicy+=velocity
            
            
            
            #print velocity
            
            
            pygame.draw.circle(gameDisplay,black, (352,260) ,3, 3)
            
            '''
            if(sonicy<=(inity-distance) and (jumpf==1 or stopf==1) and flag1==0):
                fallf=1
                jumpf=0
                stopf=0
                
                
                time=0
                flag1=1
            '''
            
            if(velocity<=0 and flag1==0):
                fallf=1
                jumpf=0
                stopf=0
                
                time=0
                flag1=1
            
            
            
            
                
            #Keyboard Hit check
            
            
            if event.type==pygame.KEYDOWN and event.key==273 and keyinit==0 and step<2 :
                
                keyinit=1
               
                #print "hl"
                #print step
                
                
                if(step==0):    #First jump     
                    run=0
                    stopf=1
                    stop=1
                    
                    
                elif(step==1):      #Second Jump
                    jump=1
                    jumpf=1
                    fallf=0
                    flag1=0
                    #time=0
                    #inity=sonicy
                    initialvelocity=-velocity
                    #distance=distance/2
                    
                
                step+=1
                
                
                
                
                
                
                #print "help"
                
                
                            
            if event.type==pygame.KEYUP  and event.key==273 and keyinit==1:
                keyinit=0
                    
                #stickgrow.stop()
                #kick.stop()
                #kick.play()
                
            
            #print stop
                    
            
            
            if(run==1):
                
                sprite.set_clip(pygame.Rect(running[r][0], running[r][1],\
                    runningwd[r][0], runningwd[r][1])) 
            
            
            
            elif(stop==1):
                sprite.set_clip(pygame.Rect(stops[0], stops[1],\
                stopwd[0], stopwd[1])) 
            
            
              
            
            elif(jump==1):
                sprite.set_clip(pygame.Rect(jumping[j][0], jumping[j][1],\
                jumpingwd[j][0], jumpingwd[j][1]))
                
                
                
            elif(fall==1):
                sprite.set_clip(pygame.Rect(falls[f][0], falls[f][1],\
                fallswd[f][0], fallswd[f][1]))     
                
            
            elif(touch==1):
                sprite.set_clip(pygame.Rect(touchs[t][0], touchs[t][1],\
                touchswd[t][0], touchswd[t][1])) 
                
                
                
                
            # Colored Pillars Disp    
            
            
            
            pygame.draw.rect(gameDisplay,color[3],(350,454,490,768))
            
            
            
            #  Sonic Display
            
            

            draw_me = sprite.subsurface(sprite.get_clip()) #Extract the sprite you want

            #backdrop = pygame.Rect(0,0,350,768) #Create the whole screen so you can draw on it

            gameDisplay.blit(pygame.transform.scale(draw_me,\
                
            (draw_me.get_width()+10,draw_me.get_height()+10)),(355,sonicy)) #'Blit' on the backdrop
            
            
            
            
            
            
            
            # BLACK RECTANGLES DISPLAY
                      
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

            
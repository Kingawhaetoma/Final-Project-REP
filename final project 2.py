# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:13:20 2024

@author: kinga
"""

import pygame
import simpleGE


class Guy1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("guy1.png")
        self.setSize(50, 50)
        self.position = (50, 400)
        self.inAir = True
        
           
    def process(self):
        if self.inAir:
            self.addForce(.2, 270)
        
        if self.y > 450:
            self.inAir = False
            self.y = 450
            self.dy = 0          
        
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5   
        if self.scene.isKeyPressed(pygame.K_SPACE):
            if not self.inAir:
                self.addForce(6, 90)
                self.inAir = True

        self.inAir = True
        for platform in self.scene.platforms:
            if self.collidesWith(platform):                
                if self.dy > 0:
                        self.bottom = platform.top
                        self.dy = 0
                        self.inAir = False
        
class Platform(simpleGE.Sprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position = (position)
        self.setImage("platform.png")
        #self.setSize(50, 15)
       
    def update(self):
        super().update()
        if self.mouseDown:
            self.position = pygame.mouse.get_pos()

class Exit(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("exit.png")
        self.setSize(60, 60)  # Adjust the size of the exit image as needed
        self.position = (600, 40)  # Adjust the position as needed
        
        
        
class StartButton(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("start_btn.png")
        self.setSize(110, 70)
        self.position = (200, 250)
    
     

class ExitButton(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("exit_btn.png")
        self.setSize(110, 70)
        self.position = (500, 250)

class IntroPage(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("plainField.png")
        self.StartButton = StartButton(self)
        self.ExitButton = ExitButton(self)
        self.sprites = [self.StartButton, self.ExitButton]

    def process(self):
        if self.StartButton.clicked:
            self.response = "play"
            self.stop()
            
        elif self.ExitButton.clicked:
             self.response = "quit"
             self.quit()
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("sky.png")
        
        self.guy1 = Guy1(self)
        
        
        self.platforms = [Platform(self, (150, 450)),
                          Platform(self, (270, 450)),
                          Platform(self, (300, 350)),
                          Platform(self, (300, 460)),
                          Platform(self, (350, 350)),
                          Platform(self, (400, 470))
]
        self.exit = Exit(self)  # Instantiate the exit sprite      
        self.sprites = [self.platforms, self.guy1, self.exit] 
        # Add the exit sprite to the list of sprites

class Instruction(simpleGE.Scene):
    def __init__(self, scene):
        super().__init__()
        self.setImage("plainField.png")


def main():
    keepGoing = True
    while keepGoing:
        
        game = IntroPage()
        game.start()

        if game.response == "Play":
            pass
    
        if game.response == "Quit":
            keepGoing = False
        
    
    
if __name__ == "__main__":
    main()
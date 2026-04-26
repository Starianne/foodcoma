import pygame
from random import randint

class Flipping:
    def __init__(self, screen, clock):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen
        self.clock = clock
        self.dt = 0

        self.flip_meter_surface1 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect1 = self.flip_meter_surface1.get_rect(center = (4*self.screen_width/5, self.screen_height/10))
        self.flip_meter_surface2 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect2 = self.flip_meter_surface2.get_rect(center = (4*self.screen_width/5, self.screen_height/10))
        self.flip_meter_surface3 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect3 = self.flip_meter_surface3.get_rect(center = (4*self.screen_width/5, self.screen_height/10))
        self.flip_meter_surface4 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect4 = self.flip_meter_surface4.get_rect(center = (4*self.screen_width/5, self.screen_height/10))

        self.flip_meter = [self.flip_meter_surface1, self.flip_meter_surface2, self.flip_meter_surface3, self.flip_meter_surface4, self.flip_meter_rect1, self.flip_meter_rect2, self.flip_meter_rect3, self.flip_meter_rect4]



    def check_match(self):
        #i want to 
        pass

    def set_flip_height(self):
        flip_height = randint(1,4)
        self.screen.blit(self.flip_meter[flip_height], self.flip_meter[flip_height*2])


    def run(self):
        
        self.screen.fill("#DCD6F7")
        events = pygame.events.get
        #i need to go through 15 randomly generated intervals of pancake flipping heights, mapped to 1234
        #i need to have 
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == 1:
                    pass

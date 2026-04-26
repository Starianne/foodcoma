import pygame
from random import randint
from stacking import Stacking

class Flipping:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.dt = 0
        self.running = True
        self.completed = False
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.flip_meter_surface1 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect1 = self.flip_meter_surface1.get_rect(center = (4*self.screen_width/5, self.screen_height/10))
        self.flip_meter_surface2 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect2 = self.flip_meter_surface2.get_rect(center = (4*self.screen_width/5, self.screen_height/10))
        self.flip_meter_surface3 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect3 = self.flip_meter_surface3.get_rect(center = (4*self.screen_width/5, self.screen_height/10))
        self.flip_meter_surface4 = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.flip_meter_rect4 = self.flip_meter_surface4.get_rect(center = (4*self.screen_width/5, self.screen_height/10))

        self.flip_meter_surfaces = [self.flip_meter_surface1, self.flip_meter_surface2, self.flip_meter_surface3, self.flip_meter_surface4]
        self.flip_meter_rects = [self.flip_meter_rect1, self.flip_meter_rect2, self.flip_meter_rect3, self.flip_meter_rect4]

    def set_flip_height(self):
        self.flip_height = randint(1,4)
        self.screen.blit(self.flip_meter[self.flip_height-1], self.flip_meter[self.flip_height-1])

    def check_match(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.key.key_code(f"{self.flip_height}"):
                    return True




    def run(self):
        while self.running:
            self.screen.fill("#DCD6F7")
            events = pygame.event.get()

            for i in range(1,16):
                passed = False
                while not passed:
                    passed = self.check_match(events)

            self.completed = True
            self.running = False

        if self.completed:
            stacking = Stacking(self.screen, self.clock)
            stacking.run()

            
                        


import pygame
from random import randint
from stacking import Stacking

class Flipping:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.completed = False
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.flip_height = 0
        self.flips_done = 0
        self.total_flips = 20
        self.waiting_for_input = False

        self.text_font = pygame.font.Font('assets/font/MADETommySoftBoldPERSONALUSE.otf', size=60)
        self.hint_surface = self.text_font.render('Flip the pancakes to the right height!', False, (230, 96, 110))
        self.hint_rect = pygame.Surface.get_rect(self.hint_surface)

        self.pan_surface = pygame.image.load('assets/imgs/Frypan.png').convert_alpha() 
        self.transformed_pan = pygame.transform.scale_by(self.pan_surface, 0.05) 
        self.current_key_pressed = None
        


        self.flip_meter_surfaces = [
            pygame.image.load('assets/imgs/25%_individual.png').convert_alpha(),
            pygame.image.load('assets/imgs/50%_individual.png').convert_alpha(),
            pygame.image.load('assets/imgs/75%_individual.png').convert_alpha(),
            pygame.image.load('assets/imgs/100%_individual.png').convert_alpha(),
        ]

        self.cloud_centers = [
        (4*self.screen_width/5, 8*self.screen_height/10),  #cloud centers 
        (4*self.screen_width/5, 6*self.screen_height/10),  
        (4*self.screen_width/5, 4*self.screen_height/10),  
        (4*self.screen_width/5, 2*self.screen_height/10),  
        ]

        

        self.flip_meter_rects = [
            surf.get_rect(center=(4*self.screen_width/5, self.screen_height/10))
            for surf in self.flip_meter_surfaces
        ]

        # Number key map
        self.key_map = {
            1: pygame.K_1,
            2: pygame.K_2,
            3: pygame.K_3,
            4: pygame.K_4,
        }

        self.set_flip_height()

    def set_flip_height(self):
        self.flip_height = randint(1, 4)
        self.waiting_for_input = True

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    for num, key in self.key_map.items():
                        if event.key == key:
                            self.current_key_pressed = num
                            
                    if self.waiting_for_input:
                        if event.key == self.key_map[self.flip_height]:
                            self.flips_done += 1
                            print(f"Correct! Flip {self.flips_done}/{self.total_flips}")

                            if self.flips_done >= self.total_flips:
                                self.completed = True
                                self.running = False
                            else:
                                self.set_flip_height()  #Next flip

            self.screen.fill("#DCD6F7")

            idx = self.flip_height - 1  #used for the flip meter

            if self.current_key_pressed is not None:
                pan_idx = self.current_key_pressed - 1
                pan_rect = self.transformed_pan.get_rect(center=self.cloud_centers[pan_idx])
                self.screen.blit(self.transformed_pan, pan_rect)  #goes to cloud
                

            transformed_current_flip = pygame.transform.scale_by(self.flip_meter_surfaces[idx], 0.3)
            transformed_current_flip_rect = transformed_current_flip.get_rect(center=(3*self.screen_width/4, self.screen_height/2))
            self.screen.blit(transformed_current_flip, transformed_current_flip_rect)
                
            self.screen.blit(self.hint_surface, self.hint_rect)

            pygame.display.flip()
            self.clock.tick(60)

        if self.completed:
            print("Go to stacking")
            stacking = Stacking(self.screen, self.clock)
            stacking.run()
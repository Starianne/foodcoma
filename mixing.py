import pygame

from flipping import Flipping

class Mixing:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.completed = False 

        self.rotations = 0

        self.maxrotations = 15

        self.font = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50)
        self.first_image = pygame.image.load('assets/imgs/mixingbowl_empty.png').convert_alpha()
        self.first_image = pygame.transform.scale(self.first_image, (self.first_image.get_width() * 0.25, self.first_image.get_height() * 0.25))
        self.second_image = pygame.image.load('assets/imgs/Mixing_mix.png').convert_alpha()
        self.second_image = pygame.transform.scale(self.second_image, (self.second_image.get_width() * 0.25, self.second_image.get_height() * 0.25))
        self.third_image = pygame.image.load('assets/imgs/mixingbowl_full.png').convert_alpha()
        self.third_image = pygame.transform.scale(self.third_image, (self.third_image.get_width() * 0.25, self.third_image.get_height() * 0.25))
        self.spoon_image = pygame.image.load('assets/imgs/mixingspoon.png').convert_alpha()
        self.spoon_image = pygame.transform.scale(self.spoon_image, (self.spoon_image.get_width() * 0.25, self.spoon_image.get_height() * 0.25))
        self.text_surface = self.font.render("Mix, Mix, Mix the Batter!!!", True, (0, 0, 0))
        self.text_encouragement = self.font.render("Keep Mixing!!!", True, (0, 0, 0))
        self.text_final = self.font.render("You're almost there!", True, (0, 0, 0))

                
    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events: 
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_5:
                        print("up")
                        self.rotations += 1
                    elif event.key == pygame.K_6:
                        print("right")
                        self.rotations += 1
                    elif event.key == pygame.K_7:
                        print("down")
                        self.rotations += 1
                    elif event.key == pygame.K_8:
                        print("left")
                        self.rotations += 1
   
            self.screen.fill("#DCD6F7")
            self.screen.blit(self.text_surface, (self.screen.get_width()//2 - self.text_surface.get_width()//2, self.screen.get_height()//4 - self.text_surface.get_height()//2))

            if self.rotations < 5: 
                self.screen.blit(self.first_image, (self.screen.get_width()//2 - self.first_image.get_width()//2, self.screen.get_height()//2 - self.first_image.get_height()//2))
                self.screen.blit(self.spoon_image, (self.screen.get_width()//2 - self.spoon_image.get_width()//2, self.screen.get_height()//2 - self.spoon_image.get_height()//2))
            elif self.rotations < 12:
                self.screen.blit(self.second_image, (self.screen.get_width()//2 - self.second_image.get_width()//2, self.screen.get_height()//2 - self.second_image.get_height()//2))
                self.screen.blit(self.spoon_image, (self.screen.get_width()//2 - self.spoon_image.get_width()//2, self.screen.get_height()//2 - self.spoon_image.get_height()//2))
                self.screen.blit(self.text_encouragement, (self.screen.get_width()//2 - self.text_encouragement.get_width()//2, self.screen.get_height()//1.5 - self.text_encouragement.get_height()//2))
            else:
                self.screen.blit(self.third_image, (self.screen.get_width()//2 - self.third_image.get_width()//2, self.screen.get_height()//2 - self.third_image.get_height()//2))
                self.screen.blit(self.spoon_image, (self.screen.get_width()//2 - self.spoon_image.get_width()//2, self.screen.get_height()//2 - self.spoon_image.get_height()//2))
                self.screen.blit(self.text_final, (self.screen.get_width()//2 - self.text_final.get_width()//2, self.screen.get_height()//1.5 - self.text_final.get_height()//2))
            if self.rotations >= self.maxrotations:
                self.completed = True
                self.running = False
                

            pygame.display.flip()
            self.clock.tick(60)
        
        self.results = self.rotations
        if self.completed:
            flipping = Flipping(self.screen, self.clock)
            flipping.run()
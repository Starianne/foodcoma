import pygame

from flipping import Flipping

class Mixing:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.completed = False 

        self.rotations = 0

        self.maxrotations = 40

        self.font = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50)
        self.first_image = pygame.image.load('assets/imgs/first.png').convert_alpha()
        self.second_image = pygame.image.load('assets/imgs/second.png').convert_alpha()
        self.third_image = pygame.image.load('assets/imgs/third.png').convert_alpha()

                
    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events: 
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.rotations += 1
                        print("Up key pressed")
                    elif event.key == pygame.K_RIGHT:
                        self.rotations += 1
                        print("Right key pressed")
                    elif event.key == pygame.K_DOWN:
                        print("Down key pressed")
                        self.rotations += 1
                    elif event.key == pygame.K_LEFT:
                        print("Left key pressed")
                        self.rotations += 1
   
            self.screen.fill("#DCD6F7")
            text = "Make the Batter!!!"
            if self.rotations < 15: 
                self.screen.blit(self.first_image, (self.screen.get_width()//2 - self.first_image.get_width()//2, self.screen.get_height()//2 - self.first_image.get_height()//2))
            elif self.rotations < 30:
                self.screen.blit(self.second_image, (self.screen.get_width()//2 - self.second_image.get_width()//2, self.screen.get_height()//2 - self.second_image.get_height()//2))
            else:
                self.screen.blit(self.third_image, (self.screen.get_width()//2 - self.third_image.get_width()//2, self.screen.get_height()//2 - self.third_image.get_height()//2))

            if self.rotations >= self.maxrotations:
                self.completed = True
                self.running = False
                
            pygame.display.flip()
            self.clock.tick(60)
        
        self.results = self.rotations
        if self.completed:
            flipping = Flipping(self.screen, self.clock)
            flipping.run()
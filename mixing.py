import pygame
import flipping import Flipping 
class Mixing:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.completed = False 

        self.rotations = 0
        self.input_sequence = []

        self.clockwise = ['up', 'right', 'down', 'left']
        self.maxrotations = 5

        self.font = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50)
        self.first_image = pygame.image.load('assets/imgs/nicheapple.jpg').convert_alpha()

    def check_rotation(self):
        last4 = self.input_sequence[-4:]

        for i in range(4):
            if last4 == self.clockwise[i:] + self.clockwise[:i]:
                if self.rotations < self.maxrotations:
                    self.rotations += 1
                    print(f"Rotation {self.rotations} detected!")
                    if self.rotations >= self.maxrotations:
                        self.completed = True
                        self.running = False 
                self.input_sequence = []
                return
                
    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events: 
                print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.input_sequence.append('up')
                    elif event.key == pygame.K_RIGHT:
                        self.input_sequence.append('right')
                    elif event.key == pygame.K_DOWN:
                        self.input_sequence.append('down')
                    elif event.key == pygame.K_LEFT:
                        self.input_sequence.append('left')
            
            if len(self.input_sequence) >= 4:
                self.check_rotation()
            

            self.screen.fill("#da7676")
            text = "Make the Batter!!!"
            self.screen.blit(self.first_image, (self.screen.get_width()//2 - self.first_image.get_width()//2, self.screen.get_height()//2 - self.first_image.get_height()//2))


            pygame.display.flip()
            self.clock.tick(60)
        
        self.results = self.rotations
        if self.completed:
            flipping = Flipping(self.screen, self.clock)
            flipping.run()
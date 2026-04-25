import pygame

class Mixing:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.completed = False 

        self.rotations = 0
        self.input_sequence = []

        self.closewise = ['up', 'right', 'down', 'left']
        self.maxrotations = 20

        self.font = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50)

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
                if event.type == pygame.K_UP:
                    self.input_sequence.append('up')
                elif event.type == pygame.K_RIGHT:
                    self.input_sequence.append('right')
                elif event.type == pygame.K_DOWN:
                    self.input_sequence.append('down')
                elif event.type == pygame.K_LEFT:
                    self.input_sequence.append('left')
            
            if len(self.input_sequence) >= 4:
                self.check_rotation()
            

            self.screen.fill("#da7676")
            text = "Make the Batter!!!"
            font = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50)


            pygame.display.flip()
            self.clock.tick(60)
        
        self.results = self.rotations
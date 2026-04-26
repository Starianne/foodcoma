import pygame

class Stacking:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.completed = False

#timer + combos
    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill("#E6A4AB")
            pygame.display.flip()
            self.clock.tick(60)

        if self.completed:
            return self.completed
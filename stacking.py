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

        if self.completed:
            return self.completed
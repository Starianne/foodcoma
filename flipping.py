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
        self.total_flips = 15
        self.waiting_for_input = False

        self.flip_meter_surfaces = [
            pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha(),
            pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha(),
            pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha(),
            pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha(),
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

                if event.type == pygame.KEYDOWN and self.waiting_for_input:
                    if event.key == self.key_map[self.flip_height]:
                        self.flips_done += 1
                        print(f"Correct! Flip {self.flips_done}/{self.total_flips}")

                        if self.flips_done >= self.total_flips:
                            self.completed = True
                            self.running = False
                        else:
                            self.set_flip_height()  # Next flip

            self.screen.fill("#DCD6F7")

            # Draw the current flip meter image
            idx = self.flip_height - 1
            self.screen.blit(self.flip_meter_surfaces[idx], self.flip_meter_rects[idx])

            pygame.display.flip()
            self.clock.tick(60)

        if self.completed:
            stacking = Stacking(self.screen, self.clock)
            stacking.run()
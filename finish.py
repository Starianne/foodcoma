import pygame

from main import Game

class Finish:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.text_success = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50).render("Congratulations! You've made the perfect pancake!", True, (0, 0, 0))
        
    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("#DCD6F7")
            self.screen.blit(self.text_success, (self.screen.get_width()//2 - self.text_success.get_width()//2, self.screen.get_height()//2 - self.text_success.get_height()//2))

    
            # You can add any end game screen elements here, such as a "Game Over" message or final score display.

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
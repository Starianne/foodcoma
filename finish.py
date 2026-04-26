import pygame

from main import Game

class Finish:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.status = True #True = success, False = fail

        self.text_success = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50).render("Congratulations! You've made the perfect pancake!", True, (0, 0, 0))
        self.text_fail = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50).render("You burnt the pancakes!!", True, (0, 0, 0))
        
        self.sleeping_image = pygame.image.load('assets/imgs/Bunny_sleeping.png').convert_alpha()
        self.angry_image = pygame.image.load('assets/imgs/Angry_Bunny.png').convert_alpha()

        self.pancakes_image = pygame.image.load('assets/imgs/pancakes.png').convert_alpha()
        self.fryingpan_image = pygame.image.load('assets/imgs/Frypan.png').convert_alpha()
    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("#DCD6F7")
            self.screen.blit(self.text_success, (self.screen.get_width()//2 - self.text_success.get_width()//2, self.screen.get_height()//2 - self.text_success.get_height()//2))

    
            # You can add any end game screen elements here, such as a "Game Over" message or final score display.

            
            if self.status == True:
                self.screen.blit(self.sleeping_image, (self.screen.get_width()//2 - self.sleeping_image.get_width()//2, self.screen.get_height()//1.5 - self.sleeping_image.get_height()//2))
                self.screen.blit(self.pancakes_image, (self.screen.get_width()//2 - self.pancakes_image.get_width()//2, self.screen.get_height()//1.5 - self.pancakes_image.get_height()//2 + 100))
            else:
                self.screen.blit(self.angry_image, (self.screen.get_width()//2 - self.angry_image.get_width()//2, self.screen.get_height()//1.5 - self.angry_image.get_height()//2))
                self.screen.blit(self.pancakes_image, (self.screen.get_width()//2 - self.pancakes_image.get_width()//2, self.screen.get_height()//1.5 - self.pancakes_image.get_height()//2 + 100))

            
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
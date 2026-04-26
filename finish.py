import pygame


class Finish:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.text_success = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50).render("Congratulations! You've made the perfect pancake!", True, (0, 0, 0))
        self.text_again = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf', 50).render("Press SPACE to play again", True, (0, 0, 0))
        
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    from mixing import Mixing  
                    mixing = Mixing(self.screen, self.clock)
                    mixing.run()
                    
                        

            self.screen.fill("#DCD6F7")
            self.screen.blit(self.text_success, (self.screen.get_width()//2 - self.text_success.get_width()//2, self.screen.get_height()//2 - self.text_success.get_height()//2))

    
            # You can add any end game screen elements here, such as a "Game Over" message or final score display.

            self.screen.blit(self.text_again, (self.screen.get_width()//2 - self.text_again.get_width()//2, self.screen.get_height()//2 + 100))
            self.screen.blit(self.pancakes_image, (self.screen.get_width()//2 - self.pancakes_image.get_width()//2, self.screen.get_height()//1.5 - self.pancakes_image.get_height()//2 + 100))

            
            pygame.display.flip()
            self.clock.tick(60)

        self.running = False
import pygame
import os
import asyncio

from mixing import Mixing

#buttons to be used in game
class Button:
    def __init__(self, x, y, width, height, font, text='Button', screen=None):
        #ordered to match main.py buttons
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.screen = screen

        #use in function later? putting them here for now
        self.fill_colors = {
            'normal': "#E6A4AB",
            'hover': "#E6606E",
            'pressed': '#6988E0',
        }

        self.surface = pygame.Surface((width, height))
        self.padding = 12
        self.text_lines = self.wrap_text(self.text, (self.rect.width - self.padding * 2))
        self.text_surfs = [
            self.font.render(line.strip(), True, "white")
            for line in self.text_lines 
        ]


    def wrap_text(self, text, max_width):
        words = text.split(" ") #splits text into array with words
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + (" " if current_line != "" else "") + word #ternary operators might be the goat
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else: 
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines
    


    def draw(self, is_selected=False):

        color = self.fill_colors['hover'] if is_selected else self.fill_colors['normal']
        self.surface.fill(color)

        if self.text_surfs:
            total_text_height = sum(surf.get_height() for surf in self.text_surfs)
            start_y = (self.surface.get_height() - total_text_height) // 2

            for surf in self.text_surfs:
                text_rect = surf.get_rect(centerx = self.surface.get_width() // 2, y = start_y)
                self.surface.blit(surf, text_rect)
                start_y += surf.get_height()


        if self.screen:

            self.screen.blit(self.surface, self.rect)     

    def select(self, events):
        for event in events:  
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                self.button_select = (self.button_select + 1) % 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                self.button_select = (self.button_select - 1) % 2
        self.draw(self.titlebuttons[self.button_select], self.fill_colors['hover'])
        

#in a class so that incase later it needs to be web playable I can make it use asyncio + pybag quicker
class Game:
    def __init__(self):
        pygame.init()

        #setting up screen 
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        #getting clock and setting running variable 
        self.clock = pygame.time.Clock()
        self.running = True

        #used to iterate through button selection on screens
        self.button_select = 0

        #used to display main menu screen
        self.game_started = False

        self.text_font = pygame.font.Font('assets/font/MADETommySoftRegularPERSONALUSE.otf')

        self.title_surface = pygame.image.load('assets/imgs/FOODCOMA.png').convert_alpha()  
        self.title_rect = self.title_surface.get_rect(center = (self.screen_width/2, (self.screen_height/2)-200))

        self.title_buttons = []

        self.title_buttons.append(Button(7*self.screen_width/18, self.screen_height/2+(self.screen_height/10), 400, 100, self.text_font, 'Start Game!', self.screen))
        self.title_buttons.append(Button(7*self.screen_width/18, self.screen_height/2 + (self.screen_height/5), 400, 100, self.text_font, 'Quit Game', self.screen))

    def start_game(self):
        self.game_started = True
        return self.game_started


    def end_game(self):
        self.running = False
        return self.running

    async def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.end_game()

            if not self.game_started:
                self.screen.fill("#DCD6F7")
                self.screen.blit(self.title_surface, self.title_rect)


                for i, btn in enumerate(self.title_buttons):
                    btn.draw(is_selected=(i == self.button_select))

                for event in events:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            self.button_select = (self.button_select + 1) % len(self.title_buttons)
                        elif event.key == pygame.K_UP:
                            self.button_select = (self.button_select - 1) % len(self.title_buttons)
                        elif event.key == pygame.K_SPACE:
                            if self.button_select == 0:
                                self.start_game()
                            elif self.button_select == 1:
                                self.end_game()
                            
                
            else:
                mixing = Mixing(self.screen, self.clock)
                mixing.run()

                if mixing.completed:
                    pass
                else:
                    self.game_started = False 

            self.dt = self.clock.tick(60) / 1000

            pygame.display.flip()
            await asyncio.sleep(0)
        
        pygame.quit()

if __name__ == "__main__":
    app = Game()
    asyncio.run(app.run())
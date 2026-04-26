import pygame
from random import randint, choice
from finish import Finish

TOPPINGS = ["syrup", "powdered_sugar", "nutella", "bananas", "strawberries"]

class Stacking:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.dt = 0
        self.running = True
        self.completed = False

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.text_font = pygame.font.Font('assets/font/MADETommySoftBoldPERSONALUSE.otf', 40)
        self.small_font = pygame.font.Font('assets/font/MADETommySoftBoldPERSONALUSE.otf', 28)

        # load topping images as surfaces (not just paths)
        self.topping_images = {
            "pancake":       pygame.transform.scale_by(pygame.image.load('assets/imgs/pancake.png').convert_alpha(), 0.3),
            "syrup":         pygame.transform.scale_by(pygame.image.load('assets/imgs/syrup.jpg').convert_alpha(), 0.3),
            "powdered_sugar":pygame.transform.scale_by(pygame.image.load('assets/imgs/powdered_sugar.png').convert_alpha(), 0.3),
            "nutella":       pygame.transform.scale_by(pygame.image.load('assets/imgs/nutella.png').convert_alpha(), 0.3),
            "bananas":       pygame.transform.scale_by(pygame.image.load('assets/imgs/bananas.png').convert_alpha(), 0.3),
            "strawberries":  pygame.transform.scale_by(pygame.image.load('assets/imgs/strawberries_icon.png').convert_alpha(), 0.3),
        }

        # for making selection
        self.selection_pos = 0
        self.selection_opt = ["pancake", "syrup", "powdered_sugar", "nutella", "bananas", "strawberries"]

        # for time
        self.time_limit = 30
        self.time_left = self.time_limit

        self.stack = [] 

        # basically lives
        self.mistakes = 0

        self.order = self.generate_order()
        self.order_pos = 0

        # feedback flash
        self.flash_timer = 0
        self.flash_correct = False

    def generate_order(self):
        order = []
        num_pancakes = randint(2, 4)
        num_toppings = randint(2, 4)

        # always start with a pancake, then randomly mix the rest
        order.append("pancake")
        num_pancakes -= 1

        remaining = (["pancake"] * num_pancakes) + ([choice(TOPPINGS) for _ in range(num_toppings)])
        # shuffle but never put two toppings in a row without a pancake
        for item in remaining:
            order.append(item)

        return order

    def place_item(self, item):
        expected = self.get_next_expected()

        if item == expected:
            self.stack.append(item)
            self.order_pos += 1
            self.flash_correct = True
            self.flash_timer = 0.2

            if self.order_pos >= len(self.order):
                self.completed = True
                self.running = False
        else:
            self.mistakes += 1  # pancake gets more hangry
            self.flash_correct = False
            self.flash_timer = 0.2

    def get_next_expected(self):
        return self.order[self.order_pos]  

    def draw_stack(self):
        layer_height = 60
        base_y = self.screen_height - 100

        for i, item in enumerate(self.stack):
            y = base_y - (i * layer_height)
            img = self.topping_images[item]
            rect = img.get_rect(centerx=self.screen_width // 2, bottom=y)
            self.screen.blit(img, rect)

    def draw_order(self):
        line_height = 36
        padding = 12
        base_y = padding
        base_x = 20

        title = self.small_font.render('ORDER:', True, (80, 80, 80))
        self.screen.blit(title, (base_x, base_y))
        base_y += line_height

        for i, item in enumerate(self.order):
            # highlight already placed items
            if i < self.order_pos:
                color = (150, 220, 150)  # greyed out / done
            elif i == self.order_pos:
                color = (230, 96, 110)   # current item to place
            else:
                color = (0, 0, 0)

            order_item_surface = self.small_font.render(
                ('> ' if i == self.order_pos else '  ') + item, True, color
            )
            self.screen.blit(order_item_surface, (base_x, base_y + i * line_height))

    def draw_selector(self):
        x = self.screen_width - 380
        y = self.screen_height // 2 - (len(self.selection_opt) * 40) // 2

        hint = self.small_font.render('W / S   SPACE to place', True, (120, 120, 120))
        self.screen.blit(hint, (x, y - 36))

        for i, option in enumerate(self.selection_opt):
            is_selected = (i == self.selection_pos)
            color = (230, 96, 110) if is_selected else (180, 180, 200)
            label = self.text_font.render(('> ' if is_selected else '  ') + option, True, color)
            self.screen.blit(label, (x, y + i * 40))

    def draw_timer(self):
        color = (220, 60, 60) if self.time_left < 10 else (80, 80, 80)
        timer_surf = self.text_font.render(f'Time: {max(0, int(self.time_left))}s', True, color)
        self.screen.blit(timer_surf, (self.screen_width // 2 - timer_surf.get_width() // 2, 20))

    def draw_mistakes(self):
        m_surf = self.small_font.render(f'Mistakes: {self.mistakes}', True, (180, 80, 80))
        self.screen.blit(m_surf, (self.screen_width // 2 - m_surf.get_width() // 2, 70))

    def run(self):
        while self.running:
            self.time_left -= self.dt
            if self.time_left <= 0:
                self.running = False
                self.completed = False

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.selection_pos = (self.selection_pos - 1) % len(self.selection_opt)
                    if event.key == pygame.K_s:
                        self.selection_pos = (self.selection_pos + 1) % len(self.selection_opt)
                    if event.key == pygame.K_SPACE:
                        self.place_item(self.selection_opt[self.selection_pos])

            # flash feedback
            if self.flash_timer > 0:
                self.flash_timer -= self.dt
                flash_surf = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                flash_color = (100, 220, 100, 40) if self.flash_correct else (220, 80, 80, 40)
                flash_surf.fill(flash_color)
                self.screen.blit(flash_surf, (0, 0))

            self.screen.fill("#DBDBDB")

            self.draw_order()
            self.draw_stack()
            self.draw_selector()
            self.draw_timer()
            self.draw_mistakes()

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000  

        if self.completed:
            finish = Finish(self.screen, self.clock)
            finish.run()
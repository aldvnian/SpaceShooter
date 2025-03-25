import simplegui

WIDTH, HEIGHT = 500, 400


class Story:
    

    def __init__(self):
      
        self.background_url = "https://t3.ftcdn.net/jpg/01/94/53/22/360_F_194532293_5DQuTyT4ni7eCuVvifJgkMRNi92CoTjk.jpg"
        self.background = simplegui.load_image(self.background_url)

        self.title = "Space Raider Origin Story"
        self.title_size = 32
        self.title_font = "monospace"

        self.story_text = [
            "In the year 4035...",
            "The Aliens have invaded our universe",
            "The Galatic Defense Federation is falling",
            "You are humanity's last flame of hope",
            "Pilot your trusty spaceship and save humanity from the aliens",
            "and uncover the truth behind their invasion...",

        ]

       
        self.button_width, self.button_height = 100, 40
        self.button_x = (WIDTH - self.button_width) // 2
        self.button_y = 240
        self.button_text = "Play"

        
        self.frame = simplegui.create_frame("Story", WIDTH, HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_mouseclick_handler(self.click)

    def draw(self, canvas):
        
        
        if self.background.get_width() > 0 and self.background.get_height() > 0:
            canvas.draw_image(
                self.background,
                (self.background.get_width() / 2, self.background.get_height() / 2),
                (self.background.get_width(), self.background.get_height()),
                (WIDTH / 2, HEIGHT / 2),
                (WIDTH, HEIGHT)
            )

        # Draw title
        title_width = self.frame.get_canvas_textwidth(self.title, self.title_size, self.title_font)
        canvas.draw_text(self.title, [(WIDTH - title_width) // 2, 40], self.title_size, "White", self.title_font)

        # Draw story text
        y_offset = 90
        for line in self.story_text:
            text_width = self.frame.get_canvas_textwidth(line, 18, "serif")
            canvas.draw_text(line, [(WIDTH - text_width) // 2, y_offset], 18, "White", "serif")
            y_offset += 25

            # Draw start button
        canvas.draw_polygon(
            [(self.button_x, self.button_y), (self.button_x + self.button_width, self.button_y),
             (self.button_x + self.button_width, self.button_y + self.button_height),
             (self.button_x, self.button_y + self.button_height)],
            2, "White", "Gray"
        )

        # Draw button text
        text_width = self.frame.get_canvas_textwidth(self.button_text, 20, self.title_font)
        canvas.draw_text(self.button_text,
                         [(self.button_x + (self.button_width - text_width) / 2), self.button_y + 28],
                         20, "White", self.title_font)

    def click(self, pos):
       
        x, y = pos
        if self.button_x <= x <= self.button_x + self.button_width and self.button_y <= y <= self.button_y + self.button_height:
            self.start_game()

    def start_game(self):
        print("")
        
        


# Create and start the story screen
StoryScreen = Story()
StoryScreen.frame.start()

import simplegui

class Menu:
    def __init__(self):
        self.canvas_width = 400
        self.canvas_height = 300
        self.background = simplegui.load_image("https://t3.ftcdn.net/jpg/01/94/53/22/360_F_194532293_5DQuTyT4ni7eCuVvifJgkMRNi92CoTjk.jpg")
        self.title = "Space Raider"
        self.title_size = 36
        self.title_font = "monospace"
        self.instructions_title = "Instructions"
        self.instructions_size = 24
        self.instructions = [
            "- Use arrow keys to move and spacebar to shoot.", 
            "- Move up and down to avoid obstacles.", 
            "- Shoot aliens, avoid projectiles, and survive!"
        ]
        self.start_width = 100
        self.start_height = 40
        self.start_x = self.canvas_width/2
        self.start_y = self.canvas_height - 150
        self.start_text = "Start"
        self.frame = simplegui.create_frame("Space Raider Game", width, height)
        self.frame.set_draw_handler(draw)
        self.frame.set_mouseclick_handler(click)
        self.frame.start()

    def draw(canvas):
        if background.get_width() > 0:
            canvas.draw_image(
                background, 
                (background.get_width()/2, background.get_height()/2), 
                (background.get_width(), background.get_height()), 
                (width/2, height/2), 
                (width, height)
            )
        
        title_width = frame.get_canvas_textwidth(title, title_size, title_font)
        canvas.draw_text(title, [self.canvas_width/2, 40], self.title_size, "White", self.title_font)

        heading_width = frame.get_canvas_textwidth(self.instructions_title, self.instructions_size, "serif")
        canvas.draw_text(self.instructions_title, [self.canvas_width/2, 90], self.instructions_size, "White", "serif")
    
        y_value = 120
        for line in self.instructions:
            text_width = frame.get_canvas_textwidth(line, 18, "serif")
            canvas.draw_text(line, [self.canvas_width/2, y_value], 18, "White", "serif")
            y_value += 25  
    
        canvas.draw_polygon(
            [(self.start_x, self.start_y), (self.start_x + self.start_width, self.start_y), 
             (self.start_x + self.start_width, self.start_y + self.start_height), (self.start_x, self.start_y + self.start_height)], 
            2, "White", "Gray"
        )
    
        text_width = frame.get_canvas_textwidth(self.start_text, 20, title_font)
        text_pos = [(self.start_x + (self.start_width - text_width) / 2), self.start_y + 28]
        canvas.draw_text(self.start_text, text_pos, 20, "White", self.title_font)

    def click(pos):
        x, y = pos
        if self.start_x <= x <= self.start_x + self.start_width:
            if self.start_y <= y <= self.start_y + self.start_height:
                self.start_game()
    
    def start_game():
        print("Game started!")

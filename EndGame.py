import simplegui

# Canvas size
WIDTH = 400
HEIGHT = 300

# Load background image
background_url = "https://t3.ftcdn.net/jpg/01/94/53/22/360_F_194532293_5DQuTyT4ni7eCuVvifJgkMRNi92CoTjk.jpg"
background = simplegui.load_image(background_url)

# Button settings
button_width = 120
button_height = 40
button_x = (WIDTH - button_width) // 2
button_y = 210
button_text = "Play Again"

# Draw everything
class Endgame:
    def __init_(self, score):
        self.frame = simplegui.create_frame("Game Over", WIDTH, HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_mouseclick_handler(self.click)
        self.frame.start()
        self.score
        
    def draw(canvas):
        # Background
        if background.get_width() > 0:
            canvas.draw_image(
                background,
                (background.get_width() / 2, background.get_height() / 2),
                (background.get_width(), background.get_height()),
                (WIDTH / 2, HEIGHT / 2),
                (WIDTH, HEIGHT)
            )
    
        # Game Over title
        title = "GAME OVER"
        title_size = 40
        title_width = frame.get_canvas_textwidth(title, title_size, "monospace")
        canvas.draw_text(title, ((WIDTH - title_width) // 2, 80), title_size, "White", "monospace")
    
        # Score
        score_label = "Score: " + str(self.score)
        score_size = 24
        score_width = frame.get_canvas_textwidth(score_label, score_size, "monospace")
        canvas.draw_text(score_label, ((WIDTH - score_width) // 2, 150), score_size, "White", "monospace")
    
        # Button
        canvas.draw_polygon(
            [(button_x, button_y),
             (button_x + button_width, button_y),
             (button_x + button_width, button_y + button_height),
             (button_x, button_y + button_height)],
            2, "White", "Gray"
        )
    
        text_size = 20
        text_width = frame.get_canvas_textwidth(button_text, text_size, "monospace")
        canvas.draw_text(button_text, ((button_x + (button_width - text_width) // 2), button_y + 28), text_size, "White", "monospace")
    
    # Handle mouse click
    def click(pos):
        x, y = pos
        if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
            print("Play Again clicked")
            score.reset()
            # You can add logic to go back to start screen here

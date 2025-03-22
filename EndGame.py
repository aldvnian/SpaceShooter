import simplegui

# Canvas size
WIDTH = 400
HEIGHT = 300

# Load background image
background_url = "https://t3.ftcdn.net/jpg/01/94/53/22/360_F_194532293_5DQuTyT4ni7eCuVvifJgkMRNi92CoTjk.jpg"
background = simplegui.load_image(background_url)

# Button settings
btn_width = 120
btn_height = 40
btn_x = (WIDTH - btn_width) // 2
btn_y = 210
btn_text = "Play Again"

# Score tracker
class Score:
    def __init__(self):
        self.value = 0

    def reset(self):
        self.value = 0

    def get(self):
        return self.value

    def add(self, points):
        self.value += points

score = Score()

# Draw everything
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
    score_label = "Score: " + str(score.get())
    score_size = 24
    score_width = frame.get_canvas_textwidth(score_label, score_size, "monospace")
    canvas.draw_text(score_label, ((WIDTH - score_width) // 2, 150), score_size, "White", "monospace")

    # Button
    canvas.draw_polygon(
        [(btn_x, btn_y),
         (btn_x + btn_width, btn_y),
         (btn_x + btn_width, btn_y + btn_height),
         (btn_x, btn_y + btn_height)],
        2, "White", "Gray"
    )

    text_size = 20
    text_width = frame.get_canvas_textwidth(btn_text, text_size, "monospace")
    canvas.draw_text(btn_text, ((btn_x + (btn_width - text_width) // 2), btn_y + 28), text_size, "White", "monospace")

# Handle mouse click
def click(pos):
    x, y = pos
    if btn_x <= x <= btn_x + btn_width and btn_y <= y <= btn_y + btn_height:
        print("Play Again clicked")
        score.reset()
        # You can add logic to go back to start screen here

# Create the window
frame = simplegui.create_frame("Game Over", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.start()

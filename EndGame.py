import simplegui

# Screen size
WIDTH = 400
HEIGHT = 300

# Background image
bg_url = "https://t3.ftcdn.net/jpg/01/94/53/22/360_F_194532293_5DQuTyT4ni7eCuVvifJgkMRNi92CoTjk.jpg"
background = simplegui.load_image(bg_url)

# Button setup
button_w, button_h = 120, 40
button_x = (WIDTH - button_w) // 2
button_y = 210
button_label = "Play Again"

# Score tracker
class TotalScore:
    def __init__(self):
        self.value = 0

    def reset(self):
        self.value = 0

    def add(self, points):
        self.value += points

    def get(self):
        return self.value

score = TotalScore()

# Drawing everything on screen
def draw(canvas):
    # Draw background
    if background.get_width() > 0:
        canvas.draw_image(
            background,
            (background.get_width() / 2, background.get_height() / 2),
            (background.get_width(), background.get_height()),
            (WIDTH / 2, HEIGHT / 2),
            (WIDTH, HEIGHT)
        )

    # Draw game over text
    title = "GAME OVER"
    title_size = 40
    title_w = frame.get_canvas_textwidth(title, title_size, "monospace")
    canvas.draw_text(title, ((WIDTH - title_w) // 2, 80), title_size, "White", "monospace")

    # Draw score
    score_text = "Score: " + str(score.get())
    score_size = 24
    score_w = frame.get_canvas_textwidth(score_text, score_size, "monospace")
    canvas.draw_text(score_text, ((WIDTH - score_w) // 2, 150), score_size, "White", "monospace")

    # Draw button
    canvas.draw_polygon(
        [(button_x, button_y), (button_x + button_w, button_y), 
         (button_x + button_w, button_y + button_h), (button_x, button_y + button_h)],
        2, "White", "Gray"
    )

    label_size = 20
    label_w = frame.get_canvas_textwidth(button_label, label_size, "monospace")
    canvas.draw_text(button_label, ((button_x + (button_w - label_w) / 2), button_y + 28), label_size, "White", "monospace")

# Handle button clicks
def click(pos):
    x, y = pos
    if btn_x <= x <= button_x + button_w and button_y <= y <= button_y + button_h:
        print("Play Again clicked")
        score.reset()
        # Restart logic goes here if needed

# Set up frame
frame = simplegui.create_frame("Game Over", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.start()

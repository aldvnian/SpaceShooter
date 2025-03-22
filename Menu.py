import simplegui

# Canvas size
width, height = 400, 300

# Load background image
background_url = "https://t3.ftcdn.net/jpg/01/94/53/22/360_F_194532293_5DQuTyT4ni7eCuVvifJgkMRNi92CoTjk.jpg"
background = simplegui.load_image(background_url)

# Title settings
title = "Space Raider"
title_size = 36
title_font = "monospace"

# Instructions
instructions_title = "Instructions"
instructions_size = 24
instructions = [
    "- Use arrow keys to move and spacebar to shoot.", 
    "- Move up and down to avoid obstacles.", 
    "- Shoot aliens, avoid projectiles, and survive!"
]

# Start button settings
button_width, button_height = 100, 40
button_x = (width - button_width) // 2
button_y = 240
button_text = "Start"

def draw(canvas):
    """Draws everything on the screen."""
    if background.get_width() > 0 and background.get_height() > 0:
        canvas.draw_image(
            background, 
            (background.get_width() / 2, background.get_height() / 2), 
            (background.get_width(), background.get_height()), 
            (width / 2, height / 2), 
            (width, height)
        )
    
    # Draw title
    title_width = frame.get_canvas_textwidth(title, title_size, title_font)
    canvas.draw_text(title, [(width - title_width) // 2, 40], title_size, "White", title_font)

    # Draw instructions title
    heading_width = frame.get_canvas_textwidth(instructions_title, instructions_size, "serif")
    canvas.draw_text(instructions_title, [(width - heading_width) // 2, 90], instructions_size, "White", "serif")

    # Draw instructions
    y_offset = 120
    for line in instructions:
        text_width = frame.get_canvas_textwidth(line, 18, "serif")
        canvas.draw_text(line, [(width - text_width) // 2, y_offset], 18, "White", "serif")
        y_offset += 25  

    # Draw start button
    canvas.draw_polygon(
        [(button_x, button_y), (button_x + button_width, button_y), 
         (button_x + button_width, button_y + button_height), (button_x, button_y + button_height)], 
        2, "White", "Gray"
    )

    # Draw button text
    text_width = frame.get_canvas_textwidth(button_text, 20, title_font)
    canvas.draw_text(button_text, [(button_x + (button_width - text_width) / 2), button_y + 28], 20, "White", title_font)

def click(pos):
    """Handles button clicks."""
    x, y = pos
    if btn_x <= x <= btn_x + btn_width and btn_y <= y <= btn_y + btn_height:
        start_game()

def start_game():
    """Placeholder for starting the game."""
    print("Game started!")

# Create frame
frame = simplegui.create_frame("Space Raider Game", width, height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.start()

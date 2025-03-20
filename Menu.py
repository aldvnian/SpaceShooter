import simplegui

# Canvas properties
WIDTH = 400
HEIGHT = 300
# Load background image (Use a direct, working URL)
BACKGROUND_URL = "https://t3.ftcdn.net/jpg/01/94/53/22/360_F_194532293_5DQuTyT4ni7eCuVvifJgkMRNi92CoTjk.jpg"
background = simplegui.load_image(BACKGROUND_URL)

# Title properties
title_text = "Space Raider"
title_size = 36
title_font = "monospace"

# Instructions heading
instructions_heading = "Instructions"
instructions_size = 24

# Game instructions
instructions = [
    "- Use arrow keys to move and spacebar to shoot.", 
    "- Move up and down to avoid obstacles.", 
    "- Shoot aliens, avoid projectiles, and survive!"
]

# Button properties
button_width = 100
button_height = 40
button_pos = [(WIDTH - button_width) // 2, 240]  # Centered horizontally
button_text = "Start"

# Draw handler
def draw(canvas):
    # Check if the image loaded properly
    if background.get_width() > 0 and background.get_height() > 0:
        # Draw background image
        canvas.draw_image(background, 
                          (background.get_width() / 2, background.get_height() / 2), 
                          (background.get_width(), background.get_height()), 
                          (WIDTH / 2, HEIGHT / 2), 
                          (WIDTH, HEIGHT))
    # Draw title
    text_width = frame.get_canvas_textwidth(title_text, title_size, title_font)
    title_pos = [(WIDTH - text_width) // 2, 40]  # Centered horizontally
    canvas.draw_text(title_text, title_pos, title_size, "White", title_font)

    # Draw Instructions Heading
    heading_width = frame.get_canvas_textwidth(instructions_heading, instructions_size, "serif")
    heading_pos = [(WIDTH - heading_width) // 2, 90]
    canvas.draw_text(instructions_heading, heading_pos, instructions_size, "White", "serif")

    # Draw instructions (bullet points)
    y_offset = 120
    for instruction in instructions:
        text_width = frame.get_canvas_textwidth(instruction, 18, "serif")
        canvas.draw_text(instruction, [(WIDTH - text_width) // 2, y_offset], 18, "White", "serif")
        y_offset += 25  # Space between lines
    # Draw Start button (rectangle)
    canvas.draw_polygon(
        [button_pos,
         [button_pos[0] + button_width, button_pos[1]],
         [button_pos[0] + button_width, button_pos[1] + button_height],
         [button_pos[0], button_pos[1] + button_height]],
        2, "White", "Gray"
    )
    
    # Draw button text
    button_text_size = 20
    text_width = frame.get_canvas_textwidth(button_text, button_text_size, title_font)
    text_pos = [button_pos[0] + (button_width - text_width) / 2,
                button_pos[1] + (button_height + button_text_size) / 2 - 5]
    
    canvas.draw_text(button_text, text_pos, button_text_size, "White", title_font)

# Mouse click handler
def click(pos):
    x, y = pos
    if (button_pos[0] <= x <= button_pos[0] + button_width and
        button_pos[1] <= y <= button_pos[1] + button_height):
        start_game()

# Start game function
def start_game():
    print("Game started!")  # You can replace this with actual game logic

# Create frame
frame = simplegui.create_frame("Space Raider Game", WIDTH, HEIGHT)

# Set handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# Start frame
frame.start()

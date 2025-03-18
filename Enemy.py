import simplegui, math, random
from user304_rsf8mD0BOQ_1 import Vector

canvasWidth = 700
canvasHeight = 600

class Enemy(Spaceship):
    def __init__(self, pos, enemyShipImageURL, startingRotation, canvasWidth, canvasHeight):
        super().__init__(enemyShipImageURL, pos, startingRotation, canvasWidth, canvasHeight)
        self.enemyWidthHeightDest = (65, 65)
        self.current_rotation = math.pi/2
               
    def draw(self, canvas):
        centre = (self.shipImage.get_width()/2, self.shipImage.get_height()/2)
        widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
        canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.enemyWidthHeightDest, self.current_rotation)

    def update(self):
        super().update()

    def turn(self, degrees):
        self.current_rotation = degrees

enemy = Enemy(
    (canvasWidth/2, canvasHeight - 550),  
    "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png",
    math.pi/2,
    canvasWidth,
    canvasHeight
)

def draw_handler(canvas):
    enemy.update()
    enemy.draw(canvas)

frame = simplegui.create_frame('Enemy', canvasWidth, canvasHeight)
frame.set_canvas_background('black') 
frame.set_draw_handler(draw_handler)
frame.start()

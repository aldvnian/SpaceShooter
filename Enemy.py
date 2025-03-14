import simplegui, math, random
from user304_rsf8mD0BOQ_1 import Vector

canvasWidth = 700
canvasHeight = 600

class Enemy:
    def __init__(self, pos, enemyShipImageURL):
        self.pos = pos
        self.vel = Vector()
        self.enemyShipImage = simplegui.load_image(enemyShipImageURL)
        self.enemyWidthHeightDest = (65, 65)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.current_rotation = -math.pi/2
               
    def draw(self, canvas):
        centre = (self.enemyShipImage.get_width()/2, self.enemyShipImage.get_height()/2)
        widthHeightSource = (self.enemyShipImage.get_width(), self.enemyShipImage.get_height())
        canvas.draw_image(self.enemyShipImage, centre, widthHeightSource, self.centreDest, self.enemyWidthHeightDest, self.current_rotation)

    def update(self):
        self.pos.add(self.vel)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.vel.multiply(0.2)

    def turn(self, degrees):
        self.current_rotation = degrees

enemy = Enemy(Vector(canvasWidth/2, canvasHeight - 550 ), "https://www.cs.rhul.ac.uk/home/znac614/cs1822/Spaceshooter/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png")

def draw_handler(canvas):
    enemy.update()
    enemy.draw(canvas)

frame = simplegui.create_frame('Enemy', canvasWidth, canvasHeight)
frame.set_canvas_background('black') 
frame.set_draw_handler(draw_handler)
frame.start()

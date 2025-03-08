import simplegui, math
from user304_rsf8mD0BOQ_1 import Vector

canvasWidth = 700
canvasHeight = 600

class Player:
    def __init__(self, name, pos, shipImageURL, startingRotation):
        self.name = name
        self.pos = pos
        self.vel = Vector()
        self.shipImage = simplegui.load_image(shipImageURL)
        self.widthHeightDest = (100, 100)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.current_rotation = -math.pi/2

    def draw(self, canvas):
        centre = (self.shipImage.get_width()/2, self.shipImage.get_height()/2)
        widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
        canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.widthHeightDest, self.current_rotation)
        
    def turn(self, degrees):
        self.current_rotation = degrees
                
    def update(self):
        self.pos.add(self.vel)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.vel.multiply(0.85)
                
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.rightKeyDown = False
        self.leftKeyDown = False
        self.upKeyDown = False
        self.downKeyDown = False
        
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            if self.left == True:
                self.left = False
            self.right = True
            self.rightKeyDown = True
        elif key == simplegui.KEY_MAP['left']:
            if self.right == True:
                self.right = False
            self.left = True
            self.leftKeyDown = True
        elif key == simplegui.KEY_MAP['up']:
            if self.down == True:
                self.down = False
            self.up = True
            self.upKeyDown = True
        elif key == simplegui.KEY_MAP['down']:
            if self.up == True:
                self.up = False
            self.down = True
            self.downKeyDown = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.rightKeyDown = False
            self.right = False
            if self.leftKeyDown:
                self.left = True
        elif key == simplegui.KEY_MAP['left']:
            self.leftKeyDown = False
            self.left = False
            if self.rightKeyDown:
                self.right = True
        elif key == simplegui.KEY_MAP['up']:
            self.upKeyDown = False
            self.up = False
            if self.downKeyDown:
                self.down = True
        elif key == simplegui.KEY_MAP['down']:
            self.downKeyDown = False
            self.down = False
            if self.upKeyDown:
                self.up = True
                
class Interaction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard
        
    def update(self, canvas):
        if self.keyboard.up:
            self.player.vel.add(Vector(0, -1))
            self.player.turn(-math.pi/2)
        if self.keyboard.down:
            self.player.vel.add(Vector(0, 1))
            self.player.turn(math.pi/2)
        if self.keyboard.left:
            self.player.vel.add(Vector(-1, 0))
            self.player.turn(-math.pi)
        if self.keyboard.right:
            self.player.vel.add(Vector(1, 0))
            self.player.turn(0)

player = Player("Adnan", 
                Vector(canvasWidth/2, canvasHeight - 100), 
                "https://www.cs.rhul.ac.uk/home/znac614/cs1822/Spaceshooter/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship6/Ship6.png",
               -math.pi/2)
kbd = Keyboard()
inter = Interaction(player, kbd)

def draw_handler(canvas):
    inter.update(canvas)
    player.update()
    player.draw(canvas)

frame = simplegui.create_frame('Player', canvasWidth, canvasHeight)
frame.set_canvas_background('black')
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()

import simplegui, math
from user304_rsf8mD0BOQ_1 import Vector

canvasWidth = 800
canvasHeight = 600

class Player(Spaceship):
    def __init__(self, shipImageURL, startingRotation, canvasWidth, canvasHeight):
        super().__init__(shipImageURL, (canvasWidth/2, canvasHeight - 70), startingRotation, canvasWidth, canvasHeight)
        self.moving = False
        self.boost = Spritesheet("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship6/Exhaust/Normal_flight/Exhaust1/boost_animation_sprite.png", 
                                1, 4, (self.pos.x, self.pos.y + 55), (40, 40), math.pi/2, 4)
        self.shot = Spritesheet("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Shots/Shot6/Shot6_spritesheet.png",
                               2, 12, (self.pos.x, self.pos.y - 70), (80, 80), -math.pi/2, 15)
        self.borderRight = canvasWidth - self.widthHeightDest[0]/2
        self.borderLeft = self.widthHeightDest[0]/2
        self.borderUp = canvasHeight/2 + self.widthHeightDest[1]/2
        self.borderDown = canvasHeight - self.widthHeightDest[1]/2 - 50
        self.shoot = False

    def draw(self, canvas):
        super().draw(canvas)
        print(self.shoot)
        if self.shoot:
            self.shot.draw(canvas, 5)
        if self.moving:
            self.boost.draw(canvas, "None")
        
    def inBorder(self):
        if self.pos.x > self.borderRight:
            self.pos.x = self.borderRight
            self.vel.x = 0
        elif self.pos.x < self.borderLeft:
            self.pos.x = self.borderLeft
            self.vel.x = 0

        if self.pos.y > self.borderDown:
            self.pos.y = self.borderDown
            self.vel.y = 0
        elif self.pos.y < self.borderUp:
            self.pos.y = self.borderUp
            self.vel.y = 0
            
    def update(self):
        self.pos.add(self.vel)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.boost.centreDest = (self.centreDest[0], self.centreDest[1] + 55)
        self.shot.centreDest = (self.centreDest[0], self.centreDest[1] - 70)
        self.vel.multiply(0.73)

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
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
        elif key == simplegui.KEY_MAP['space']:
            self.space = True

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
        elif key == simplegui.KEY_MAP['space']:
            self.space = False
                
class Interaction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard
        
    def update(self, canvas):
        self.player.inBorder()
        if self.keyboard.up:
            self.player.vel.add(Vector(0, -1))
            self.player.moving = True
        else:
            self.player.moving = False
        if self.keyboard.down:
            self.player.vel.add(Vector(0, 1))
        if self.keyboard.left:
            self.player.vel.add(Vector(-1, 0))
        if self.keyboard.right:
            self.player.vel.add(Vector(1, 0))
        if self.keyboard.space:
            self.player.shoot = True
        else:
            self.player.shoot = False


player = Player("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts%26Spriter_Animation/Ship6/Ship6.png",
               -math.pi/2, canvasWidth, canvasHeight)
kbd = Keyboard()
inter = Interaction(player, kbd)

def draw_handler(canvas):
    player.update()
    inter.update(canvas)
    player.draw(canvas)

frame = simplegui.create_frame('Player', canvasWidth, canvasHeight)
frame.set_canvas_background('black')
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()

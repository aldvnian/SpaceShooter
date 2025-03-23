import simplegui, math
from user304_rsf8mD0BOQ_1 import Vector

canvasWidth = 800
canvasHeight = 600

class Spritesheet:
    def __init__(self, url, rows, columns, center_dest, size_drawn, rotation, num_frames):
        self.url = url
        self.rows = rows
        self.columns = columns
        self.image = simplegui.load_image(self.url)
        self.orgSize = (self.image.get_width(), self.image.get_height())
        self._init_dimension()
        self.frameIndex = [0, 0]
        self.centreDest = center_dest
        self.extraFrames = num_frames % (columns)
        self.rotation = rotation
        self.sizeDrawn = size_drawn
        self.clock = 0
        
    def _init_dimension(self):
        self.frameWidth = self.orgSize[0] / self.columns
        self.frameHeight = self.orgSize[1] / self.rows
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        
    def draw(self, canvas):
        if self.orgSize[0] > 0:
            sourceCentre = (
                self.frameIndex[0] * self.frameWidth + self.frameCentreX,
                self.frameIndex[1] * self.frameHeight + self.frameCentreY
            )
            sourceSize = (self.frameWidth, self.frameHeight)
            canvas.draw_image(self.image, sourceCentre, sourceSize, self.centreDest, self.sizeDrawn, self.rotation)
            self.clock += 1
            if self.clock == 20:
                self.next()
                self.clock = 0
        
    def next(self):
        if self.frameIndex[1] == self.rows - 1 and self.rows != 1:
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.extraFrames
        else:
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.columns
        if self.frameIndex[0] == 0:
            self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows
            
class Spaceship():
    def __init__(self, shipImageURL, pos, startingRotation, canvasWidth, canvasHeight):
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector()
        self.shipImage = simplegui.load_image(shipImageURL)
        self.widthHeightDest = (90, 90)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.currentRotation = startingRotation

    def draw(self, canvas):
        centre = (self.shipImage.get_width()/2, self.shipImage.get_height()/2)
        widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
        canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.widthHeightDest, self.currentRotation)

    def move(self, coordinate):
        self.centreDest = coordinate

    def update(self):
        self.pos.add(self.vel)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.vel.multiply(0.73)
        
class Bullet:
    def __init__(self, imgURL, centreDest, size, rotation):
        self.image = simplegui.load_image(imgURL)
        self.pos = centreDest
        self.size = size
        self.rotation = rotation
        
    def draw(self, canvas):
        if self.image.get_width() > 0:
            canvas.draw_image(self.image, (self.image.get_width()/2, self.image.get_height()/2),
                             (self.image.get_width(), self.image.get_height()),
                             self.pos, self.size,
                             self.rotation)
        
    def update(self, posAdder):
        self.pos = (self.pos[0], self.pos[1] + posAdder)
        
    def animation(self):
        pass
        
        
class Player(Spaceship):
    def __init__(self, shipImageURL, startingRotation, canvasWidth, canvasHeight):
        super().__init__(shipImageURL, (canvasWidth/2, canvasHeight - 70), startingRotation, canvasWidth, canvasHeight)
        self.moving = False
        self.boost = Spritesheet("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship6/Exhaust/Normal_flight/Exhaust1/boost_animation_sprite.png", 
                                1, 4, (self.pos.x, self.pos.y + 55), (40, 40), math.pi/2, 4)
        self.shot_animation = Spritesheet("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Shots/Shot6/Shot6_spritesheet.png",
                               2, 12, (self.pos.x, self.pos.y - 70), (80, 80), -math.pi/2, 15)
        self.borderRight = canvasWidth - self.widthHeightDest[0]/2
        self.borderLeft = self.widthHeightDest[0]/2
        self.borderUp = canvasHeight/2 + self.widthHeightDest[1]/2
        self.borderDown = canvasHeight - self.widthHeightDest[1]/2 - 50
        self.shoot = False
        self.shots = []
        self.alive = True
        self.health = 5

    def draw(self, canvas):
        super().draw(canvas)
        if self.moving:
            self.boost.draw(canvas)
        if self.shoot:
            for bullet in self.shots:
                bullet.draw(canvas)
                bullet.update(-4)
    
    def loadBullet(self):
        self.shots.append(Bullet("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Shots/Shot6/shot6_3.png",
                                    (self.pos.x, self.pos.y - 70),
                                    (120, 120),
                                    -math.pi/2))
    
    def removeBullet(self, bullet):
        self.shots.remove(bullet)
        
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
        self.shot_animation.centreDest = (self.centreDest[0], self.centreDest[1] - 70)
        self.vel.multiply(0.73)

        
class Enemy(Spaceship):
    def __init__(self, pos, enemyShipImageURL, startingRotation, canvasWidth, canvasHeight, health):
        super().__init__(enemyShipImageURL, pos, startingRotation, canvasWidth, canvasHeight)
        self.enemyWidthHeightDest = (65, 65)
        self.current_rotation = math.pi/2
        self.enemyBullets = []
        self.shotsDelay = 1000
        self.timer = simplegui.create_timer(self.shotsDelay, self.loadBullet)
        self.timer.start()
        self.alive = True
        self.health = health
               
    def draw(self, canvas):
        centre = (self.shipImage.get_width()/2, self.shipImage.get_height()/2)
        widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
        canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.enemyWidthHeightDest, self.current_rotation)
        for bullet in self.enemyBullets:
            bullet.draw(canvas)

        
    def loadBullet(self):
        newEnemyBullet = Bullet("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Animations/Shots/Shot1/shot1_exp1.png",
                                    (self.pos.x, self.pos.y + 50),
                                    (30, 30),
                                    -math.pi/2
        )
        self.enemyBullets.append(newEnemyBullet)
        
    def removeBullet(self, bullet):
        if bullet in self.enemyBullets:
            self.enemyBullets.remove(bullet)
    
    def update(self):
        super().update()
        for bullet in self.enemyBullets[:]:
            bullet.update(4)
            if bullet.pos[1] > canvasHeight:
                self.removeBullet(bullet)
                
    def getWidth(self):
        return self.enemyWidthHeightDest[0]
    
    def getHeight(self):
        return self.enemyWidthHeightDest[1]
          
        
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
        self.bullet_timer = 0
        self.space_down = False
        
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
            if not self.space_down:
                if self.bullet_timer >= 40:
                    self.player.loadBullet()
                    self.player.shoot = True
                    self.bullet_timer = 0
                    self.space_down = True
        else:
            self.space_down = False
        self.bullet_timer += 1

'''
player = Player("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts%26Spriter_Animation/Ship6/Ship6.png",
               -math.pi/2, canvasWidth, canvasHeight)
kbd = Keyboard()
inter = Interaction(player, kbd)
background = simplegui.load_image("https://aldvnian.github.io/Spaceshooter-sprites/Background.png")


enemy = Enemy(
    (canvasWidth/2, canvasHeight - 550),  
    "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png",
    math.pi/2,
    canvasWidth,
    canvasHeight,
    1
)
'''

class Game:
    def __init__(self, canvasWidth, canvasHeight):
        self.player = Player("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts%26Spriter_Animation/Ship6/Ship6.png",
                      -math.pi/2, canvasWidth, canvasHeight)
        self.keyboard = Keyboard()
        self.inter = Interaction(self.player, self.keyboard)
        self.enemies = []
        self.stage = 1
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.frame = simplegui.create_frame('Player', canvasWidth, canvasHeight)
        self.frame.set_draw_handler(self.draw_handler)
        self.frame.set_keydown_handler(self.keyboard.keyDown)
        self.frame.set_keyup_handler(self.keyboard.keyUp)
        self.background = simplegui.load_image("https://aldvnian.github.io/Spaceshooter-sprites/Background.png")
        
        
    def runGame(self):
        if self.stage == 1:
            self.trioFormation((80, 80))
            self.trioFormation((350, 80))
            self.trioFormation((620, 80))
            self.frame.start()
            
    def loadEnemy(self, startPos, url, rotation, health):
        enemy = Enemy(startPos, url, rotation, self.canvasWidth, self.canvasHeight, health)
        self.enemies.append(enemy)
        
    def trioFormation(self, pos):
        leftEnemy = self.loadEnemy(pos, "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png",
                             math.pi/2, 1)
        enemy = self.enemies[len(self.enemies) - 1]
        width, height = enemy.getWidth(), enemy.getHeight()
        middleEnemy = self.loadEnemy((pos[0] + width, pos[1] + height),
                               "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png",
                               math.pi/2, 1)
        rightEnemy = self.loadEnemy((pos[0] + 2*width, pos[1]),
                              "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png",
                              math.pi/2, 1)
        
    def draw_handler(self, canvas):
        canvas.draw_image(self.background, (self.background.get_width()/2, self.background.get_height()/2),
                     (self.background.get_width(), self.background.get_height()),
                     (canvasWidth/2, canvasHeight/2), (canvasWidth, canvasHeight))
        
        self.inter.update(canvas)
        
        if self.player.alive:
            self.player.draw(canvas)
            self.player.update()
        
        for enemy in self.enemies:
            if enemy.alive:
                enemy.draw(canvas)
                enemy.update()
            
        for bullet in self.player.shots:
            for enemy in self.enemies:
                if self.checkShipCollision(bullet.pos, enemy):
                    enemy.health -= 1
                    if enemy.health == 0:
                        enemy.alive = False
                    self.player.removeBullet(bullet)
        
        for enemy in self.enemies:
            for bullet in enemy.enemyBullets:
                if self.checkShipCollision(bullet.pos, self.player):
                    self.player.health -= 1
                    if self.player.health == 0:
                        self.player.alive = False
                    enemy.removeBullet(bullet)
   
    def checkShipCollision(self, bulletPos, ship):
        if ship.alive == False:
            return False
            
        shipWidth, shipHeight = ship.widthHeightDest
        shipLeft = ship.pos.x - shipWidth/2
        shipRight = ship.pos.x + shipWidth/2
        shipFront = ship.pos.y + shipHeight/2
        shipBack = ship.pos.y - shipHeight/2
            
        bulletX, bulletY = bulletPos
            
        return (shipLeft <= bulletX <= shipRight and shipBack <= bulletY <= shipFront)

game = Game(canvasWidth, canvasHeight)
game.runGame()
'''
def draw_handler(canvas):
    canvas.draw_image(background, (background.get_width()/2, background.get_height()/2),
                     (background.get_width(), background.get_height()),
                     (canvasWidth/2, canvasHeight/2), (canvasWidth, canvasHeight))
   
    inter.update(canvas)
    
    if enemy.alive:
        enemy.update()
        enemy.draw(canvas)
        
    for bullet in player.shots:
        if checkShipCollision(bullet.pos, enemy):
            enemy.health -= 1
            if enemy.health == 0:
                enemy.alive = False
            player.removeBullet(bullet)
            
    if player.alive:
        player.draw(canvas)
        player.update()
        
    for bullet in enemy.enemyBullets:
        if checkShipCollision(bullet.pos, player):
            player.health -= 1
            if player.health == 0:
                player.alive = False
            enemy.removeBullet(bullet)

        
frame = simplegui.create_frame('Player', canvasWidth, canvasHeight)
frame.set_canvas_background('black')
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
'''

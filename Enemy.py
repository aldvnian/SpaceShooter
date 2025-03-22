import simplegui, math, random
from user304_rsf8mD0BOQ_1 import Vector

canvasWidth = 700
canvasHeight = 600
score = 0
enemies = []
enemy_bullets = []


class Spaceship:
    def __init__(self, shipImageURL, pos, startingRotation, canvasWidth, canvasHeight):
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector()
        self.shipImage = simplegui.load_image(shipImageURL)
        self.widthHeightDest = (70, 70)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.currentRotation = startingRotation
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

    def draw(self, canvas):
        centre = (self.shipImage.get_width() / 2, self.shipImage.get_height() / 2)
        widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
        canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.widthHeightDest,
                          self.currentRotation)

    def update(self):
        self.pos.add(self.vel)
        self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
        self.vel.multiply(0.73)
    
    def move(self, coordinate):
        self.centreDest = coordinate



class Enemy(Spaceship):
    def __init__(self, pos, enemyShipImageURL, startingRotation, canvasWidth, canvasHeight):
        super().__init__(enemyShipImageURL, pos, startingRotation, canvasWidth, canvasHeight)
        self.enemyWidthHeightDest = (65, 65)
        self.enemyBullets = []
        self.current_rotation = math.pi / 2
        self.shotsDelay = 2000
        self.timer = simplegui.create_timer(self.shotsDelay, self.loadBullet)
        self.timer.start()

    def draw(self, canvas):
        centre = (self.shipImage.get_width() / 2, self.shipImage.get_height() / 2)
        widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
        canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.enemyWidthHeightDest,
                          self.current_rotation)

        for bullet in self.enemyBullets:
            bullet.draw(canvas)

    def loadBullet(self):
        newEnemyBullet = Bullet(
            "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Animations/Shots/Shot1/shot1_exp1.png",
            (self.pos.x, self.pos.y + 50),
            (30, 30),
            math.pi / 2,
            4)
        self.enemyBullets.append(newEnemyBullet)

    def update(self):
        global enemies
        self.pos.y += 2
        self.centreDest = (self.pos.x, self.pos.y)

        if self.pos.y > canvasHeight:
            enemies.remove(self)

        for bullet in self.enemyBullets[:]:
            bullet.update()
            if bullet.pos[1] > canvasHeight:
                self.enemyBullets.remove(bullet)
                
def spawn_enemy():
    x = random.randint(50, canvasWidth - 50)
    new_enemy = Enemy((x, 50),
                      "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png",
                      math.pi / 2, canvasWidth, canvasHeight)
    enemies.append(new_enemy)
                
  



class Bullet:
    def __init__(self, imgURL, centreDest, size, rotation, speed):
        self.image = simplegui.load_image(imgURL)
        self.pos = list(centreDest)
        self.size = size
        self.rotation = rotation
        self.speed = speed

    def draw(self, canvas):
        canvas.draw_image(self.image, (self.image.get_width() / 2, self.image.get_height() / 2),
                          (self.image.get_width(), self.image.get_height()),
                          self.pos, self.size,
                          self.rotation)

    def update(self):
        self.pos[1] += self.speed
    
    def animation(self):
        pass      



def draw_handler(canvas):
    global score

    for enemy in enemies[:]:
        enemy.update()
        enemy.draw(canvas)

    for bullet in enemy_bullets[:]:
        bullet.update()
        bullet.draw(canvas)



    canvas.draw_text(f"Score: {score}", (10, 30), 24, "White")


enemy_timer = simplegui.create_timer(2000, spawn_enemy)


frame = simplegui.create_frame('Space Shooter', canvasWidth, canvasHeight)
frame.set_canvas_background('black')
frame.set_draw_handler(draw_handler)


frame.start()
enemy_timer.start()




# import simplegui, math, random
# from user304_rsf8mD0BOQ_1 import Vector

# canvasWidth = 700
# canvasHeight = 600


# class Spaceship():
#     def __init__(self, shipImageURL, pos, startingRotation, canvasWidth, canvasHeight):
#         self.pos = Vector(pos[0], pos[1])
#         self.vel = Vector()
#         self.shipImage = simplegui.load_image(shipImageURL)
#         self.widthHeightDest = (70, 70)
#         self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
#         self.currentRotation = startingRotation

#     def draw(self, canvas):
#         centre = (self.shipImage.get_width()/2, self.shipImage.get_height()/2)
#         widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
#         canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.widthHeightDest, self.currentRotation)

#     def move(self, coordinate):
#         self.centreDest = coordinate

#     def update(self):
#         self.pos.add(self.vel)
#         self.centreDest = (self.pos.get_p()[0], self.pos.get_p()[1])
#         self.vel.multiply(0.73)
        
# class Enemy(Spaceship):
#     def __init__(self, pos, enemyShipImageURL, startingRotation, canvasWidth, canvasHeight):
#         super().__init__(enemyShipImageURL, pos, startingRotation, canvasWidth, canvasHeight)
#         self.enemyWidthHeightDest = (65, 65)
#         self.current_rotation = math.pi/2
#         self.enemyBullets = []
#         self.shotsDelay = 1000
#         self.timer = simplegui.create_timer(self.shotsDelay, self.loadBullet)
#         self.timer.start()
               
#     def draw(self, canvas):
#         centre = (self.shipImage.get_width()/2, self.shipImage.get_height()/2)
#         widthHeightSource = (self.shipImage.get_width(), self.shipImage.get_height())
#         canvas.draw_image(self.shipImage, centre, widthHeightSource, self.centreDest, self.enemyWidthHeightDest, self.current_rotation)
#         for bullet in self.enemyBullets:
#             bullet.draw(canvas)

        
#     def loadBullet(self):
#         newEnemyBullet = Bullet("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Animations/Shots/Shot1/shot1_exp1.png",
#                                     (self.pos.x, self.pos.y + 50),
#                                     (30, 30),
#                                     -math.pi/2
#         )
#         self.enemyBullets.append(newEnemyBullet)
        
#     def removeBullet(self, bullet):
#         if bullet in self.enemyBullets:
#             self.enemyBullets.remove(bullet)
    
#     def update(self):
#         super().update()
#         for bullet in self.enemyBullets[:]:
#             bullet.update(4)
#             if bullet.pos[1] > canvasHeight:
#                 self.removeBullet(bullet)
        
        
# class Bullet:
#     def __init__(self, imgURL, centreDest, size, rotation):
#         self.image = simplegui.load_image(imgURL)
#         self.pos = list(centreDest)
#         self.size = size
#         self.rotation = rotation
        
#     def draw(self, canvas):
#         canvas.draw_image(self.image, (self.image.get_width()/2, self.image.get_height()/2),
#                          (self.image.get_width(), self.image.get_height()),
#                          self.pos, self.size,
#                          self.rotation)
       
#     def update(self, posAdder):
#         self.pos[1] = self.pos[1] + posAdder
        
#     def animation(self):
#         pass      
        
    

        
        
# enemy = Enemy(
#     (canvasWidth/2, canvasHeight - 550),  
#     "https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts&Spriter_Animation/Ship1/Ship1.png",
#     math.pi/2,
#     canvasWidth,
#     canvasHeight
# )

# def draw_handler(canvas):
#     enemy.update()
#     enemy.draw(canvas)

# frame = simplegui.create_frame('Enemy', canvasWidth, canvasHeight)
# frame.set_canvas_background('black') 
# frame.set_draw_handler(draw_handler)
# frame.start()

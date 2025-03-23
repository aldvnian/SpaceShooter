class Game:
    def __init__(self):
        self.player = Player("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts%26Spriter_Animation/Ship6/Ship6.png",
               		  -math.pi/2, canvasWidth, canvasHeight)
        self.keyboard = Keyboard()
        self.inter = Interaction(self.player, self.keyboard)
        self.spaceship = Spaceship()
        self.bullet = Bullet()
        self.enemy = Enemy()
		self.stage = 1
        
        
	def runGame():
		if self.stage == 1:
   
     def checkShipCollision(bulletPos, ship):
        if ship.alive == False:
	    	return False
	        
	    shipWidth, shipHeight = ship.widthHeightDest
	    shipLeft = ship.pos.x - shipWidth/2
	    shipRight = ship.pos.x + shipWidth/2
	    shipFront = ship.pos.y + shipHeight/2
	    shipBack = ship.pos.y - shipHeight/2
	        
	    bulletX, bulletY = bulletPos
	        
	    return (shipLeft <= bulletX <= shipRight and shipBack <= bulletY <= shipFront)
    
#def draw_handler(canvas):
#    canvas.draw_image(background, (background.get_width()/2, background.get_height()/2),
#                     (background.get_width(), background.get_height()),
#                    (canvasWidth/2, canvasHeight/2), (canvasWidth, canvasHeight))
   
#    inter.update(canvas)
    
#    if enemy.alive:
#        enemy.update()
#        enemy.draw(canvas)
        
#    for bullet in player.shots[:]:
#        if checkEnemyCollision(bullet.pos, enemy):
#            enemy.alive = False
#            player.removeBullet(bullet)
            
#    if player.alive:
#        player.draw(canvas)
#        player.update()
        
#    for bullet in enemy.enemyBullets[:]:
#        if checkPlayerCollision(bullet.pos, player):
#            player.alive = False  
#            enemy.removeBullet(bullet)

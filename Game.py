class Game:
    def __init__(self):
        self.player = Player("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts%26Spriter_Animation/Ship6/Ship6.png",
               		  -math.pi/2, canvasWidth, canvasHeight)
        self.keyboard = Keyboard()
        self.inter = Interaction(self.player, self.keyboard)
        self.spaceship = Spaceship()
        self.bullet = Bullet()
        self.enemy = Enemy()
        
        
	def runGame():
        gameStageOne
        pass
    
   
    def checkCollision(bulletPos, enemy): 
        if enemy.alive == False:
            return False
        #Enemy hit box
        enemyWidth, enemyHeight = enemy.enemyWidthHeightDest
        enemyLeft = enemy.pos.x - enemyWidth/2
        enemyRight = enemy.pos.x + enemyWidth/2
        enemyFront = enemy.pos.y + enemyHeight/2
        enemyBack = enemy.pos.y - enemyHeight/2
        
        bulletX, bulletY = bulletPos
        # gives the 
        return (enemyLeft <= bulletX <= enemyRight and enemyBack <= bulletY <= enemyFront)
    
    
    def checkPlayerCollision(bulletPos,player):
        if player.alive == False:
            return False
        
        playerWidth, playerHeight = player.widthHeightDest
        playerLeft = player.pos.x - playerWidth/2
        playerRight = player.pos.x + playerWidth/2
        playerFront = player.pos.y + playerHeight/2
        playerBack = player.pos.y - playerHeight/2
        
        bulletX, bulletY = bulletPos
        
        return (playerLeft <= bulletX <= playerRight and playerBack <= bulletY <= playerFront)
    

class Game:
    def __init__(self):
        self.player = Player("https://aldvnian.github.io/Spaceshooter-sprites/craftpix-991101-free-pixel-art-enemy-spaceship-2d-sprites/PNG_Parts%26Spriter_Animation/Ship6/Ship6.png",
               		  -math.pi/2, canvasWidth, canvasHeight)
        self.keyboard = Keyboard()
        self.inter = Interaction(self.player, self.keyboard)

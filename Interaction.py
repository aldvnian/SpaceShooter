class Interaction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard
        self.bullet_timer = 0
        
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
            if self.bullet_timer >= 60:
                self.player.loadBullet()
                self.player.shoot = True
                self.bullet_timer = 0
        self.bullet_timer += 1

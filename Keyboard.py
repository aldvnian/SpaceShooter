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

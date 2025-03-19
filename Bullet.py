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

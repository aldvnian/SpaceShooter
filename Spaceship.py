import simplegui

class Spaceship():
    def __init__(self, shipImageURL, pos, startingRotation, canvasWidth, canvasHeight):
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector()
        self.shipImage = simplegui.load_image(shipImageURL)
        self.widthHeightDest = (70, 70)
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

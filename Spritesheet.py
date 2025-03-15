import simplegui

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
        
    def draw(self, canvas, limit):
        if self.orgSize[0] > 0:
            sourceCentre = (
                self.frameIndex[0] * self.frameWidth + self.frameCentreX,
                self.frameIndex[1] * self.frameHeight + self.frameCentreY
            )
            sourceSize = (self.frameWidth, self.frameHeight)
            canvas.draw_image(self.image, sourceCentre, sourceSize, self.centreDest, self.sizeDrawn, self.rotation)
            self.clock += 1
            if limit == "None":
                if self.clock == 20:
                    self.next()
                    self.clock = 0
            elif not limit == 0:
                if self.clock == 20:
                    self.next()
                    limit -= 1
                    self.clock = 0
        
    def next(self):
        if self.frameIndex[1] == self.rows - 1 and self.rows != 1:
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.extraFrames
        else:
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.columns
        if self.frameIndex[0] == 0:
            self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows

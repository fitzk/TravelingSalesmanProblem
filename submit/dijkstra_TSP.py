import math
Class Graph:
    def __init__(self):
        self.vertices = {}


Class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,x,y):
        return math.floor(math.sqrt(math.pow(self.x-x) + math.pow(self.y-y,2)))

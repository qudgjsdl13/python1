class Car:
    color=""
    speed=0


    def __init__(self):
        self.color ="Red"
        self.speed =50

    def upSpeed(self,value):
        self.speed +=value

    def downSpeed(self,value):
        self.speed -=value

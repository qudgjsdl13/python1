import io
import sys

sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")


class Car:
    name=""
    speed=0
    color=""

    def __init__(self,name,speed,color):
        self.name=name
        self.speed=speed
        self.color=color

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getColor(self):
        return self.color

car1=None
car2=None

car1=Car("아우디",0,"Red")
car2=Car("벤츠",30,"Blue")

print("%s의 현재 속도는 %d입니다. %s"%(car1.getName(),car1.getSpeed(),car1.getColor()))
print("%s의 현재 속도는 %d입니다. %s"%(car2.getName(),car2.getSpeed(),car2.getColor()))

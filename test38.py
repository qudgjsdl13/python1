import io
import sys

sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

class Car:
    speed=0
    def upSpeed(self,value):
        self.speed+=value

        print("현재 속도(슈퍼 클래스):%d"%self.speed)


class Sedan(Car):
    def upSpeed(self,value):
        self.speed+=value

        if self.speed>150:
            self.speed=150

            print("현재 속도(서브 클래스):%d"%self.speed)

class Truck(Car):
    pass

sedan1=None
truck1=None


truck1=Truck()
sedan1=Sedan()

print("트럭 -->", end="")
truck1.upSpeed(200)

print("승용차 -->", end="")
sedan1.upSpeed(200)

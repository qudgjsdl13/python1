import io
import sys

sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

from test34 import Car


myCar=Car()

myCar.color="Red"
myCar.speed=50

myCar.upSpeed(30)
myCar.downSpeed(8)

print("자동차의 색상은 %s 이며, 현재 속도는 %d km입니다." %(myCar.color,myCar.speed))
import io
import sys

sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

from test34 import Car


myCar=Car()

myCar.color="Red"
myCar.speed=15

myCar.upSpeed(30)
myCar.downSpeed(8)

print("자동차의 색상은 %s 이며, 현재 속도는 %d km입니다." %(myCar.color,myCar.speed))

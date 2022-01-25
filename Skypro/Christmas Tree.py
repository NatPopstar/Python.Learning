from turtle import * #посмотреть документацию turtle
from pygame import mixer
from random import random, randint
from time import sleep
import math

n = 80.0
speed(0)
ht() #hide - спрятать
window = Screen()
window.bgpic('chris.png')
window.setup(width=902, height=601)

mixer.init()
mixer.Channel(0).play(mixer.Sound("Hedwig's Theme.mp3"))

#отрисовка звезды
lt(90)
fd(3*n)
color("orange", "yellow")
begin_fill()
lt(126)
for i in range(5):
	fd(n/5)
	rt(144)
	fd(n/5)
	lt(72)
end_fill()
rt(126)

color('ivory')
bk(n*4.8)

#рисуем елку
def tree(d, s):
	pensize(8)

	if d <= 0:
		return
	fd(s)
	tree(d - 1, s * .8)
	rt(120)
	tree(d - 3, s * .5)
	rt(120)
	tree(d - 3, s * .5)
	rt(120)
	bk(s)


tree(10, n)
bk(n / 2)

#рисуем сердечки
def heart():
	color("orange", "hot pink")
	pensize(2)
	d = 20
	r = d / math.tan(math.radians(67.5))
	up()
	seth(45)
	begin_fill()
	down()
	fd(d)
	circle(r, 225)
	lt(180)
	circle(r, 225)
	fd(d)
	end_fill()

	for i in range(50):
		a = 200 - 400 * random()
		b = -200 - 18 * random()
		up()
		goto(a, b)
		down()
		heart()
up()
pensize(2)

x_base = 50
x_mov = 90
year = "2022"

goto(x_base, 90)
for i in range(4):
    color("#FFD700", "#FFD700")
    write(year[i], move=False, align="left", font=("Arial", 122, "normal"))
    sleep(1)

    goto(x_base + 3, 90 - 3)
    color("#B29700", "#B29700")
    write(year[i], move=False, align="left", font=("Arial", 122, "normal"))
    sleep(1)

    x_base += x_mov
    goto(x_base, 90)

def move():
    up()
    x = randint(-450, 450)
    y = randint(-300, 300)
    goto(x, y)
    pd()


def firework(size):
    mixer.Channel(1).play(mixer.Sound("petardy.mp3"))
    for num in range(30):
        fd(size)
        rt(180 - (360 / 20))


# Begin Config #
C_BRIGHT_MIN = 0x10
C_BRIGHT_MAX = 0xef
F_SIZE_MIN = 15
F_SIZE_MAX = 200
FIREWORK_PER_CLEAR = 2
count = 1
# End Config #

while count <= 20:
    # this generates a random color sequence using RGB
    color_r = hex(randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
    color_g = hex(randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
    color_b = hex(randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
    color('#' + color_r + color_g + color_b)
    sleep(randint(3, 8))
    for i in range(FIREWORK_PER_CLEAR):
        firework(randint(F_SIZE_MIN, F_SIZE_MAX))
        move()
    count += 1

exitonclick()


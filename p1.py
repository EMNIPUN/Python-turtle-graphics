import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(200)
t.pensize(0.5)
def draw():
    h = 0
    n = 700
    t.up()
    t.goto(420,-20)
    t.down()
    for i in range(1000):
        c = colorsys.hsv_to_rgb(h,1,1)
        t.color(c)
        h += 1/n
        t.circle(i,179)
        t.fd(65)
        t.bk(27)
        t.circle(229,121)
draw()
t.done
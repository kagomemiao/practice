import turtle

def sier(l, d):
    if d == 0:
        t.begin_fill()
        for i in range(0,3):
            t.fd(l)
            t.left(120)
        t.end_fill()

    else:
        sier(l/2,d-1)
        t.fd(l/2)
        sier(l/2,d-1)
        t.bk(l/2)
        t.left(60)
        t.fd(l/2)
        t.right(60)
        sier(l/2,d-1)
        t.left(60)
        t.bk(l/2)
        t.right(60)

window = turtle.Screen()
t = turtle.Turtle()
t.color("blue","green")
t.speed(0)
sier(200,3)
window.exitonclick()

import turtle


def lit_tri(param):
    for i in range(1,4):
        param.forward(30)
        param.right(120)

def draw_tri():
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("blue","green")
    t.shape("turtle")
    
    #t.right(60)
    #lit_tri(t)


    window.exitonclick()

draw_tri()

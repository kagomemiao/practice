import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)
        
def draw_scircle(some_turtle):
    for k in range(1,37):
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)
        some_turtle.right(10)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    s = turtle.Turtle()
    s.shape("turtle")
    s.color("yellow")
    s.speed(1)
    draw_square(s)
    
    c = turtle.Turtle()
    c.shape("circle")
    c.color("blue")
    c.speed(1)
    c.circle(100)

    t = turtle.Turtle()
    t.shape("triangle")
    t.color("black")
    t.speed(1)
    draw_triangle(t)

    sc = turtle.Turtle()
    sc.shape("triangle")
    sc.color("black")
    sc.speed(0)
    for i in range(1,37):
        draw_square(sc)
        sc.right(10)

    window.exitonclick()
    
draw_art()

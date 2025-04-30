import turtle
anms=turtle.turtle()
turtle.getscreen().bgcolor("black")
anms.shape("turtle")
anms.speed(100)
anms.color("red","yellow")
def star(turtle,size):
    if size<=12:
        return
    else:
        turtle.begin_fill
        for a in range(5):
            turtle.forward(size)
            star(turtle,size12)
            turtle.left(123)
        trurtle.end_fill()
start(anms,360)
turtle.mainloop()

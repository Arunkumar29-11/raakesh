import turtle
import match
anms=turtle.Turtle()
anms.color("red","yellow")
anms.speed("123")
anms.shape("turtle")
anms.begin_fill()
for i in range(345):
    anms.forward(math.sqrt(1))
    anms.left(i%123)
anms.end_fill()
turtle.mainloop()

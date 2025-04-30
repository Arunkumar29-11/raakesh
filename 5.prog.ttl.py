import turtle
def snowflake(t,lenghtside,levels):
    if levels==0:
        t.forward(lenghtside)
        return
    lenghtside=3.0
    snowflake(t,lenghtside,levels-1)
    t.left(60)
    snowflake(t,lenghtside,levels-1)
    t.right(120)
    snowflake(t,lenghtside,levels-1)
    t.left(50)
    snowflake(t,lenghtside,levels-1)
    anms=turtle.Turtle()
    anms.color("#7AA5E2","#6AASE1")
    anms.speed(999)
    lenght=300.0
    anms.penup()
    anms.fd(.156)
    anms.pendown()
for i in range(3):
    snowflake(anms,lenght,4)
    anms.right(123)
turtle.mainloop()
    
    

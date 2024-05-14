import turtle

def main():
    t = turtle.Turtle()
    t.speed(0) 

    #Initial parameters
    size = 700

    period1 = 7   #period of base (fabric) layer
    col1 = size//period1

    period2 = 11   #period of revealing layer (3D-printed grid)
    col2 = size//period2
    angle = 1.5   #angle in degrees


    t.up()
    t.goto(x=-(size//2), y=-(size//2))
    t.width(3.5)
    #t.color('red')

    for i in range(col1//2):
        t.down()
        t.forward(size)
        t.up()
        t.left(90)
        t.forward(period1)
        t.left(90)
        t.down()
        t.forward(size)
        t.up()
        t.right(90)
        t.forward(period1)
        t.right(90)

    t.up()
    t.goto(x=-(size//2), y=-(size//2))
    t.left(angle)
    t.width(3.5)
    #t.color("blue")

    for i in range(col2//2):
        t.down()
        t.forward(size)
        t.up()
        t.left(90)
        t.forward(period2)
        t.left(90)
        t.down()
        t.forward(size)
        t.up()
        t.right(90)
        t.forward(period2)
        t.right(90)

    turtle.done()

if __name__ == "__main__":
    main()

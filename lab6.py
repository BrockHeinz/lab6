import turtle


def main():
    stars_file = open('./draw_stars/stars.txt', 'r')
    stars = []
    for line in stars_file:
        stars.append(line[0:len(line) - 1].split(" "))
    stars_file.close()
    print(stars[0])
    # this is the turtle object
    # You'll call its methods to draw like t.goto()
    t = turtle.Turtle()
    turtle.bgcolor('black')
    turtle.screensize(500, 500)
    turtle.speed(0)
    turtle.tracer(1, 0)
    t.color('white')
    for star in stars:
        jump(t, float(star[0]) * 250, float(star[1]) * 250)
        size = 10 / (float(star[4]) + 2)
        size *= (float(star[2]) + 1) / 2
        size = min(10, max(size, 1))
        if size > 1:
            square(t, size)
        else:
            t.fd(1)
    # Causes the drawing area to stay until you click on it
    # This should be the absolute LAST thing that you call
    # in your program after all of the drawing is over.
    turtle.exitonclick()


def jump(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()


def square(turt, side):
    offset = side / 2
    jump(turt, turt.xcor() - offset, turt.ycor() - offset)
    turt.seth(90)
    turt.begin_fill()
    for _ in range(4):
        turt.fd(side)
        turt.right(90)
    turt.end_fill()
    jump(turt, turt.xcor() + offset, turt.ycor() + offset)


if __name__ == '__main__':
    main()

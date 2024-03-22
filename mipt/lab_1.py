import turtle


def draw_polygons():
    for angle in range(3, 14):
        for _ in range(angle):
            turtle.forward(50)
            turtle.left(360/angle)
        turtle.penup()
        turtle.goto(-10, -10)
        turtle.pendown()


draw_polygons()

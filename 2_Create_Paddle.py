from turtle import Turtle, Screen


screen = Screen()

screen.bgcolor("black")
screen.title("Welcome to the Pong")
screen.setup(width=800, height=600)
screen.tracer(0)




def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()

from turtle import Turtle as T, Screen as S

tommy = T()
tommy.shape("triangle")
tommy.color("blue")

for _ in range(15):
    tommy.forward(10)
    tommy.pendown()
    tommy.forward(10)
    tommy.penup()

screen = S()
screen.exitonclick()

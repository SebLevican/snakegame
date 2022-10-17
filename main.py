from turtle import Screen
import time
from snake import snake
from food import Food
from scoreboard import score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snake game')

snake = snake()
food = Food()
score = score()

screen.listen()
screen.onkey(snake.Up,'Up')
screen.onkey(snake.Down, 'Down')
screen.onkey(snake.Left, 'Left')
screen.onkey(snake.Right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detec collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()

    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            snake.reset()




screen.exitonclick()
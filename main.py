from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moving segments on screen
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.segments[0].xcor() > 288 or snake.segments[0].xcor() < -288 or snake.segments[0].ycor() > 288 or snake.segments[0].ycor() < -288:
        game_is_on = False
        scoreboard.game_over()

    # Detecting collisions with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

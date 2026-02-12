from turtle import Screen
import time
from scoreBoard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("SnakeWorld")
screen.tracer(0)
sleeptime = 0.3
# turtle.tracer(n, delay) n=update the screen after n turtle actions, delay= time in ms
#with tracer = 0 (animations are off) fastest
score = ScoreBoard()
snake = Snake(screen)
food = Food()
food.refresh()

game_over = False
while not game_over:
    screen.update()
    time.sleep(sleeptime)
    snake.move()
    snake.binding_keys()
    if snake.segments[0].distance(food) < 15:

        snake.increase_length()
        food.refresh()
        score.increase_score()

    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -285:
        score.game_over()
        game_over = True

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.game_over()
            game_over = True

screen.exitonclick()








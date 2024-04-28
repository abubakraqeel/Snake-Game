from turtle import Turtle, Screen
import random, time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)



snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
i = 0
while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    #function to detect collision with wall
    
    
    #detect collision with food
    if snake.head.distance(food)<15:
        i+=1
        food.new_food()
        score.update_score()
        snake.length()

    #detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()
        
    snake.wall_collision()    

        





screen.exitonclick()
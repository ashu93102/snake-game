import turtle as t
import time
import snake
import food
import scoreboard as sco

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = sco.Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if (snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 270 or
            snake.segment[0].ycor() < -280):
        game_on = False
        score.game_over()

    # Detect collision with tail.
    # Slicing [1 : ] this will check all items in list except item at 0 position.
    for seg in snake.segment[1:]:
        # Slicing list to bypass below if statement.
        # if seg == snake.segment[0]:
        #     pass
        if snake.segment[0].distance(seg) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()

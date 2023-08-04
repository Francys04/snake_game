"""Built-in module that provides functions to generate random numbers and perform random selections."""
import random
"""Built-in module that provides various functions to work with time-related operations, 
including measuring time intervals, suspending program execution, and converting time values."""
import time
from main import *


# main loop
while True:
    screen.update()

    #  snake and fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        scoring.clear()
        score += 1

        scoring.write("Score: {}".format(score), align="center", font=("Coursier", 24, "bold"))
        delay -= 0.001

        # creating new foods
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # adding ball to snake

    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    # snake and border collision

    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("    Game Over  \n Your score is {}".format(score), align="center",
                      font=("Coursera", 30, "bold"))

    # snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("    Game Over  \n Your score is {}".format(score), align="center",
                          font=("Coursera", 30, "bold"))

    time.sleep(delay)

    turtle.Terminator()
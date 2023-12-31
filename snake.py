import turtle as t

STARTING_POS = [(0, 0), (-20, 0), (-40, 0), ]
MOVE_DISTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        super().__init__()
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """Create 3 turtle and sets its color and append it into segment list"""
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        """Create snake"""
        snake = t.Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.segment.append(snake)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        """This function is allow 2 and 3 turtle to follow 1 turtle"""
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)

        self.segment[0].forward(MOVE_DISTANT)

    def up(self):
        """This is used to move turtle up"""
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        """This is used to move turtle down"""
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def right(self):
        """This is used to move turtle right"""
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def left(self):
        """This is used to move turtle left"""
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

from turtle import *

class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return False if self.items else True


class State:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f"({self.x}, {self.y}, {self.angle})"

    def __repr__(self):
        return f"State({self.x}, {self.y}, {self.angle})"

    def set_state(self, t: Turtle):
        self.x, self.y = t.position()
        self.angle = t.heading()

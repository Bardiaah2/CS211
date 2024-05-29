from typing import *
import turtle


class LSystem:
    """
    Represents an L-system with its axiom, rules, rewriting,
    and drawing methods.
    """

    def __init__(self, axiom, rules, angle, step, n=3,
    starting_pos=(-200, 0), starting_angle=0, color="blue"):
        self.axiom: str = axiom
        self.rules: dict = rules
        self.angle: int | float = angle
        self.step: int = step
        self.n: int = n
        self.starting_pos: Tuple[int, int] = starting_pos
        self.starting_angle: int = starting_angle
        self.color: str = color

    def iterate(self):
        while self.n:
            self.commands = self.axiom.translate(self.rules)
            self.n -= 1

    def draw(self):
        moves = {'F': turtle.forward(10), '+': turtle.left(self.angle), "-": turtle.right(self.angle)}

        for move in self.commands:
            moves[move]

        turtle.mainloop()

    def plot(self):
        pass



    
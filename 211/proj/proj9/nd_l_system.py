from typing import *
import turtle
import state
import random


class LSystem:
    """
    Represents an L-system with its axiom, rules, rewriting,
    and drawing methods.
    """

    def __init__(self, axiom, rules, angle, step, n=3,
    starting_pos=(0, -200), starting_angle=90, color="blue"):
        self.axiom: str = axiom
        self.rules: dict = rules
        self.angle: int | float = angle
        self.step: int = step
        self.n: int = n
        self.starting_pos: Tuple[int, int] = starting_pos
        self.starting_angle: int = starting_angle
        self.color: str = color

    def iterate(self):
        new_rules = {}
        self.commands = self.axiom

        for _ in range(self.n):
            for key in self.rules.keys():
                new_rules[key] = random.choices([i[1] for i in self.rules[key]], [i[0] for i in self.rules[key]])[0]

            self.commands = self.commands.translate({ord(c): y for (c, y) in new_rules.items()})

    def draw(self):
        t = turtle.Turtle()
        t.speed(0)
        t.pu()
        t.setposition(self.starting_pos)
        t.pd()
        t.setheading(self.starting_angle)
        t.color(self.color)

        states = state.Stack()

        moves = {'F': (t.forward, self.step), '+': (t.left, self.angle), "-": (t.right, self.angle)}

        for move in self.commands:
            if move == 'f':
                t.pu()
                moves['F'][0](moves['F'][1])
                t.pd()
                continue

            elif move == '[':
                states.push(state.State(t.xcor(), t.ycor(), t.heading()))
                continue

            elif move == ']':
                t.pu()
                new_state = states.pop()
                t.goto(new_state.x, new_state.y)
                t.setheading(new_state.angle)
                t.pd()
                continue

            if move in moves.keys():

                moves[move][0](moves[move][1])

            else:
                continue

        turtle.exitonclick()

    def plot(self):
        self.iterate()
        self.draw()


if __name__ == '__main__':
    # ls1 = LSystem(axiom="-L",
    # rules={"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "-LFLF+RFRFR+F+RF-LFL-FR"},
    # angle=90, step=10, n=3
    # )
    # ls1.plot()

    nd_ls_1 = LSystem(axiom="F",
    rules = {"F": [(.33, "F[+F]F[-F]F"), (.33, "F[+F]F"), (.33, "F[-F]F")]},
    angle=25.7, step=10, n = 5
    )

    nd_ls_2 = LSystem(axiom="X",
                     rules = {'X': "F[+X][-X]FX", "F": "FF"},
                     angle=25.7,
                     step=10,
                     n=7)
    nd_ls_1.plot()

from typing import *
import turtle
import state


class LSystem:
    """
    Represents an L-system with its axiom, rules, rewriting,
    and drawing methods.
    """

    def __init__(self, axiom, rules, angle, step, n=3,
    starting_pos=(-200, -800), starting_angle=90, color="blue"):
        self.axiom: str = axiom
        self.rules: dict = rules
        self.angle: int | float = angle
        self.step: int = step
        self.n: int = n
        self.starting_pos: Tuple[int, int] = starting_pos
        self.starting_angle: int = starting_angle
        self.color: str = color

    def iterate(self):
        self.commands = self.axiom.translate({ord(c): y for (c, y) in self.rules.items()})

        for _ in range(self.n - 1):
            self.commands = self.commands.translate({ord(c): y for (c, y) in self.rules.items()})
        print(self.commands)

    def draw(self):
        t = turtle.Turtle()
        # t.speed(0)
        t.pu()
        t.setposition(self.starting_pos)
        t.pd()
        t.setheading(self.starting_angle)
        t.color(self.color)

        states = state.Stack()
        last_state = state.State()

        moves = {'F': (t.forward, self.step), '+': (t.left, self.angle), "-": (t.right, self.angle)}

        for move in self.commands:
            if move == 'f':
                t.pu()
                moves['F'][0](moves['F'][1])
                t.pd()

            elif move == '[':
                last_state.set_state(t)
                states.push(last_state)

            elif move == ']':
                t.pu()
                new_state = states.pop()
                t.goto(new_state.x, new_state.y)
                t.setheading(new_state.angle)
                t.pd()

            if move in moves.keys():

                moves[move][0](moves[move][1])

        turtle.exitonclick()

    def plot(self):
        self.iterate()
        self.draw()


if __name__ == '__main__':
    ls1 = LSystem(axiom="-L",
    rules={"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "-LFLF+RFRFR+F+RF-LFL-FR"},
    angle=90, step=10, n=3
    )
    # ls1.plot()

    ls2 = LSystem(axiom="X", 
                     rules = {'X': "F[+X][-X]FX", "F": "FF"},
                     angle=25.7,
                     step=5,
                     n=7)
    
    ls3 = LSystem(axiom="F", 
                     rules = {"F": "F[+F]F[-F]F"},
                     angle=25.7,
                     step=10,
                     n=5)
    ls3.plot()



"""Reverse Polish Notation calculator.

"""

from calculator.expr import *
from typing import List

def is_binop(op:str)->bool:
    pass

def is_unop(op:str)->bool:
    pass

def is_var(op:str)->bool:
    pass

def binop_class(op:str)->"BinOp":
    pass

def unop_class(op:str)->"UnOp":
    pass

def rpn_parse(text: str) -> List[Expr]:
    """Parse text in reverse Polish notation
    into a list of expressions (exactly one if
    the expression is balanced).
    Example:
        rpn_parse("5 3 + 4 *")
          => [ Times(Plus(IntConst(5), IntConst(3)), IntConst(4))))]
    """
    pass

def calc(text: str):
    """Read and evaluate a single line formula."""
    pass

def rpn_calc():
    pass


if __name__ == "__main__":
    """RPN Calculator as main program"""
    rpn_calc()

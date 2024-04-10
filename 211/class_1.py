from functools import singledispatchmethod

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @singledispatchmethod
    def move(self, d: "Point") -> "Point":
        x = self.x + d.x
        y = self.y + d.y
        return Point(x, y)

    @move.register
    def _(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def __eq__(self, __value: object) -> bool:
        return (self.x == __value.x and self.y == __value.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
#-----------------------------------------------------------#

def all_same(l: list) -> bool:
    i, j = 0 ,1
    if len(l) > 1:
        while j < len(l):
            if l[i] != l[j]:
                return False
            i += 1
            j += 1
    
    return True

def dedup(l: list) -> list:
    i, j = 0, 1
    l_copy = l[:]

    if len(l_copy) > 1:

        while j < len(l_copy):

            if l_copy[i] == l_copy[j]:
                del l_copy[j]

            else:
                i += 1
                j += 1
    
    return l_copy

def max_run(l: list) -> int:
    i, j = 0, 1
    curr_max = 0
    if len(l) >= 1:
        curr_max += 1
        while j < len(l):
            
            if l[i] == l[j]:
                j += 1
            else:
                curr_max = max(curr_max, j-i)
                i = j
                j += 1
        curr_max = curr_max = max(curr_max, j-i)
    
    return curr_max

if __name__ == '__main__':
    p = Point(3, 4)
    v = Point(5, 6)
    m = p.move(v)
    p.move(2, 2)
    print(p)
    print(m)

    assert m.x == 8 and m.y == 10

    #-------------------------------------------------------#
    print("all_same:")
    print(all_same([1, 1 ,1, 1]),
          all_same([]), 
          all_same([1, 3, 1]))
    
    print('dedup:')
    print(dedup([1, 1, 2, 1, 1]))
    print(dedup([1]))

    print('max_run:')
    print(max_run([1, 1, 3, 3, 3, 5])) # 3
    print(max_run([3, 4, 5, 5, 5])) # 3
    print(max_run([])) # 0

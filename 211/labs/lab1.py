"""Closed intervals of integers
Bardia Ahmadi Dafchahi, date, CIS 211
"""

class Intervals:
    """An interval [m..n] represent the set of integers
    from m to n.
    """
    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high
        
        if low > high:
            raise ValueError("The low value of the interval cannot be higher than the high value.")
        
    def contains(self, i: int) -> bool:
        return i in range(self.low, self.high+1)
    
    def overlaps(self, other: "Intervals") -> bool:
        if other.low in range(self.low, self.high+1) or other.high in range(self.low, self.high+1):
            return True
        if other.low < self.low and other.high > self.high:
            return True
        return False
        
    def __eq__(self, __value: object) -> bool:
        return (self.low == __value.low and self.high == __value.high)
    
    def join(self, other: "Intervals") -> "Intervals":
        low = min(self.low , other.low)
        high = max(self.high, other.high)
        return Intervals(low, high)
    
    def __str__(self) -> str:
        return f"[{self.low}..{self.high}]"
    
    def __repr__(self) -> str:
        return f"Interval ({self.low}, {self.high})"
    
    
if __name__ == '__main__':
    i = Intervals(3, 5)
    print(i)  # [3..5]
    print(i.contains(4))  # True
    print(i.contains(2))  # False
    m = Intervals(2, 4)
    n = i.join(m)
    print(n)  # [2..5]
    print(i.overlaps(m))  # True
    
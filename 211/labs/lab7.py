""" Lab 06 BinaryNumbers
    Harsha Siddagangaiah
"""
from typing import List

class BinaryNumber:

    def __init__(self, bits: List[int]):
        self.bits = bits

    def __str__(self):
        return f"{self.bits}"

    def __or__(self, other):
        bitArray = []
        if len(self.bits) != len(other.bits):
            raise ValueError("")
        for i in range(0, len(self.bits)):
            if self.bits[i] == 0 and other.bits[i] == 0:
                bitArray.append(0)
            else:
                bitArray.append(1)
        return BinaryNumber(bitArray)

    def __and__(self, other):
        bitArray = []
        if len(self.bits) != len(other.bits):
            raise ValueError("")
        for i in range(len(self.bits)):
            if not self.bits[i] or not other.bits[i]:
                bitArray.append(0)
            else:
                bitArray.append(1)
        return BinaryNumber(bitArray)

    def left_shift(self):
        self.bits[:-1] = self.bits[1:]
        self.bits[-1] = 0

    def right_shift(self):
        self.bits[1:] = self.bits[:-1]
        self.bits[0] = 0

    def extract(self, start: int, end: int):
        slice = self.bits[-end-1:-start]
        return BinaryNumber([0 for _ in range(len(self.bits) - (end - start + 1))] + slice)


if __name__ == "__main__":
    # execute and verify

    bn = BinaryNumber([1, 0, 1, 0, 1])
    bn2 = BinaryNumber([1, 1, 1, 0, 0])
    print("1st binary number =", bn)

    print("2nd binary number =", bn2)

    print("AND", bn & bn2)
    print("OR", bn | bn2)

    bn.right_shift()
    print("1st number right-shifted =", bn)

    bn.left_shift()
    print("1st number left-shifted =", bn)

    bn = BinaryNumber([1, 0, 0, 1, 0, 1, 1, 1])
    extracted = bn.extract(2, 4)
    print(extracted)

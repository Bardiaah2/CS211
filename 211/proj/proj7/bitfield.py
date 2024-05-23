"""
A bit field is a range of binary digits within an
unsigned integer. Bit 0 is the low-order bit,
with value 1 = 2^0. Bit 31 is the high-order bit,
with value 2^31.

A bitfield object is an aid to encoding and decoding
instructions by packing and unpacking parts of the
instruction in different fields within individual
instruction words.

Note that we are treating Python integers as if they
were 32-bit unsigned integers.  They aren't ... Python
actually uses a variable length signed integer
representation, but we ignore that because we are trying
to simulate a machine-level representation.
"""

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

WORD_SIZE = 32

def sign_extend(field: int, width: int) -> int:
    """Interpret field as a signed integer with width bits.
    If the sign bit is zero, it is positive.  If the sign bit
    is negative, the result is sign-extended to be a negative
    integer in Python.
    width must be 2 or greater. field must fit in width bits.
    Sign extension is a little bit wacky in Python, because Python
    doesn't really use 32-bit integers ... rather it uses a special
    variable-length bit-string format, which makes *most* logical
    operations work in the extpected way  *most* of the time, but
    with some differences that show up especially for negative
    numbers.  I've written this sign extension function for you so
    that you don't have to spend time plotting a way to make it work.
    You'll probably want to convert it to a method in the BitField
    class.

    Examples:
       Suppose we have a 3 bit field, and the field
       value is 0b111 (7 decimal).  Since the high
       bit is 1, we should interpret it as
       -2^2 + 2^1  + 2^0, or -4 + 3 = -1

       Suppose we hve the same value, decimal 7 or
       0b0111, but now it's in a 4 bit field.  In thata
       case we should interpret it as 2^2 + 2^1 + 2^0,
       or 4 + 2 + 1 = 7, a positive number.

       Sign extension distinguishes these cases by checking
       the "sign bit", the highest bit in the field.

    """
    assert width > 1
    assert field >= 0 and field < 1 << (width + 1)
    sign_bit = 1 << (width - 1) # will have form 1000... for width of field
    mask = sign_bit - 1         # will have form 0111... for width of field
    if (field & sign_bit):
        # It's negative; sign extend it
        extended = (field & mask) - sign_bit
        return extended
    else:
        return field

class BitField(object):
    """A BitField object extracts specified
    bitfields from an integer.
    """
    def __init__(self, from_bit: int, to_bit: int) -> None:
        """Tool for  extracting bits
        from_bit ... to_bit, where 0 is the low-order
        bit and 31 is the high-order bit of an unsigned
        32-bit integer. For example, the low-order 4 bits
        could be represented by from_bit=0, to_bit=3.
        """
        # The constructor should take two integers, from_bit and to_bit,
        # indicating the bounds of the field.  Unlike a Python range, these
        # are inclusive, e.g., if from_bit=0 and to_bit = 4, then it is a
        # 5 bit field with bits numbered 0, 1, 2, 3, 4.

        # You might want to precompute some additional values in the constructor
        # rather than recomputing them each time you insert or extract a value.
        # I precomputed the field width (used in several places), a mask (for
        # extracting the bits of interest), the inverse of the mask (for clearing
        # a field before I insert a new value into it), and a couple of other values
        # that could be useful to have in sign extension (see the sign_extend
        # function below).
        self.from_bit = from_bit
        self.to_bit = to_bit


    def extract(self, word: int) -> int:
        """Extract the bitfield and return it in the
        low-order bits.  For example, if we are extracting
        bits 3..5, the result will be an
        integer between 0 and 7 (0b000 to 0b111).
        """
        a = sum([2 ** i for i in range(self.from_bit, self.to_bit+1)])
        extracted = a & word
        return extracted >> self.from_bit

    def insert(self, value: int, word: int) -> int:
        """Insert value, which should be in the low order
         bits and no larger than the bitfield, into the
         bitfield, which should be zero before insertion.
         Returns the combined value.
         Example: BitField(3,5).insert(0b101, 0b110) == 0b101110
        """
        # method insert takes a field value (an int) and a word (an int)
        # and returns the word with the field value replacing the old contents
        # of that field of the word.
        # For example,
        #   if word is   xaa00aa00 and
        #   field_val is x0000000f
        #   and the field is bits 4..7
        #   then insert gives xaa00aaf0

        # shift the value by from_bit
        if value < 0:
            value = 2 ** 31 + value - 1
            value = self.extract(value)
        value = value << self.from_bit

        # cut the word in two, 0 - from_bit-1 and to_bit+1 - END
        right_half, left_half = BitField(0, self.from_bit-1).extract(word), BitField(self.to_bit+1, WORD_SIZE).extract(word)

        # shift the left half by to_bit+1
        left_half = left_half << self.to_bit+1

        # return the sum of all
        return right_half + value + left_half


    def extract_signed(self, word: int) -> int:
        """Extract bits in bitfield as a signed integer."""
        # method extract takes a word and returns the value of the field
        # (which was set in the constructor)
        #
        # method extract_signed does the same as extract, but then if the
        # sign bit of the field is 1, it sign-extends the value to form the
        # appropriate negative integer.  extract_signed could call the function
        # extract_signed below, but you may prefer to incorporate that logic into

        # make a list of the 0s and 1s in word
        extracted = [int(i) for i in bin(self.extract(word))[2:]]
        res = 0

        # go through the made list and subtract the first one and add the rest in a accumilator pattern
        for i, num in enumerate(extracted):
            if i == 0 and self.to_bit - self.from_bit + 1 == len(extracted):
                res -= 2 ** (len(extracted) - 1) * num
                continue
            res += 2 ** (len(extracted) - 1 -i) * num

        # return the sum
        return res

if __name__ == '__main__':
    obj = BitField(3, 5)
    print(obj.extract(0b000010111))
    print(BitField(3,5).insert(-1, 0), bin(BitField(3,5).insert(-1, 0)), BitField(3,5).insert(-1, 0) == 56)

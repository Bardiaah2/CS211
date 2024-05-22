import unittest
from instr_format import *

class TestDecode(unittest.TestCase):
    """Encoding and decoding should be inverses"""
    def test_encode_decode(self):
        instr = Instruction(OpCode.SUB, CondFlag.M | CondFlag.Z, NAMED_REGS["r2"], NAMED_REGS["r1"], NAMED_REGS["r3"], -12)
        word = instr.encode()
        text = str(decode(word))
        self.assertEqual(text, str(instr))


if __name__ == '__main__':
    unittest.main()
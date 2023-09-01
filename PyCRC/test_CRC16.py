from unittest import TestCase

from PyCRC.CRC16 import CRC16


class CRC16Test(TestCase):
    def test_golden_values(self):
        crc16 = CRC16()

        values = [
            (b'', 0),
            (bytes.fromhex('ff'), 16448),
            (bytes.fromhex('ffffffffffffffff'), 33857),
            (bytes.fromhex('00'), 0),
            (bytes.fromhex('0000000000000000'), 0),
            (bytes.fromhex('12345670'), 62074),
            (bytes.fromhex('5A261977'), 42424),
            (bytes.fromhex('df51133927072dfcd42544b59cb4d534'), 59555),
            (bytes.fromhex('b401d9527713ea3dede1a26aee7a1ddb'), 50444),
            (bytes.fromhex('fca34da5898bd779d5'), 37946),
            (bytes.fromhex('f9f443c3738fca34da5898bd779d5d9eff943d1cc952009b895641660cc79b5f9cc5a9fbca57582970589459a419aa99b2848cf66a7b0f207b0cc7ee7c221fd8df51133927072dfcd42544b59cb4d534f55fc15779555a55de25d2fc08bf830ce2e60562b60d19540194767ff7d0637ff4487016bf0b521ae717dc4a0995c6e4b401d9527713ea3dede1a26aee7a1ddb8388399ce86c232f13b60207652be388'), 28022),
        ]

        for inp, expected_out in values:
            output = crc16.calculate(inp)
            print("CRC16({}) = {}".format(inp.hex(), output))
            self.assertEqual(output, expected_out)

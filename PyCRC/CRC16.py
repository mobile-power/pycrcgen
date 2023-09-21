# -*- coding: utf8 -*-

#
# CRC16 MODULE
#
# includes CRC16 and CRC16 MODBUS
#

from ctypes import c_ushort
from typing import Union, List


class CRC16(object):
    crc16_tab: List[int] = []

    # The CRC's are computed using polynomials. Here is the most used
    # coefficient for CRC16
    crc16_constant = 0xA001  # 40961

    def __init__(self, modbus_flag=False):
        # initialize the precalculated tables
        if not len(self.crc16_tab):
            self.init_crc16()
        self.mdflag = bool(modbus_flag)

    def calculate(self, input_data: Union[bytes, str]):
        if isinstance(input_data, str):
            input_data = input_data.encode('ascii')

        crcValue = 0x0000 if not self.mdflag else 0xffff

        crc16_tab = self.crc16_tab
        for d in input_data:
            crcValue = ((crcValue >> 8) & 0xFFFF) ^ crc16_tab[(crcValue ^ d) & 0x00ff]

        return crcValue

    def init_crc16(self):
        '''The algorithm uses tables with precalculated values'''
        for i in range(0, 256):
            crc = c_ushort(i).value
            for j in range(0, 8):
                if (crc & 0x0001):
                    crc = c_ushort(crc >> 1).value ^ self.crc16_constant
                else:
                    crc = c_ushort(crc >> 1).value
            self.crc16_tab.append(crc)

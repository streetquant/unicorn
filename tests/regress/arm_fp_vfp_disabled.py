#!/usr/bin/python
# coding=utf8

# Added by Peter Mackay, relating to issue 571
# "ARM NEON/VFP support seems to exist but is disabled by default"
# https://github.com/unicorn-engine/unicorn/issues/571

from unicorn import *
from unicorn.arm_const import *

import regress

class FpVfpDisabled(regress.RegressTest):

    def runTest(self):
        code = '11EE501F' + '41F47001'
        code += '01EE501F'
        code += '4FF00001'
        code += '07EE951F'
        code += '4FF08040'
        code += 'E8EE100A'
        # vpush {d8}
        code += '2ded028b'

        address = 0x1000
        mem_size = 0x1000
        code_bytes = code.decode('hex')

        uc = Uc(UC_ARCH_ARM, UC_MODE_THUMB)
        uc.mem_map(address, mem_size)
        uc.mem_write(address, code_bytes)
        uc.reg_write(UC_ARM_REG_SP, address + mem_size)
        uc.emu_start(address + 1, address + len(code_bytes))

if __name__ == '__main__':
    regress.main()

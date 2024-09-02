from __future__ import annotations
from typing import Union

class Machine_code():
    
    __comp_to_binary = {
            '0'     : '0101010',
            '1'     : '0111111',
            '-1'    : '0111010',
            'D'     : '0001100',
            'A'     : '0110000',
            'M'     : '1110000',
            '!D'    : '0001101',
            '!A'    : '0110001',
            '!M'    : '1110001',
            '-D'    : '0001111',
            '-A'    : '0110011',
            '-M'    : '1110011',
            'D+1'   : '0011111',
            'A+1'   : '0110111',
            'M+1'   : '1110111',
            'D-1'   : '0001110',
            'A-1'   : '0110010',
            'M-1'   : '1110010',
            'D+A'   : '0000010',
            'D+M'   : '1000010',
            'D-A'   : '0010011',
            'D-M'   : '1010011',
            'A-D'   : '0000111',
            'M-D'   : '1000111',
            'D&A'   : '0000000',
            'D&M'   : '1000000',
            'D|A'   : '0010101',
            'D|M'   : '1010101',
            }

    __dest_to_binary = {
            ''   : '000',
            'M'  : '001',
            'D'  : '010',
            'MD' : '011',
            'A'  : '100',
            'AM' : '101',
            'AD' : '110',
            'AMD': '111',
            }

    __jump_to_binary = {
            ''   : '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
            }

    @classmethod
    def jump_value(cls, jmp_code: str) -> Union[str,None]:
        return cls.__jump_to_binary[jmp_code] if jmp_code in cls.__jump_to_binary else None

    @classmethod
    def comp_value(cls, comp_code: str) -> Union[str,None]:
        return cls.__comp_to_binary[comp_code] if comp_code in cls.__comp_to_binary else None

    @classmethod
    def dest_value(cls, dest_code: str) -> Union[str,None]:
        return cls.__dest_to_binary[dest_code] if dest_code in cls.__dest_to_binary else None

    @classmethod
    def value(cls, value: str) -> Union[str,None]:

#       One-liner
#       return bin(int(value))[2:].zfill(15)

        try:
            int_value = int(value) % 32768
            return_value = ''
            for i in range(14,-1,-1):
                if int_value >= 2 ** i:
                    return_value += '1'
                    int_value -= 2 ** i
                else:
                    return_value += '0'
            return return_value
        except:
            return None

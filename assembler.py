from __future__ import annotations
from typing import List

import argparse
import re
from parser import Parser
from machine_code import Machine_code

def main(fileName : str) -> None:

    PARSER = Parser(fileName)
    binary_instructions=[]
    while PARSER.has_more_instructions():

        instruction = PARSER.current_instruction()

        if instruction.type == 'A':
            binary_instruction = '0' + Machine_code.value(instruction.value)
        elif instruction.type == 'C':
            binary_instruction = '111' + Machine_code.comp_value(instruction.comp) + Machine_code.dest_value(instruction.dest) + Machine_code.jump_value(instruction.jump) 

        binary_instructions.append(binary_instruction)
        PARSER.advance()

    write_binary_instructions(fileName, binary_instructions)


def write_binary_instructions(fileName: str, binary_instructions: List[str]) -> None:

    output_file = re.search(r'(.*)\.asm', fileName).group(1) + '.hack'
    with open(output_file, 'w') as out:
        out.write('\n'.join(binary_instructions))


if __name__ == '__main__':

    # Parse the asm file
    parser = argparse.ArgumentParser()
    parser.add_argument('fileName.asm', help='Hack assembly program to be assembled')
    args = parser.parse_args()
    fileName = vars(args)['fileName.asm']

    if not re.match(r'.+\.asm', fileName):
        raise Exception("File extension has to be .asm")

    main(fileName)



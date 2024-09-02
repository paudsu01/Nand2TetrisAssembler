from __future__ import annotations
from typing import List
from instruction import Instruction
from symbol_table import Symbol_table

import re

class Parser:
    
    """ Init """ 
    def __init__(self, filename: str) -> None:

        with open(filename, 'r') as infile:
            assembly_lines = infile.readlines()

        # Initialize the symbol table
        self.__symbol_table = Symbol_table()

        # Add the labels and their respective values to the symbol table
        filtered_lines = self.__first_scan(assembly_lines)
        # Translate the labels and variables into their respective addresses
        self.__instructions = self.__second_scan(filtered_lines)

        # Initialize current pc and max pc
        self.__pc = len(self.__instructions) - 1
        self.__current_pc = 0

    """ Public methods"""

    def current_instruction(self) -> Instruction:
        return Instruction(self.__instructions[self.__current_pc])

    def has_more_instructions(self) -> bool:
        return True if self.__current_pc <= self.__pc else False

    def advance(self) -> None:
        if self.has_more_instructions():
            self.__current_pc += 1
        else:
            return None
    
    """ Private methods"""

    def __first_scan(self, lines : List[str]) -> List[str]:
        """ Removes comments and whitespaces
            Add labels into the symbol table """

        filtered_lines = []
        comment_pattern = re.compile(r'^(.*?)(//.*)?$')
        label_pattern = re.compile(r'^\(([^0-9][0-9A-Za-z._$:]*)\)$')

        for line in lines:
            no_whitespace = ''.join([i for i in line.strip() if i != ' '])
            # Ignore empty lines
            if no_whitespace != '':

                no_whitespace_and_no_comment = comment_pattern.search(no_whitespace).group(1)
                # Ignore commented lines
                if no_whitespace_and_no_comment != '':

                    # if label, add symbol and pc value to the hash map
                    if label_pattern.match(no_whitespace_and_no_comment):
                        label = label_pattern.search(no_whitespace_and_no_comment).group(1)
                        self.__symbol_table.add(label, len(filtered_lines))
                    else:
                        # else add filtered line to the filtered_lines list
                        filtered_lines.append(no_whitespace_and_no_comment)
        return filtered_lines

    def __second_scan(self, lines : List[str]) -> List[str]:
        """ Replace any variable/label names in A-instructions with their appropriate memory addresses"""
        """ Lookup in the symbol table, if it isn't there, it is a variable """

        filtered_lines = []
        a_instruction_pattern = re.compile(r'^@(.+)$')
        a_instruction_pattern_with_address = re.compile(r'^@[0-9]+$')
        current_free_memory = 16

        for line in lines:

            a_instruction = a_instruction_pattern.search(line)
            if a_instruction and not a_instruction_pattern_with_address.match(line):

                value = a_instruction.group(1)
                if self.__symbol_table.contains(value):
                    filtered_lines.append(f'@{self.__symbol_table.get_address(value)}')
                else:
                    filtered_lines.append(f'@{current_free_memory}')
                    self.__symbol_table.add(value, current_free_memory)
                    current_free_memory += 1
            else:
                filtered_lines.append(line)
        return filtered_lines

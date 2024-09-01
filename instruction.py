from __future__ import annotations
import re

class Instruction:

    def __init__(self, assembly: str) -> None:

        # 'A' for A-instructions, 'C' for C-Instructions
        Apattern = re.compile(r'^@(\d+)$')
        Cpattern = re.compile(r'^((M|D|MD|A|AM|AD|AMD)=)?(0|-?1|[-!]?[DAM]|[DAM][+-][1AM]|[AM]-D|D[&|][AM])(;(JGT|JEQ|JGE|JLT|JNE|JLE|JMP))?$')
        Apattern_match_object = Apattern.search(assembly)
        Cpattern_match_object = Cpattern.search(assembly)

        if Apattern_match_object:
            self.__type = 'A'
            self.__value = Apattern_match_object.group(1)
            
        elif Cpattern_match_object:
            self.__type = 'C'
            self.__dest = Cpattern_match_object.group(2)
            self.__comp = Cpattern_match_object.group(3)
            self.__jump = Cpattern_match_object.group(5)
        else:
            self.__type = None
    
    @property
    def type(self) -> str:
        return self.__type

    @property
    def value(self) -> str:
        # only for a instructions
        return self.__value if self.type == 'A' else None

    @property
    def dest(self) -> str:
        # only for c instructions with destinations
        return self.__dest if self.type == 'C' and self.__dest != '' else None
    
    @property
    def comp(self) -> str:
        return self.__comp if self.type == 'C' and self.__comp != '' else None
    
    @property
    def jump(self) -> str:
        return self.__jump if self.type == 'C' and self.__jump != '' else None

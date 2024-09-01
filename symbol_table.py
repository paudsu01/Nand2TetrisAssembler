from __future__ import annotations
from typing import Union, Dict

class Symbol_table:

    def __init__(self):
        
        self.__mapping = {
                'SP' : 0,
                'LCL' : 1,
                'ARG': 2,
                'THIS': 3,
                'THAT': 4,
                'SCREEN' : 16384,
                'KBD' : 24576
                }
        self.__create_mapping_for_r_values()

    def __create_mapping_for_r_values(self) -> None:

        for i in range(16):
            self.__mapping[f'R{i}'] = i
    
    @property
    def mapping(self) -> Dict:
        return self.__mapping

    def get_address(self, key: str) -> Union[None,int]:
        return self.mapping[key] if key in self.mapping else None

    def add(self, key: str, value: int) -> None:
        self.mapping[key] = value

    def contains(self, key: str) -> bool:
        return key in self.mapping

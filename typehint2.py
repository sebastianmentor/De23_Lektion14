# Lite lätt om typehint
from typing import Any
import math

def rolig_konkatenering(tal:int, s:str, f:float) -> str|None:
    """Konkatenerar ett tal med sig själv, tal måste vara större än 0"""
    if tal< 1: 
        return None
    else:
        return tal*str(tal)
    
roligt_tal1 = rolig_konkatenering(9, 'Bananer', 88.0)
print(roligt_tal1)
roligt_tal2 = rolig_konkatenering(0, 'abc', 0.1)
print(roligt_tal2)
# roligt_tal3 = rolig_konkatenering(2.5)
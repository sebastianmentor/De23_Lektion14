# Lite lätt om typehint
from typing import Any, List

MENINGEN_MED_LIVET:int = 42
alltiallo_var:Any = None
sträng_eller_int_eller_none: str|int|None = None

def inmatning_från_användare() -> str|int|None:
    inmatat = input("Skriv in något")

    if inmatat.isdigit(): 
        return int(inmatat)
    elif len(inmatat) < 12:
        return inmatat
    else:
        return None
    
def amazing_list_funk(tal:int) -> List[list[int]]:
    ...

inp = inmatning_från_användare()
print(inp, f"{type(inp)=}")

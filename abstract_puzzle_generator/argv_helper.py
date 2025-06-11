from typing import TypeVar, List
from collections.abc import Callable

T = TypeVar("T", int, float)



def cast_number(type: Callable[[str], T], number_str: str, default: T, minimum: T):
    try:
        value = max(minimum, type(number_str))
    except Exception:
        return default
    else:
        return value
        
def cast_bool(current_args: List[str]):
    return True if current_args[1].lower() == 'true' else False

def get_from_argvs(current_args: List[str], 
                   once_def: bool = True,
                   width_def: int = 82, 
                   height_def: int = 22, 
                   sleep_time_def: float = 1) -> tuple[bool, int, int, float]:

    once = once_def
    width = width_def
    height = height_def
    sleep_time = sleep_time_def
    
    match len(current_args):
        case 2: 
            once = cast_bool(current_args)
        case 3:             
            once = cast_bool(current_args)
            width = cast_number(int, current_args[2], width_def, 0)
        case 4: 
            once = cast_bool(current_args)
            width = cast_number(int, current_args[2], width_def, 0)
            height = cast_number(int, current_args[3], height_def, 0)
        case 5: 
            once = cast_bool(current_args)
            width = cast_number(int, current_args[2], width_def, 0)
            height = cast_number(int, current_args[3], height_def, 0)
            sleep_time = cast_number(float, current_args[4], sleep_time_def, 0.0)
        case _:
            pass
    
    
    return once, width, min(width, height), sleep_time


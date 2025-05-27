import numpy as np
from piece_key_constants import PIECE_KEY_BASE, PIECE_KEY_NUMBER_DIGITS, MAX_NUMBER_PIECE_KEYS

def int_to_significant(value:int)->str:
    if value < 0 or value >= MAX_NUMBER_PIECE_KEYS:
        raise ValueError()
    return np.base_repr(value,base=PIECE_KEY_BASE)
    
def pad_zeros(significant:str):

    if len(significant) > PIECE_KEY_NUMBER_DIGITS:
        raise ValueError()
    
    return ''.join(['0']*(PIECE_KEY_NUMBER_DIGITS - len(significant))) + significant
    


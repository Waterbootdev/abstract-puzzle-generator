from collections.abc import Callable
from piece_key_constants import PIECE_KEY_NUMBER_DIGITS
from piece_keys import PIECE_KEYS 

def rotate_piece_cw(piece:str) -> str:
    return piece[-1] + piece[:-1]

def rotate_piece_ccw(piece:str) -> str:
    return piece[1:] + piece[0]

def piece_rotation_group(rotate:Callable[[str] ,str], piece:str)->list[str]:
    
    if len(piece) != PIECE_KEY_NUMBER_DIGITS:
        raise ValueError()
    
    group = [piece]
    current = piece
    for _ in range(PIECE_KEY_NUMBER_DIGITS - 1):
         current = rotate(current)
         group.append(current)
    return group

def shorten_rotation_group(group):
    return group[:len(set(group))]

def generate_rotation_groups(rotation:Callable[[str] ,str]=rotate_piece_ccw):
    done = set()
    groups = dict()
    for piece in PIECE_KEYS:
        if piece not in done:
            group = piece_rotation_group(rotation, piece)
            shorten_group = shorten_rotation_group(group)
            groups[piece] = (group, shorten_group if len(shorten_group) < len(group) else group)
            for piece in shorten_group:
                done.add(piece)
    return groups

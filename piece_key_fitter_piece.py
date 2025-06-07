
from piece_key_piece import PieceKeyPiece, Directions, Coordinate
from edge import Edge
from piece_keys import PIECE_KEYS, PIECE_KEYS_STARTS_WITH, PIECE_KEY_LISTS
from typing import List, Tuple

class PieceKeyFitterPice(PieceKeyPiece):
    
    OPPOSITEKEYS = {key :''.join([{'0':'0', '1':'2', '2':'1'}[p] for p in key]) for key in  PIECE_KEYS}
    
    def __init__(self, piece_key: str , frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate) -> None:
        super().__init__(piece_key, PieceKeyFitterPice.OPPOSITEKEYS[piece_key], frame_index, rotation_index, rotated, directions, coordinate)
        self.inital_piece_key =  PIECE_KEY_LISTS[piece_key]

    def fit_left(self) -> Tuple[bool, str]:
        left = self.links[Edge.LEFT]
        if left:
            return self.set_key_part(left.get_opposite_key_part(self.rotation_index, Edge.RIGHT), Edge.LEFT)
        else:
            raise Exception()
    
    def fit_up(self) -> Tuple[bool, str]:
        up = self.links[Edge.UP]
        if up:
            return self.set_key_part(up.get_opposite_key_part(self.rotation_index, Edge.DOWN), Edge.UP)
        else:
            raise Exception()
    
    def fit_right(self) -> Tuple[bool, str]:
        right = self.links[Edge.RIGHT]
        if right:
            return self.set_key_part(right.get_opposite_key_part(self.rotation_index, Edge.LEFT), Edge.RIGHT)
        else:
            raise Exception()
    
    def fit_down(self) -> Tuple[bool, str]:
        down = self.links[Edge.DOWN]
        if down:
            return self.set_key_part(down.get_opposite_key_part(self.rotation_index, Edge.UP),Edge.DOWN)
        else:
            raise Exception()
    
    def set_key_part(self, fit_part: str, index: int) -> Tuple[bool, str]:
        part = self.piece_key[index]
        if part != fit_part:
            piece_key = self.piece_key[0:index] + fit_part + self.piece_key[index+1:]
            piece_key = PIECE_KEYS_STARTS_WITH[piece_key][0]
            self.piece_key = piece_key
            self.opposite_key = PieceKeyFitterPice.OPPOSITEKEYS[piece_key]
            return True, fit_part
        return False, fit_part
       

from piece_key_piece import PieceKeyPiece, Directions, Coordinate, Callable
from edge import Edge, OPPOSITE_EDGE
from piece_keys import PIECE_KEYS, PIECE_KEYS_IDENTITY
from typing import List, Tuple

class PieceKeyFitterPice(PieceKeyPiece):
    
    OPPOSITEKEYS = {key: PIECE_KEYS_IDENTITY[''.join([{'0':'0', '1':'2', '2':'1'}[p] for p in key])] for key in  PIECE_KEYS}
    
    def __init__(self, piece_key: str, print_positions: Callable[[Coordinate, List[Directions]], List[str]], frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> None:
        super().__init__(piece_key, PieceKeyFitterPice.OPPOSITEKEYS[piece_key], print_positions, frame_index, rotation_index, rotated, directions, coordinate, edges)
    
    def fit(self, this: Edge) -> Tuple[bool, str]:
        opposite_link = self.links[this]
        if opposite_link:
            return self.set_key_part(opposite_link.get_opposite_key_part(self.rotation_index, OPPOSITE_EDGE[this]), this)
        else:
            raise Exception()
    
    def set_key_part(self, fit_part: str, index: int) -> Tuple[bool, str]:
        part = self.piece_key[index]
        if part != fit_part:
            piece_key = PIECE_KEYS_IDENTITY[self.piece_key[0:index] + fit_part + self.piece_key[index+1:]]
            self.piece_key = piece_key
            self.opposite_key = PieceKeyFitterPice.OPPOSITEKEYS[piece_key]
            return True, fit_part
        return False, fit_part
    
    def fit_edges(self) -> List[Tuple[bool, str]]:
        return list(map(self.fit, self.edges))

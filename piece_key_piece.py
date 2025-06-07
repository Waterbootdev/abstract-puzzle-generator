from base_piece import List, BasePiece, Directions, Coordinate
from rotation_matrix import INDEX_ROTATION_MATRIX

class PieceKeyPiece(BasePiece):
    def __init__(self, piece_key: str, opposite_key: str, frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate) -> None:
        super().__init__(frame_index, rotation_index, rotated, directions, coordinate)
     
        self.piece_key = piece_key
        self.opposite_key = opposite_key
        rotation_matrix = INDEX_ROTATION_MATRIX[rotation_index]
        self.rotation_matrix = rotation_matrix
        self.rotation = rotation_matrix[0]

    def __repr__(self) -> str:
        return ''.join(self.rotated_piece_key())

    def rotated_piece_key(self) -> List[str]:
        return [self.piece_key[i] for i in self.rotation]
       
    def get_opposite_key_part(self, rotation_index: int, piece_key_index: int) -> str:
        return self.opposite_key[self.rotation_matrix[rotation_index][piece_key_index]]

    def set_part_positions(self, part_positions: List[str]):
        self.part_positions = part_positions
        

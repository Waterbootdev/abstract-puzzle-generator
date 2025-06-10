from piece_keys import PIECE_KEYS
from piece_key_fitter_piece import List, PieceKeyFitterPice, Directions, Coordinate, PieceKeyPiece, Edge, Tuple
from piece_generator import PieceGenerator, Callable
import random

class RandomPieceKeyFitter:
    
    def __init__(self, number_columns: int, number_rows: int, print_positions: Callable[[Coordinate, List[Directions]], List[str]], opposite_key: str) -> None:
        
        if number_rows > number_columns or number_columns < 1:
            raise ValueError() 
       
        self.piece_generator: PieceGenerator[PieceKeyFitterPice] = PieceGenerator[PieceKeyFitterPice](number_columns + 2, number_rows + 2)
    
        def new_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> PieceKeyFitterPice:
            piece_key = PIECE_KEYS[0]
            if frame_index > 0:
                piece_key = random.choice(PIECE_KEYS)
            return PieceKeyFitterPice(piece_key, opposite_key, print_positions, frame_index, rotation_index, rotated, directions, coordinate, edges)
       
        spiral: List[PieceKeyFitterPice] = self.piece_generator.generate(new_piece)
    
        self.spiral: List[PieceKeyFitterPice] = spiral
   
        self.pieces: List[PieceKeyFitterPice] = [piece for piece  in spiral if piece.frame_index > 0]
        
        self.first_piece: PieceKeyFitterPice = spiral[self.pieces[0].coordinate.index]

        self.last_piece: PieceKeyFitterPice = spiral[-1]


    def fit_all(self) -> None:
        for piece in self.pieces:
            _ = piece.fit_edges()
    
    def fit_and_print_all(self, print: Callable[[PieceKeyFitterPice, List[Tuple[bool, str]]], None]) -> None:
        for piece in self.pieces:
            print(piece, piece.fit_edges())
                        
    def bottom_left(self) -> PieceKeyPiece:
        return self.spiral[self.piece_generator.turns[2]]
        
if __name__ == '__main__':
    pass
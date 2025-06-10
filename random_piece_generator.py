from random_piece_key_piece import List, RandomPieceKeyPiece, Directions, Coordinate, PieceKeyPiece, Edge
from piece_generator import PieceGenerator, Callable

class RandomPieceGenerator:
    
    def __init__(self, number_columns: int, number_rows: int, print_positions: Callable[[Coordinate, List[Directions]], List[str]], opposite_key: str) -> None:
        
        if number_rows > number_columns or number_columns < 1:
            raise ValueError() 
       
        self.piece_generator: PieceGenerator[RandomPieceKeyPiece] = PieceGenerator[RandomPieceKeyPiece](number_columns + 2, number_rows + 2)
    
        def new_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> RandomPieceKeyPiece:
            return RandomPieceKeyPiece(opposite_key, print_positions, frame_index, rotation_index, rotated, directions, coordinate, edges)

        spiral: List[RandomPieceKeyPiece] = self.piece_generator.generate(new_piece)
       
        self.pieces: List[RandomPieceKeyPiece] = [piece for piece  in spiral if piece.frame_index > 0]

        for piece in self.pieces:
            piece.fit_edges()

        self.spiral: List[RandomPieceKeyPiece] = spiral

        self.border:  List[RandomPieceKeyPiece] = [piece for piece  in spiral if piece.coordinate.index > 0 and piece.frame_index == 0 and not piece.rotated]

        self.border.append(spiral[self.piece_generator.turns[3]])

                             
    def bottom_left(self) -> PieceKeyPiece:
        return self.spiral[self.piece_generator.turns[2]]
        
if __name__ == '__main__':
    pass
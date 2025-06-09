from piece_key_fitter_piece import List, PieceKeyFitterPice, PIECE_KEYS, Directions, Coordinate, PieceKeyPiece, Edge, Tuple
from piece_generator import PieceGenerator, Callable
from piece_key_fitter_pice_edge_printer import PieceKeyPiceEdgePrinter
import random

class RandomBasePieceKeyFitter:
    
    def __init__(self, number_columns: int, number_rows: int, print_positions: Callable[[Coordinate, List[Directions]], List[str]]) -> None:
        
        if number_rows > number_columns or number_columns < 1:
            raise ValueError() 
       
        self.piece_generator: PieceGenerator[PieceKeyFitterPice] = PieceGenerator[PieceKeyFitterPice](number_columns + 2, number_rows + 2)
    
        def new_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> PieceKeyFitterPice:
            piece_key = PIECE_KEYS[0]
            if frame_index > 0:
                piece_key = random.choice(PIECE_KEYS)
            return PieceKeyFitterPice(piece_key, print_positions, frame_index, rotation_index, rotated, directions, coordinate, edges)
       
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
        

    def first_fit_and_print_all(self, printer:PieceKeyPiceEdgePrinter):
        def fit(piece: PieceKeyFitterPice):
            printer.print(piece, piece.fit(printer.edge))
        RandomBasePieceKeyFitter.run_forward_single(fit, self.first_piece)
    
    def first_fit_all(self, edge: Edge):
        def fit(piece: PieceKeyFitterPice):
            _ = piece.fit(edge)
        RandomBasePieceKeyFitter.run_forward_single(fit, self.first_piece)
           
    @staticmethod
    def run_forward_single(apply: Callable[[PieceKeyFitterPice], None], first_piece: PieceKeyFitterPice):
        piece = first_piece
        while piece:
            apply(piece)
            piece = piece.forward
    
                
    def bottom_left(self) -> PieceKeyPiece:
        return self.spiral[self.piece_generator.turns[2]]
        
    
    

if __name__ == '__main__':
    random.seed(5)
    pass
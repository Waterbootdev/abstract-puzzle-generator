from piece_key_fitter_piece import List, PieceKeyFitterPice, PIECE_KEYS, Directions, Coordinate, Edge
from base_pice_generator import BasePieceGenerator
import random

class RandomBasePieceKeyFitter:
    
    def __init__(self, number_columns: int, number_rows: int) -> None:
        
        if number_rows > number_columns or number_columns < 1:
            raise ValueError() 
       
        base_piece_generator: BasePieceGenerator = BasePieceGenerator(number_columns + 2, number_rows + 2)
    
        def new_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate) -> PieceKeyFitterPice:
            piece_key = PIECE_KEYS[0]
            if frame_index > 0:
                piece_key = random.choice(PIECE_KEYS)
            return PieceKeyFitterPice(piece_key,frame_index, rotation_index, rotated, directions, coordinate)
       
        spiral = base_piece_generator.generate(new_piece)
    
        self.spiral = spiral
   
        self.pieces = [piece_holder for piece_holder  in spiral if piece_holder.frame_index > 0]
        
        self.first_piece = self.pieces[0]

    
    def fit_all_pices(self, printer_left=None, printer_up=None, printer_right=None, printer_down=None):
        
        printer_left = printer_left if printer_left else  lambda x, y: x 
        printer_up = printer_up if printer_up else  lambda x, y: x 
        printer_right = printer_right if printer_right else  lambda x, y : x 
        printer_down = printer_down if printer_down else  lambda x, y : x 

        for fit  in [lambda p: printer_left(p, p.fit(Edge.LEFT)), lambda p: printer_up(p, p.fit(Edge.UP)), lambda p: printer_right(p, p.fit(Edge.RIGHT)), lambda p: printer_down(p, p.fit(Edge.DOWN))]:
            self.run_piece(fit, self.first_piece)
       
    def run_piece(self, fit, piece: PieceKeyFitterPice|None):
        while piece:
            assert isinstance(piece, PieceKeyFitterPice)
            fit(piece)
            piece = piece.forward
    
    

if __name__ == '__main__':
    random.seed(5)
    pass
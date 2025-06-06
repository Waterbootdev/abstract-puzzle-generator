from piece_key_fitter_piece import PieceKeyFitterPice, PIECE_KEYS, Directions, Coordinate
from base_pice_generator import BasePieceGenerator
import random

class RandomBasePieceKeyFitter:
    
    def __init__(self, number_columns, number_rows) -> None:
        
        def new_piece(frame_index:int, rotation_index:int, rotated:bool, directions:list[Directions], coordinate:Coordinate):
            piece_key = PIECE_KEYS[0]
            if frame_index > 0:
                piece_key = random.choice(PIECE_KEYS)
            return PieceKeyFitterPice(piece_key,frame_index, rotation_index, rotated, directions, coordinate)
        

        base_piece_generator :BasePieceGenerator = BasePieceGenerator(number_columns + 2, number_rows + 2)
    
        spiral = base_piece_generator.generate(new_piece)
    
        self.spiral = spiral
   
        self.pieces = [piece_holder for piece_holder  in spiral if piece_holder.frame_index > 0]
        
        self.first_piece = self.pieces[0]

    
    def fit_all_pices(self, printer_left=None, printer_up=None, printer_right=None, printer_down=None):
        
        printer_left = printer_left if printer_left else  lambda x, y: x 
        printer_up = printer_up if printer_up else  lambda x, y: x 
        printer_right = printer_right if printer_right else  lambda x,y : x 
        printer_down = printer_down if printer_down else  lambda x,y : x 

        for fit  in [lambda p: printer_left(p, p.fit_left()), lambda p: printer_up(p, p.fit_up()), lambda p: printer_right(p, p.fit_right()), lambda p: printer_down(p, p.fit_down())]:
            self.run_piece(fit, self.first_piece)
       
    def run_piece(self, fit, piece):
        while piece:
            assert isinstance(piece, PieceKeyFitterPice)
            fit(piece)
            piece = piece.forward
    
    

if __name__ == '__main__':
    random.seed(5)
    pass
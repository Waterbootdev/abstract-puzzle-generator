from piece_key_fitter_piece import List, PieceKeyFitterPice, PIECE_KEYS, Directions, Coordinate, PieceKeyPiece, Edge
from piece_generator import PieceGenerator, Callable
from piece_key_fitter_pice_edge_printer import PieceKeyFitterPiceEdgePrinter
from edge import LEFT_UP, LEFT_UP_DOWN, LEFT_UP_RIGHT, LEFT_UP_RIGHT_DOWN, NUMBER_EDGES

import random

class RandomBasePieceKeyFitter:
    
    def __init__(self, number_columns: int, number_rows: int) -> None:
        
        if number_rows > number_columns or number_columns < 1:
            raise ValueError() 
       
        self.piece_generator: PieceGenerator[PieceKeyFitterPice] = PieceGenerator[PieceKeyFitterPice](number_columns + 2, number_rows + 2)
    
        def new_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate) -> PieceKeyFitterPice:
            piece_key = PIECE_KEYS[0]
            if frame_index > 0:
                piece_key = random.choice(PIECE_KEYS)
            return PieceKeyFitterPice(piece_key,frame_index, rotation_index, rotated, directions, coordinate)
       
        spiral: List[PieceKeyFitterPice] = self.piece_generator.generate(new_piece)
    
        self.spiral: List[PieceKeyFitterPice] = spiral
   
        self.pieces: List[PieceKeyPiece] = [piece for piece  in spiral if piece.frame_index > 0]
        
        self.first_piece: PieceKeyFitterPice = spiral[self.pieces[0].coordinate.index]
        self.last_piece: PieceKeyFitterPice = spiral[-1]

    def first_fit_and_print_all(self, printer:PieceKeyFitterPiceEdgePrinter):
        def fit(piece: PieceKeyFitterPice):
            printer.print(piece, piece.fit(printer.edge))
        RandomBasePieceKeyFitter.run_forward_single(fit, self.first_piece)
    
    def first_fit_all(self, edge: Edge):
        def fit(piece: PieceKeyFitterPice):
            _ = piece.fit(edge)
        RandomBasePieceKeyFitter.run_forward_single(fit, self.first_piece)
    def number_edes(self, piece):
            max = NUMBER_EDGES

            if self.last_piece != piece:
                if piece.rotated:
                    max -=1
                else:
                    max -=2
            return max

    @staticmethod
    def fit_edges(piece: PieceKeyFitterPice, edges: List[Edge]):
        for edge in edges:
            _ = piece.fit(edge)
        
    def second_fit_all(self):

        def fit(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_edges(piece, LEFT_UP)
        
        def fit_turn(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_edges(piece, LEFT_UP_RIGHT)
        
        def fit_after_last_turn(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_edges(piece, LEFT_UP_DOWN)

        def fit_last(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_edges(piece, LEFT_UP_RIGHT_DOWN)
 
        RandomBasePieceKeyFitter.run_forward_multiple(fit, fit_turn, fit_after_last_turn, fit_last, self.first_piece, self.spiral[self.piece_generator.turns[-1]])
    
    @staticmethod
    def fit_and_print_edges(piece: PieceKeyFitterPice, edges: List[Edge], printers: List[PieceKeyFitterPiceEdgePrinter]):
        for edge in edges:
            printers[edge].print(piece, piece.fit(edge))
    
    def second_fit_and_print_all(self, printers: List[PieceKeyFitterPiceEdgePrinter]):

        def fit(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_and_print_edges(piece, LEFT_UP, printers)
        
        def fit_turn(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_and_print_edges(piece, LEFT_UP_RIGHT, printers)
        
        def fit_after_last_turn(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_and_print_edges(piece, LEFT_UP_DOWN, printers)

        def fit_last(piece: PieceKeyFitterPice):
            RandomBasePieceKeyFitter.fit_and_print_edges(piece, LEFT_UP_RIGHT_DOWN, printers)
 
        RandomBasePieceKeyFitter.run_forward_multiple(fit, fit_turn, fit_after_last_turn, fit_last, self.first_piece, self.spiral[self.piece_generator.turns[-1]])

      
               
    @staticmethod
    def run_forward_single(apply: Callable[[PieceKeyFitterPice], None], first_piece: PieceKeyFitterPice):
        piece = first_piece
        while piece:
            apply(piece)
            piece = piece.forward
    
    @staticmethod
    def run_forward_multiple(apply: Callable[[PieceKeyFitterPice], None], apply_turn: Callable[[PieceKeyFitterPice], None], apply_after_last_turn: Callable[[PieceKeyFitterPice], None], apply_last: Callable[[PieceKeyFitterPice], None], first_piece: PieceKeyFitterPice, last_turn: PieceKeyFitterPice):
        assert last_turn.rotated
        assert first_piece.coordinate.index < last_turn.coordinate.index    
        
        piece = first_piece
        ok = True
        
        while ok and piece:
            if piece.rotated:
                apply_turn(piece)
                ok = piece != last_turn
            else:
                apply(piece)
            
            piece = piece.forward
        
        assert piece

        while piece.forward:
            apply_after_last_turn(piece)
            piece = piece.forward

        apply_last(piece)
                
    def bottom_left(self) -> PieceKeyPiece:
        return self.spiral[self.piece_generator.turns[2]]
        
    
    

if __name__ == '__main__':
    random.seed(5)
    pass
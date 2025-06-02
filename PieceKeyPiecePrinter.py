from piece_key_piece_print_positions import PieceKeyPiecePrintPositions
from piece_key_fitter_piece import PieceKeyFitterPice
from escape_color import EscapeColor
from edge import Edge
import time

class PieceKeyFitterPiceEdgePrinter:
    def __init__(self, edge:Edge, seconds:float, red:EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green :EscapeColor = EscapeColor.GREEN ) -> None:
        self.edge = edge
        self.seconds = seconds
        self.red = red
        self.yellow = yellow
        self.green = green

    def print(self, piece:PieceKeyFitterPice, t:tuple[bool,str]):
        not_fitted, part = t
        PieceKeyFitterPicePrinter.print_animated(self.seconds, piece, not_fitted, part, self.edge, self.red, self.yellow, self.green)  
        

class PieceKeyFitterPicePrinter:

    @staticmethod
    def print_at(position, color:EscapeColor, part):
        print(position + color.value + part)
        
    @staticmethod
    def print_animated(seconds:float, piece:PieceKeyFitterPice, not_fitted:bool, part:str, index: int, red:EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green :EscapeColor = EscapeColor.GREEN):
        
        initial_part = part
        final_color = green
        
        if not_fitted:
            initial_part = piece.inital_piece_key[index]
            final_color = red
        
        position = piece.part_positions[index]

        PieceKeyFitterPicePrinter.print_at(position, yellow, initial_part)

        time.sleep(seconds)

        PieceKeyFitterPicePrinter.print_at(position, final_color, part)

    def __init__(self, spiral:list, scale_x, scale_y, x, y, seconds:float,  red:EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green :EscapeColor = EscapeColor.GREEN) -> None:
        self.pieces = PieceKeyPiecePrintPositions.init_set_part_positions(spiral, scale_x, scale_y, x, y)
        self.edge_printer = [object() for _ in range(Edge.MAX)]

        self.edge_printer[Edge.LEFT] = PieceKeyFitterPiceEdgePrinter(Edge.LEFT, seconds, red, yellow, green)
        self.edge_printer[Edge.UP] = PieceKeyFitterPiceEdgePrinter(Edge.UP, seconds, red, yellow, green)
        self.edge_printer[Edge.RIGHT] = PieceKeyFitterPiceEdgePrinter(Edge.RIGHT, seconds, red, yellow, green)
        self.edge_printer[Edge.DOWN] = PieceKeyFitterPiceEdgePrinter(Edge.DOWN, seconds, red, yellow, green)
        

    def print_pieces(self, edge : Edge, color:EscapeColor):
        print(color.value)
        for piece in self.pieces:
            PieceKeyPiecePrintPositions.print(piece, edge)

    

    def get_printer(self, edge:Edge):
        printer = self.edge_printer[edge]
        assert isinstance(printer, PieceKeyFitterPiceEdgePrinter)
        return printer.print 
        



if __name__ == '__main__':
    import random
    from random_piece_key_fitter import RandomBasePieceKeyFitter
    import os
    while True:
        w = random.choice(range(8,45))

        h = random.choice(range(4, min(w, 17)))


        fitter = RandomBasePieceKeyFitter(w,h)
    
        os.system("clear")
  
        printer : PieceKeyFitterPicePrinter = PieceKeyFitterPicePrinter([s for s in fitter.spiral if s.frame_index > -1], 6, 4, 2, 1,0.3)  
   
        printer.print_pieces(Edge.LEFT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.RIGHT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.UP, EscapeColor.BLUE)      
        printer.print_pieces(Edge.DOWN, EscapeColor.BLUE)      

        fitter.fit_all_pices(printer.get_printer(Edge.LEFT),printer.get_printer(Edge.UP),printer.get_printer(Edge.RIGHT),printer.get_printer(Edge.DOWN))

        time.sleep(2)
 
    



    

    


        

from piece_key_fitter_pice_edge_printer import PieceKeyFitterPiceEdgePrinter
from piece_key_piece_print_positions import List, init_set_part_positions
from escape_color import EscapeColor
from edge import Edge, LEFT_UP_RIGHT_DOWN
from printer_helper import print_edge

class PieceKeyFitterPicePrinter:

    def __init__(self, spiral: List, scale_x: int, scale_y: int, x: int, y: int, seconds: float,  red: EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green: EscapeColor = EscapeColor.GREEN) -> None:
        self.pieces = init_set_part_positions(spiral, scale_x, scale_y, x, y)
        self.edge_printer: List[PieceKeyFitterPiceEdgePrinter] = [PieceKeyFitterPiceEdgePrinter(edge, seconds, red, yellow, green) for edge in LEFT_UP_RIGHT_DOWN]
        
    def print_pieces(self, edge : Edge, color: EscapeColor):
        print(color.value)
        for piece in self.pieces:
            print_edge(piece, edge)

    def get_printer(self, edge: Edge) -> PieceKeyFitterPiceEdgePrinter:
        printer = self.edge_printer[edge]
        if not printer:
            raise Exception()
        else:
            return printer
    
if __name__ == '__main__':
   pass

    


        

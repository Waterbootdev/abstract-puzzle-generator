from piece_key_fitter_pice_edge_printer import PieceKeyFitterPiceEdgePrinter
from piece_key_piece_print_positions import init_set_part_positions
from escape_color import EscapeColor
from edge import Edge
from printer_helper import print_edge

class PieceKeyFitterPicePrinter:

   
    def __init__(self, spiral:list, scale_x, scale_y, x, y, seconds:float,  red:EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green :EscapeColor = EscapeColor.GREEN) -> None:
        self.pieces = init_set_part_positions(spiral, scale_x, scale_y, x, y)
        self.edge_printer = [object() for _ in range(Edge.MAX)]

        self.edge_printer[Edge.LEFT] = PieceKeyFitterPiceEdgePrinter(Edge.LEFT, seconds, red, yellow, green)
        self.edge_printer[Edge.UP] = PieceKeyFitterPiceEdgePrinter(Edge.UP, seconds, red, yellow, green)
        self.edge_printer[Edge.RIGHT] = PieceKeyFitterPiceEdgePrinter(Edge.RIGHT, seconds, red, yellow, green)
        self.edge_printer[Edge.DOWN] = PieceKeyFitterPiceEdgePrinter(Edge.DOWN, seconds, red, yellow, green)
        

    def print_pieces(self, edge : Edge, color:EscapeColor):
        print(color.value)
        for piece in self.pieces:
            print_edge(piece, edge)

    

    def get_printer(self, edge:Edge):
        printer = self.edge_printer[edge]
        assert isinstance(printer, PieceKeyFitterPiceEdgePrinter)
        return printer.print 
    

if __name__ == '__main__':
   pass

    


        

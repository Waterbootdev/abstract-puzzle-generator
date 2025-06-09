from piece_key_fitter_pice_edge_printer import PieceKeyPiceEdgePrinter, Tuple, PieceKeyPiece
from escape_color import EscapeColor
from edge import Edge, LEFT_UP_RIGHT_DOWN, List
from printer_helper import print_edge
from piece_key_piece_helper import KeyPiece
class PieceKeyFitterPicePrinter:

    def __init__(self, seconds: float,  red: EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green: EscapeColor = EscapeColor.GREEN) -> None:
        self.edge_printer: List[PieceKeyPiceEdgePrinter] = [PieceKeyPiceEdgePrinter(edge, seconds, red, yellow, green) for edge in LEFT_UP_RIGHT_DOWN]
        
    def print_pieces(self, pieces: List[KeyPiece],  edge : Edge, color: EscapeColor):
        print(color.value)
        for piece in pieces:
            print_edge(piece, edge)

    def get_printer(self, edge: Edge) -> PieceKeyPiceEdgePrinter:
        printer = self.edge_printer[edge]
        if not printer:
            raise Exception()
        else:
            return printer
        
    def print(self, piece: PieceKeyPiece, ts: List[Tuple[bool, str]]):
        for edge, t in zip(piece.edges, ts):
            self.edge_printer[edge].print(piece, t)
    
if __name__ == '__main__':
   pass

    


        

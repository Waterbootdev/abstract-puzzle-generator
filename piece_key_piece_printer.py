from escape_color import EscapeColor
from edge import Edge, List,LEFT_UP_RIGHT_DOWN
from printer_helper import print_piece_key_edge, print_initial_piece_key_edge
from piece_key_piece_helper import KeyPiece, PieceKeyPiece
from time import sleep

class PieceKeyPiecePrinter:

    def __init__(self, seconds: float,  red: EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green: EscapeColor = EscapeColor.GREEN, blue: EscapeColor = EscapeColor.BLUE) -> None:        
        self.seconds = seconds
        self.red = red
        self.yellow = yellow
        self.green = green

    def print_pieces(self, pieces: List[KeyPiece],  edge : Edge, color: EscapeColor):
        print(color.value)
        for piece in pieces:
            print_piece_key_edge(piece, edge)

    def print_blue(self, piece: PieceKeyPiece):
        print(EscapeColor.BLUE.value)
        for edge in LEFT_UP_RIGHT_DOWN:
            print_initial_piece_key_edge(piece, edge)

    def print_yellow(self, piece: PieceKeyPiece):
        print(self.yellow.value)
        for edge in piece.edges:
            print_initial_piece_key_edge(piece, edge)
                
    def print_red_or_green(self, piece: PieceKeyPiece):
        for edge in piece.edges:
            if piece.is_changed(edge):
                print(self.red.value)
            else:
                print(self.green.value)
            print_piece_key_edge(piece, edge)
            
    def print_changes(self, pieces: List[KeyPiece]):
        for piece in pieces:
            self.print_blue(piece)
            sleep(self.seconds/2.0)
            self.print_yellow(piece)
            sleep(self.seconds)
            self.print_red_or_green(piece)

if __name__ == '__main__':
   pass

    


        

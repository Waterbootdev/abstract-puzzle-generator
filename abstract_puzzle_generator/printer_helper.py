from random_piece_key_piece import PieceKeyPiece
from edge import Edge
from escape_color import EscapeColor

TOPLEFT: str ="\033[%d;%dH" %(1,1)

def print_piece_key_edge(piece: PieceKeyPiece, index: Edge):
    print(piece.print_positions[index]+piece.piece_key[index])

def print_initial_piece_key_edge(piece: PieceKeyPiece, index: Edge):
    print(piece.print_positions[index]+piece.inital_piece_key[index])

def print_at(position: str, color: EscapeColor, part: str):
    print(position + color.value + part)
        

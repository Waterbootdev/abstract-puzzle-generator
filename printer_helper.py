from piece_key_fitter_piece import PieceKeyPiece
from edge import Edge
from escape_color import EscapeColor
from time import sleep

TOPLEFT: str ="\033[%d;%dH" %(1,1)

def print_edge(piece: PieceKeyPiece, index: Edge):
    print(piece.print_positions[index]+piece.piece_key[index])
    #print(TOPLEFT+' ')


def print_at(position, color: EscapeColor, part):
    print(position + color.value + part)
        
def print_animated(seconds: float, piece: PieceKeyPiece, not_fitted: bool, part: str, index: int, red: EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green: EscapeColor = EscapeColor.GREEN):
        
    initial_part = part
    final_color = green
        
    if not_fitted:
        initial_part = piece.inital_piece_key[index]
        final_color = red
        
    position = piece.print_positions[index]

    print_at(position, yellow, initial_part)
    
    sleep(seconds)

    print_at(position, final_color, part)


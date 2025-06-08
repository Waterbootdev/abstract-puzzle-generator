from piece_key_piece import List, PieceKeyPiece, Coordinate, Directions
from edge import Edge
from escape_color import EscapeColor
def escape_position(row: int, column: int):
    return"\033[%d;%dH" %(row, column)

def intit_position(coordinate: Coordinate, directions: Directions) -> str:
    x, y = coordinate.left(directions)
    return escape_position(y + 1, x + 1)

def set_piece_key_part_positions(piece: PieceKeyPiece, scale_x: int, scale_y: int, x: int, y: int) -> PieceKeyPiece:
    assert isinstance(piece, PieceKeyPiece)
    coodinate = piece.coordinate.scale_add(scale_x, scale_y, x, y)
    piece.set_part_positions([intit_position(coodinate, directions)  for directions in piece.directions])
    return piece
        
def init_set_part_positions(pieces: List[PieceKeyPiece], scale_x: int, scale_y: int, x: int, y: int) -> List[PieceKeyPiece]:        
    return [set_piece_key_part_positions(piece, scale_x, scale_y, x, y) for piece in pieces]

def print_row_position(piece: PieceKeyPiece, edge: Edge,  scale_x: int, scale_y: int, x: int, y: int) -> None:
    coordinate = piece.coordinate.scale_add(scale_x, scale_y, x, y)
    _, row = coordinate.left(piece.directions[edge])
    print(escape_position(row + 1, 1) + EscapeColor.RESET.value)


from piece_key_piece import PieceKeyPiece, Coordinate, Directions
from edge import Edge

def escape_position(row: int, column: int):
    return"\033[%d;%dH" %(row, column)

def intit_position(coordinate: Coordinate, directions: Directions) -> str:
    x, y = coordinate.left(directions)
    return escape_position(y + 1, x + 1)

def print_row_position(piece: PieceKeyPiece, edge: Edge,  scale_x: int, scale_y: int, x: int, y: int) -> None:
    coordinate = piece.coordinate.scale_add(scale_x, scale_y, x, y)
    _, row = coordinate.left(piece.directions[edge])
    print(escape_position(row + 1, 1))
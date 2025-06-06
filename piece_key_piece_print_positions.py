from piece_key_piece import PieceKeyPiece
from edge import Edge
from coordinate import Coordinate
from directions import Ring, DIRECTIONSLIST

   
def escape_position(row, column):
        return"\033[%d;%dH" %(row, column)

def intit_position(coordinate:Coordinate, ring:Ring) -> str:
        x, y = coordinate.left(ring.current())
        ring.forward()
        return escape_position(y + 1, x + 1)

def set_piece_key_part_positions(piece_key_piece:PieceKeyPiece, ring : Ring, scale_x, scale_y, x, y) -> PieceKeyPiece:
        assert isinstance(piece_key_piece, PieceKeyPiece)
        coodinate = piece_key_piece.coordinate.scale_add(scale_x, scale_y, x, y)
        rotation_index = piece_key_piece.rotation_index
        ring.set_to(rotation_index)
        piece_key_piece.part_positions =[intit_position(coodinate, ring)  for _ in range(Edge.MAX)]
        return piece_key_piece
        
def init_set_part_positions(pieces:list[PieceKeyPiece], scale_x, scale_y, x, y) -> list[PieceKeyPiece]:
        ring = Ring(DIRECTIONSLIST)
        return [set_piece_key_part_positions(piece, ring, scale_x, scale_y, x, y) for piece in pieces]
    
    
    
    



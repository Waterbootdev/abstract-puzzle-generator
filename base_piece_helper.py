from base_piece import BasePiece
from itertools import starmap

def get_link(base_pieces:list[BasePiece], index):
        return base_pieces[index] if index else None
    
def set_links(base_pieces:list[BasePiece], piece:list, indexes:list):
        for i, index in enumerate(indexes):
            piece[i] = get_link(base_pieces, index)


def link(base_pieces:list[BasePiece], piece : BasePiece, links, forward, backward):
        set_links(base_pieces, piece.links, links)
        piece.forward = get_link(base_pieces, forward)
        piece.backward = get_link(base_pieces, backward)


def generate_linked_base_pieces(get_new_base_piece, frame_index, rotation_index, rotated, directions, coordinates, links, forward, backward):
        base_pieces = list(starmap(get_new_base_piece, zip(frame_index, rotation_index, rotated, directions, coordinates)))
        list(starmap(lambda base_piece, links, forward, backward: link(base_pieces, base_piece, links, forward, backward), zip(base_pieces, links, forward, backward)))
        return base_pieces
 


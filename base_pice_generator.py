from generate_functions import generate_backward, generate_coordinates, generate_directions, generate_forward, generate_frame_index, generate_links, generate_rotated
from base_piece import BasePiece
from itertools import starmap

class BasePieceGenerator:

    def __init__(self, width:int , height:int) -> None:
        self.width = width
        self.height = height

        self.rotated = generate_rotated(width, height)

        self.frame_index, self.rotation_index = generate_frame_index(self.rotated)

        self.directions = generate_directions(self.rotated)

        self.coordinates = generate_coordinates(self.rotated, self.directions)

        self.links = generate_links(width, height, self.coordinates, self.directions)

        for coordinate in self.coordinates:
            coordinate.decrement()

        self.forward = generate_forward(len(self.rotated))
        self.backward = generate_backward(len(self.rotated))

    def Generate(self, get_new_base_piece):
        def new_pice(frame_index, rotation_index, rotated, directions, coordinates):
            return get_new_base_piece(frame_index, rotation_index, rotated, directions, coordinates)
        base_pieces = list(starmap(new_pice, zip(self.frame_index, self.rotation_index, self.rotated, self.directions, self.coordinates)))
        list(starmap(lambda base_piece, links, forward, backward: self.link(base_pieces, base_piece, links, forward, backward), zip(base_pieces, self.links, self.forward, self.backward)))
        return base_pieces


    def link(self, base_pieces:list[BasePiece], piece : BasePiece, links, forward, backward):
        BasePieceGenerator.set_links(base_pieces, piece.links, links)
        piece.forward = BasePieceGenerator.get_link(base_pieces, forward)
        piece.backward = BasePieceGenerator.get_link(base_pieces, backward)

    @staticmethod
    def get_link(base_pieces:list[BasePiece], index):

        return base_pieces[index] if index else None
    @staticmethod
    def set_links(base_pieces:list[BasePiece], piece:list, indexes:list):
        for i, index in enumerate(indexes):
            if index:
                piece[i] = BasePieceGenerator.get_link(base_pieces, index)


if __name__ == '__main__':

    base_pice_generator = BasePieceGenerator(4,4)

    test = base_pice_generator.Generate(BasePiece)

    print(test)



    
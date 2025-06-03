from generate_spiral import generate_spiral
from base_piece_helper import generate_linked_base_pieces
from base_piece import BasePiece

class BasePieceGenerator:

    def __init__(self, width:int , height:int) -> None:
        self.width = width
        self.height = height

        self.rotated, self.frame_index, self.rotation_index, self.directions, self.coordinates, self.links, self.forward, self.backward = generate_spiral(width, height)

    def generate(self, get_new_base_piece):
        return generate_linked_base_pieces(get_new_base_piece, self.frame_index, self.rotation_index, self.rotated, self.directions, self.coordinates, self.links, self.forward, self.backward)
       
    
if __name__ == '__main__':

    base_pice_generator = BasePieceGenerator(4,4)

    test = base_pice_generator.generate(BasePiece)

    print(test)



    
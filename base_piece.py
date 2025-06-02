from coordinate import Coordinate
from directions import Directions 
class BasePiece:
    def __init__(self, frame_index:int, rotation_index:int, rotated:bool, directions:list[Directions], coordinate:Coordinate) -> None:
        self.frame_index = frame_index
        self.rotation_index = rotation_index
        self.rotated = rotated
        self.directions = directions
        self.coordinate = coordinate
        self.links = [None, None, None, None]
        self.forward = None
        self.backward = None

    def __repr__(self) -> str:
        return f'{self.frame_index}:{self.rotation_index}:{self.coordinate}:{self.rotated}:{self.directions}'
    




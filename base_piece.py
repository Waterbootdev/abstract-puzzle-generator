from coordinate import Coordinate
from directions import List, Directions
from typing import TypeVar,Generic

P = TypeVar("P")

class BasePiece(Generic[P]):

    def __init__(self, frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate) -> None:

      
        self.frame_index = frame_index
        self.rotation_index = rotation_index
        self.rotated = rotated
        self.directions = directions
        self.coordinate = coordinate
        self.links: List[P|None] = [None, None, None, None]
        self.forward: P|None = None
        self.backward: P|None = None

    def __repr__(self) -> str:
        return f'{self.frame_index}:{self.rotation_index}:{self.coordinate}:{self.rotated}:{self.directions}'

Piece = TypeVar("Piece", bound=BasePiece)
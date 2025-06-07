from enum import IntEnum
from typing import Dict

class Edge(IntEnum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    #MAX = 4

NUMBER_EDGES = 4

OPPOSITE_EDGE: Dict[Edge, Edge] = {Edge.LEFT: Edge.RIGHT, Edge.UP: Edge.DOWN, Edge.RIGHT: Edge.LEFT, Edge.DOWN: Edge.UP}
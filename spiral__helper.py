from coordinate import Coordinate
from directions import Directions

from itertools import starmap
from copy import copy    

def decrement_coordinates(coordinates):
    for coordinate in coordinates:
        coordinate.decrement()
    return coordinates

def generate_coordinates(coordinate:Coordinate, rotated:list[bool], directions:list[list[Directions]]) -> list[Coordinate]:
    
    def step(rotate, directions):
        save = copy(coordinate)
        direction = directions[0]
        if rotate:
            coordinate.step_down(direction)
        else:
            coordinate.step_right(direction)
        return save
    
    return list(starmap(step, zip(rotated, directions)))

def incremented_coordinate():
    coordinate = Coordinate()
    coordinate.increment()
    return coordinate


def to_matrix(width, height, coordinates:list[Coordinate]):
    matrix = [[None for _ in range(height + 2)] for _ in range(width + 2)]

    for coordinate in coordinates:
        assert isinstance(coordinate, Coordinate)
        coordinate.set_to_matrix(matrix)
    
    return matrix 


def generate_links(width, height, directions, coordinates):
    matrix = to_matrix(width, height, coordinates)
    
    def links(coordinate:Coordinate, directions:list[Directions]) -> list[int|None]:
        return list(map(lambda direction: coordinate.matix_left(matrix, direction) ,directions))
        
    return list(starmap(links, zip(coordinates, directions)))



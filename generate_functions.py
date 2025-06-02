

from itertools import chain, starmap
from copy import copy
from directions import Ring, DIRECTIONSLISTLIST, Directions
from coordinate import Coordinate
    
def generate_directions(rotated:list[bool]) -> list[list[Directions]]:
    ring = Ring(DIRECTIONSLISTLIST)
   
    def generate(step_rotate):
        current = ring.current()
        if step_rotate:
            ring.forward()
        return current

    return list(map(generate, rotated))

def generate_coordinates(rotated:list[bool], directions:list[list[Directions]]) -> list[Coordinate]:
    
    coordinate = Coordinate()

    coordinate.increment()

    def step(rotate, directions):
        save = copy(coordinate)
        direction = directions[0]
        if rotate:
            coordinate.step_down(direction)
        else:
            coordinate.step_right(direction)
        return save
    
    return list(starmap(step, zip(rotated, directions)))

def to_matrix(width, height, coordinates:list[Coordinate]):
    matrix = [[None for _ in range(height + 2)] for _ in range(width + 2)]

    for coordinate in coordinates:
        assert isinstance(coordinate, Coordinate)
        coordinate.set_to_matrix(matrix)
    
    return matrix 

def generate_links(width, height, coordinates:list[Coordinate],  directions:list[list[Directions]]) -> list[list[int|None]]:
    matrix = to_matrix(width, height, coordinates)
    def links(coordinate:Coordinate, directions:list[Directions]) -> list[int|None]:
        return list(map(lambda direction: coordinate.matix_left(matrix, direction) ,directions))
    return list(starmap(links, zip(coordinates, directions)))
   
def generate_frame_index(rotated:list[bool]):
    frame_index = 0
    rotation_index = 0
    frame_indexes = []
    rotation_indexes = []
    
    for rotate in rotated:
        current_frame_index = frame_index
        current_rotation_index = rotation_index
        
        if rotate:
            if rotation_index < 3:
                rotation_index += 1
            else:
                rotation_index = 0
                frame_index += 1
        
        frame_indexes.append(current_frame_index)
        rotation_indexes.append(current_rotation_index)

    return frame_indexes, rotation_indexes 
    
def generate_rotated(width, height):
    if height > width or width < 2 or height < 2:
        raise Exception()

    right = width
    down = height - 1
    left = width - 1
    up = height - 2

    step_counts = []

    if height == 2:
        step_counts = [right,down, left] 
    else:
        frame = [right, down, left, up]
    
        step_counts = copy(frame)

        while frame[-1] > 2:
            frame = [steps - 2 for steps in frame]
            step_counts.extend(frame)

        (last_right, last_down, last_left, last_up) = tuple(frame)

        match last_up:
            case 1:
                step_counts.append(last_right - 2)
            case 2:
                step_counts.extend([last_right - 2, last_down - 2, last_left -2])
    
    rotated = list(chain.from_iterable(map(lambda steps_without_rotation : [False for _ in range(steps_without_rotation - 1)] + [True], step_counts)))

    rotated[-1] = False

    assert len(rotated) == width * height
    return rotated    

def generate_forward(length):
    last = length - 1
    return[None if i == last else i + 1 for i in range(length)]

def generate_backward(length):
    return[None if i == 0 else i - 1 for i in range(length)]
    

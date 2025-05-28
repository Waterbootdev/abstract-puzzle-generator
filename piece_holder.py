from coordinate import Coordinate
from directions import Directions
from last_frame_type import LastFrameType
from copy import copy, deepcopy

class PieceHolder:
    def __init__(self, coordinate:Coordinate) -> None:
        self.coodinate = copy(coordinate)
    def __repr__(self) -> str:
        return f'{self.coodinate}'

def init_piece_holders(number_columns: int, number_rows:int) -> tuple[list[list[PieceHolder]]|list[list[None]], list[PieceHolder], list[Directions], int, LastFrameType]:
    if number_rows > number_columns or  number_columns < 2 or number_rows < 2  :
        raise ValueError()
    
    matrix = [[None for _ in range(number_rows)] for _ in range(number_columns)]
    spiral = []
    directions = []

    coordinate = Coordinate()

    current_directions =step_rotate_twice_twice(matrix, spiral, directions, coordinate, Directions(), number_columns - 1, number_rows - 1)
  
    current_width = number_columns - 2
    current_height = number_rows - 2

    frame_count = 1

    while current_width >= 2 and current_height >= 2:
        frame_count += 1
        
        coordinate  = copy(coordinate)     
        coordinate.step_right_down(current_directions)

        current_directions =step_rotate_twice_twice(matrix, spiral, directions, coordinate, Directions(), current_width - 1, current_height - 1)
    
        current_width-=2
        current_height-=2

    last_frame_type = LastFrameType.EVEN

    if current_width > 0 and current_height > 0:
        last_frame_type = LastFrameType.ODD
        frame_count += 1
        coordinate  = copy(coordinate)     
        coordinate.step_right_down(current_directions)
        run(matrix, spiral, directions, coordinate, current_directions, max(current_width, current_height))        
        
    return matrix, spiral, directions, frame_count, last_frame_type

def step_rotate_twice_twice(matrix, spiral, directions, coordinate, current_directions, first_number_steps, second_number_steps):
    current_directions = step_and_rotate_twice(matrix, spiral, directions, coordinate, current_directions, first_number_steps, second_number_steps)
    return step_and_rotate_twice(matrix, spiral, directions, coordinate, current_directions, first_number_steps, second_number_steps)

def step_and_rotate_twice(matrix, spiral, directions, coordinate, current_directions, first_number_steps, second_number_steps):
    current_directions = step_and_rotate(matrix, spiral, directions, coordinate, current_directions, first_number_steps)
    return step_and_rotate(matrix, spiral, directions, coordinate, current_directions, second_number_steps)

def step_and_rotate(matrix, spiral, directions, coordinate, current_directions, number_steps):
    run(matrix, spiral, directions, coordinate, current_directions, number_steps)       
    return rotate(directions, current_directions)

def run(matrix, spiral, directions, coordinate, current_directions, number_steps):
    for _ in range(number_steps):
        step(matrix, spiral, directions, coordinate, current_directions)

def rotate(directions:list[Directions], current_directions:Directions)->Directions:
    new_directions = deepcopy(current_directions)
    new_directions.rotate_ccw()
    directions.append(new_directions)
    return new_directions

def step(matrix, spiral, directions:list[Directions], coordinate:Coordinate, current_directions:Directions) -> None:
    
    directions.append(current_directions)

    holder = PieceHolder(coordinate)
        
    spiral.append(holder)

    matrix[coordinate.x][coordinate.y] = holder

    coordinate.step_right(current_directions)


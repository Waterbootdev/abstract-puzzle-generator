

from spiral_helper import generate_rotated, generate_frame_index, generate_directions, generate_coordinates_and_links, generate_forward, generate_backward


def generate_spiral(width, height):
    if height > width or width < 2 or height < 2:
        raise Exception()

    length = width * height
      
    rotated = generate_rotated(width, height, length)

    frame_index, rotation_index = generate_frame_index(rotated)

    directions = generate_directions(rotated)

    coordinates, links = generate_coordinates_and_links(width, height, rotated, directions)

    forward = generate_forward(length)
    backward = generate_backward(length)

    return rotated, frame_index, rotation_index, directions, coordinates, links, forward, backward
    

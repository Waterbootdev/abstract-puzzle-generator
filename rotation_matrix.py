from edge import Edge

def generation_rotation_matrix():
        
    identity = [Edge.LEFT, Edge.UP, Edge.RIGHT, Edge.DOWN]
    rotations =[identity[rotation_index:] + identity[:rotation_index]  for rotation_index in range(Edge.MAX)]
    rotation_matrix = [[[] for _ in range(Edge.MAX)] for _ in range(Edge.MAX)]
    for first in range(Edge.MAX):
        for second in range(Edge.MAX):
            rotation_index = second - first
            if rotation_index < 0:
                rotation_index += Edge.MAX
            rotation_matrix[first][second]= rotations[rotation_index]
    return rotation_matrix 

INDEX_ROTATION_MATRIX = generation_rotation_matrix()
    

       
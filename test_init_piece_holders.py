from piece_holder import PieceHolder, init_piece_holders
from last_frame_type import LastFrameType
def test_matrix(matrix, number_columns, number_rows):
    for x in range(number_columns):
        column = matrix[x]
        for y in range(number_rows):
            holder:PieceHolder = column[y]
            if not holder:
               return False
            elif holder.coodinate.x != x:
               return False
            elif holder.coodinate.y != y:
               return False
            else:
               pass
    return True
               
def test_spiral(spiral, number_columns, number_rows):
    length = number_columns * number_rows

    if(length != len(spiral)):
        return False
    
    for index in range(length):
        holder:PieceHolder = spiral[index]
        if not holder:
            return False
        elif holder.coodinate.index != index:
            return False
        else:
            pass

    return True

if __name__ == '__main__':
    
    number_columns = [5,8,10, 13, 121]
    number_rows = [5,8,9,10, 111]
    
    for i in range(min(len(number_columns), len(number_rows))):
        matrix, spiral, directions, frame_count, last_frame_typ = init_piece_holders(number_columns[i], number_rows[i])
        print(test_matrix(matrix, number_columns[i], number_rows[i]))
        print(test_spiral(spiral, number_columns[i], number_rows[i]))    
        print(directions[0].x.x == directions[-1].x.x)
        print(directions[0].x.y == directions[-1].x.y)
        print(directions[0].y.x == directions[-1].y.x)
        print(directions[0].y.y == directions[-1].y.y)
        print(len(directions) == number_rows[i] * number_columns[i] +  (frame_count - (1 if last_frame_typ == LastFrameType.ODD else 0)) * 4)

from opposite_piece_keys import DEFAULT_OPPOSITE_KEY, OPPOSITE_KEYS

def cast_number(type, number_str: str, default, minimum):
    try:
        value = max(minimum, type(number_str))
    except Exception:
        return default
    else:
        return value

def valid_opposite_key(opposite_key) -> str:
    return opposite_key if opposite_key in OPPOSITE_KEYS else DEFAULT_OPPOSITE_KEY
        

def get_from_argvs(current_args, max_width = 40, max_height = 15, sleep_time = .1, count = 0, opposite_key = DEFAULT_OPPOSITE_KEY):

    match len(current_args):
        case 2:
            max_width = cast_number(int, current_args[1], max_width, 1)
        case 3:
            max_width = cast_number(int, current_args[1], max_width, 1)
            max_height = cast_number(int, current_args[2], max_height, 1)
        case 4:
            max_width = cast_number(int, current_args[1], max_width, 1)
            max_height = cast_number(int, current_args[2], max_height, 1)
            sleep_time = cast_number(float, current_args[3], sleep_time, 0)
        case 5:
            max_width = cast_number(int, current_args[1], max_width, 1)
            max_height = cast_number(int, current_args[2], max_height, 1)
            sleep_time = cast_number(float, current_args[3], sleep_time, 0)
            count = cast_number(int, current_args[4], count, 1)
        case 6:
            max_width = cast_number(int, current_args[1], max_width, 1)
            max_height = cast_number(int, current_args[2], max_height, 1)
            sleep_time = cast_number(float, current_args[3], sleep_time, 0)
            count = cast_number(int, current_args[4], count, 1)
            opposite_key = valid_opposite_key(current_args[5])
        case _:
            pass
    
    return max_width, max_height, sleep_time, count, opposite_key
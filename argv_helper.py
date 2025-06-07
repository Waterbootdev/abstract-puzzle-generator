def cast_number(type, number_str: str, default, minimum):
    try:
        value = max(minimum, type(number_str))
    except Exception:
        return default
    else:
        return value


def get_from_argvs(current_args, max_width = 40, max_height = 15, sleep_time = 1.0):

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

    return max_width, max_height, sleep_time
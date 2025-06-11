def cast_number(type, number_str: str, default, minimum):
    try:
        value = max(minimum, type(number_str))
    except Exception:
        return default
    else:
        return value
        
def cast_bool(current_args):
    return True if current_args[1].lower() == 'true' else False

def get_from_argvs(current_args, 
                   once_def = True,
                   width_def = 82, 
                   height_def = 22, 
                   sleep_time_def = 1):

    once = once_def
    width = width_def
    height = height_def
    sleep_time = sleep_time_def
    
    match len(current_args):
        case 2: 
            once = cast_bool(current_args)
        case 3:             
            once = cast_bool(current_args)
            width = cast_number(int, current_args[2], width_def, 0)
        case 4: 
            once = cast_bool(current_args)
            width = cast_number(int, current_args[2], width_def, 0)
            height = cast_number(int, current_args[3], height_def, 0)
        case 5: 
            once = cast_bool(current_args)
            width = cast_number(int, current_args[2], width_def, 0)
            height = cast_number(int, current_args[3], height_def, 0)
            sleep_time = cast_number(float, current_args[4], sleep_time_def, 0.0)
        case _:
            pass
    
    
    return once, width, min(width, height), sleep_time


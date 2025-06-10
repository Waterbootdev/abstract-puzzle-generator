from opposite_piece_keys import DEFAULT_OPPOSITE_KEY, OPPOSITE_KEYS

def cast_number(type, number_str: str, default, minimum):
    try:
        value = max(minimum, type(number_str))
    except Exception:
        return default
    else:
        return value

def valid_opposite_key(ok_str) -> str: # ok_str for "opposite key string"
    return ok_str if ok_str in OPPOSITE_KEYS else DEFAULT_OPPOSITE_KEY
        

def get_from_argvs(current_args, 
                   count_def = 0,
                   max_width_def = 40, 
                   max_height_def = 15, 
                   sleep_time_def = .1, 
                   opposite_key_def = DEFAULT_OPPOSITE_KEY):

    # Initialize local variables that will store the final values.
    # These are initialized with the defaults passed into the function.
    count = count_def
    max_width = max_width_def
    max_height = max_height_def
    sleep_time = sleep_time_def
    opposite_key = opposite_key_def
    
    # argument order: count, width, height, delay, rule_id
    # current_args[0] is script name
    # current_args[1] is count
    # current_args[2] is width
    # current_args[3] is height
    # current_args[4] is delay
    # current_args[5] is rule_id

    match len(current_args):
        case 2: # script_name + 1 arg (count)
            count = cast_number(int, current_args[1], count_def, 0) # min 0 for count
        case 3: # script_name + 2 args (count, width)
            count = cast_number(int, current_args[1], count_def, 0)
            max_width = cast_number(int, current_args[2], max_width_def, 1)
        case 4: # script_name + 3 args (count, width, height)
            count = cast_number(int, current_args[1], count_def, 0)
            max_width = cast_number(int, current_args[2], max_width_def, 1)
            max_height = cast_number(int, current_args[3], max_height_def, 1)
        case 5: # script_name + 4 args (count, width, height, delay)
            count = cast_number(int, current_args[1], count_def, 0)
            max_width = cast_number(int, current_args[2], max_width_def, 1)
            max_height = cast_number(int, current_args[3], max_height_def, 1)
            sleep_time = cast_number(float, current_args[4], sleep_time_def, 0.0)
        case 6: # script_name + 5 args (count, width, height, delay, rule_id)
            count = cast_number(int, current_args[1], count_def, 0)
            max_width = cast_number(int, current_args[2], max_width_def, 1)
            max_height = cast_number(int, current_args[3], max_height_def, 1)
            sleep_time = cast_number(float, current_args[4], sleep_time_def, 0.0)
            opposite_key = valid_opposite_key(current_args[5])
        case _:
            pass
    
    
    return count, max_width, max_height, sleep_time, opposite_key
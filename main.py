import random
import os 
import time
from argv_helper import get_from_argvs
from edge import Edge
from random_piece_generator import RandomPieceGenerator
from piece_key_piece_printer import PieceKeyPiecePrinter, EscapeColor
from piece_key_piece_helper import print_key_groups_counts
from piece_key_piece_print_positions import print_row_position  
from print_positions import DEFAULT_PRINT_POSITIONS
from opposite_piece_keys import OPPOSITE_KEYS, DEFAULT_OPPOSITE_KEY
import sys

def main():

    current_argv = sys.argv

    once, width, height, sleep_time = get_from_argvs(current_argv)

    printer : PieceKeyPiecePrinter = PieceKeyPiecePrinter(sleep_time)
    
    if once:
            do_once(printer, generate_random_pieces(width, height))
    else:
        while True:

            do_once_random(width, height, printer)

            time.sleep(4 * sleep_time)

def do_once_random(width, height, printer):
    
    w = random.choice(range(width)) + 1
    h = random.choice(range(min(w, height))) + 1

    do_once(printer, generate_random_pieces(w, h, opposite_key = random.choice(OPPOSITE_KEYS)))

def generate_random_pieces(width, height, print_positions = DEFAULT_PRINT_POSITIONS, opposite_key = DEFAULT_OPPOSITE_KEY):

    return RandomPieceGenerator(width, height,print_positions.print_positions, opposite_key)


def do_once(printer, random_pieces, print_positions = DEFAULT_PRINT_POSITIONS):
    
    os.system("clear")
      
    printer.print_pieces(random_pieces.border, Edge.DOWN, EscapeColor.MAGENTA)      

    printer.print_changes(random_pieces.pieces)      

    print_row_position(random_pieces.bottom_left(), Edge.UP, print_positions.scale_x, print_positions.scale_y, print_positions.x, print_positions.y)

    print(EscapeColor.YELLOW.value)

    _ = print_key_groups_counts(random_pieces.pieces)


main()
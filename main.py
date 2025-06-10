import random
import os 
import time
from argv_helper import get_from_argvs
from edge import Edge
from random_piece_key_fitter import RandomPieceKeyFitter
from piece_key_piece_printer import PieceKeyPiecePrinter, EscapeColor
from piece_key_piece_helper import print_key_groups_counts
from piece_key_piece_print_positions import print_row_position  
from print_positions import PrintPositions
from opposite_piece_keys import OPPOSITE_PIECE_KEY_DIGITS, OPPOSITE_KEYS
import sys

def main():

    current_argv = sys.argv

    max_width, max_height, sleep_time, count, opposite_key = get_from_argvs(current_argv)

    scale_x = 3
    scale_y = 3
    x = 1
    y = 1

    if count > 0:
        for _ in range(count):
            once(max_width, max_height, sleep_time, scale_x, scale_y, x, y, opposite_key)
    else:
        while True:

            w = random.choice(range(max_width)) + 1
            h = random.choice(range(min(w, max_height))) + 1

            opposite_key = random.choice(OPPOSITE_KEYS)

            once(w, h, sleep_time, scale_x, scale_y, x, y, opposite_key)


def once(w, h, sleep_time, scale_x, scale_y, x, y, opposite_key):
    
    os.system("clear")

    fitter = RandomPieceKeyFitter(w, h, PrintPositions(scale_x, scale_y, x, y).print_positions, opposite_key)
    
    printer : PieceKeyPiecePrinter = PieceKeyPiecePrinter(sleep_time)  
        
    printer.print_pieces(fitter.pieces, Edge.LEFT, EscapeColor.BLUE)      
    printer.print_pieces(fitter.pieces, Edge.RIGHT, EscapeColor.BLUE)      
    printer.print_pieces(fitter.pieces, Edge.UP, EscapeColor.BLUE)      
    printer.print_pieces(fitter.pieces, Edge.DOWN, EscapeColor.BLUE)      

    fitter.fit_and_print_all(printer.print)

    print_row_position(fitter.bottom_left(), Edge.UP, scale_x, scale_y, x, y)

    print()

    print(f'{w} : {h} : {OPPOSITE_PIECE_KEY_DIGITS[opposite_key]}')
       
    _ = print_key_groups_counts(fitter.pieces)

    time.sleep(4)

main()
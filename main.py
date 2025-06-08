import random
import os 
import time
from argv_helper import get_from_argvs
from edge import Edge
from random_piece_key_fitter import RandomBasePieceKeyFitter
from piece_key_piece_printer import PieceKeyFitterPicePrinter, EscapeColor
from piece_key_piece_helper import print_key_groups_counts
from piece_key_piece_print_positions import print_row_position  
import sys

def main():

    current_argv = sys.argv

    max_width, max_height, sleep_time = get_from_argvs(current_argv)

    scale_x = 4
    scale_y = 4
    x = 1
    y = 1

    while True:

        os.system("clear")

        w = random.choice(range(max_width)) + 1

        h = random.choice(range(min(w, max_height))) + 1

        fitter = RandomBasePieceKeyFitter(w, h)
    
        printer : PieceKeyFitterPicePrinter = PieceKeyFitterPicePrinter(fitter.spiral, scale_x, scale_y, x, y, sleep_time)  
        
        printer.print_pieces(Edge.LEFT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.RIGHT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.UP, EscapeColor.BLUE)      
        printer.print_pieces(Edge.DOWN, EscapeColor.BLUE)      

        if random.choice([False]):
            fitter.first_fit_and_print_all(printer.get_printer(Edge.LEFT))
            fitter.first_fit_and_print_all(printer.get_printer(Edge.UP))
            fitter.first_fit_and_print_all(printer.get_printer(Edge.RIGHT))
            fitter.first_fit_and_print_all(printer.get_printer(Edge.DOWN))
        else:
            fitter.second_fit_and_print_all(printer.edge_printer)

        print_row_position(fitter.bottom_left(), Edge.UP, scale_x, scale_y, x, y)

        print()

        _ = print_key_groups_counts(fitter.pieces)

        time.sleep(2)
    
main()
import random
import os 
import time
from argv_helper import get_from_argvs
from edge import Edge
from random_piece_key_fitter import RandomBasePieceKeyFitter
from piece_key_piece_printer import PieceKeyFitterPicePrinter, EscapeColor
from piece_key_piece_helper import print_key_groups_counts
from piece_key_piece_print_positions import print_row_position  
from print_positions import PrintPositions
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

        fitter = RandomBasePieceKeyFitter(w, h, PrintPositions(scale_x, scale_y, x, y).print_positions)
    
        printer : PieceKeyFitterPicePrinter = PieceKeyFitterPicePrinter(sleep_time)  
        
        printer.print_pieces(fitter.spiral, Edge.LEFT, EscapeColor.BLUE)      
        printer.print_pieces(fitter.spiral, Edge.RIGHT, EscapeColor.BLUE)      
        printer.print_pieces(fitter.spiral, Edge.UP, EscapeColor.BLUE)      
        printer.print_pieces(fitter.spiral, Edge.DOWN, EscapeColor.BLUE)      

        match random.choice(range(3)):
            case 0:
                fitter.fit_and_print_all(printer.print)
            case 1:
                fitter.first_fit_and_print_all(printer.get_printer(Edge.LEFT))
                fitter.first_fit_and_print_all(printer.get_printer(Edge.UP))
                fitter.first_fit_and_print_all(printer.get_printer(Edge.RIGHT))
                fitter.first_fit_and_print_all(printer.get_printer(Edge.DOWN))
            case 2:
                fitter.fit_all()
                printer.print_pieces(fitter.pieces, Edge.LEFT, EscapeColor.MAGENTA)      
                printer.print_pieces(fitter.pieces, Edge.RIGHT, EscapeColor.MAGENTA)      
                printer.print_pieces(fitter.pieces, Edge.UP, EscapeColor.MAGENTA)      
                printer.print_pieces(fitter.pieces, Edge.DOWN, EscapeColor.MAGENTA)      
         
          
        print_row_position(fitter.bottom_left(), Edge.UP, scale_x, scale_y, x, y)

        print()

        _ = print_key_groups_counts(fitter.pieces)

        time.sleep(4)
    
main()
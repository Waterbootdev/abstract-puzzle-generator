import random
import os 
import time
from argv_helper import get_from_argvs
from edge import Edge
from random_piece_key_fitter import RandomBasePieceKeyFitter
from piece_key_piece_printer import PieceKeyFitterPicePrinter, EscapeColor
import sys

def main():

    current_argv = sys.argv

    max_width, max_height, sleep_time = get_from_argvs(current_argv)

    while True:

        os.system("clear")

        w = random.choice(range(max_width)) + 1

        h = random.choice(range(min(w, max_height))) + 1

        fitter = RandomBasePieceKeyFitter(w, h)
    
        printer : PieceKeyFitterPicePrinter = PieceKeyFitterPicePrinter(fitter.spiral, 6, 4, 2, 1, sleep_time)  
        
        printer.print_pieces(Edge.LEFT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.RIGHT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.UP, EscapeColor.BLUE)      
        printer.print_pieces(Edge.DOWN, EscapeColor.BLUE)      

        fitter.fit_all_pices(printer.get_printer(Edge.LEFT),printer.get_printer(Edge.UP),printer.get_printer(Edge.RIGHT),printer.get_printer(Edge.DOWN))

        time.sleep(2)

    
main()
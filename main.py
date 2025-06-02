import random
import os 
import time
from edge import Edge
from random_piece_key_fitter import RandomBasePieceKeyFitter
from PieceKeyPiecePrinter import PieceKeyFitterPicePrinter, EscapeColor

def main():

    while True:

        w = random.choice(range(8,45))

        h = random.choice(range(4, min(w, 17)))

        fitter = RandomBasePieceKeyFitter(w,h)
    
        os.system("clear")
  
        printer : PieceKeyFitterPicePrinter = PieceKeyFitterPicePrinter(fitter.spiral, 6, 4, 2, 1, 1)  
   
        printer.print_pieces(Edge.LEFT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.RIGHT, EscapeColor.BLUE)      
        printer.print_pieces(Edge.UP, EscapeColor.BLUE)      
        printer.print_pieces(Edge.DOWN, EscapeColor.BLUE)      

        fitter.fit_all_pices(printer.get_printer(Edge.LEFT),printer.get_printer(Edge.UP),printer.get_printer(Edge.RIGHT),printer.get_printer(Edge.DOWN))

        time.sleep(2)
    
main()
from edge import Edge
from escape_color import EscapeColor
from printer_helper import print_animated
from piece_key_piece import PieceKeyPiece
from typing import Tuple

class PieceKeyPiceEdgePrinter:
    def __init__(self, edge: Edge, seconds: float, red: EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green :EscapeColor = EscapeColor.GREEN ) -> None:
        self.edge = edge
        self.seconds = seconds
        self.red = red
        self.yellow = yellow
        self.green = green

    def print(self, piece: PieceKeyPiece, t: Tuple[bool,str]):
        not_fitted, part = t
        print_animated(self.seconds, piece, not_fitted, part, self.edge, self.red, self.yellow, self.green)
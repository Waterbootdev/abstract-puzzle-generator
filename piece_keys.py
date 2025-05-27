from piece_key_parts import int_to_significant, pad_zeros
from piece_key_constants import MAX_NUMBER_PIECE_KEYS

PIECE_KEY_PARTS = [int_to_significant(i) for i in range(MAX_NUMBER_PIECE_KEYS)]
PIECE_KEYS = [pad_zeros(significant) for significant in PIECE_KEY_PARTS]
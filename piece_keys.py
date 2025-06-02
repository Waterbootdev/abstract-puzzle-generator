from piece_key_parts import int_to_significant, pad_zeros
from piece_key_constants import MAX_NUMBER_PIECE_KEYS

PIECE_KEY_PARTS = [int_to_significant(i) for i in range(MAX_NUMBER_PIECE_KEYS)]
PIECE_KEYS = [pad_zeros(significant) for significant in PIECE_KEY_PARTS]

PIECE_KEYS_1 =[key[:1] for key in  PIECE_KEYS]
PIECE_KEYS_12 =[key[:2] for key in  PIECE_KEYS]
PIECE_KEYS_123 =[key[:3] for key in  PIECE_KEYS]

PIECE_KEYS_STARTS = set(PIECE_KEYS + PIECE_KEYS_1 + PIECE_KEYS_12 + PIECE_KEYS_123)

PIECE_KEYS_STARTS_WITH = {start : [key for key in PIECE_KEYS if key.startswith(start)] for start in PIECE_KEYS_STARTS}

PIECE_KEYS_ENDS_WITH_STARTS_WITH = {end : {start : [key for key in [key for key in PIECE_KEYS if key.endswith(end)] if key.startswith(start)] for start in PIECE_KEYS_STARTS}  for end in PIECE_KEYS_STARTS}




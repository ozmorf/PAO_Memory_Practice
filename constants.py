from ascii import *

ASCII_MAP = {
    0: range_zeroes_small,
    10: range_tens_small,
    20: range_twenties_small,
    30: range_thirties_small,
    40: range_forties_small,
    50: range_fifties_small,
    60: range_sixties_small,
    70: range_seventies_small,
    80: range_eighties_small,
    90: range_nineties_small,
}

CONVERT_NUMBERS_MAP = {
    "easy": convert_numbers_easy,
    "medium": convert_numbers_medium,
    "hard": convert_numbers_hard,
    "custom": convert_numbers_custom
}

CONVERT_PHRASES_MAP = {
    "easy": convert_phrases_easy,
    "medium": convert_phrases_medium,
    "hard": convert_phrases_hard,
    "custom": convert_phrases_custom,
}
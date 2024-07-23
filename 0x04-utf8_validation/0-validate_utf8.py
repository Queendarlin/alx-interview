#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Checks if the given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes
    :return: Boolean value indicating if the data is valid UTF-8
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF  # Ensure byte is within 8 bits
        if n_bytes == 0:
            # Check the leading byte
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif byte >> 7:
                return False
        else:
            # Check continuation byte
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0

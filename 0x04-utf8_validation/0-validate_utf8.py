#!/usr/bin/python3
"""Function to check for valid utf-8"""


def validUTF8(data):
    """Helper function to check if a byte is a valid continuation byte"""
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    """Iterate through the data bytes"""
    i = 0
    while i < len(data):
        byte = data[i]

        """Check the number of bytes in the current character"""
        if (byte & 0b10000000) == 0:
            i += 1
        elif (byte & 0b11100000) == 0b11000000:
            if i + 1 >= len(data) or not is_continuation(data[i + 1]):
                return False
            i += 2
        elif (byte & 0b11110000) == 0b11100000:
            if i + 2 >= len(data) or not is_continuation(
                    data[i + 1]) or not is_continuation(data[i + 2]):
                return False
            i += 3
        elif (byte & 0b11111000) == 0b11110000:
            if i + 3 >= len(data) or not is_continuation(
                    data[i + 1]) or not is_continuation(
                    data[i + 2]) or not is_continuation(data[i + 3]):
                return False
            i += 4
        else:
            """Invalid starting byte"""
            return False

    """All checks passed, the data is a valid UTF-8 encoding"""
    return True

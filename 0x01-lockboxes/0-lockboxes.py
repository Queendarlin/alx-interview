#!/usr/bin/python3
"""function correctly determines whether all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened starting from the first box (box 0).

    Args:
    boxes (list of list of int): A list where each index represents a box

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False

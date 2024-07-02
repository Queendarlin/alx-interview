#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened starting from the first box (box 0).
    
    Args:
    boxes (list of list of int): A list where each index represents a box and
                                 each element is a list of keys contained in that box.
    
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    num_boxes = len(boxes)
    opened = set()
    keys = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in opened:
            opened.add(box)
            keys.update(boxes[box])
            for key in boxes[box]:
                if key < num_boxes and key not in opened:
                    queue.append(key)

    return len(opened) == num_boxes

#!/usr/bin/python3
"""Lockboxes function """


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Parameters:
    - boxes (List[List[int]]): A list of lists representing
    the boxes and their keys.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if boxes is None or not isinstance(boxes, list):
        return False

    opened_boxes = {0}
    closed_boxes = set(range(1, len(boxes)))
    keys = set(boxes[0])

    def open_box(key):
        """Open each box"""
        if key in closed_boxes:
            opened_boxes.add(key)
            closed_boxes.remove(key)
            new_keys = boxes[key]
            for new_key in new_keys:
                open_box(new_key)

    for key in keys:
        open_box(key)

    if len(closed_boxes) > 0:
        return False
    else:
        return True


if __name__ == "__main__":
    canUnlockAll([[]])

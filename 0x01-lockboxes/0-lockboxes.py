#!/usr/bin/env python3
"""Lockboxes function """


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Parameters:
    - boxes (List[List[int]]): A list of lists representing the boxes and their keys.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        # Invalid input, return False
        return False

    # Initialize a set to keep track of the opened boxes
    opened_boxes = set()

    # Add the first box to the set of opened boxes
    opened_boxes.add(0)

    # Initialize a stack to perform depth-first search
    stack = [0]

    # Perform depth-first search to open boxes
    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in opened_boxes:
                # If the key opens a new box, add it to the set of opened boxes
                opened_boxes.add(key)
                stack.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)


if __name__ == "__main__":
    canUnlockAll([[]])

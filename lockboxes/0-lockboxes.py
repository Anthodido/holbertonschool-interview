#!/usr/bin/python3

"""Lockboxes module."""


def canUnlockAll(boxes):

    """Determines if all the boxes can be opened."""

    if not boxes:
        return False
    opened = set([0])
    to_open = [0]
    while to_open:
        box = to_open.pop()
        for key in boxes[box]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                to_open.append(key)
    return len(opened) == len(boxes)

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Initialize the stack with the first box

    while stack:
        box = stack.pop()  # Get the top box from the stack

        # Iterate over the keys in the current box
        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True  # Mark the box as visited
                stack.append(key)  # Add the box to the stack

    # Check if all boxes have been visited
    return all(visited)

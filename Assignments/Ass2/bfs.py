LEFT_BUCKET_CAPACITY = 4
RIGHT_BUCKET_CAPACITY = 3

GOAL = (0, 2)
RESULT = []

def move_left_to_right(jug):
    allowed_space = min(RIGHT_BUCKET_CAPACITY - jug[1], jug[0])
    return (jug[0] - allowed_space, jug[1] + allowed_space)

def move_right_to_left(jug):
    allowed_space = min(LEFT_BUCKET_CAPACITY - jug[0], jug[1])
    return (jug[0] + allowed_space, jug[1] - allowed_space)

def empty_left(jug):
    return (0, jug[1])

def empty_right(jug):
    return (jug[0], 0)

def fill_left(jug):
    return (LEFT_BUCKET_CAPACITY, jug[1])

def fill_right(jug):
    return (jug[0], RIGHT_BUCKET_CAPACITY)

def get_available_operations(jug):
    operations = {
        move_left_to_right,
        move_right_to_left,
        empty_left,
        empty_right,
        fill_left,
        fill_right
    }

    # if left jug is empty
    if jug[0] == 0:
        operations.remove(empty_left)
        operations.remove(move_left_to_right)
    
    # if left jug is full
    elif jug[0] == LEFT_BUCKET_CAPACITY:
        operations.remove(fill_left)
        operations.remove(move_right_to_left)
    
    # if right jug is empty
    if jug[1] == 0:
        operations.remove(empty_right)
        try: operations.remove(move_right_to_left)
        except KeyError: pass

    # if right jug is full
    elif jug[1] == RIGHT_BUCKET_CAPACITY:
        operations.remove(fill_right)
        try: operations.remove(move_left_to_right)
        except KeyError: pass

    return operations

class Node:
    def __init__(self, jug: tuple[int, int], parent = None) -> None:
        self.jug = jug
        self.parent = parent

def grow_tree(parent: Node, previous = {(0, 0)}) -> bool:
    queue = [parent]

    while len(queue) != 0:
        node = queue[0]
        queue.pop(0) # Remove first elemnt from queue

        operations = get_available_operations(node.jug)
        # Iterate over all operations for current node
        # Assign the child nodes to parent
        for op in operations:
            child_jug = op(node.jug)
            child = Node(child_jug, node)

            if child_jug == GOAL:
                RESULT.append(child)
                return True

            if child_jug in previous:
                continue
            else:
                previous.add(child_jug)
            
            queue.append(child)

    return False

def main():
    seed = Node((0, 0))

    if grow_tree(seed):
        print("The full path is")
        for endpoint in RESULT:
            path = []
            while endpoint.parent:
                path.append(endpoint.jug)
                endpoint = endpoint.parent
            
            path = reversed(path)
            print("(0, 0)", end='')
            for p in path:
                print(' ->', p, end='')
    else:
        print("Could not reach the goal", GOAL)


if __name__ == '__main__':
    main()
    # For (0, 2)
    # (0, 0) -> (0, 3) -> (3, 0) -> (3, 3) -> (4, 2) -> (0, 2)
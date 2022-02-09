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
    def __init__(self, jug: tuple[int, int]) -> None:
        self.jug = jug
        self.children: list[Node] = []

def grow_tree(node: Node, previous = {(0, 0)}, maxdepth = 10) -> bool:
    if maxdepth == 0 or node.jug[0] < 0 or node.jug[1] < 0:
        return False

    operations = get_available_operations(node.jug)
    # print("\n\nAvailable operations for", node.jug, "are", operations)
    # (0, 0) -> (0, 3) -> (3, 0) -> (3, 3) -> (4, 2) -> (0, 2)
    for op in operations:
        child = op(node.jug)
        
        if child == GOAL:
            # print(child)
            RESULT.append(GOAL)
            return True
        
        if child in previous:
            # print("Failed at", node.jug, "on", op)
            continue
        else:
            previous.add(child)
            pass

        node.children.append(Node(child))
        if grow_tree(node.children[-1], previous, maxdepth - 1):
            # print(node.children[-1].jug)
            RESULT.append(node.children[-1].jug)
            return True
        else:
            node.children.pop()
            pass
    
    # print("Failed at", node.jug)
    return False

def main():
    seed = Node((0, 0))

    if grow_tree(seed):
        print("The full path is \n(0, 0)", end='')
        for path in reversed(RESULT):
            print(' ->', path, end='')
    else:
        print("Could not reach the goal", GOAL)


if __name__ == '__main__':
    main()
    # For (0, 2)
    # (0, 0) -> (0, 3) -> (3, 0) -> (3, 3) -> (4, 2) -> (0, 2)
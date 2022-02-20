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

def get_operation_name(operation) -> str:
    return {
        fill_left: 'fill left jug',
        fill_right: 'fill right jug',
        empty_left: 'empty left jug',
        empty_right: 'empty right jug',
        move_left_to_right: 'pour left jug into right jug',
        move_right_to_left: 'pour right jug into left jug',
    }[operation]

class Node:
    def __init__(self, jug: tuple[int, int], operation_name: str = None) -> None:
        self.jug = jug
        self.children: list[Node] = []
        self.operation_name = operation_name

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.jug == other.jug
        elif isinstance(other, tuple):
            return self.jug == other
        else:
            return False

    def __repr__(self) -> str:
        return str(self.jug)

def grow_tree(node: Node, previous = {(0, 0)}, maxdepth = 10) -> bool:
    if maxdepth == 0:
        return False

    operations = get_available_operations(node.jug)
    for op in operations:
        child = op(node.jug)
        
        if child == GOAL:
            RESULT.append(Node(GOAL, get_operation_name(op)))
            return True
        
        if child in previous:
            continue
        else:
            previous.add(child)
            pass

        node.children.append(Node(child, get_operation_name(op)))
        if grow_tree(node.children[-1], previous, maxdepth - 1):
            RESULT.append(node.children[-1])
            return True
        else:
            node.children.pop()
            pass
    
    return False

# This function prunes the nodes which can be reached directly by root (0, 0)
def optimise(result: list[Node]) -> list[Node]:
    operations = get_available_operations((0, 0))
    for op in operations:
        child = op((0, 0))
        try:
            index = result.index(child)
            result = result[index:]
        except ValueError:
            pass
    
    return result

def main():
    seed = Node((0, 0))

    if grow_tree(seed):
        print("The full path is")
        print("From (0, 0)".rjust(49))
        result = list(reversed(RESULT))
        result = optimise(result)
        for i, node in enumerate(result):
            print(f'Step {i + 1}   {node.operation_name.ljust(30)} => {node.jug}')
            
    else:
        print("Could not reach the goal", GOAL)


if __name__ == '__main__':
    main()
    # For (0, 2)
    # (0, 0) -> (0, 3) -> (3, 0) -> (3, 3) -> (4, 2) -> (0, 2)
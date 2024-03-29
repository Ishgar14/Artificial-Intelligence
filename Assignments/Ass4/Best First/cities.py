SOURCE = "Latur"
DESTINATION = "Navi Mumbai"

DISTANCE_FROM_DESTINATION = {
    "Solapur": 340,
    "Satara": 177,
    "Navi Mumbai": 0,
    "Nashik": 133,
    "Ahmednagar": 180,
    "Aurangabad": 265,
    "Nanded": 451,
    "Latur": 373,
    "Pune": 105,
}

# A weighted undirected map of cities
GRAPH = {}

def put_city(city1: str, city2: str, weight: int) -> None:
    global GRAPH

    if city1 in GRAPH:
        GRAPH[city1].append((city2, weight))
    else:
        GRAPH[city1] = [(city2, weight)]

    if city2 in GRAPH:
        GRAPH[city2].append((city1, weight))
    else:
        GRAPH[city2] = [(city1, weight)]

def generate_map() -> None:
    put_city("Pune", "Navi Mumbai", 106)
    put_city("Pune", "Satara", 112)
    put_city("Pune", "Solapur", 234)
    put_city("Solapur", "Satara", 203)
    put_city("Solapur", "Latur", 104)
    put_city("Nanded", "Latur", 113)
    put_city("Nanded", "Aurangabad", 221)
    put_city("Nashik", "Aurangabad", 159)
    put_city("Nanded", "Ahmednagar", 267)
    put_city("Pune", "Ahmednagar", 120)
    put_city("Nashik", "Pune", 165)
    put_city("Nashik", "Navi Mumbai", 136)


def distance(from_: str, to: str) -> int:
    if from_ == to:
        return 0

    array = GRAPH[from_]
    for name, weight in array:
        if name == to:
            return weight

    return 10 ** 10

class Node:
    def __init__(self, city: str, prev: object, weight: int) -> None:
        self.city = city
        self.prev = prev
        self.weight = weight

    def __repr__(self) -> str:
        return self.city

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.city == other.city
        elif isinstance(other, str):
            return self.city == other
        else:
            return False

def objective(city) -> int:
    return DISTANCE_FROM_DESTINATION[city]

def main() -> None: 
    generate_map()
    print('=' * 40)
    print("Starting city is Latur")
    print("Destination city is Navi Mumbai")
    # from pprint import pprint
    # pprint(GRAPH)

    current = Node(SOURCE, None, 0)
    opened = []
    closed = [current]

    while len(closed) > 0:
        print('=' * 40)
        print("Opened list:", opened)
        print("Closed list:", closed)

        closed.sort(
                key=lambda node: objective(node.city),
                reverse=True
        )

        current = closed.pop()

        if current not in opened:
            opened.append(current)

        if current == DESTINATION:
            print("🎉We got there!🎉".center(40, ' '))
            break

        print("Selected", current)

        # Add all neighbours of current city into queue
        print(f"The neighbouring cities of {current} are")
        for name, dist in GRAPH[current.city]:
            print(f"{name:>12} with distance {dist}")

            if name not in opened:
                closed.append(Node(name, current, dist))
        print()
    
    path = []
    while current:
        path.append(current)
        current = current.prev
    
    print("=" * 40)
    print("The full path is ")
    for city in path[::-1]:
        if city.prev:
            print(f"{city.prev.city} to {city.city} with distance {city.weight}")

if __name__ == '__main__':
    main()
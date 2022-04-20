Graph = dict[str, list[str]]
COLORS = ["red", "green", "blue", "yellow"]


def generate_graph() -> dict:
    graph = {}

    def put_neighbours(n1: str, n2: str):
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
        
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]
    
    put_neighbours('a', 'b')
    put_neighbours('a', 'c')

    put_neighbours('b', 'c')
    put_neighbours('b', 'f')

    put_neighbours('c', 'e')
    put_neighbours('c', 'd')

    put_neighbours('d', 'e')
    
    put_neighbours('e', 'f')

    put_neighbours('f', 'a')
    put_neighbours('f', 'b')
    put_neighbours('f', 'c')

    put_neighbours('g', 'e')


    return graph


def neighbour_colors(node: str, graph: Graph, node_colors: dict[str, str]) -> list[str]:
    # This function returns colours of neighbours of `node`
    neighbours = graph[node]
    return { n:node_colors[n] for n in neighbours if n in node_colors }


def start(graph: Graph, node_colors: dict[str, str] = {}):
    for key in graph:
        if key in node_colors:
            continue

        nc = neighbour_colors(key, graph, node_colors)
        available_colours = [color for color in COLORS if color not in nc.values()]
        print(f"Colours available for {key} are", available_colours)

        for c in available_colours:
            node_colors[key] = c
            print(f"Applying colour {c} to node {key}\n")
            
            if color_list := start(graph, node_colors):
                if len(color_list) == len(graph):
                    return color_list

    return node_colors


def main() -> None: 
    graph = generate_graph()

    print(" Structure of Graph ".center(40, '='))
    for node, neighbours in graph.items():
        print(f"Node {node} has neighbours:", neighbours)
    print('\n', ' Applying Colours '.center(40, '='), sep='')

    colors = start(graph)
    # from pprint import pprint
    # pprint(graph)
    # pprint(colors)

    print('\n', " After colouring ".center(40, '='), sep='')
    for node, color in colors.items():
        print(f"Node {node} gets {color:<6} colour")


if __name__ == '__main__':
    main()
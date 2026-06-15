import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, travel_time):
        self.edges[from_node].append((to_node, travel_time))
        self.edges[to_node].append((from_node, travel_time))   # Undirected graph


def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))

    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0

    shortest_path = {node: None for node in graph.nodes}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, shortest_path


def shortest_route(graph, start, end):
    distances, shortest_path = dijkstra(graph, start)

    route = []
    current_node = end

    while current_node is not None:
        route.append(current_node)
        current_node = shortest_path[current_node]

    route.reverse()

    return route, distances[end]


def main():
    graph = Graph()

    num_nodes = int(input("Enter number of locations: "))
    print("Enter locations:")

    for _ in range(num_nodes):
        node = input().strip()
        graph.add_node(node)

    num_edges = int(input("Enter number of paths: "))
    print("Enter path details (from to time):")

    for _ in range(num_edges):
        from_node, to_node, travel_time = input().split()
        graph.add_edge(from_node, to_node, int(travel_time))

    start = input("Enter starting location: ").strip()
    end = input("Enter destination: ").strip()

    route, time = shortest_route(graph, start, end)

    print("Shortest route:", " -> ".join(route))
    print("Travel time:", time)
if __name__ == "__main__":
    main()
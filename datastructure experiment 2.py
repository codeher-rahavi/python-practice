import heapq

def dijkstra(graph, source, target):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if u == target:
            break

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u].items():
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    path = []
    node = target
    while node:
        path.append(node)
        node = prev[node]
    path.reverse()

    return path, dist[target]



graph = {}

n = int(input("Enter number of locations: "))
print("Enter location names:")

locations = []
for i in range(n):
    loc = input(f"Location {i+1}: ")
    locations.append(loc)
    graph[loc] = {}

e = int(input("Enter number of roads: "))

print("Enter roads (source destination travel_time):")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    graph[u][v] = w
    graph[v][u] = w

source = input("Enter source location: ")
target = input("Enter destination location: ")

path, distance = dijkstra(graph, source, target)

print("\nShortest Route:", " -> ".join(path))
print("Minimum Travel Time:", distance)
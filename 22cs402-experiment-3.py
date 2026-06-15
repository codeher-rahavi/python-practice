def find(parent, node):
    if parent[node] == node:
        return node
    return find(parent, parent[node])


def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        parent[root_v] = root_u


def kruskal(vertices, edges):
    parent = {}
    mst = []

    # Initialize parent
    for vertex in vertices:
        parent[vertex] = vertex

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Process edges
    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, u, v)

    return mst


def main():
    vertices = input("Enter cities separated by spaces: ").split()
    num_edges = int(input("Enter number of connections: "))

    edges = []

    print("Enter connections in format: city1 city2 cost")
    for _ in range(num_edges):
        u, v, weight = input().split()
        edges.append((u, v, int(weight)))

    mst = kruskal(vertices, edges)

    print("\nMinimum Spanning Tree:")
    total_cost = 0

    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")
        total_cost += weight

    print("Total Cost:", total_cost)


if __name__ == "__main__":
    main()
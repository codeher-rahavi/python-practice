from collections import deque

landmark = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':[],
    'G':[]
}
def bfs(start, end):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        visited.add(current)
        for neighbor in landmark.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None


landmark1= {
    'A':['B','C'],
    'B':['D'],
    'C':['E','F'],
    'D':[],
    'E':['G'],
    'F':['h'],
    'G':[]
}
def dfs(current, end, visited, path):
    visited.add(current)
    path.append(current)
    if current == end:
        return path.copy()
    for neighbor in landmark1.get(current, []):
        if neighbor not in visited:
            result = dfs(neighbor, end, visited, path)
        if result:
            return result
    path.pop()
    return None
def get_directions_dfs(start, end):
    return dfs(start, end, set(), [])
def main():
    print("Available Landmarks for BFS:")
    for i in landmark:
        print(f"{i}: connects to {landmark[i]}")
    start=input("enter the starting landmark:").strip().upper()
    end=input("enter the ending landmark:").strip().upper()
    if start not in landmark or end not in landmark:
        print("invalid landmark")
        return
    path=bfs(start,end)
    method = "BFS"
    if path:
        print(f"Directions using {method}:")
        print(" -> ".join(path))
    else:
        print("no path found")

    print("Available Landmarks for DFS:")
    for i in landmark1:
        print(f"{i}: connects to {landmark1[i]}")
    start = input("enter the starting landmark:").strip().upper()
    end = input("enter the ending landmark:").strip().upper()
    if start not in landmark1 or end not in landmark1:
        print("invalid landmark")
        return

    path = get_directions_dfs(start, end)
    method = "DFS"
    if path:
        print(f"Directions using {method}:")
        print(" -> ".join(path))
    else:
        print("no path found")


if __name__ == "__main__":
    main()
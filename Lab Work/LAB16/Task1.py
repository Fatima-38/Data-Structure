# =========================
# Graph + DFS (Week 16)
# =========================
# We store the graph using an Adjacency List:
# graph["A"] = ["B", "C"] means A is connected to B and C.

from typing import Dict, List, Set


class Graph:
    def __init__(self, directed: bool = False) -> None:
        # If directed=True, edges go one way (u -> v)
        # If directed=False, edges go both ways (u <-> v)
        self.directed = directed

        # adjacency list: dictionary of vertex -> list of neighbors
        self.adj: Dict[str, List[str]] = {}

    # -------------------------
    # ADD VERTEX
    # -------------------------
    def add_vertex(self, v: str) -> None:
        # If vertex doesn't exist, create an empty neighbor list
        if v not in self.adj:
            self.adj[v] = []

    # -------------------------
    # ADD EDGE
    # -------------------------
    def add_edge(self, u: str, v: str) -> None:
        # Ensure both vertices exist
        self.add_vertex(u)
        self.add_vertex(v)

        # Add v to u's neighbor list (avoid duplicates)
        if v not in self.adj[u]:
            self.adj[u].append(v)

        # If graph is undirected, also add u to v's list
        if not self.directed:
            if u not in self.adj[v]:
                self.adj[v].append(u)

    # -------------------------
    # DISPLAY GRAPH
    # -------------------------
    def display(self) -> None:
        # Print each vertex and its neighbors
        for v in sorted(self.adj.keys()):
            print(v, "->", self.adj[v])

    # -------------------------
    # DFS RECURSIVE
    # -------------------------
    def dfs_recursive(self, start: str) -> List[str]:
        visited: Set[str] = set()   # to avoid infinite loops
        order: List[str] = []       # store visit order

        def dfs(v: str) -> None:
            # Mark visited and record this node
            visited.add(v)
            order.append(v)

            # Visit all neighbors
            for nbr in self.adj.get(v, []):
                if nbr not in visited:
                    dfs(nbr)

        # Run DFS from start if it exists
        if start in self.adj:
            dfs(start)

        return order

    # -------------------------
    # DFS USING STACK (ITERATIVE)
    # -------------------------
    def dfs_stack(self, start: str) -> List[str]:
        if start not in self.adj:
            return []

        visited: Set[str] = set()
        order: List[str] = []

        stack: List[str] = [start]  # start node in stack

        while stack:
            v = stack.pop()         # take the last element (LIFO)

            # If already visited, skip it
            if v in visited:
                continue

            # Mark visited and record
            visited.add(v)
            order.append(v)

            # Add neighbors to stack
            # Reverse keeps order similar to recursive (optional)
            for nbr in reversed(self.adj.get(v, [])):
                if nbr not in visited:
                    stack.append(nbr)

        return order

# -------------------------
# MINI TEST (Run this)
# -------------------------
if __name__ == "__main__":
    g = Graph(directed=False)

    # Sample graph
    # A connected to B and C
    # B connected to D
    # C connected to E
    # D connected to F
    edges = [("A","B"), ("A","C"), ("B","D"), ("C","E"), ("D","F"), ("E","F")]

    for u, v in edges:
        g.add_edge(u, v)

    print("Adjacency List:")
    g.display()

    print("DFS Recursive from A:", g.dfs_recursive("A"))
    print("DFS Stack from A:", g.dfs_stack("A"))

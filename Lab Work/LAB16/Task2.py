# ==========================================
# Week 16: Dijkstra + MST (Prim + Kruskal)
# ==========================================
# We use a weighted adjacency list:
# graph["A"] = [("B", 4), ("C", 2)]  means A-B weight 4, A-C weight 2

from typing import Dict, List, Tuple
import heapq


WeightedGraph = Dict[str, List[Tuple[str, int]]]


# -------------------------
# DIJKSTRA (Shortest Path)
# -------------------------
def dijkstra(graph: WeightedGraph, start: str) -> Dict[str, int]:
    # distance dictionary: start is 0, others are infinity
    INF = 10**9
    dist: Dict[str, int] = {node: INF for node in graph}
    dist[start] = 0

    # min-heap stores (distance, node)
    pq: List[Tuple[int, str]] = [(0, start)]

    while pq:
        cur_dist, u = heapq.heappop(pq)

        # If we already found a better distance, skip
        if cur_dist > dist[u]:
            continue

        # Try to relax edges (u -> v)
        for v, w in graph[u]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


# -------------------------
# PRIM (MST)
# -------------------------
def prim_mst(graph: WeightedGraph, start: str) -> List[Tuple[str, str, int]]:
    # MST edges: (u, v, weight)
    mst: List[Tuple[str, str, int]] = []

    visited = set([start])

    # min-heap stores edges (weight, from, to)
    pq: List[Tuple[int, str, str]] = []

    # push all edges from start
    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq and len(visited) < len(graph):
        w, u, v = heapq.heappop(pq)

        # If v already in MST, skip (to avoid cycles)
        if v in visited:
            continue

        # Accept this edge
        visited.add(v)
        mst.append((u, v, w))

        # Add edges from the new vertex
        for nxt, w2 in graph[v]:
            if nxt not in visited:
                heapq.heappush(pq, (w2, v, nxt))

    return mst


# -------------------------
# UNION-FIND (Disjoint Set)
# -------------------------
class UnionFind:
    def __init__(self, nodes: List[str]) -> None:
        # parent[x] = parent of x (initially x itself)
        self.parent = {x: x for x in nodes}
        # rank helps keep trees shallow
        self.rank = {x: 0 for x in nodes}

    def find(self, x: str) -> str:
        # Find root parent with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: str, b: str) -> bool:
        # Join two sets, return True if union happened
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # already connected (would form cycle)

        # Union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


# -------------------------
# KRUSKAL (MST)
# -------------------------
def kruskal_mst(nodes: List[str], edges: List[Tuple[str, str, int]]) -> List[Tuple[str, str, int]]:
    # Sort edges by weight
    edges_sorted = sorted(edges, key=lambda x: x[2])

    uf = UnionFind(nodes)
    mst: List[Tuple[str, str, int]] = []

    for u, v, w in edges_sorted:
        # Take edge if it doesn't create a cycle
        if uf.union(u, v):
            mst.append((u, v, w))

        # Stop when MST has (n-1) edges
        if len(mst) == len(nodes) - 1:
            break

    return mst

# -------------------------
# MINI TEST (Run this)
# -------------------------
if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 3)],
        "F": [("D", 6), ("E", 3)]
    }

    print("Dijkstra from A:", dijkstra(graph, "A"))

    print("Prim MST from A:", prim_mst(graph, "A"))

    # For Kruskal we need all edges (u, v, w) unique (undirected)
    edges = [
        ("A","B",4), ("A","C",2), ("B","C",1), ("B","D",5),
        ("C","D",8), ("C","E",10), ("D","E",2), ("D","F",6), ("E","F",3)
    ]
    print("Kruskal MST:", kruskal_mst(list(graph.keys()), edges))


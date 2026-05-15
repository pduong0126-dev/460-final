"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Phu Duong
Student ID:   132120388

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    return  """
        
    Computing only single shortest-path will not figure out which order of relic chambers is the most optimal.

    What order of relic chambers to visit respective to their costs should be taken to minimize fuel costs.

   Search over orders because we are finding the most optimal order of relic chambers to visit.

    """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    sources = []
    for node in [spawn] + relics + [exit_node]:
        if node not in sources:
            sources.append(node)
    return sources


def run_dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    pq = [(0, source)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_cost > distances[current_node]:
            continue

        for neighbor, edge_cost in graph.get(current_node, []):
            new_cost = current_cost + edge_cost

            if neighbor not in distances:
                distances[neighbor] = float('inf')

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return distances


def precompute_distances(graph, spawn, relics, exit_node):
    sources = select_sources(spawn, relics, exit_node)
    dist_table = {}

    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
   return  """
    For nodes already finalized (in S), their stored distance is locked in as the minimum possible cost from the source.
    For nodes not yet finalized (not in S), their stored distance is the best route found so far using only finalized nodes as intermediate stops.
    The invariant holds before initialization because the first node is the entrance, a source with a distance of 0 and distances of inf to all other nodes, hence no other shortest path.
    Finalizing the min-dist node is always correct because all edge weights are nonnegative, so any other later paths cannot be shorter than the min-dist node.
    When the algorithm ends, the invariant guarantees that every reachable node has been finalized with its shortest path from the source. Unreachable nodes are 'inf'.
    Correct shortest path distance ensures that the torchbearer compares relic orders using real travel costs instead of false costs.

    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    return """
        Greedy fails because it does not consider which order of relics will be the most optimal. Choosing a local relic may cascade into more expensive choices later.
        Let's say S->A=1, S->B=2, A->B=100, A->C=100, B->C=1, C->A=1, A->T=1. Greedy starts with A because it is the cheapest locally, then B or C because there are no other options. Total cost is 100+.
        Optimal picks B, C, A, then T. Total cost is 5, much lower than greedy.
        Greedy picks immediate cheapest, forsaking later better paths.
        The algorithm must explore all possible path combinations such that the order of relics chosen is its minimzal cost.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    best = [float('inf'), []]
    relics_remaining = set(relics)

    _explore(
        dist_table,
        spawn,
        relics_remaining,
        [],
        0,
        exit_node,
        best
    )

    return best[0], best[1]


def _explore(dist_table, current_location, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    A recursive branch is pruned when it is not a potential best route.
    Furthermore, nonnegative weights ensures that even if we continue the branch, it cannot get any lower than the best route so far.
    """
    if cost_so_far >= best[0]:
        return

    if not relics_remaining:
        exit_cost = dist_table[current_location].get(exit_node, float('inf'))
        total_cost = cost_so_far + exit_cost

        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = list(relics_visited_order)

        return

    for next_relic in list(relics_remaining):
        travel_cost = dist_table[current_location].get(next_relic, float('inf'))

        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(next_relic)
        relics_visited_order.append(next_relic)

        _explore(
            dist_table,
            next_relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )

        relics_visited_order.pop()
        relics_remaining.add(next_relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()

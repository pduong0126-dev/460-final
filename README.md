# The Torchbearer

**Student Name:** Phu Duong
**Student ID:** 132120388
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  Computing only single shortest-path will not figure out which order of relic chambers
  is the most optimal. 

- **What decision remains after all inter-location costs are known:**
  What order of relic chambers to visit respective to their costs should be taken to
  minimize fuel costs.

- **Why this requires a search over orders (one sentence):**
  Search over orders because we are finding the most optimal order of relic chambers
  to visit.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Entrance | The torchbearer starts from here. |
| Relic Chambers | After reaching a relic, the current chamber is the source for the next chamber/exit. |
| Exit | The torchbearer exits here, included for completeness |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary |
| What the keys represent | Outer key is source node, inner key is destination node |
| What the values represent | Cheapest path from source to destination |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Python hashes keys so dictionary lookups are typically O(1) |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** k+2
- **Cost per run:** O(m log n)
- **Total complexity:** O((k+2)m log n)
- **Justification (one line):** There exists k relic chambers, 1 entrance, 1 exit; hence k+2

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  Their stored distance is locked in as the minimum possible cost from the source.

- **For nodes not yet finalized (not in S):**
  Their stored distance is the best route found so far using only finalized nodes as intermediate stops.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  The first node is the entrance, a source with a distance of 0 and distances of inf to all other nodes,
  hence no other shortest path.

- **Maintenance : why finalizing the min-dist node is always correct:**
  All edge weights are nonnegative, so any other later paths cannot be shorter than the min-dist node. 

- **Termination : what the invariant guarantees when the algorithm ends:**
  Every reachable node has been finalized with its shortest path from the source. Unreachable nodes are 'inf'.

### Part 3c: Why This Matters for the Route Planner

Correct shortest path distance ensures that the torchbearer compares relic orders using real travel costs instead
of false costs.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** Greedy fails because it does not consider which order of relics will be the most optimal.
Choosing a local relic may cascade into more expensive choices later.
- **Counter-example setup:** Let's say S->A=1, S->B=2, A->B=100, A->C=100, B->C=1, C->A=1, A->T=1.
- **What greedy picks:** Greedy starts with A because it is the cheapest locally, then B or C because there
are no other options. Total cost is 100+.
- **What optimal picks:** Optimal picks B, C, A, then T. Total cost is 5.
- **Why greedy loses:** Greedy picks immediate cheapest, forsaking later better paths.

### What the Algorithm Must Explore

- The algorithm must explore all possible path combinations such that the order of relics chosen is its
minimzal cost.

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | 'current_location' | node | The current location, also the end of the route thus far |
| Relics already collected | 'relics_visited_order' | list[node] | The relics collected so far in the order they were visited |
| Fuel cost so far | 'cost_so_far' | float | The cost incurred so far |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | 'set' named 'relics_remaining' |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Gives fast updates and allows for efficient backtracking |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** k!
- **Why:** This is considering the algorithm tries every possible combination

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** The best/cheapest route and its relic order computed so far
- **When it is used:** Before expanding new recursive branches in explore()
- **What it allows the algorithm to skip:** Routes that already have greater costs than the cheapest

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** Current location, relics remaining, relics visited order, cost so far, and the best/cheapest route so far
- **What the lower bound accounts for:** The cost so far
- **Why it never overestimates:** All edge weights are nonnegative, therefore final cost cannot be less than the cost so far

### Part 6c: Pruning Correctness

- A recursive branch is pruned when it is not a potential best route.
- Furthermore, nonnegative weights ensures that even if we continue the branch, it cannot get any lower than the best route so far.

---

## References

- 

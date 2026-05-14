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

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

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
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._

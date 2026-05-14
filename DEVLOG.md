# Development Log – The Torchbearer

**Student Name:** Phu Duong
**Student ID:** 132120388

---

## Entry 1 – [05/14/2026 - 2:00 PM]: Initial Plan

- Format the entrance, exit, and relic chambers as important nodes. At each important node, run 
Dijkstra's to find shortest-paths to all other nodes, retain only the distances found between
two important nodes, then visiting each relic chamber exactly once before finishing at the exit.
DP is required to find optimal path and avoid recomputing with Dijsktra's redundantly and so
that it can decide the most optimal order of relic chambers to visit. A single shortest-path
will not be able to do this. 

---

## Entry 2 – [05/14/2026 - 2:40 PM]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

The very first time I pressed run module, despite making no code changes, I got the error "TypeError: cannot unpack non-iterable NoneType object".
I searched it up, found out it's because I have none/nil variables returned from the solve() function. I 

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis + Setup | 30 minutes |
| Part 2: Precomputation Design | 20 minutes |
| Part 3: Algorithm Correctness | 30 minutes |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |

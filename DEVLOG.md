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

## Entry 2 – [05/14/2026 - 2:00-4:00 PM]: Parts 1-6 & Errors

The very first time I pressed run module, despite making no code changes, I got the error "TypeError: cannot unpack non-iterable NoneType object".
I searched it up, found out it's because I have none/nil variables returned from the solve() function. To circumvent this, I had to temporarily comment out lines in main that required run_dijkstra(), precompute_distances(), and select_sources(), readding them when necessary.

---

## Entry 3 – [05/14/2026 - 4:00-7:25 PM]: Code Implementation

The code implementation was fairly smooth due to the sheer amount of theory I had to prepare beforehand. Debugging was not an issue because of this as well.

---

## Entry 4 – [05/14/2026 - 9:00 PM]: Post-Implementation Reflection

The assignment being around 70% conceptual and 30% coding helped me have a more enjoyable experience overall. Often during coding assignments, I would spend a majority of the time debugging and figuring out why IDE shell was pure red. Functions like run_dijkstra() and select_sources() were pretty straightforward due to the lectures and parts 1-6. Most of my time spent was in the explore() function and all of its moving parts.

---

## Final Entry – [05/14/2026 - 11:59 PM]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis + Setup | 30 minutes |
| Part 2: Precomputation Design | 20 minutes |
| Part 3: Algorithm Correctness | 30 minutes |
| Part 4: Search Design | 15 minutes |
| Part 5: State and Search Space | 20 minutes |
| Part 6: Pruning | 30 minutes |
| Part 7: Implementation | 2.5 Hours |
| README and DEVLOG writing | 35 Minutes |
| **Total** | 5 Hours |

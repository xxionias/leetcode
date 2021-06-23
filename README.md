# leetcode

## 1143:
There are a couple of strategies we use to design a tractable (non-exponential)
algorithm for an optimization problem.

1. Identifying a greedy algorithm
2. Dynamic programming

There is no guarantee that either is possible. Additionally, greedy algorithms
are strictly less common than dynamic programming algorithms and are often more
difficult to identify. However, if a greedy algorithm exists, then it will
almost always be better than a dynamic programming one. You should, therefore,
at least give some thought to the potential existence of a greedy algorithm
before jumping straight into dynamic programming.

Recall that there are two different techniques we can use to implement a dynamic
programming solution; memoization and tabulation.

1. **Memoization** is where we add caching to a function (that has no side
  effects). In dynamic programming, it is typically used on recursive functions
  for a top-down solution that starts with the initial problem and then
  recursively calls itself to solve smaller problems.
2. **Tabulation** uses a table to keep track of subproblem results and works in
a bottom-up manner: solving the smallest subproblems before the large ones, in
an iterative manner. Often, people use the words "tabulation" and "dynamic
programming" interchangeably.

For most people, it's easiest to start by coming up with a recursive brute-force
solution and then adding memoization to it. After that, they then figure out how
to convert it into an (often more desired) bottom-up tabulated algorithm.

# leetcode

(ctrl + shift + m to preview .md in Atom)

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

## 149. Max Points on a Line
One can run a fun experiment to calculate the result for the operation of ```1.2 − 1.0``` in the Python shell. (spoiler alert: we would get the value of 0.19999999999999996 as the result.)

Therefore, it is not wise to use the float/double value to represent a unique slope, since they are not accurate.

To circumvent the above issue, one could use a pair of **co-prime integers** to represent unique slope.
As a reminder, **two integers are co-primes, if and only if their greatest common divisor is 1**.

As one can see, due to the property of co-prime numbers, they can be used to represent the slope values of different lines. For example, for the slope values of 1/3, 2/6, 3/9, they all can be represented with the co-prime numbers of (1, 3).

## 914. X of a Kind in a Deck of Cards

The **reduce(fun,seq)** function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in **“functools”** module.

Working :
- At first step, first two elements of sequence are picked and the result is obtained.
- Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
- This process continues till no more elements are left in the container.
- The final returned result is returned and printed on console.

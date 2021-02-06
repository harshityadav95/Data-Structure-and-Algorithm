# Algorithm Design

### 1. Exhaustive Search or Brute Force Algorithm

An exhaustive search, or brute force, algorithm examines every possible alternative to find one particular solution.

### 2. Branch and Bound Algorithm  

Suppose you were exhaustively searching the first floor and heard the phone ringing above your head. You could immediately rule out the need to search the basement or the first floor. What may have taken three hours  may now only take one, depending on the amount of space that you can rule out

### 3. Greedy Algorithm

Greedy algorithms choose the “most attractive” alternative at each it-eration, for example, the largest denomination possible. In the case of theUS denominations,Changeused quarters, then dimes, then nickels, andfinally pennies \(in that order\) to make change. Of course, we showed thatthis greedy strategy produced incorrect results when certain new denom-inations were included.

### 4. Dynamic Programming

Some algorithms break a problem into smaller subproblems and use the solutions of the subproblems to construct the solution of the larger one. During this process, the number of subproblems may become very large, and some algorithms solve the same subproblem repeatedly, needlessly increasing the running time. Dynamic programming organizes computations to avoid re computing values that you already know, which can often save a great deal of time

### 5. Recursive  Algorithms

Recursion is one of the most ubiquitous algorithmic concepts. Simply, analgorithm is recursive if it calls itself.

### 6. Divide and Conquer Algorithm

One big problem may be hard to solve, but two problems that are half the size may be significantly easier. In these cases, divide-and-conquer al-gorithms fare well by doing just that: splitting the problem into smaller  subproblems, solving the subproblems independently, and combining the solutions of subproblems into a solution of the original problem.

### 7. Randomized Algorithm

If you happen to have a coin, then before even starting to search for the phone, you could toss it to decide whether you want to start your search on the first floor if the coin comes up heads, or on the second floor if the coin comes up tails. If you also happen to have a die, then after deciding on the second floor of your mansion, you could roll it to decide in which of the six rooms on the second floor to start your search. Although tossing coinsand rolling dice may be a fun way to search for the phone, it is certainly not the intuitive thing to do, nor is it at all clear whether it gives you any algorithmic advantage over a deterministic algorithm














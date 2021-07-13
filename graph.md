# Graph

![](.gitbook/assets/image%20%287%29.png)

## Understanding the properties of graphs, in theory, is great and all, but when it comes down to solving the problem we need to know how to actually implement them in code. We’ll go through a few common ways of building out graphs from scratch, each with its own set of strengths and tradeoffs. <a id="398c"></a>

It’s important to remember that graphs as data structures are an abstract concept. They have basic components, like **nodes**, **edges,** and **weights**. They have a set of properties like **connectivity** and **directionality.** And they also have a set of behaviors that enable certain functionality, like adding/removing nodes and connections.

But this says nothing about HOW you implement those components, properties, and behaviors under the hood.

Some implementations are more **space-efficient**, some are easier to **traverse**, some give you the ability to **add or remove nodes quickly**, some are better at managing the **connections between nodes**, some give you more **flexible functionality**, and some contain the bare **minimum information** to express the graph.

And like most problems, your choice of implementation should depend on knowing what’s the best tool for getting the job done.

So let’s start with an example graph and a single question:

> If I asked you to build the graph below, how would you do it?

![](https://miro.medium.com/max/60/1*Xx9uatuEKH4WOnw95Lw2pw.png?q=20)![](https://miro.medium.com/max/700/1*Xx9uatuEKH4WOnw95Lw2pw.png)

## **Adjacency Matrix Implementation** <a id="bc59"></a>

The first approach we’ll cover uses **matrices**, which themselves are typically implemented as an **array of arrays**.

There are a couple of ways you can use think of matrices as graphs. One is very visual, where the graph is constrained into being a lattice, where each node can have at most 4 connections to other nodes: one above, one below, one to the left, and one to the right.

There are a couple of interesting problems that use this implementation of matrices as a graph:[Number of Islands - LeetCodeLevel up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared…leetcode.com](https://leetcode.com/problems/number-of-islands/)

The constraint of a maximum of 4 connections per node allows you to make certain guarantees. Namely that the number of edges for a graph with N nodes will never exceed 4N. This is good for coming up with path-finding or maze-solving algorithms in 2D grids, like streets in a city.![](https://miro.medium.com/max/60/1*2gNH5XsNgUVQTaSQ4s3kPw.png?q=20)![](https://miro.medium.com/max/700/1*2gNH5XsNgUVQTaSQ4s3kPw.png)

But if you want a graph that can allow more than a more flexible way of uses matrices to represent graphs is through something called an _adjacency matrix_.

To translate this particular graph into an adjacency matrix first we need to label each node. Let’s call them v1 through v6.![](https://miro.medium.com/max/60/1*BJC6bU0yMtgBX8rTJvejOg.png?q=20)![](https://miro.medium.com/max/700/1*BJC6bU0yMtgBX8rTJvejOg.png)

Labeling things is a good general problem-solving technique to get into because it lets you reference and work with specific examples of objects more easily and in this case it lets us talk about each unique node individually.

Once we’ve labeled every node, we need to create an NxN matrix, where N is the number of nodes present in the graph. We then label each row and column after each node in the graph \(v1…v6\)![](https://miro.medium.com/max/60/1*_gn6UW3vAhAVaFAHfI5Ocw.png?q=20)![](https://miro.medium.com/max/700/1*_gn6UW3vAhAVaFAHfI5Ocw.png)

Now here’s the **key idea behind adjacency matrices:**

> “Each cell in this matrix represents a connection between two nodes.”

Every **row** represents the connections originating from that node.

And every **column** represents the connections arriving at that particular node.

So for example, if there is a connection from v1 to v2, then we would put an entry in the cell corresponding to row v1 and column v2.

This entry can simply be an integer like the number 1. If you wanted to add weighting to your graph then you could use other integers or even floats for extra precision.

But if there are no connections between two nodes then you would typically insert a zero, or the matrix would be filled with zeroes when initialized.![](https://miro.medium.com/max/60/1*U4Sr5U_V6BqueDBt8gGQHg.png?q=20)![](https://miro.medium.com/max/700/1*U4Sr5U_V6BqueDBt8gGQHg.png)

One interesting observation you can make about the adjacency matrix implementation of a graph is the contrast between undirected and directed graphs. Namely, it’s the idea of **symmetry**.

On a conceptual level, symmetry means that in a connection between two nodes, either one can be the origin or destination. Enforcing this constraint means that in your adjacency matrix you’ll have a mirror-image along the diagonal line of the matrix.![](https://miro.medium.com/max/60/1*-gqrF97lbn63Hruw5fwh4Q.png?q=20)![](https://miro.medium.com/max/700/1*-gqrF97lbn63Hruw5fwh4Q.png)

In an undirected graph, no such constraint exists so you won’t necessarily get this mirror-image effect.

Another small convention is that usually the diagonal line is populated with 1s since every node can be thought of as having a connection to itself.

Matrices give a visual understanding of what’s going on with graphs that I think can help with our intuition around key operations like making connections between nodes, and ideas of symmetry.

But matrices aren’t very space-efficient, especially for sparsely connected graphs. Empty cells in the matrix are essentially a waste of space and only become useful once a new connection is made. The amount of space used scales at a rate of N-squared because every time you add a new node you need to add another row and column.

And what’s worse is that if you want to remove a node, you need to remove its row, but also all the columns associated with it, which requires a lot of array slicing.

But these are a good choice if you know the number of nodes you’ll be working with is fixed, and they are highly connected to one another. Matrices also allow you to allocate memory upfront which can speed up the performance of accessing/making/removing connections since you’re just writing integers to an array of arrays.

So to summarize, adjacency matrices are great for highly connected matrices, with a fixed number of nodes, and with simple edges connecting them, but terrible for adding new nodes or removing old ones.

## **Edge List Implementation** <a id="7d27"></a>

The issue that matrices had was that they pre-allocated a lot of memory upfront because each node had its own row and column.

But what if instead of focusing on the nodes, we instead focused on the connections between nodes?

We could instead just store the connections between nodes as a list of tuples. These tuples could just be two-element arrays for our purposes. The first element would be the node where the connection originates. The second element would be where the connection terminates.

What we get if we do this for the whole graph is an **edge list**.![](https://miro.medium.com/max/60/1*wReDgDwbFJxOPTHi-Ae1vQ.png?q=20)![](https://miro.medium.com/max/700/1*wReDgDwbFJxOPTHi-Ae1vQ.png)

This edge list contains the minimum amount of information needed to represent this graph, which makes it a good compressed format for storing the data or transmitting it.

If we wanted to add functionality for the edge weights between nodes then we can simply add another value to the tuple \(now a triple\). The more mathematical notation for this is usually **\(u, v, w\)**, for the origin, destination, and weight.![](https://miro.medium.com/max/60/1*_efHWcQjQrADimeBXiTfbA.png?q=20)![](https://miro.medium.com/max/700/1*_efHWcQjQrADimeBXiTfbA.png)

The amount of memory this implementation uses is only proportional to the number of edges. This means for a densely connected graph, this won’t be any better than a matrix implementation, but the fewer connections you have between nodes the better.

But the minimalism of using an edge list has its own set of tradeoffs.

For one, you don’t have an easy sense of how many nodes are in your network. With the matrix, you can check the number of rows easily, but with an edge list, you need to look through all the edges and count up the unique nodes you see.

This also causes problems for removing the nodes from the list: you need to search through the whole thing and remove any connections that might contain the node you’re trying to remove.

You also can’t easily add nodes to your graph unless you connect them to another node, so this isn’t great for disjoint graphs. Though you can get around this by adding edges for nodes between themselves. This is similar to that diagonal line of symmetry I mentioned in the

But most importantly, edge lists aren’t great for traversals. If you want to follow a trail of connections through the graph, it can become very cumbersome very quickly. This is because the edges themselves don’t give you any sense of where other edges in the graph might be. You’ll potentially have to look through the entire set of edges just to find the next step in the traversal, which is far from ideal.

In summary, edge lists are good for capturing all the information of a graph in a simple manner that’s easy to understand. And they do this well even when the nodes are sparsely connected, but they are very poor for choices for performing traversals on.

## **Adjacency List/Set Implementation** <a id="c9c2"></a>

Adjacency lists give you the best of both worlds. A happy middle-ground between the previous two implementations.

The best way to implement this kind of graph is to think of it as a dictionary where all the nodes are keys, and the values are an array containing the nodes they are connected to.

Representing your graph this way lets you quickly see how many nodes there are, which is just the number of keys in your dictionary, and how many edges there are, which is the sum of the lengths of the arrays.

Adjacency lists are also very easy to perform traversals on, regardless of whether they are breadth-first or depth-first. I’ll cover how to perform those in more detail in the next post.![](https://miro.medium.com/max/60/1*QGnPqATukMTfCccmrp219A.png?q=20)![](https://miro.medium.com/max/700/1*QGnPqATukMTfCccmrp219A.png)

Just know that this implementation is also usually more efficient than using an adjacency matrix since you’ll often need to scan through a lot of empty cells to check for connections. And it’s FAR better than using an edge-list, which fails miserably at traversals since every step of the traversal requires you to scan through the full list of edges.

As for basic operations, adding new nodes is simple: just add a new key to the dictionary, with an empty array as the value, since it has no connections.

Adding a new connection between nodes is as simple as adding a new entry into that array. If you’re implementing an undirected graph, then you would add one entry into the array corresponding to the origin node, and one in the one for the destination node. If it’s directed, then just add it to the origin node’s array.

Something important to consider when adding new connections between nodes is that you need to make sure a previous connection doesn’t already exist between those two nodes. This means you need to scan through the list, which can be time-consuming if there are already a lot of connections in there. And the more connections you add, the longer each successive scan will take.![](https://miro.medium.com/max/60/1*jD1Rf9x2OiMdDr7afKS7QA.png?q=20)![](https://miro.medium.com/max/700/1*jD1Rf9x2OiMdDr7afKS7QA.png)

This same scanning problem applies to removing a connection between nodes, but you also have to account for the time it takes to splice that connection out of the array, and the time that re-indexing existing elements will take.

And because removing connections can be time-consuming, removing nodes is also expensive because you need to loop through all the other nodes and remove any connections to the node you’re removing. This is more of a problem in directed graphs than in undirected graphs because they lack symmetry, though there are a few ways to get around this that involve sacrificing some additional space. Essentially each node would need to keep track of which nodes are pointing to it, in addition to which nodes it is a point to.![](https://miro.medium.com/max/60/1*rsScbM-heP7pRwW8N3IoaA.png?q=20)![](https://miro.medium.com/max/700/1*rsScbM-heP7pRwW8N3IoaA.png)

One way to address these problems, and make this implementation more efficient is to **substitute the array for a set**. It may seem like a minor change, but there are three important features of sets that dramatically simplify our code and improve efficiency.

**First**, sets are constrained to only having unique elements. How they do this efficiently is fascinating and a topic for another post, but this feature allows us to avoid doing a lot of manual duplicate checking when adding new connections between nodes.

**Second**, looking up an element in a set takes constant time \(on average\), which means we don’t need to scan through the whole set to find out if an element is in there, we can just query it. This saves time on

**And third**, because there are no indices in sets because \(sets are unordered\), they don’t need any reindexing when we splice elements out of them.

Those three things can massively speed up making and breaking connections between nodes, as well as removing nodes entirely.

And the cherry on top is that the code for implementing the basic operations in an adjacency set is astonishingly simple since you no longer have to worry about duplicates:

So to summarize:

Pros: Space-efficient, easy to traverse, and easy to perform basic operations \(if using a Set\).

Cons: Some of the basic node operations are slightly more complex than the adjacency matrix implementation, like finding all the connections that point to a specific node.

And if you aren’t using a set, some of the basic operations are both algorithmically complex to check for duplicates, as well as being somewhat inefficient. Making them more efficient requires the use of additional space, and introduces additional complexity in your code.

## **Object-Oriented Approach** <a id="e695"></a>

The last approach is to use traditional OOP principles.

You have an encapsulating graph class that contains a set of labeled nodes, which themselves are their own class. The nodes usually in some kind of dictionary, where the keys are the labels and the values are the node instances.![](https://miro.medium.com/max/60/1*PeBVnS79W6RhdPaMBVf4-A.png?q=20)![](https://miro.medium.com/max/700/1*PeBVnS79W6RhdPaMBVf4-A.png)

I won’t cover the object-oriented implementation of graphs in too much depth since it’s very similar to the adjacency list/set with some extra overhead for the class definitions. Though this overhead can be helpful for organizing your methods and properties.

Each node contains references to the nodes it’s connected to, and optionally, what nodes are connected to it, and any other data associated with it, like weights between connections, metadata, and any information specific to your use-case \(think back to airports, social media profiles, etc.\)

Adding/removing nodes/connections is pretty similar to the previous approach, with the only change being the need to instantiate new objects \(rather than using strings or numbers like in the previous example\) and that you are using class methods instead of standalone functions.

The main tradeoff is you need to write more code for the extra functionality. For example, where an adjacency matrix has the number of nodes implicitly in the number of rows, you’ll need to make sure you have some data stored on the graph class level that gives you that information, like a size property. You then also have to explicitly increment or decrement the size anytime you add or remove nodes, which can create room for errors.

This is why it’s sometimes better to use a lightweight implementation of a graph, especially in an interview setting.

But if you’re working with graphs on any practical level you’re going to need these more abstract implementations.

## **Conclusion** <a id="e6ea"></a>

This was an overview of some of the common implementations of graphs and the tradeoffs between them. Like in any problem, it’s always good to know not only what the best tool for the job is, but also why it’s the best. Having a few different approaches to model a graph will give us flexibility in how we’re able to go about solving it.

In the next post, we’ll look at how the original problem actually converts into a graph problem, and we’ll explore a few different ways we’re able to actually perform graph traversal algorithms.

Hopefully, you enjoyed this post, and stay tuned for the next part in the series on how to solve the Alien Dictionary Problem!What is a Graph?

In theoretical computer science, graphs are different from what you learned about in middle school. They are not bar charts.![](https://miro.medium.com/max/12000/0*RnSO2a60n7lDURgS)Photo by [M. B. M.](https://unsplash.com/@m_b_m?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral). \(This is not what a graph in Computer Science is\)

Graphs in theoretical Computer Science and Discrete Mathematics are an abstract way of representing various types of relationships such as roads connecting cities and other types of networks. Graphs are made up of two components: edges and vertices. A vertex is a point on a graph and an edge is what connects two points on a graph.![](https://miro.medium.com/max/60/1*8uYV2SIT7c6AwxYXu9vbDQ.png?q=20)![](https://miro.medium.com/max/570/1*8uYV2SIT7c6AwxYXu9vbDQ.png)An example of a graph

Graph problems in competitive programming will usually be talking about things like networks and grids in the problem statement.

Here’s a list of all the graph terminology you need to know:

* **Path:** A sequence of edges which joins a sequence of distinct \(different\) vertices.
* **Walk:** Walks are paths, but they don’t require a sequence of distinct vertices.
* **Cycle:** A group of vertices linked together in a closed chain. In the picture above, \[1,2,4\] is a cycle.
* **Connected Graph:** A graph where any pair of vertices have a path between them.
* **Tree:** A connected graph that does not contain a cycle.
* **Undirected Graph:** A graph where the edges have no direction, the picture above shows an undirected graph. In an undirected graph, you can travel in any direction along an edge.
* **Directed Graph:** A graph where the edges have directions, the directions are represented by arrows. In a directed graph, you can only travel along an edge in the direction it goes.

## Representing Graphs in Code <a id="1ce3"></a>

Before we’re able to code up any graph algorithms, you will need to know how to represent graphs in code. All of the following code will be in C++ since that is my favorite language for competitive programming due to its speed and built-in functions that make it easy to write up solutions to problems.

I’ll be showing you two ways to represent graphs: Adjacency Matrices and Adjacency Lists. Most of the time you’ll be using the Adjacency List representation.

### Adjacency Matrices: <a id="213d"></a>

An Adjacency Matrix represents a graph as a 2D matrix with dimensions V x V where V is the number of vertices of the graph. Adjacency matrices are best to use when V² roughly equals E \(number of edges\), that is when the graph is dense. Entry a\_ij represents how many edges connect vertex i and vertex j.![](https://miro.medium.com/max/60/1*KVgpkmM3DxjA5AhcAbWPmg.png?q=20)![](https://miro.medium.com/max/481/1*KVgpkmM3DxjA5AhcAbWPmg.png)A directed graph, it’s adjacency matrix is below![](https://miro.medium.com/max/60/1*XXSuCPMHbL_I8ApW0ceWgw.png?q=20)![](https://miro.medium.com/max/278/1*XXSuCPMHbL_I8ApW0ceWgw.png)A 6 x 6 matrix that represents the directed graph.

**Code:**

The following code constructs an adjacency matrix for an undirected graph. To modify it to construct an adjacency matrix for a directed graph, change the add\_edge function by removing the second line within it: `matrix[v][u] = 1;`

```text
#include<bits/stdc++.h>
using namespace std;
int matrix[20][20]; //the adjacency matrix initially 0
int count = 0;
//The following function is just used to output the 
void displayMatrix(int v) {
   int i, j;
   for(i = 0; i < v; i++) {
      for(j = 0; j < v; j++) {
         cout << matrix[i][j] << " ";
      }
      cout << endl;
   }
}
void add_edge(int u, int v){  //function to add edge into the matrix
   matrix[u][v] = 1;
   matrix[v][u] = 1;
}
main(int argc, char* argv[]) {
   int v = 6;    //there are 6 vertices in the graph
   add_edge(0, 4);
   add_edge(0, 3);
   add_edge(1, 2);
   add_edge(1, 4);
   add_edge(1, 5);
   add_edge(2, 3);
   add_edge(2, 5);
   add_edge(5, 3);
   add_edge(5, 4);
   displayMatrix(v);
}
```

### Adjacency Lists <a id="af52"></a>

The other common way to represent graphs in code is through Adjacency Lists. Essentially, you create lists of neighbors for each vertex and then put all of those lists inside of another list. These are good to use when you have a small number of edges in your graph, i.e. when your graph is sparse. If you are representing a weighted graph, where each edge has some value, the list will contain pairs of \(neighbor, weight\) for the edges instead.

**Code:**

```text
#include<bits/stdc++.h>using namespace std;void addEdge(vector<int> adj[], int u, int v){
  adj[u].push_back(v); 
  adj[v].push_back(u);//remove this line for directed graphs
}int main(){
 int v = 5; //5 vertices 
 vector<int> adj[v];
 addEdge(adj, 0, 1);
 addEdge(adj, 0, 4);
 addEdge(adj, 1, 2);
 addEdge(adj, 1, 3);
 addEdge(adj, 1, 4);
 addEdge(adj, 2, 3);
 addEdge(adj, 3, 4); 
}
```

## Depth First Search <a id="e8cd"></a>

Now that we’ve learned how to represent Graphs in code, we can begin learning some graph algorithms! We will begin with Depth First Search \(DFS\) and finish out with Breadth-First Search \(BFS\), for the sake of brevity, pathfinding algorithms will not be included in this article.

Depth First search is one of the most basic graph algorithms and it is used to find the distance from one vertex to other vertices in a graph. It is a **traversal algorithm.**

DFS will put each vertex in a graph into one of two labels: visited or not visited. The algorithm marks each vertex as visited while avoiding cycles. It works as follows:

1. Put any one of the graph’s vertices at the top of a stack.
2. Take the item at the top of the stack and add it to the visited list.
3. Create a list of that vertex’s neighbors. Add the ones which are not in the visited list to the top of the stack.
4. Repeat steps 2 and 3 until the stack is empty.

![](https://miro.medium.com/freeze/max/54/0*4UuhDJ0uZ8l1lPnn.gif?q=20)![](https://miro.medium.com/max/289/0*4UuhDJ0uZ8l1lPnn.gif)An animation of DFS. The search starts at vertex 1.

**Code:**

```text
#include <bits/stdc++.h>using namespace std;const int N = 100000;
vector<int> adj[N];
bool visited[N];void dfs(int s) {
  if (visited[s]) return;
  visited[s] = true;
  for (auto u: adj[s]) {
   dfs(u);
  }
}
```

## Breadth-First Search <a id="79a4"></a>

Breadth-First Search is also a graph traversal algorithm and along with DFS will be a big chunk of your Competitive Programming journey, at least when it comes to graphs.

Just like Depth First Search, BFS puts each vertex in a graph into one of two categories, visited or not visited. The purpose for the algorithm is also the same, to mark each vertex in a graph as visited while avoiding cycles. It works as follows:

1. Put any vertex in the graph at the back of a queue.
2. Take the item at the front of the queue and add it to the visited list.
3. Create a list of that vertex’s neighbors. Add the ones which are not visited to the back of the queue.
4. Repeat 2 and 3 until the queue is empty.

As you can see the algorithm is very similar to DFS. However, instead of going down a branch of a graph or tree like DFS does, BFS goes through each level.![](https://miro.medium.com/freeze/max/60/0*e79U49476sXVmS1s.gif?q=20)![](https://miro.medium.com/max/463/0*e79U49476sXVmS1s.gif)BFS Animation. It starts at vertex 1.

**Code:**

```text
// A Quick implementation of BFS using
// vectors and queue
#include <bits/stdc++.h>
#define pb push_backusing namespace std;vector<bool> v;
vector<vector<int> > g;void edge(int a, int b){
  g[a].pb(b);
  // for undirected graph add this line
  // g[b].pb(a);
}void bfs(int u){
  queue<int> q;
  q.push(u);
  v[u] = true;
  while (!q.empty()) {
    int f = q.front();
    q.pop();
    // Enqueue all adjacent of f and mark them visited
    for (auto i = g[f].begin(); i != g[f].end(); i++) {
      if (!v[*i]) {
        q.push(*i);
        v[*i] = true;
      }
    }
  }
}
```


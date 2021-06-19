# Graph



## What is a Graph? <a id="398c"></a>

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


# Heap

## What is a Heap? <a href="#10c5" id="10c5"></a>

A **Heap** is a complete binary tree-based data structure. You should have a good understanding of [trees](https://medium.com/@mariam.jaludi/data-structures-trees-1bafa942cd60) before jumping to this section. Heaps have specific ordering properties. The ordering can be one of two types:

1. **Max-Heap**: The value of each node is less than or equal to the value of the parent. The greatest value is at the root. The same property must be true for all subtrees.
2. **Min-Heap**: The value of each node is greater than or equal to the value of its parent. The smallest value is at the root. The same property must be true for all subtrees.

Let’s visualize what these two types look like:![](https://miro.medium.com/max/60/1\*EU964HO0LZyypp7\_MLkY8A.jpeg?q=20)![](https://miro.medium.com/max/700/1\*EU964HO0LZyypp7\_MLkY8A.jpeg)Max and Min Heaps

Heaps are **not** sorted. There is no particular relationship between nodes at any level. Since heaps are complete binary trees, the height of a tree with N nodes has O(logN) height.

## When are Heaps useful? <a href="#7ece" id="7ece"></a>

Heaps are used when the highest or lowest order/priority element needs to be removed. They allow quick access to this item in O(1) time. One use of a heap is to implement a priority queue.

Binary heaps are usually implemented using arrays, which save overhead cost of storing pointers to child nodes.

### Cons of Using Heaps <a href="#f6b1" id="f6b1"></a>

Heaps only provide easy access to the smallest/greatest item. Finding other items in the heap takes O(n) time because the heap is not ordered. We must iterate through all the nodes.

## Implementation of a Heap <a href="#fb53" id="fb53"></a>

We are going to try to implement a min-heap using an array. Let’s put the min-heap in the image above into an array:![](https://miro.medium.com/max/60/1\*A052UOlhgb7MAA4Q-IoUUQ.jpeg?q=20)![](https://miro.medium.com/max/561/1\*A052UOlhgb7MAA4Q-IoUUQ.jpeg)

If we are looking at the i-th index in an array:

* It’s parent is at the _floor_ (i-1)/2 index.
* It’s left child is at 2 \* i + 1 index.
* It’s right child is at 2 \*i + 2 index.

In complete binary trees, each level is filled up before another level is added and the levels are filled from left to right.

### Insertion <a href="#fef2" id="fef2"></a>

To insert a node:

1. Add the node to the bottom of the tree.
2. Look at the parent node. If the parent is greater than the node, swap them.
3. Continue comparing and swapping to allow the node to _**bubble up**_ until it finds a parent node that is smaller than it.

Cost: As mentioned before, the height of a tree is log(n). Therefore, the worst case scenario is that the newly added node is smaller than every single parent node, causing us to traverse all the way to the top of the tree. This will cost us O(log(n)) time.

### Deletion (Removing the smallest element) <a href="#e56d" id="e56d"></a>

Because our min-heap has the smallest element at the root node, we know exactly where it is in our array. Accessing this element takes O(1) time.

If we want to delete the element, we must shift the entire tree upwards to fill the root node’s place. To do this:

1. Take the bottom level’s right most node (the last element in the array) and move it to top, replacing the deleted node.
2. Compare the new root to its children. If it is larger than either child, swap the item with the smaller of the two children.
3. Continue comparing and swapping, _**bubbling down**_ the node until it is smaller than both of its children.

Like insertion, the worst case scenario is that we have to traverse the entire tree, but this time we are moving downwards. The cost of this is O(log(n)).

## Transforming Unordered Arrays Into Heaps <a href="#e7a1" id="e7a1"></a>

If we had an unordered array that we wanted to transform into a heap, we could do this by bubbling down the largest elements to allow smaller values to reach the top.

Let’s say we have the following input array:![](https://miro.medium.com/max/60/1\*Zcmgsk\_vsJlakdfBOMfaXQ.jpeg?q=20)![](https://miro.medium.com/max/561/1\*Zcmgsk\_vsJlakdfBOMfaXQ.jpeg)Unordered array![](https://miro.medium.com/max/60/1\*rkvjkMvRg1mRlCT9CbXkWQ.jpeg?q=20)![](https://miro.medium.com/max/461/1\*rkvjkMvRg1mRlCT9CbXkWQ.jpeg)Our unordered array as a tree

To turn this into a valid heap, we have to compare each node with its children. If a node is larger than its children, swap it with the smaller child, i.e. _**bubble down**_ nodes until the smaller values reach the top. This is the same action as removing nodes from a heap.

For the above array, we start at index 0. `array[0] = 20`. Its children are 17 and 30. 17 is less than 20 so we swap the two:![](https://miro.medium.com/max/60/1\*zSa8epv8fWNP6zN4CncVIQ.jpeg?q=20)![](https://miro.medium.com/max/561/1\*zSa8epv8fWNP6zN4CncVIQ.jpeg)![](https://miro.medium.com/max/60/1\*yH9xhxXMo0WMP5tK66TkDw.jpeg?q=20)![](https://miro.medium.com/max/461/1\*yH9xhxXMo0WMP5tK66TkDw.jpeg)

20 is now at index 1. If we look at its children, we have 2 and 5. 2 is the smaller child node so we swap the two:![](https://miro.medium.com/max/60/1\*RvbrI7Iew0gS7ZqltPDT0Q.jpeg?q=20)![](https://miro.medium.com/max/561/1\*RvbrI7Iew0gS7ZqltPDT0Q.jpeg)![](https://miro.medium.com/max/60/1\*JW9V5bciTliKC6Ip8vhHjw.jpeg?q=20)![](https://miro.medium.com/max/461/1\*JW9V5bciTliKC6Ip8vhHjw.jpeg)

Once 20 has become a leaf node, we move on to the new root element, 17. We continue to bubble nodes down until our array is a valid heap. Our final result will look like this:![](https://miro.medium.com/max/60/1\*DJ8wdkr-7lhPs5DhifhKHA.jpeg?q=20)![](https://miro.medium.com/max/561/1\*DJ8wdkr-7lhPs5DhifhKHA.jpeg)![](https://miro.medium.com/max/60/1\*nhOZtMIk-IoQ\_89e2VXZmw.jpeg?q=20)![](https://miro.medium.com/max/461/1\*nhOZtMIk-IoQ\_89e2VXZmw.jpeg)

Cost: Since binary heaps are based on complete binary trees, there will be n/2 nodes at the bottom level, n/4 nodes at the second-to-last, and so on. Each time we go up a level, the number of nodes are cut in half. The worst case time complexity will be O(n). (You can find the sum of the geometric series of all these operations to calculate time complexity to O(n)).

## Building a Heap in Code <a href="#d681" id="d681"></a>

Now that we know what insert, delete, and transforming an array to a heap look like in theory, let’s code it.

First we create our heap class:

```
class BinHeap:
    def __init__(self, array):
        self.heapList = array
        self.currentSize = len(array)
```

We start with a constructor in our heap class. Since our heap can be represented in a list, we initialize it with the unordered list (array) that will be used to build our heap. We also have a `currentSize` attribute to track the length of our heap. Of course, if we wanted to initialize an empty heap, we could pass in an empty list.

Next we will want to add our **push** method. As mentioned previously, we start by adding a new element to the end of our array and then bubble it up to its correct position. We will have two methods: one for pushing and one to bubble an element up:

```
def push(self, node):
    self.heapList.append(node)
    self.currentSize += 1
    index = self.currentSize - 1
    self.bubbleUp(index)def bubbleUp(self, i):
    parentIdx = abs(i - 1) // 2
    while i > 0 and self.heapList[i] < self.heapList[parentIdx]:
        self.heapList[i], self.heapList[parentIdx] = self.heapList[parentIdx], self.heapList[i]
        i = parentIdx
        parentIdx = (i - 1) // 2
```

Now to add our **pop** method. We want to remove the top node, take the right most child (last element in the array) and then bubble it down until it is less than its children. Popping is a little more involved so we will have a delete method and some helper functions to do this:

```
def pop(self):
    last = self.heapList[self.currentSize - 1]
    self.heapList[0] = last
    self.currentSize -= 1
    self.heapList.pop()
    self.bubbleDown()def bubbleDown(self, i=0):
    node = self.heapList[i]
    leftIdx = 2*i + 1
    rightIdx = 2*i + 2
    children = self.getChildren(leftIdx, rightIdx)
    smaller, smallerIdx = self.getSmaller(children)
    while children and val > smaller:
        self.heapList[i], self.heapList[smallerIdx] = self.heapList[smallerIdx], self.heapList[i]
        i = smallerIdx
        leftIdx = 2*i + 1
        rightIdx = 2*i + 2
        children = self.getChildren(leftIdx, rightIdx)
        smaller, smallerIdx = self.getSmaller(children)def getChildren(self, leftI, rightI):
    children = []
    if leftI < self.currentSize:
        children.append((self.heapList[leftI], leftI))
    if rightI < self.currentSize:
        children.append((self.heapList[rightI], rightI))
    return childrendef getSmaller(self, children):
    if len(children) == 0:
        return float('inf'), None
    if len(children) == 1:
        return children[0]
    else:
        childA, iA = children[0]
        childB, iB = children[1]
        return children[0] if childA < childB else children[1]
```

Next, we want to **transform a non-ordered array into a heap**. **** Because bubbleDown has already been implemented, we can reuse it here.

```
def transformList(self):
    i = (self.currentSize - 1) // 2
    while (i >= 0):
        self.bubbleDown(i)
        i -= 1
```

The last thing we can add is to actually call our `transformList` method in our constructor so that we can immediately initiate a valid heap when we create a new heap object using an array:

```
class BinHeap:
    def __init__(self, array):
        self.heapList = array
        self.currentSize = len(array)
        self.transformList()
```

And there we have our full heap class.

## heapq in Python <a href="#4b61" id="4b61"></a>

Now that we know how to build a min heap, we’re qualified to use a handy [built-in min heap ](https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)in Python!

`heapq` is a module in Python that you can use to build a min heap quickly. Whenever elements are pushed or popped, **heap structure is maintained**.

If you want to implement a max heap with heapq, enter your values as negative values and when you want to pop values from your max heap, change the sign of the popped value back to positive.

Let’s see this in action.

### Min Heap Using heapq <a href="#fa33" id="fa33"></a>

```
import heapqarray = [1, 4, 6, 2, 5, 3, 9, 8, 7]
minHeap = []
for num in array:
    heapq.heappush(minHeap, num)
print("minHeap:",minHeap)==> minHeap: [1, 2, 3, 4, 5, 6, 9, 8, 7]
```

If you are struggling to visualize the heap, have a look at the diagram below:![](https://miro.medium.com/max/60/1\*TN9HYUsEHorz66EXWqqyQw.jpeg?q=20)![](https://miro.medium.com/max/541/1\*TN9HYUsEHorz66EXWqqyQw.jpeg)

### Max Heap Using heapq <a href="#a225" id="a225"></a>

```
import heapqarray = [1, 4, 6, 2, 5, 3, 9, 8, 7]
maxHeap = []
for num in array:
    heapq.heappush(maxHeap, -num)
print("maxHeap:", maxHeap)==> maxHeap: [-9, -8, -6, -7, -2, -3, -4, -1, -5]
```

![](https://miro.medium.com/max/60/1\*zYJgdBe1GxnWmF8EanmfCg.jpeg?q=20)![](https://miro.medium.com/max/541/1\*zYJgdBe1GxnWmF8EanmfCg.jpeg)

If you ignore the negative sign, you have a max Heap :).

To see all of the methods you can use with `heapq`, check out the [Python docs on heapq](https://docs.python.org/3.7/library/heapq.html).

Thanks for reading!

### Resources <a href="#ceac" id="ceac"></a>

[Heap Data Structure - GeeksforGeeksRecent articles on Heap ! A Heap is a special Tree-based data structure in which the tree is a complete binary tree…www.geeksforgeeks.org](https://www.geeksforgeeks.org/heap-data-structure/)[Heap Data Structure | Interview CakeA binary heap is a binary tree where every node is smaller than all its children. This puts the very smallest node at…www.interviewcake.com](https://www.interviewcake.com/concept/java/heap)[7.10. Binary Heap Implementation - Problem Solving with Algorithms and Data StructuresIn order to make our heap work efficiently, we will take advantage of the logarithmic nature of the binary tree to…runestone.academy](https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html)



Reference &#x20;

* [Simplest Way to achieve Heapify](https://levelup.gitconnected.com/a-better-way-to-understand-heap-data-structure-3c60b74295e8)
* [Heap Data Structure](https://shreeji.medium.com/heaps-data-structure-871e88153204)

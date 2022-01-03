# Apple

## Apple’s interview questions database <a href="#816e" id="816e"></a>

[![Anjali Viramgama](https://miro.medium.com/fit/c/96/96/1\*VqaGfT-BML1xC2qv0hgnJQ.jpeg)](https://anjaliviramgama.medium.com/?source=post\_page-----784d72f8d061--------------------------------)[Anjali Viramgama](https://anjaliviramgama.medium.com/?source=post\_page-----784d72f8d061--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F\_%2Fsubscribe%2Fuser%2Fb9e3e12f9963\&operation=register\&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fapples-interview-questions-database-784d72f8d061\&user=Anjali%20Viramgama\&userId=b9e3e12f9963\&source=post\_page-b9e3e12f9963----784d72f8d061---------------------follow\_byline-----------)[Jun 2](https://levelup.gitconnected.com/apples-interview-questions-database-784d72f8d061?source=post\_page-----784d72f8d061--------------------------------) · 4 min read

Here is a list of 42 questions asked by Apple in their interviews with a link to their solution. I got the questions from Glassdoor. I prepared this database before my own interview and since I found them useful, I thought I’d publish it as a quick resource. Try to solve or at least skim through all of these starting 2 weeks before your scheduled interview, and you’ll be good to go. For more information about the internship interview, read more [**here.**](https://levelup.gitconnected.com/apples-software-engineering-intern-interview-5b4d250d06a7)![](https://miro.medium.com/max/12000/0\*fKqqK1dcVKrQ4PCo)Photo by [Medhat Dawoud](https://unsplash.com/@medhatdawoud) on [Unsplash](https://unsplash.com)

## Non- DSA: <a href="#a511" id="a511"></a>

1\. Advantages of using MacOS

Better multitasking features

Better optimization of hardware and software

Simple and clean interface

Less Malware

More info [**here**](https://www.itrelease.com/2019/10/what-are-advantages-and-disadvantages-of-macos/).

2\. Unix vs Linux — Read [**here**](https://www.softwaretestinghelp.com/unix-vs-linux/#:\~:text=Linux%20refers%20to%20the%20kernel,family%20of%20derived%20operating%20systems.)

3\. What do you think of Siri? What improvement can you suggest for Siri?

4\. What’s your career plan in the next coming 5 years?

5\. What happens when you click on a URL? **** [**Solution**](https://www.freecodecamp.org/news/what-happens-when-you-hit-url-in-your-browser/)

## DSA <a href="#f1ce" id="f1ce"></a>

## Easy: <a href="#0436" id="0436"></a>

1. Given an array of integers and a value, determine if there are any three integers in the array whose sum equals the given value.

After asking about edge case handling, the solution should be similar to [**ThreeSum**](https://leetcode.com/problems/3sum/)**.**

2\. Given a sorted array, return the sorted array of their squares — Read discuss section of leetcode [**here**](https://leetcode.com/problems/squares-of-a-sorted-array/discuss/?currentPage=1\&orderBy=most\_votes\&query=)**.**

3\. Determine whether a string is a palindrome. [**Solution**](https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/)

4\. Implement a Queue With Two Stacks. [**Solution**](https://www.geeksforgeeks.org/queue-using-stacks/)

5\. Revert an integer bitwise. [**Solution1**](https://www.geeksforgeeks.org/reverse-actual-bits-given-number/) **or** [**Solution2**](https://leetcode.com/problems/reverse-bits/solution/)

6\. Design a HashSet. [**Solution**](https://leetcode.com/problems/design-hashset/discuss/?currentPage=1\&orderBy=most\_votes\&query=)

7\. Design HashMap. [**Solution**](https://leetcode.com/problems/design-hashmap/)

8\. Given a list of strings, provide the number of strings that are unique within the list.

Solution- Throw everything in a hashset and then build a list out of it.

```
ArrayList<String> answer = new ArrayList<>(new HashSet<String>(givenList));
```

9\. Find depth of a binary tree. [**Solution**](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/)

10\. Write a function that counts the number of times a given int occurs in a Linked List. [**Solution**](https://www.geeksforgeeks.org/write-a-function-that-counts-the-number-of-times-a-given-int-occurs-in-a-linked-list/)

## Medium <a href="#5421" id="5421"></a>

1. Implement an iterator that supports the peek operation on a list in addition to the hasNext and the next operation: [**Solution**](https://leetcode.com/problems/peeking-iterator/discuss/?currentPage=1\&orderBy=most\_votes\&query=)

2\. Copy a graph. [**Solution**](https://leetcode.com/problems/clone-graph/discuss/?currentPage=1\&orderBy=most\_votes\&query=)

3\. Reverse a linked list. [**Solution**](https://www.geeksforgeeks.org/reverse-a-linked-list/)

4\. Word search, Given a grid of characters board and a string word, returns true if the word exists in the grid. [**Solution**](https://leetcode.com/problems/word-search/discuss/?currentPage=1\&orderBy=most\_votes\&query=)

5\. Given a function magicNumber() that returns a random integer 1 or 0, write a new function that will generate a random number that uses this magicNumber() function.

Solution — Ask for the range of the number (example up to 100) and then generate a bit for that many digits using magicNumber() function.

6\. Perform matrix multiplication given 2 matrices. [**Solution**](https://www.geeksforgeeks.org/c-program-multiply-two-matrices/)

7\. Design a data structure that can be used for [**Least Recently Used (LRU) cache**](https://en.wikipedia.org/wiki/Cache\_replacement\_policies#LRU). [**Solution**](https://leetcode.com/problems/lru-cache/discuss/?currentPage=1\&orderBy=most\_votes\&query=)

8\. Check completeness of a binary tree. [**Solution**](https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-complete-tree-or-not/)

9\. Find Least common ancestor in a binary tree. [**Solution**](https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/)

10\. Integrate interval ranges. [**Solution**](https://leetcode.com/problems/merge-intervals/solution/)

11\. Implement Merge Sort. [**Solution**](https://www.geeksforgeeks.org/merge-sort/)

12\. Exchange the odd and even bits of an integer. [**Solution**](https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/)

13\. Maximum subarray sum. [**Solution**](https://www.geeksforgeeks.org/design-data-structures-algorithms-memory-file-system/)

14\. Topological sorting. [**Solution**](https://www.geeksforgeeks.org/topological-sorting/)

15\. Merge overlapping intervals. [**Solution**](http://geeksforgeeks.org/merging-intervals/)

16\. Count number of ways to reach nth stair in a staircase. **** [**Solution**](https://www.geeksforgeeks.org/count-ways-reach-nth-stair/)

## Hard <a href="#47a2" id="47a2"></a>

1. Given a board of characters and a list of strings words, return all the words on the board. [**Solution**](https://leetcode.com/problems/word-search-ii/discuss/?currentPage=1\&orderBy=most\_votes\&query=)
2. Given three strings and return true if the third string is the interleaving of the other two. [**Solution**](https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/)

3\. Design a data structure for a [**Least Frequently Used (LFU)**](https://en.wikipedia.org/wiki/Least\_frequently\_used) **** cache. [**Solution**](https://www.geeksforgeeks.org/least-frequently-used-lfu-cache-implementation/)

4\. Select a random node from LinkedList. [**Solution**](https://www.geeksforgeeks.org/select-a-random-node-from-a-singly-linked-list/)

5\. Implement a quadtree. [**Solution**](https://www.geeksforgeeks.org/quad-tree/)

6\. Find median from a stream. [**Solution**](https://leetcode.com/problems/find-median-from-data-stream/)

7\. Write a code to add two linked lists that contained a digit each to represent huge numbers. [**Solution**](https://www.geeksforgeeks.org/sum-of-two-linked-lists/)

8\. Design file management system. [**Solution**](https://www.geeksforgeeks.org/design-data-structures-algorithms-memory-file-system/)

9\. Write a program that uses two threads to print the numbers from 1 to n. [**Solution**](https://www.geeksforgeeks.org/print-even-and-odd-numbers-in-increasing-order-using-two-threads-in-java/)

10\. Print the different ways to open and close brackets with x opens. For 3, this would be : . [**Solution**.](https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/)

11\. Sort an array of 10M unique ints faster than merge/quick sort. Solution: Since we know the range, use [**radix sort.**](https://www.geeksforgeeks.org/radix-sort/)

That’s all, I’ll add more as I find them. I hope this was helpful. Thanks for reading, feel free to dm me if you have any questions!

Anjali Viramgama

[**LinkedIn**](http://www.linkedin.com/in/anjali-viramgama-085285166) **|** [**Instagram**](https://www.instagram.com/anjali.gama/)

Articles that might interest you:

[**Apple’s Software Engineering intern interview**](https://levelup.gitconnected.com/apples-software-engineering-intern-interview-5b4d250d06a7)

[**Facebook’s Software Developer Intern Interview**](https://levelup.gitconnected.com/nailing-the-facebook-software-developer-intern-interview-5a6dcea630af)

[**Amazon’s Internship and full-time interview guide**](https://towardsdatascience.com/amazons-internship-and-full-time-interview-guide-af3c20455e15)

[**Bloomberg’s internship and full-time guide**](https://levelup.gitconnected.com/bloombergs-internship-and-full-time-guide-cde112c9c22d)

[**The One Year Plan for Cracking Coding Interviews**](https://towardsdatascience.com/the-one-year-plan-for-competitive-coding-6af53f2f719c)

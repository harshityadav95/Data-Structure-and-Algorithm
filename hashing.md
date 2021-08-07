# Hashing

## The Hash Table: Your Friendly Neighborhood Data Structure <a id="e8cf"></a>

[![Rick Moore](https://miro.medium.com/fit/c/43/43/1*ZCy3bBAG7FDeDGWctfOd2Q.jpeg)](https://dirklo.medium.com/?source=post_page-----68186fbf5a08--------------------------------)[Rick Moore](https://dirklo.medium.com/?source=post_page-----68186fbf5a08--------------------------------)Follow[Jul 30](https://medium.com/nerd-for-tech/the-hash-table-your-friendly-neighborhood-data-structure-68186fbf5a08?source=post_page-----68186fbf5a08--------------------------------) · 7 min read![](https://miro.medium.com/max/630/0*matWZ733bc33_cjz)Photo by [Road Trip with Raj](https://unsplash.com/@roadtripwithraj?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Considering the common data structures employed by all coding languages, few hold as much importance under-the-hood as the hash table. Though relatively simple in concept, many very smart people over many years have devised implementations of the concept to make faster, leaner, and more accessible data storage strategies.

In this article, I’ll go over the basics of what a hash table is, how it works, and some clever ways to implement it into your algorithm writing workflow.

### Basic Structure and Operations <a id="2824"></a>

A hash table is built on the concept of a **“Dictionary”**, in that we are storing and maintaining a set of data, each with a **key** that we can reference to perform one of three primary functions:

* Insert \(an item\)
* Delete \(an item\)
* Search \(for a key\) - Returns the item with corresponding key or reports that it doesn’t exist

![](https://miro.medium.com/max/27/1*JULnUFpUCHIOy7A1APjRzA.png?q=20)![](https://miro.medium.com/max/630/1*JULnUFpUCHIOy7A1APjRzA.png)Storing Example

When inserting items into a hash table, a hashing function is applied to the key of the item, and an index is generated corresponding to the hash table where the item will eventually be stored.

This is most useful when our items are set up as `key=>value` pairs where the key can be transformed into an index number.

A common implementation of a basic hashing function will derive an integer value from the key of the item, and use a modulo \(%\) operator with the length of the hash table to determine the index where it should be stored. For example, if the keys of our items were names of people, I could convert the letters in the name to an integer by adding up their ASCII code values, then using the modulo operator with 5 \(the length of our target hash table\) to derive an index to store that item.

* Dan - D=068, a=097, n=110. \(68 + 97 + 110\) % 5 = **index 0**
* Tim - T=084, i=105, m=109. \(84 + 105+ 109\) % 5 = **index 3**
* Jan - J=074, a=097, n=110. \(74 + 97 + 110\) % 5 = **index 1**

Perhaps Dan has a date of birth and a height in an object like this:

```text
{
    Dan: {
        dateOfBirth: 1986-5-14, 
        height: 187
    }
}
```

Our key for deriving the target index in the hash table will remain as the string “Dan”, and the value in that pair is an object containing the details for Dan. This data could also be an instance of a class, if we want to take an OOP approach.

After storing our objects in our hash table, we have something that looks like this:![](https://miro.medium.com/max/27/1*kF9gax8owYgBwVbLRqkoJA.png?q=20)![](https://miro.medium.com/max/580/1*kF9gax8owYgBwVbLRqkoJA.png)Stored Example 1

Keep in mind, these pieces of data are not sorted by any part of their content, in fact, the hash table by design works the best when the derived index values are “uniformly random”. Storing is optimized when each piece of data has an equal probability of being placed in any bucket of the hash table.

This brings us to the next step, the quick retrieval of data. Imagine needing to find a particular piece of data by its key in a traditional array.

`array.find("Item 6")`![](https://miro.medium.com/max/27/1*pm_sIvO5ndNcncepht94eA.png?q=20)![](https://miro.medium.com/max/630/1*pm_sIvO5ndNcncepht94eA.png)Array Traversal

We would traverse along the array, checking each and every item, until we match the key we are searching for. This is incredibly inefficient and would run in worst case O\(n\) time, where n is the number of items in the array.

Now let’s imagine finding that same item, but the item can tell us its own index in the array, so we know where to look.

```text
index = item6.indexarray[index]
```

![](https://miro.medium.com/max/27/1*EK34mKntQ0qFHCqtOh2GQQ.png?q=20)![](https://miro.medium.com/max/630/1*EK34mKntQ0qFHCqtOh2GQQ.png)Retrieval by Index

This is much more efficient, but we generally wouldn’t hard-code a location index within an object. This is where the hashing function comes in. Using the key, we can derive the index of where we need to look for the data we need by passing the key into our hashing function. In an ideal world, this would run in constant time, O\(1\), meaning it would always return the information in the same amount of time regardless of the size of the hash table.

This is great! But it also raises some possible issues that would need to be optimized to get us closer to that perfect algorithm.

### Handling Collisions <a id="3355"></a>

The most prevalent issue with this idea of deriving an index from some function, is the possibility that two different keys when passed into the function, would return the same index. Let’s go back to our first example.

We have the keys of `“Dan”`, `“Tim”`, and `“Jan”`. With our hashing function adding their ASCII codes together and using the modulo function to fit them into an index between 0 and 5, they each get their own index. Great! Now, what if we wanted to add Bob to the hash table?

* `Dan =>` **`index 0`**
* `Tim =>` **`index 3`**
* `Jan =>` **`index 1`**
* Bob - B=066, o=111, b=98. \(66 + 111+ 98\) % 5 = **index 0**

Uh-oh, both Bob and Dan return `0` from our hashing function. What do we do now? There are two popular solutions:

* **Linear Probing,** sometimes called Open Addressing
* **Chaining**, or Closed Addressing

**Linear Probing**

Open addressing essentially means that there is no guarantee that the item stored will be at the exact index returned from the hashing algorithm, so all indexes are “open” possibilities when storing or retrieving from the hash table. In the storing phase, if the target index is already occupied, the algorithm will check for the next available index in the hash table, and store the data there.![](https://miro.medium.com/max/27/1*1BPUSpe39TWUGLBmqLg_Aw.png?q=20)![](https://miro.medium.com/max/630/1*1BPUSpe39TWUGLBmqLg_Aw.png)Linear Probing Storing

* **Attempt 1:** We check the target index 0, and see that it is already occupied by Dan.
* **Attempt 2:** We move on to check the next index, 1. This one is also occupied by Jan,
* **Attempt 3:** Finally we move on to check index 2, and we have an available slot to place Bob.

We would need to go through this process of starting at the target index and iterating through the following slots on both storing and retrieving data.

Open addressing may be susceptible to “Primary Clustering”, where many keys output the same address, and get spread out over a wider index range. You can see in this example, looking up the newly added Bob object would require checking two other slots before finding the correct data. We might be able to optimize this through a few different strategies:

* **Plus 3 rehash -** We may decide to check every third slot for the next available index.
* **Quadratic Probing -** We could square the distance to look ahead each time we encounter an occupied slot. \(_failed attempts_\)².
* **Double Hashing -** In double hashing, a second hashing algorithm is applied to the key when a collision occurs.

### Chaining <a id="a968"></a>

The other popular method for collision avoidance is chaining, or closed addressing. With this strategy, we can employ a linked list stored at the index number in question.![](https://miro.medium.com/max/27/1*Pzz48MFS73KVJgYx3yg0JQ.png?q=20)![](https://miro.medium.com/max/549/1*Pzz48MFS73KVJgYx3yg0JQ.png)Chaining Storing

When storing, we check the target index 0, sees that it’s occupied, but add our entry to the end of a linked list. The Dan entry now points to the bob entry, and during lookup, we would only need to navigate to index 0 and check one other entry before arriving at the data we need.

Again, depending on the needs of the particular situation, you may choose one implementation over another.

### How Do We Write the “Perfect” Hashing Function? <a id="523d"></a>

Theoretically, if we knew exactly how many pieces of data we needed to store, it is not outside the realm of possibility that we could write an algorithm that perfectly populates a hash table, but since we don’t live in a perfect world, it’s better to follow some guidelines to try and meet these primary objectives.

* Minimize Collisions - The more random you can make you hashing function, the more likely you will have minimum collisions in its implementation.
* Uniform Distribution - The closer we can get to one piece of data per index in our hash table, the better.
* Easy to Calculate - The hashing function will be running a lot, so the easier and faster the calculation, the better.
* Resolves any Collisions - Any hash table needs a clear strategy to handle collisions that have a 0% chance of breaking down.

## Conclusion <a id="c17c"></a>

Hashing and hash tables are used literally everywhere, in nearly every system we work and interact with on a daily basis. They give us the power to index large amounts of data, and calculate the memory location of the data using the data itself. Taking the time to optimize the collision handling of the algorithm can raise the efficiency of the data structure even further.



Reference :

* [ Introduction to Locality-Sensitive Hashing](http://tylerneylon.com/a/lsh1/)


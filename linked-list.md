# Linked List

 

![](.gitbook/assets/image%20%2811%29.png)

* Contains Duplicate III \([Source](https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3446/discuss/824603/Python-SortedList-O%28n-log-k%29-solution-explained.)\)

```text
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = bisect_left(SList, nums[i] - t)
            pos2 = bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
        
        return False
```


# Searching

Searching Algorithms









### Problems to Solve

* \[Binary Search\] [First Bad Version](https://leetcode.com/problems/first-bad-version)

{% tabs %}
{% tab title="C++ " %}
```text
class Solution {
public:
    int firstBadVersion(int n) {
          int left=1;
  int right=n;
    while (left<right) {
        int mid=left+(right-left)/2;
        if (isBadVersion(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
  return left;        
    }
};
```
{% endtab %}

{% tab title="Python" %}

{% endtab %}

{% tab title="Java" %}
```text
public int firstBadVersion(int n) {
    for (int i = 1; i < n; i++) {
        if (isBadVersion(i)) {
            return i;
        }
    }
    return n;
}
```
{% endtab %}
{% endtabs %}






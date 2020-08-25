# Searching

Searching Algorithms









### Problems to Solve

* \[Binary Search\] [First Bad Version ](https://leetcode.com/problems/first-bad-version)

{% tabs %}
{% tab title="C++ " %}
```text
#include<iostream>
using namespace std;
int main()
{
  //arr size
  int size;
  int bad;
  cin>>size;
  cin>>bad;
  int arr[20];
  for(int i=0;i<size;i++)
  {
    arr[i]=i+1;
  }
  //displaying the array
  for(int i=0;i<size;i++)
  {
    cout<<arr[i]<<" ";
  }
  
  return 1;

}
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






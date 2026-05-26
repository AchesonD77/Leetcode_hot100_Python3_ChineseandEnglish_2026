# 49. Group Anagrams


## Core Problem

Given an array of strings, group together:

```text
words with the same letters but different order
```

into the same group.

---

# What is an Anagram?

For example:

```python
"eat"
"tea"
"ate"
```

They contain:

```text
the same letters
```

but in different order.

---

# Key Idea

## Use Sorted String as Hashmap Key

Because:

```python
"eat" -> "aet"
"tea" -> "aet"
"ate" -> "aet"
```

After sorting, they become identical.

So:

```text
sorted string
```

can be used as:

```text
hashmap key
```

---

# Final Python Code

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        hashmap = defaultdict(list)

        for s in strs:

            key = "".join(sorted(s))

            hashmap[key].append(s)

        return list(hashmap.values())
```

---

# Code Explanation

## 1. Create Hashmap

```python
hashmap = defaultdict(list)
```

Purpose:

```text
automatically create empty lists
```

Example:

```python
hashmap["aet"] = []
```

---

## 2. Traverse Strings

```python
for s in strs:
```

Example:

```python
s = "eat"
```

---

## 3. Sort String (Core Step)

```python
key = "".join(sorted(s))
```

Example:

```python
sorted("eat")
```

Result:

```python
['a', 'e', 't']
```

Then:

```python
"".join(...)
```

becomes:

```python
"aet"
```

---

## 4. Add into Group

```python
hashmap[key].append(s)
```

Example:

```python
hashmap["aet"] = ["eat", "tea", "ate"]
```

---

## 5. Return Result

```python
return list(hashmap.values())
```
### list()
```python
list()
```

is a built-in Python function used to convert iterable objects into a list.


Output:

```python
[
    ["eat","tea","ate"],
    ["tan","nat"],
    ["bat"]
]
```
### List of Lists

```python
[[], [], []]
```

is called a:

```text
2D List / List of Lists
```

not a dictionary.

---

# Time Complexity

$$
O(n \cdot k \log k)
$$

Where:

```text
n = number of strings
k = average string length
```

Because every string needs sorting.

---

# Space Complexity

$$
O(nk)
$$

Because the hashmap stores all strings.

---

# Key Takeaway

## Core Pattern

```text
Hash Map + Sorting
```

Main idea:

```text
Convert items with the same feature
into the same key
```

---

# Important Python Syntax

## Sorting

```python
sorted(s)
```

---

## String Join

```python
"".join(...)
```

---

## defaultdict

```python
from collections import defaultdict
```

---

# What Interviewers Really Test

Not strings themselves.

But:

```text
How to find the same feature
```

And:

```text
How to classify using hashmap
```
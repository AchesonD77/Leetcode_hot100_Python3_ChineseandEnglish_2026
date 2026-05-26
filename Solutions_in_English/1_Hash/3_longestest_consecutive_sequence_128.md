# 128. Longest Consecutive Sequence

## Core Problem

Given an unsorted array:

```python
nums
```

find:

```text
the length of the longest consecutive sequence
```

Important:

```text
consecutive numbers
NOT consecutive indices
```

Example:

```python
[100,4,200,1,3,2]
```

The longest consecutive sequence is:

```python
[1,2,3,4]
```

So the answer is:

```python
4
```

---

# Key Idea

## Use set for fast lookup

Because:

```text
set lookup is extremely fast
```

Time complexity:

$$
O(1)
$$

---

# Core Insight

For a number:

```python
num
```

if:

```python
num - 1 does not exist
```

then:

```text
it is the start of a sequence
```

Then keep checking:

```python
num + 1
num + 2
num + 3
```

to extend the sequence.

---

# Why?

For example:

```python
[1,2,3,4]
```

Only:

```python
1
```

satisfies:

```python
0 does not exist
```

So:

```text
1 is the starting point
```

This avoids repeated traversal.

---

# Final Python Code

```python
class Solution:
    def longestConsecutive(self, nums):

        num_set = set(nums)

        longest = 0

        for num in num_set:

            if num - 1 not in num_set:

                current_num = num
                current_length = 1

                while current_num + 1 in num_set:

                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest
```

---

# Code Explanation

## 1. Convert to set

```python
num_set = set(nums)
```

Purpose:

```text
remove duplicates
+
fast lookup
```

---

## 2. longest

```python
longest = 0
```

Stores:

```text
maximum sequence length
```

---

## 3. Traverse numbers

```python
for num in num_set:
```

Loop through every number.

---

## 4. Check starting point (Core)

```python
if num - 1 not in num_set:
```

Meaning:

```text
previous number does not exist
```

So:

```text
current number is sequence start
```

---

## 5. Expand sequence

```python
while current_num + 1 in num_set:
```

Keep extending:

```python
2
3
4
5
```

until broken.

---

## 6. Update answer

```python
longest = max(longest, current_length)
```

Update maximum length.

---

## 7. return longest

return longest must be outside the for loop because the algorithm needs to check all numbers first before returning the global longest sequence length.

# Time Complexity

$$
O(n)
$$

Because:

```text
each number is visited at most once
```

---

# Space Complexity

$$
O(n)
$$

Because we use:

```python
set
```

to store data.

---

# Key Takeaway

## Core Pattern

```text
set + sequence detection
```

Main idea:

```text
avoid repeated traversal
```

by only starting from:

```text
sequence starting points
```

---

# Important Python Syntax

---

# 1. set()

```python
set(nums)
```

is a built-in Python function used to create a set or convert iterable objects into a set (with automatic duplicate removal).

Purpose:

```text
remove duplicates
+
fast lookup
```

---

# 2. in

```python
if x in num_set
```

Purpose:

```text
check existence
```

---

# 3. not in

```python
if x not in num_set
```

Purpose:

```text
check non-existence
```

---

# 4. while

```python
while condition:
```

Purpose:

```text
repeat while condition is true
```

---

# 5. max()

```python
max(a, b)
```

Purpose:

```text
return larger value
```

Used here to:

```text
update longest length
```

---

# What Interviewers Really Test

Not consecutive sequences.

But:

```text
How to use set for O(1) lookup
```

And:

```text
How to avoid repeated traversal
```

This is a classic:

```text
hash optimization problem
```
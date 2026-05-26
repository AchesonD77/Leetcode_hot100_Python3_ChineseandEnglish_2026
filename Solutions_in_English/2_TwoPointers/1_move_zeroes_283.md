# LeetCode 283. Move Zeroes (Two Pointers)

# English Version

![alt text](<../../Snap_for_Questions/2_TwoPointers_双指针/english_verison/截屏2026-05-26 17.02.55.png>)

## 1. Problem Core

Move all `0`s in the array to the end.

Requirements:

- Keep the relative order of non-zero elements
- Modify the array in-place
- Do not create a new array

---

## 2. Core Idea (Two Pointers)

Use two pointers:

- `fast`
  - Traverses the array
- `slow`
  - Points to the next position for placing a non-zero element

Rules:

- If the current element is non-zero:
  - Swap with `slow`
  - `slow += 1`
- If the current element is `0`:
  - Skip it

---

## 3. Python Code (Must Memorize)

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
```

---

## 4. Code Explanation

```python
class Solution:
```

Defines a class.

This is the standard LeetCode format.

---

```python
def moveZeroes(self, nums: list[int]) -> None:
```

Defines a function:

- `nums`
  - Input array
- `list[int]`
  - Integer array
- `-> None`
  - No return value
  - Modify the original array directly

---

```python
slow = 0
```

Defines the slow pointer.

Purpose:

- Points to the next position where a non-zero element should be placed

Initially:

```python
slow = 0
```

Meaning:

- Start placing non-zero elements from index `0`

---

```python
for fast in range(len(nums)):
```

The fast pointer traverses the array.

Example:

```python
nums = [0,1,0,3,12]
```

Then:

```python
fast = 0,1,2,3,4
```

---

```python
if nums[fast] != 0:
```

Checks whether the current element is non-zero.

Only non-zero elements need to be moved.

---

```python
nums[slow], nums[fast] = nums[fast], nums[slow]
```

Swaps elements:

- Move the non-zero element forward
- Move `0` backward

This is a high-frequency Python swap syntax.

---

```python
slow += 1
```

The current non-zero element has been placed correctly.

So:

- Move `slow` one step forward
- Prepare for the next non-zero element

---

## 5. Execution Process (Most Important)

Input:

```python
nums = [0,1,0,3,12]
```

Process:

| fast | nums[fast] | Action | slow | Array |
|---|---|---|---|---|
| 0 | 0 | Skip | 0 | [0,1,0,3,12] |
| 1 | 1 | Swap | 1 | [1,0,0,3,12] |
| 2 | 0 | Skip | 1 | [1,0,0,3,12] |
| 3 | 3 | Swap | 2 | [1,3,0,0,12] |
| 4 | 12 | Swap | 3 | [1,3,12,0,0] |

Final result:

```python
[1,3,12,0,0]
```

---

## 6. Complexity

### Time Complexity

```text
O(n)
```

Only one traversal of the array.

---

### Space Complexity

```text
O(1)
```

No extra array is used.

---

## 7. Python Syntax You Must Master

---

### 1. range(len(nums))

```python
for i in range(len(nums)):
```

Purpose:

- Traverse array indices
- `i` goes from `0` to `len(nums)-1`

---

### 2. Array Access

```python
nums[i]
```

Meaning:

- Access the `i-th` element

---

### 3. Conditional Check

```python
if nums[i] != 0:
```

Meaning:

- The current element is not `0`

---

### 4. Python Swap Syntax (Very Important)

```python
nums[a], nums[b] = nums[b], nums[a]
```

Purpose:

- Swap two variables directly
- No temporary variable needed

Example:

```python
x, y = 1, 2

x, y = y, x
```

Result:

```python
x = 2
y = 1
```

---

### 5. += Increment

```python
slow += 1
```

Equivalent to:

```python
slow = slow + 1
```

---

## 8. The Real Algorithm Idea

# Two Pointers

Core idea:

```text
fast finds elements
slow places elements
```

This is one of the most important basic algorithms in LeetCode.

It is widely used in:

- Remove Element
- Remove Duplicates
- Fast & Slow Pointers
- Sliding Window
- In-place Array Modification

---

## 9. One-Sentence Memory Trick

```text
fast traverses the array
slow places non-zero elements
swap whenever a non-zero element is found
```

---

## One-Sentence Understanding of Two Pointers

```text
The fast pointer searches forward (from index 0 to the end) for non-zero elements, while the slow pointer places non-zero elements at the front of the array one by one.
```

---

## Easy Example

Example:

```python
nums = [0,5,0,2,8]
```

Start:

```python
slow = 0
```

---

### fast = 0

Sees:

```python
0
```

It is zero.

No swap.

Array:

```python
[0,5,0,2,8]
```

---

### fast = 1

Sees:

```python
5
```

Not zero.

Swap:

```python
nums[slow], nums[fast] = nums[fast], nums[slow]
```

That is:

```python
nums[0], nums[1]
```

Array becomes:

```python
[5,0,0,2,8]
```

Then:

```python
slow += 1
```

Now:

```python
slow = 1
```

---

### fast = 3

Sees:

```python
2
```

Not zero.

Swap:

```python
nums[1], nums[3]
```

Array becomes:

```python
[5,2,0,0,8]
```

```python
slow += 1
```

Now:

```python
slow -> nums[2]
```

---

### fast = 4

Sees:

```python
8
```

Not zero.

Swap:

```python
nums[2], nums[4]
```

Array becomes:

```python
[5,2,8,0,0]
```

---

## Final Result

```python
[5,2,8,0,0]
```

---

## Core Essence

```text
fast searches for non-zero elements,
while slow maintains the non-zero area at the front.
```
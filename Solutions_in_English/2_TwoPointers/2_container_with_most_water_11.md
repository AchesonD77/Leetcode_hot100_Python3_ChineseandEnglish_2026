# LeetCode 11. Container With Most Water

![alt text](<../../Snap_for_Questions/2_TwoPointers_双指针/english_verison/截屏2026-05-26 17.33.12.png>)

# English Version

## 1. Problem Core

Given an array:

```python
height = [1,8,6,2,5,4,8,3,7]
```

Each number represents the height of a vertical line.

Choose two lines:

- Width = distance between the two lines
- Height = the shorter line

Find:

```text
the maximum water container area
```

---

## 2. Area Formula (Must Understand)

Container area:

```text
Area = Width × Height
```

Where:

```text
Width = right - left
Height = min(height[left], height[right])
```

So:

$$
Area = Width \times Height
$$

---

## 3. Core Idea (Two Pointers)

Use two pointers:

- `left`
  - Starts from the left side
- `right`
  - Starts from the right side

For each step:

1. Calculate the current area
2. Update the maximum area
3. Move the shorter line

---

## 4. Why Move the Shorter Line (Most Important)

Because:

```text
the container height is determined by the shorter line.
```

```text
Area = Width × Shorter Height
```

The current height is determined by:

```text
min(left_height, right_height)
```

If we move the taller line:

```text
height will not increase
while width becomes smaller
```

The area cannot become larger.

So:

```text
we must move the shorter line
```

This is the core idea of this problem.

---

## 5. Python Code (Must Memorize)

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            width = right - left

            current_height = min(height[left], height[right])

            area = width * current_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

## 6. Code Explanation

---

```python
left = 0
right = len(height) - 1
```

Defines two pointers:

- `left` starts from the far left
- `right` starts from the far right

Because:

```text
the largest width may produce the maximum area
```

---

```python
max_area = 0
```

Stores:

```text
the current maximum area
```

---

## Purpose of while Loop (Most Important)

The `while` loop continuously moves the two pointers toward the center and keeps calculating the maximum area.

```python
while left < right:
```

As long as the two pointers do not meet:

continue calculating the area.

---

```python
width = right - left
```

Calculates the width.

---

```python
current_height = min(height[left], height[right])
```

Calculates the container height.

## Error Record (During Practice)

```text
Incorrect:
height = min()

Do not overwrite the original list variable `height` with an integer, otherwise you can no longer use [] indexing on it.
```

Important:

```text
The height is determined by the shorter line.
```

---

```python
area = width * current_height
```

Calculates the current area.

Formula:

$$
Area = Width \times Height
$$

---

```python
max_area = max(max_area, area)
```

Updates the maximum area.

---

```python
if height[left] < height[right]:
    left += 1
```

If the left side is shorter:

move the left pointer.

Because:

```text
only moving the shorter line
can possibly increase the height
```

---

```python
else:
    right -= 1
```

If the right side is shorter:

move the right pointer.

---

```python
return max_area
```

Returns the final answer.

---

## 7. Execution Process (Important)

Input:

```python
height = [1,8,6,2,5,4,8,3,7]
```

---

### First Step

```text
left = 0
right = 8
```

Height:

```text
min(1,7) = 1
```

Width:

```text
8
```

Area:

$$
Area = Width \times Height
$$

Move the shorter line:

```text
left += 1
```

---

### Second Step

```text
left = 1
right = 8
```

Height:

```text
min(8,7) = 7
```

Width:

```text
7
```

Area:

$$
Area = Width \times Height
$$

Update maximum value:

```text
max_area = 49
```

---

No larger area will appear afterward.

Final answer:

```python
49
```

---

## 8. Complexity

### Time Complexity

```text
O(n)
```

Only traverses the array once.

---

### Space Complexity

```text
O(1)
```

Uses only constant extra variables.

---

## 9. Python Syntax You Must Master

---

### 1. while Loop

```python
while left < right:
```

Meaning:

```text
As long as the two pointers do not meet,
continue looping.
```

---

### 2. min()

```python
min(a, b)
```

Returns the smaller value.

Example:

```python
min(3, 7)
```

Result:

```python
3
```

---

### 3. max()

```python
max(a, b)
```

Returns the larger value.

Example:

```python
max(10, 20)
```

Result:

```python
20
```

---

### 4. += and -=

```python
left += 1
right -= 1
```

Equivalent to:

```python
left = left + 1
right = right - 1
```

---

### 5. Array Access

```python
height[i]
```

Gets the `i-th` element of the array.

---

## 10. The Real Algorithm Idea

# Two Pointers

Core idea:

```text
Move inward from both sides,
always move the shorter line.
```

This is one of the most classic Two Pointer problems in LeetCode.

Many future problems use similar ideas:

- 3Sum
- Trapping Rain Water
- Remove Element
- Sorted Array Problems
- Sliding Window

---

## 11. One-Sentence Memory Trick

```text
The area is determined by the shorter line,
so always move the shorter line.
```
# 1. Two Sum（两数之和）

## 题目核心 | Core Idea

给定一个数组 `nums` 和目标值 `target`，找到两个数字之和等于 `target` 的下标。

Given an array `nums` and a target value `target`, find the indices of the two numbers whose sum equals `target`.

---

# 算法思想 | Algorithm Idea

## 哈希表优化（空间换时间）
## Hash Map Optimization (Trade Space for Time)

遍历数组时：

When traversing the array:

```text
当前数字 current number = num
需要的数字 needed number = target - num
```

如果需要的数字已经存在于哈希表中：

If the needed number already exists in the hashmap:

```text
直接返回答案
Return the result immediately
```

否则：

Otherwise:

```text
把当前数字存入哈希表
Store the current number into the hashmap
```

---

# Python 最终代码 | Final Python Code

```python
class Solution:
    def twoSum(self, nums, target):

        hashmap = {}

        for i, num in enumerate(nums):

            need = target - num

            if need in hashmap:
                return [hashmap[need], i]

            hashmap[num] = i
```

---

# 代码讲解 | Code Explanation

## 1. 创建哈希表
## Create a hashmap

```python
hashmap = {}
```

用于存储：

Used to store:

```python
数字 : 下标
number : index
```

---

## 2. 遍历数组
## Traverse the array

```python
for i, num in enumerate(nums):
```

`i` 是下标，`num` 是当前数字。

`i` is the index, `num` is the current number.

---

## 3. 计算需要的数字
## Calculate the needed number

```python
need = target - num
```

例如：

For example:

```python
target = 9
num = 2
need = 7
```

---

## 4. 判断是否已经存在
## Check whether it already exists

```python
if need in hashmap:
```

如果存在：

If it exists:

```python
说明已经找到答案
It means we found the answer
```

---

## 5. 返回结果
## Return the result

```python
return [hashmap[need], i]
```

返回：

Return:

```text
之前数字的下标 + 当前下标
previous index + current index
```

---

## 6. 存入哈希表
## Store into hashmap

```python
hashmap[num] = i
```

例如：

For example:

```python
{
    2: 0,
    7: 1
}
```

---

# 时间复杂度 | Time Complexity

## 时间复杂度
## Time Complexity

### O(n)

因为只遍历一次数组。

Because we only traverse the array once.

---

# 空间复杂度 | Space Complexity

### O(n)

因为使用了哈希表存储数据。

Because we use a hashmap to store data.

---

# 本题核心收获 | Key Takeaway

## 核心思想
## Key Insight

```text
空间换时间
Trade space for time
```

使用哈希表：

Using a hashmap:

```text
把 O(n²)
优化为
O(n)
```

Optimize from:

O(n²)

↓

O(n)

这是算法中最经典的优化思想之一。

This is one of the most classic optimization ideas in algorithms.
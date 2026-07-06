# LeetCode 138. 随机链表的复制（Copy List with Random Pointer）——（HashMap 解法）

---

![alt text](<../../Snap_for_Questions/7_Linked_Lists_链表/截屏2026-07-03 19.09.10.png>)

![alt text](<../../Snap_for_Questions/7_Linked_Lists_链表/截屏2026-07-03 19.09.34.png>)

直接代码：
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 判断是否为空 -> 是空，直接返回
        if not head:
            return None
        # 构建hashmap
        hashmap = {} # hashmap = dict()

        # 进行第一遍遍历，得到所有的复制节点
        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        
        # 第二遍遍历，进行next链接，然后random链接
        cur = head
        while cur:
            if cur.next:
                hashmap[cur].next = hashmap[cur.next]
            
            if cur.random:
                hashmap[cur].random = hashmap[cur.random]
            
            cur = cur.next
        return hashmap[head]
```


# 一、题目描述

给你一个特殊的链表，每个节点包含两个指针：

```
next
```

表示：

```
指向下一个节点
```

还有一个：

```
random
```

表示：

```
可以指向链表中的任意节点

或者

None
```

要求：

> **复制整个链表（深拷贝），返回新的链表头节点。**

注意：
复制后的链表：

- 节点值相同
- next 指向相同位置
- random 指向相同逻辑位置
- **不能指向原链表中的节点**

---

# 二、什么叫深拷贝（Deep Copy）？

例如：
原链表：

```
A(7) → B(13) → C(11)
```

其中：

```
A.random = None

B.random = A

C.random = B
```

复制以后：

```
A'(7) → B'(13) → C'(11)
```

要求：

```
B'.random

↓

A'
```

而不是：

```
B'.random

↓

A（原节点）
```

这就是：

```
Deep Copy（深拷贝）
```

---

## 错误示意（浅拷贝）

如果：

```
B'
↓
random
↓
A
```

那么，复制链表：

仍然依赖：

```
原链表
```

这种叫：

```
浅拷贝（Shallow Copy）
```

题目明确禁止。

---

# 三、本题最大的难点（★★★★★）

普通链表：

```
next
```

只有：

```
一个方向
```

例如：

```
1 → 2 → 3 → 4
```

复制非常简单。

但是 本题还有：

```
random
```

例如：

```
1 → 2 → 3 → 4

↑       ↓

└───────┘
```

甚至：

```
1.random = 4

2.random = 1

3.random = None

4.random = 2
```

random 可以：

- 向前
- 向后
- 指向自己
- 指向 None

所以：
**不能边复制边连接 random。**

---

# 四、为什么不能直接复制？

很多同学第一反应：

```python
new = Node(old.val)
new.next = old.next
new.random = old.random
```

这是错误的。

例如：

```
old.random

↓

原链表节点
```

复制以后：

```
new.random

↓

还是原链表节点
```

这样：
复制出来的新链表：

仍然依赖：

```
原链表
```

违反题意。

---

# 五、本题核心思想（★★★★★）

采用：

> **HashMap（哈希表）建立"原节点 → 新节点"的映射。**

整个流程：

```
第一次遍历
↓
复制所有节点
↓
建立映射关系
↓
第二次遍历
↓
连接 next
↓
连接 random
↓
返回新链表
```

重点：

```
HashMap

负责：

找到对应的新节点。
```

---

# 六、为什么 HashMap 能解决？

例如：

原链表：

```
A → B → C
```

第一遍复制：

```
A'

B'

C'
```

同时建立：

```
HashMap

A → A'

B → B'

C → C'
```

以后：
如果：

```
A.random = C
```

只需要：

```
HashMap[C]
```

立即得到：

```
C'
```

所以：

```
A'.random = C'
```

成功。

---

# 七、完整图解（★★★★★）

假设：

```
原链表：

7 → 13 → 11
```

random：

```
7
↓
None
```

```
13
↓
7
```

```
11
↓
13
```

---

## 第一步：复制所有节点

得到：

```
7'

13'

11'
```

注意，目前：

```
next

没有连接
```

```
random

也没有连接
```

只有：

```
HashMap
```

建立：

```
7  → 7'
13 → 13'
11 → 11'
```

---

## 第二步：连接 next

原链表：

```
7 → 13 → 11
```

因此：

```
7'.next
↓
13'
```

```
13'.next
↓
11'
```

完成：

```
7' → 13' → 11'
```

---

## 第三步：连接 random

原来：

```
13.random
↓
7
```

于是：

```
13'.random
↓
HashMap[7]
↓
7'
```

同理：

```
11'.random
↓
13'
```

完成复制。

---

# 八、LeetCode 核心代码模板（★★★★★）

```python
class Solution:
    def copyRandomList(self, head):

        if not head:
            return None

        # 原节点 -> 新节点
        hashmap = {}

        # 第一遍：复制所有节点
        cur = head

        while cur:

            hashmap[cur] = Node(cur.val)

            cur = cur.next

        # 第二遍：连接 next 和 random
        cur = head

        while cur:
            if cur.next:
                hashmap[cur].next = hashmap[cur.next]
            if cur.random:
                hashmap[cur].random = hashmap[cur.random]
            cur = cur.next

        return hashmap[head]
```

---

# 九、逐句代码讲解

## ① 判空

```python
if not head:
    return None
```

作用：如果链表为空，直接返回 `None`，避免后续访问空指针。

---

## ② 创建 HashMap

```python
hashmap = {}
```

作用：建立 **原节点 → 新节点** 的映射。

例如：

```
原节点        新节点

7   ------>   7'

13  ------>   13'

11  ------>   11'
```

注意：
这里：

```
Key

不是：

节点值 .val
```

而是：

```
节点对象 ListNode()
```

因为：

可能：

```
值重复。
```

例如：

```
3 → 3 → 3
```

如果：

```
value

作为 Key
```

就冲突了。

所以：

必须：

```
节点对象

作为 Key。
```

---

## ③ 第一遍遍历

```python
cur = head
```

作用：从链表头开始遍历。

---

## ④ 创建复制节点

```python
hashmap[cur] = Node(cur.val)
```
这里leetcode定义了class类Node，所以在平时我们要看给了我们什么class。

作用：复制当前节点。

例如：

```
原：

13
```

创建：

```
13'
```

然后：

保存：

```
13

↓

13'
```

到：

```
HashMap。
```

此时：

```
next

没有连接。
```

```
random

也没有连接。
```

这里只负责：

```
复制节点。
```

---

## ⑤ 后移

```python
cur = cur.next
```

继续复制：

下一个节点。

---

# 十、为什么第一遍不能直接连接 random？（★★★★★）

例如：
现在：

```
正在复制：
7
```

但是：

```
7.random
↓
11
```

问题：

```
11'
还没有创建！
```

所以：
第一遍：
只能：

```
复制节点
```

不能：

```
连接 random。
```

因此：
必须：

```
两次遍历。
```

第一次：

```
全部创建节点。
```

第二次：

```
再连接所有指针。
```

---

# 十一、本部分总结

HashMap 方法的核心只有一句话：

> **先建立所有新节点，再利用 HashMap 找到对应的新节点，最后统一连接 next 和 random。**

第一遍遍历负责：

```
复制节点
↓
建立：
原节点 → 新节点
映射
```

第二遍遍历负责：

```
连接 next
↓
连接 random
```

这样可以保证：

无论 `random` 指向前面、后面、自己还是 `None`，都能够正确找到对应的新节点。


---

# 十二、第二遍遍历：连接 next 和 random（★★★★★）

经过第一遍遍历，我们已经有了：

```
原链表
7 → 13 → 11
```

对应的新链表节点：

```
7'
13'
11'
```

以及 HashMap：

```
7  → 7'
13 → 13'
11 → 11'
```

但是此时：

```
7'
13'
11'
```

仍然是三个独立的节点，没有任何连接。

第二遍遍历的任务就是：

```
连接 next
↓
连接 random
```

---

## 第一步：重新回到头节点

```python
cur = head
```

作用：重新遍历原链表。

为什么？

因为第一遍遍历结束以后：

```
cur
↓
None
```

需要重新从头开始。

---

## 第二步：连接 next

```python
if cur.next:
    hashmap[cur].next = hashmap[cur.next]
```

这是整个 HashMap 解法最重要的一句。

例如：
原链表：

```
7 → 13 → 11
```

现在：

```
cur
↓
7
```

那么：

```
cur.next
↓
13
```

于是：

```
hashmap[cur]
↓
7'
```

```
hashmap[cur.next]
↓
13'
```

最终：

```
7'.next = 13'
```

是不是完全对应原链表？

原来：

```
7
↓
13
```

现在：

```
7'
↓
13'
```

整个 next 就复制完成了。

---

## 第三步：连接 random

```python
if cur.random:
    hashmap[cur].random = hashmap[cur.random]
```

例如：
原链表：
```
13.random
↓
7
```

那么：

```
hashmap[13]
↓
13'
```

```
hashmap[7]
↓
7'
```

于是：

```
13'.random = 7'
```

同样：
如果：

```
11.random
↓
13
```

得到：

```
11'.random
↓
13'
```

这样：
random 也复制完成。

---

## 第四步：继续遍历

```python
cur = cur.next
```

作用：

继续处理：

```
下一个原节点
```

直到：

```
cur == None
```

循环结束。

---

## 第五步：返回复制链表

```python
return hashmap[head]
```

为什么不是：

```python
return head
```

因为：

```
head
是：
原链表。
```

真正的新链表头：

应该是：

```
HashMap
里面：
head
对应的新节点。
```

例如：

```
head
↓
7
```

HashMap：

```
7
↓
7'
```

因此：

```
return hashmap[head]
```

返回：

```
7'
```

---

# 十三、ACM 模式

```python
def copyRandomList(head):

    if not head:
        return None

    hashmap = {}

    cur = head

    while cur:

        hashmap[cur] = Node(cur.val)

        cur = cur.next

    cur = head

    while cur:

        if cur.next:
            hashmap[cur].next = hashmap[cur.next]

        if cur.random:
            hashmap[cur].random = hashmap[cur.random]

        cur = cur.next

    return hashmap[head]
```

---

# 十五、涉及的重要 Function / Python 语法讲解

## 1. `dict()`

创建一个空字典。

```python
hashmap = {}
```

等价于：

```python
hashmap = dict()
```

作用：
保存：

```
原节点
↓
新节点
```

---

## 2. `hashmap[key]`

作用：根据 Key 找到 Value。

例如：

```python
hashmap[cur]
```

得到：

```
当前原节点
对应的新节点。
```

例如：

```
hashmap[13]
↓
13'
```

---

## 3. `Node(cur.val)`

作用：创建新的链表节点。

例如：

```python
Node(7)
```

得到：

```
7'
```

注意：

这里只复制：

```
值
```

不会复制：

```
next
random
```

这些后面统一连接。

---

## 4. `cur.next`

作用：得到：

```
当前节点的下一个节点。
```

例如：

```
7 → 13
```

那么：

```
7.next
↓
13
```

---

## 5. `cur.random`

作用：得到：

```
当前节点 random 指向的节点。
```

例如：

```
13.random
↓
7
```

那么：

```python
cur.random
```

就是：

```
7
```

---

# 十六、为什么 HashMap 的 Key 必须是节点，而不能是 val？（★★★★★）

例如：

```
3 → 3 → 3
```

如果：

```
value
作为 Key
```

HashMap：

```
3
↓
???
```

三个节点都会覆盖。

因此：不能使用：

```
值。
```

必须：

```
节点对象。
```

即：

```
NodeA
↓
NodeA'
```

```
NodeB
↓
NodeB'
```

这样：
即使：

```
值相同。
```

仍然能够正确找到对应节点。

---

# 十七、复杂度分析

第一遍：

```
O(n)
```

第二遍：

```
O(n)
```

总时间复杂度：

```
O(n)
```

---

HashMap：

保存：

```
n个节点。
```

因此：

空间复杂度：

```
O(n)
```

---

# 十八、为什么这是最容易理解的方法？（★★★★★）

优点：

✅ 思路最简单

✅ 容易调试

✅ 面试容易写对

缺点：

需要：

```
HashMap
```

额外空间：

```
O(n)
```

因此：

很多大厂会继续问：

> 能不能不用 HashMap？

答案就是：

```
O(1)

空间。

穿插节点法。
```

本题的最优解。

---

# 十九、HashMap 解法完整流程图（★★★★★）

```
开始
↓
判断空链表
↓
创建 HashMap
↓
第一次遍历
↓
复制所有节点
↓
建立 原节点 → 新节点 映射
↓
第二次遍历
↓
连接 next
↓
连接 random
↓
返回 HashMap[head]
```

整个流程只需要两次遍历。

---

# 二十、易错点总结（★★★★★）

## 易错点 1

错误：

```python
new.random = cur.random
```

原因：

random 指向：

```
原节点。
```

正确：

```python
new.random = hashmap[cur.random]
```

---

## 易错点 2

错误：

```python
hashmap[cur.val]
```

原因：

值可能重复。

正确：

```python
hashmap[cur]
```

---

## 易错点 3

忘记判断：

```python
if cur.random:
```

如果：

```
random=None
```

程序会报错。

---

## 易错点 4

返回：

```python
head
```

错误。

应该：

```python
return hashmap[head]
```

---

# 二十一、本题与 Hot100 链表题的联系

| 题目 | 核心思想 |
|------|----------|
| 2. 两数相加 | Dummy |
| 19. 删除倒数第 N 个节点 | Dummy + 双指针 |
| 21. 合并有序链表 | Dummy |
| 24. 两两交换节点 | Dummy + 局部交换 |
| 25. K 个一组翻转 | Dummy + 局部反转 |
| 138. 随机链表复制 | HashMap + 链表 |
| 141. 环形链表 | 快慢指针 |
| 142. 环形链表Ⅱ | Floyd 算法 |
| 160. 相交链表 | 双指针 |
| 206. 反转链表 | 三指针 |
| 234. 回文链表 | 快慢指针 + 反转 |

可以发现：

**138 是 Hot100 链表专题中唯一重点考察「HashMap + 链表映射」思想的题目。**

---

# 二十二、面试口诀（★★★★★）

```text
第一遍，只复制，
建立映射别着急。

第二遍，连指针，
next、random 都更新。

HashMap 找对应，
深拷贝就能完成。
```

---

# 二十三、本题总结

HashMap 解法可以概括为四步：

```
第一次遍历
↓
复制所有节点
↓
建立 原节点 → 新节点 映射
↓
第二次遍历
↓
连接 next
↓
连接 random
↓
返回新链表
```

最重要的四句代码：

```python
hashmap[cur] = Node(cur.val)

hashmap[cur].next = hashmap[cur.next]

hashmap[cur].random = hashmap[cur.random]

return hashmap[head]
```

必须牢记：

- **HashMap 的 Key 是节点对象，不是节点值。**
- **第一遍只创建节点，不连接任何指针。**
- **第二遍统一连接 next 和 random。**
- **最终返回的是复制链表的头节点，而不是原链表。**

---

# 二十四、进阶（★★★★★）

本题还有一个面试最喜欢的最优解：

> **穿插节点法（Interweaving / Weaving Method）**

特点：

- 不使用 HashMap
- 空间复杂度 **O(1)**
- 三次遍历完成复制
- 是 Google、Meta、字节、腾讯等公司高频考法

建议学习顺序：

```
HashMap 解法（必须掌握）
↓
O(1) 穿插节点法（面试进阶）
```

先理解 HashMap 的映射思想，再学习穿插节点法，会更容易理解为什么能够不用额外空间。
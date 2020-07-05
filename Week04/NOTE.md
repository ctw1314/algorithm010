## 搜索算法

- 遍历搜索

1. 每个年度都要访问一次
2. 每个官员仅要访问一次

- 暴力式搜索：时间复杂度：O（E）/空间复杂度：O（V）

1. 广度优先搜索（BFS）->层层遍历1.1已访问->记录已被访问的顶点1.2队列->存储已被访问但相连的前端未被访问的顶点

```
def BFS(graph, start, end):
    queue = []
    queue.append([start])
    
    visited = set()
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
        
    # other processing work
    ...
```

1. 深度优先搜索（DFS）->回溯思想

```
def DFS(self, tree):
    if tree.root is None: return []
    
    visited, stack = [], []
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
        
    # other processing work
    ...
def DFS(node, visited):
    visited = set()
    visited.add(node)
    
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            DFS(next_node, visited)
```

- 启发式搜索

- 实战译文

1. [二叉树最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
2. [二叉树最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
3. [括号生成](https://leetcode-cn.com/problems/generate-parentheses/#/description)
4. [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description)
5. [在每个树中找适当](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)
6. [单词接龙](https://leetcode-cn.com/problems/word-ladder/description/ /)
7. [单词接龙II](https://leetcode-cn.com/problems/word-ladder-ii/description/ /)
8. [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
9. [扫雷游戏](https://leetcode-cn.com/problems/minesweeper/description/)

## 贪心算法

- 概念解析

1. 动态规划的一种特殊情况
2. 局部最优：总是做出在当前看来是最好的选择
3. 看到限制值和期望值类别问题的时候首先要联想到贪心算法3.1尝试看下这个问题是否可以用贪心算法解决3.2举几个例子看下贪心算法产生的结果是否是最优

- 基本实现

1. 建模：建立数学模型来描述问题
2. 分解：把改进的问题分解成几个个子问题
3. 解决：对每个问题克服以得到子问题的局部最优解
4. 合并：将子问题的局部最优解合并成原问题的一个解

- 适用场景

1. 最优子结构
2. 无后效性
3. 贪心选择性

- 常考面试

1. 分糖果
2. 钱币找零
3. 区间覆盖

- 实战译文

1. [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/description/)
2. [发行饼干](https://leetcode-cn.com/problems/assign-cookies/)
3. [模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/)
4. 跳跃游戏
5. 跳跃游戏II

###### 二分查找

- 概念解析
- 初步条件

1. 单调（排序）：目标函数单调性（单调递增或递减）
2. 边界（Bounded）：存在上下界
3. 索引（Index access）：能够通过索引访问

- 基本实现

1. 循环退出的条件
2. 每次查找区间一半mid的取值
3. 左右左右的间隔区间

```
left, right = 0, len(array) - 1
while left <= right：
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

- 适用场景

1. 静态数据且没有过多的插入和删除操作

- 常考面试

1. 发现第一个值等于给定值的元素
2. 发现最后一个值等于给定值的元素
3. 发现第一个大于等于给定值的元素
4. 发现最后一个小于等于给定值的元素
5. 旋转的的二分查找

- 实战译文

1. [x的平方根](https://leetcode-cn.com/problems/sqrtx/)
2. [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)
3. [搜索旋转排序](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
4. [搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)
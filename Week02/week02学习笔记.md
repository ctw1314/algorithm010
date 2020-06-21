# week02学习笔记

> 第二周学习
>
> 原文链接：https://www.yuque.com/docs/share/9b8f5efa-7869-45dc-88e0-128a58a6e881?# 《week02学习笔记》

## 1. 总结


这周学习了哈希表，映射，集合，树，堆，图，重点是哈希表，python实现的话就是字典，和树，主要是二叉树，整体节奏还可以


## 2. 知识
### 2.1 哈希表

- 也叫散列表
- key-value结构
- 哈希碰撞
- python dict
### 2.3 集合

- set
### 2.4 树
![img](https://cdn.nlark.com/yuque/0/2020/png/359541/1592731447966-b708a674-7150-405b-a14a-5cb9107c2a86.png)
#### 2.4.1 二叉树

- 三种遍历
   - 前序
   - 中序
   - 后序
#### 2.4.2 二叉搜索树

- 左子树上所有结点的值均小于它的根结点的值；
- 右子树上所有结点的值均大于它的根结点的值；
- 查询
- 插入新结点
- 删除
### 2.5 堆

- 可以迅速找到最大值或者最小值
#### 2.5.1 二叉堆

- 完全二叉树
- 树中root>= children
- 查找O（1）
- 插入，删除 O（logn）

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1592731783782-f6f05753-74ed-46e6-858f-bee3382c06b7.png)
### 2.6 图

- 有环
- DFS
- BFS



## 3. 刷题
### 3.1 1. 两数之和

- 老生常谈的第一题
- 直接用dict，找下标
### 3.2 242. 有效的字母异位词

- 直接排序
- 直接循环判断
- 使用python内库
- 使用字典



### 3.3 49. 字母异位词分组

- 上一题的进阶
- 使用元组+字典
- 元组先把异位词解决
- 注意dict.get()

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1592732294895-d2f065f2-bd57-4585-b29e-49b1f42c7342.png)

### 3.4 二叉树

> 为了方便大家理解和记忆，都是采用最容易理解以及代码量最少的写法，尽量pythonic.
>
> 原文链接：https://www.yuque.com/docs/share/1bc6933b-38a4-4e1b-9861-af5ed1ccfafb?# 《二叉树的前序，中序，后序，层序遍历（python非递归写法总结, python 面试必备）》



#### 1. 二叉树的前序遍历(leetcode 144)

二叉树的前序遍历指的是（中—> 左 —> 右）。实现非递归算法的主要思路就是队列和栈。但是由于栈后进先出的特性，所以先压入栈的时候，先压入右孩子， 再压入左孩子。



```
Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def preorderTraversal(self, root):
        ret, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                #注意压入栈的顺序,先压入右孩子，再压入左孩子
                stack.append(node.right)
                stack.append(node.left)
        return ret          
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1592727746992-26e481ae-5167-4085-8d47-254ecc3dd48e.png)

#### 2. 二叉树中序遍历(leetcode 94)

中序遍历的意思就是（左—> 中 —> 右）的顺序遍历



```
Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def inorderTraversal(self, root):
        ret, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temNode = stack.pop()
                ret.append(temNode.val)
                root = temNode.right
        return ret
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1592727792012-b525b040-9d93-4780-a06b-bab1f5a94d6a.png)



#### 3. 二叉树后序遍历(leetcode 145)

```
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                ret.insert(0, root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return ret
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1592728007303-8866e3df-ca6b-4c89-9c3e-ebe493fc239f.png)

#### 4. 二叉树层序遍历(leetcode 102)

```
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level = [], [root]
        while any(level):
            ans.append([node.val for node in level])            
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1592728022150-17cde518-035a-49ee-a485-4081dd1d10f6.png)

#### 5. 多叉树的层序遍历(leetcode 429)

```
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ret, level = [], [root]
        while any(level):
            ret.append([node.val for node in level])
            level = [child for node in level for child in node.children if child]
        return ret
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1592728032504-889998fa-f4a2-4cb9-a23a-e10cd2b46e01.png)

#### 6. 树的深度遍历

```
def deep(root):
   if not root:
       return
   print(root.val)
   deep(root.left)
   deep(root.right)

if __name__ == '__main__':
   deep(tree)
```



#### 7. 判断两颗树是否相同

```
def isSample(p,q):
   if p == None and q == None:
       return True
   elif p and q:
       return p.val == q.val and isSample(p.left, q.left) and isSample(p.right, q.right)
   else:
       return False
```
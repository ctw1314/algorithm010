# week03学习笔记

> 第三周学习

## 1. 总结

这周学习了泛型递归，分治和回溯，理解起来不是很难，但是做题总是没有思路，递归这块还是有很多好题目，回溯的八皇后就很有意思

## 2. 知识

### 2.1 泛型递归

- 自己调自己
- 重复性（找最小重复单元）
- 代码模版

```
def recursion(level, param1, param2, ...):
    # recursion terminator
    # 递归终止条件
    if level > Max_level:
        process_result
        return
    
    # process logic in current level
    # 处理逻辑
    process(level, data...)
    
    # drill down
    # 递归调用（下钻）
    self.recursion(level+1, p1, p2,...)
    
    # reverse the current level status if needed
    # 清理变量，一般不需要，但是不能忘记
```

- 思维要点

1. 1. 不要进行人肉递归（最大误区）
   2. 找到最近最简方法，将其拆解为可重复子问题
   3. 数学归纳法思维

### 2.2 分治

- 也是递归
- 找重复性
- 将大问题分解成一个个小问题
- 将小问题的结果组合成最终结果
- 代码模版

```
# Python
def divide_conquer(problem, param1, param2, ...): 
        # recursion terminator 
      if problem is None: 
                print_result 
                return 

      # prepare data 
        data = prepare_data(problem) 
      subproblems = split_problem(problem, data) 

      # conquer subproblems 
      subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
      subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
      subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
      …

      # process and generate the final result 
      result = process_result(subresult1, subresult2, subresult3, …)
    
      # revert the current level states
```

- 思维要点

- - 和递归相比多了中间结果的组合

- 分治三部曲

1. 1. 分解：将原问题分解成一系列子问题；
   2. 解决：递归地改善各个子问题，若子问题足够小，则直接克服；
   3. 合并：将子问题的结果合并成原问题。

### 2.3 回溯

- 中心思想

- - 能进则进，进不了则换，换不了则退

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1593334999434-96f3d903-350a-43f8-b6c3-d5d9d2913f08.png)



## 3. 刷题

> 完成了作业中的两个递归，一个回溯，CPU疼

### 3.1 236. 二叉树的最近公共祖先

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1593339062451-2e5940b9-721b-4f4c-a23b-f9c1a1829833.png)

### 3.2 105. 从前序与中序遍历构造二叉树

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1593339130997-16412969-b984-4a51-937b-888d2ff84047.png)

- 先序找根，划分左右

### 3.3 77.组合

- 回溯确实有点懵

![image.png](https://cdn.nlark.com/yuque/0/2020/png/359541/1593339273347-2d496165-3947-438a-a092-03f5e49d0373.png)

- 剪枝不是很理解


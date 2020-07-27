# 第七周学习笔记

#### 1. 字典树和并查集

##### 1.1 字典树（Trie树）

> 又称单词查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串，所以经常被搜索引擎系统用于文本词频统计。
>
> 优点：最大限度的减少无谓的字符串比较，查找效率比哈希表高。

**基本性质**

1. 结点本身不存完整单词；
2. 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串；
3. 每个结点的所有子结点路径代表的字符都不相同。

**核心思想**

1. Trie树的核心思想是空间换时间；
2. 利用字符串的公共前缀降低查询时间的开销以达到提高效率的目的。

**Trie树代码模板**

```
class Trie {
    private boolean isEnd;
    private Trie[] next;
    /** Initialize your data structure here. */
    public Trie() {
        isEnd = false;
        next = new Trie[26];
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        if (word == null || word.length() == 0) return;
        Trie curr = this;
        char[] words = word.toCharArray();
        for (int i = 0;i < words.length;i++) {
            int n = words[i] - 'a';
            if (curr.next[n] == null) curr.next[n] = new Trie();
            curr = curr.next[n];
        }
        curr.isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Trie node = searchPrefix(word);
        return node != null && node.isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Trie node = searchPrefix(prefix);
        return node != null;
    }

    private Trie searchPrefix(String word) {
        Trie node = this;
        char[] words = word.toCharArray();
        for (int i = 0;i < words.length;i++) {
            node = node.next[words[i] - 'a'];
            if (node == null) return null;
        }
        return node;
    }
}
```

##### 1.2 并查集

**适用场景**

1. 组团、配对问题
2. 分组

**基本操作**

1. makeSet ( s ) : 建立并查集，包含s个元素的集合
2. unionSet ( x,y ) : 把元素x和元素y所在集合合并
3. find (x) : 找到元素x所在集合的代表

**并查集代码模板**

```
class UnionFind {
	private int count = 0; 
	private int[] parent; 
	public UnionFind(int n) { 
		count = n; 
		parent = new int[n]; 
		for (int i = 0; i < n; i++) { 
			parent[i] = i;
		}
	} 
	public int find(int p) { 
		while (p != parent[p]) { 
			parent[p] = parent[parent[p]]; 
			p = parent[p]; 
		}
		return p; 
	}
	public void union(int p, int q) { 
		int rootP = find(p); 
		int rootQ = find(q); 
		if (rootP == rootQ) return; 
		parent[rootP] = rootQ; 
		count--;
	}
}
```

> ##### **参考链接**
>
> - [二叉树的层次遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
> - [实现 Trie](https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/)
> - [Tire 树代码模板](https://shimo.im/docs/DP53Y6rOwN8MTCQH)
> - [并查集代码模板](https://shimo.im/docs/VtcxL0kyp04OBHak)
>
> **实战例题**
>
> - [实现 Trie (前缀树) ](https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description)（亚马逊、微软、谷歌在半年内面试中考过）
> - [单词搜索 II ](https://leetcode-cn.com/problems/word-search-ii/)（亚马逊、微软、苹果在半年内面试中考过）
> - 分析单词搜索 2 用 Tire 树方式实现的时间复杂度
> - [朋友圈](https://leetcode-cn.com/problems/friend-circles)（亚马逊、Facebook、字节跳动在半年内面试中考过）
> - [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)（近半年内，亚马逊在面试中考查此题达到 361 次）
> - [被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)（亚马逊、eBay、谷歌在半年内面试中考过）

#### 2. 高级搜索

##### 2.1 剪枝

**初级搜索**

1. 朴素搜索
2. 优化方式：不重复、剪枝
3. 搜索方向：DFS、BFS

**高级搜索**

1. 剪枝
2. 双向搜索、启发式搜索

**回溯法**

>  回溯法采用试错思想，尝试分步的去解决一个问题。在分步解决问题的过程中，当发现现有的分步不能得到正确的解答时，它将取消上一步甚至上几步的计算，再通过其他的分步再次尝试。
>
>  回溯法通常用递归实现，可能出现两种情况：
>
> - 找到一个可能存在的正确答案
>
> - 尝试了所有可能的方法后宣告没有答案
>
>   最坏情况下，时间复杂度是指数级的。

##### 2.2 双向BFS

> 从前后两端同时开始BFS遍历

**代码模板**

```
public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Map<String,List<String>> tempMap = new HashMap<String,List<String>>();
        // 定义两个队列
        Set<String> q1 = new HashSet<>();
        Set<String> q2 = new HashSet<>();
        // 定义visited数组
        Set<String> visited = new HashSet<String>();
        q1.add(beginWord);
        q2.add(endWord);
        int step = 1;
        while (!q1.isEmpty() && !q2.isEmpty()) {
            Set<String> temp = new HashSet<>();
            for (String cur : q1) {
                // 前后遍历相交的时候，说明找到结果了
                if (q2.contains(cur)) {
                    return step;
                }
                // 记录visited
                visited.add(cur);
                // 处理当前节点
                char[] curArr = cur.toCharArray();
                for (int i = 0; i < curArr.length; i++) {
                    char c = curArr[i];
                    curArr[i] = '*';
                    List<String> list = tempMap.get(String.valueOf(curArr));
                    if (list != null && list.size() > 0) {
                        for (String s : list) {
                            // 将相邻节点加入队列
                            if (!visited.contains(s)) {
                                temp.add(s);
                            }
                        }
                    }
                    curArr[i] = c;
                }
            }
            // 步数+1，前后队列互换
            step++;
            q1 = q2;
            q2 = temp;
        }
        return 0;
    }
```

##### 2.3 启发式搜索 Heuristic Search(A*)

**代码模板**

```
def AstarSearch(graph, start, end):
	# 将BFS的队列换成优先队列
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop()
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```

**估价函数**

>  启发式函数：h(n)，用来评价哪些节点最有希望是我们要找的节点，返回一个非负实数，可以认为是从n的目标节点路径的估计成本。
>
>  启发式函数是一种告知搜索方向的方法，它提供了一种明智的方法来猜测哪个邻居节点会导向一个目标。

> ##### **参考链接**
>
> - [DFS 代码模板](https://shimo.im/docs/UdY2UUKtliYXmk8t)
> - [BFS 代码模板](https://shimo.im/docs/ZBghMEZWix0Lc2jQ)
> - [AlphaZero Explained](https://nikcheerla.github.io/deeplearningschool/2018/01/01/AlphaZero-Explained/)
> - [棋类复杂度](https://en.wikipedia.org/wiki/Game_complexity)
> - [A* 代码模板](https://shimo.im/docs/8CzMlrcvbWwFXA8r)
> - [相似度测量方法](https://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)
> - [二进制矩阵中的最短路径的 A* 解法](https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/A*-search-in-Python)
> - [8 puzzles 解法比较](https://zxi.mytechroad.com/blog/searching/8-puzzles-bidirectional-astar-vs-bidirectional-bfs/)
>
> **实战例题**
>
> - [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)（阿里巴巴、腾讯、字节跳动在半年内面试常考）
> - [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)（亚马逊、Facebook、字节跳动在半年内面试中考过）
> - [N 皇后](https://leetcode-cn.com/problems/n-queens/)（亚马逊、苹果、字节跳动在半年内面试中考过）
> - [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/description/)（亚马逊、苹果、微软在半年内面试中考过）
> - [解数独](https://leetcode-cn.com/problems/sudoku-solver/#/description)（亚马逊、华为、微软在半年内面试中考过）
> - [单词接龙](https://leetcode-cn.com/problems/word-ladder/)（亚马逊、Facebook、谷歌在半年内面试中考过）
> - [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/)（谷歌、Twitter、腾讯在半年内面试中考过）
> - 总结双向 BFS 代码模版
> - [二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/)（亚马逊、字节跳动、Facebook 在半年内面试中考过）
> - [滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle/)（微软、谷歌、Facebook 在半年内面试中考过）
> - [解数独](https://leetcode-cn.com/problems/sudoku-solver/)（微软、华为、亚马逊在半年内面试中考过）

#### 3. 红黑树 & AVL树

##### 3.1 AVL树

1. 发明者G.M.Adelson-Velsky和Evgenii Landis

2. Balance Factor(平衡因子)：

   左子树高度 减去 右子树高度（有时相反）。

   Balance factor = {-1,0,1}

3. 通过旋转操作来进行平衡（四种）

**旋转操作**

1. 右右子树 -> 左旋
2. 左左子树 -> 右旋
3. 左右子树 -> 左右旋
4. 右左子树 -> 右左旋

**AVL总结**

1. 平衡二叉搜索树

2. 每个节点存balance factor = {-1,0,1}

3. 四种旋转操作

   不足：节点需要存储额外信息、且调整次数频繁

##### 3.2 红黑树 Red-black Tree

> 红黑树是一种**近似平衡**的二叉搜索树，满足任何一个节点的左右子树的**高度差小于两倍**。具体来说，红黑树满足如下条件：

- 每个节点要么是红色，要么是黑色
- 根结点是黑色
- 每个叶子结点（null结点，空节点）是黑色的
- 不能有相邻接的两个红色结点
- 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点

##### 3.3 对比

- 查询：AVL树优于红黑树，因为AVL树是严格平衡的
- 插入 & 删除：红黑树优于AVL树，红黑树是近似平衡的
- 存储：红黑树优于AVL树，因为AVL树每个节点需要存储balance factor,红黑树只需要1bit存储颜色信息
- 红黑树大多数用在语言类库，AVL多用在读多写少，比如数据库中

> - [平衡树](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)
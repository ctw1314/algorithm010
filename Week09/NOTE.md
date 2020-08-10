## week09学习笔记

### 1. 动态规划

> 1. 将复杂问题分解为简单的字问题
> 2. 分治+最优子结构
> 3. 顺推形式：动态递推

**DP顺推模板**

```
function DP():
	dp=[][] #二维情况
	for i = 0..M{
		for j = 0..N{
			dp[i][j] = function(dp[i'][j']...)
		}
	}
	return dp[M][N];
```

**关键点**

1. 动态规划和递归，分治没有根本上的区别，关键是看有无最优的子结构
2. 共性：找重复子问题
3. 差异性：最优子结构，中途可以淘汰次优解

**复杂度来源**

1. 状态拥有更多的维度，甚至需要压缩
2. 状态转移方程更加复杂



> **参考链接**
>
> - [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)（阿里巴巴、腾讯、字节跳动在半年内面试常考）
> - [不同路径](https://leetcode-cn.com/problems/unique-paths/)（亚马逊、微软、Facebook 在半年内面试中考过）
> - [打家劫舍](https://leetcode-cn.com/problems/house-robber/)（字节跳动、谷歌、苹果在半年内面试中考过）
> - [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)（字节跳动、谷歌、亚马逊在半年内面试中考过）
> - [股票买卖](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)（字节跳动、亚马逊、Facebook 在半年内面试常考）
> - [使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)（亚马逊在半年内面试中考过）
> - [编辑距离](https://leetcode-cn.com/problems/edit-distance/)（字节跳动、亚马逊、谷歌在半年内面试中考过）
>

### 2. 字符串算法

**字符串匹配算法**

1. 暴力法
2. Rabin-Karp算法
3. KMP算法
4. Boyer-Moore算法
5. Sunday算法

**暴力法**

```java
public static int forceSearch(String txt, String pat) {
    int M = txt.length();
    int N = pat.length();
    for (int i = 0; i <= M - N; i++) {
        int j;
        for (j = 0; j < N; j++) {
            if (txt.charAt(i + j) != pat.charAt(j))
                break;
        }
        if (j == N) {
            return i;
        }
        // 加速
        // 1. 预先判断 hash(txt.substring(i, M)) == hash(pat)
        // 2. KMP 
    }
    return -1;
}
```

**Rabin-Karp算法**

**算法思想**

1. 假设子串的长度为M（pat），目标字符串的长度为N（txt）
2. 计算子串的hash值hash_pat
3. 计算目标字符串txt中每个长度为M的子串的hash值（共需要计算N-M+1次）
4. 比较hash值：如果hash值不同，字符串必然不匹配；如果hash值相同，还需要使用朴素算法再次判断



> **参考链接**
>
> - [不可变字符串](https://lemire.me/blog/2017/07/07/are-your-strings-immutable/)
> - [ Atoi 代码示例](https://shimo.im/docs/5kykuLmt7a4DdjSP)
> - [ Boyer-Moore 算法](https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
> - [ Sunday 算法](https://blog.csdn.net/u012505432/article/details/52210975)
> - [字符串匹配暴力法代码示例](https://shimo.im/docs/8G0aJqNL86wWrPUE)
> - [ Rabin-Karp 代码示例](https://shimo.im/docs/1wnsM7eaZ6Ab9j9M)
> - [ KMP 字符串匹配算法视频](https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171)
> - [字符串匹配的 KMP 算法](http://www.ruanyifeng.com/blog/2013/05/Knuth–Morris–Pratt_algorithm.html)
>
> **字符串基础问题**
>
> - [转换成小写字母](https://leetcode-cn.com/problems/to-lower-case/)（谷歌在半年内面试中考过）
> - [最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)（苹果、谷歌、字节跳动在半年内面试中考过）
> - [宝石与石头](https://leetcode-cn.com/problems/jewels-and-stones/)（亚马逊在半年内面试中考过）
> - [字符串中的第一个唯一字符
>    ](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)（亚马逊、微软、Facebook 在半年内面试中考过）
> - [字符串转换整数 (atoi) ](https://leetcode-cn.com/problems/string-to-integer-atoi/)（亚马逊、微软、Facebook 在半年内面试中考过）
>
> **字符串操作问题**
>
> - [最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/description/)（亚马逊、谷歌、Facebook 在半年内面试中考过）
> - [反转字符串](https://leetcode-cn.com/problems/reverse-string)（亚马逊、谷歌、苹果在半年内面试中考过）
> - [反转字符串 II ](https://leetcode-cn.com/problems/reverse-string-ii/)（亚马逊在半年内面试中考过）
> - [翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)（微软、字节跳动、苹果在半年内面试中考过）
> - [反转字符串中的单词 III ](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)（微软、字节跳动、华为在半年内面试中考过）
> - [仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters/)（字节跳动在半年内面试中考过）
>
> **异位词问题**
>
> - [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)（Facebook、亚马逊、谷歌在半年内面试中考过）
> - [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)（亚马逊在半年内面试中常考）
> - [找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)（Facebook 在半年内面试中常考）
>
> **回文串问题**
>
> - [验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)（Facebook 在半年内面试中常考）
> - [验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii/)（Facebook 在半年内面试中常考）
> - [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)（亚马逊、字节跳动、华为在半年内面试中常考）
>
> **最长子串、子序列问题**
>
> - [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)（亚马逊、字节跳动、谷歌在半年内面试中考过）
> - [编辑距离](https://leetcode-cn.com/problems/edit-distance/)（亚马逊、字节跳动、谷歌在半年内面试中考过）
> - [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)（亚马逊、华为、字节跳动在半年内面试常考）
>
> **字符串 + DP 问题**
>
> - [正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)（Facebook、微软、字节跳动在半年内面试中考过）
> - [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/)（Facebook、微软、字节跳动在半年内面试中考过）
> - [不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/)（MathWorks 在半年内面试中考过）




















<h1>CodeInterview</h1>

python [::-1]

双指针

反转链表用

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currentNode, preNode = head, None
        while currentNode:
            temp = currentNode.next
            currentNode.next = preNode
            preNode = currentNode
            currentNode = temp
        return preNode
```

感觉链表的题，很多都会涉及双指针，伪指针



在做条件判断的时候，python中 is 和 == 都可以用来判别变量引用对象是否相等，而 is not 和 != 都可以用来判别变量引用对象是否不等，但在实际应用中对于不同类型的变量，实际上这两者的效果完全不同。究其根本，is 和 is not 在判断时比较的是两个变量引用对象的内存地址，而 == 和 != 则比较的是引用对象的值。



底层存储只有两种方式：数组或者链表

二叉搜索树（或叫二叉排序树、二叉查找树、BST）、AVL树、红黑树、区间树、B树

二叉树的一个小框架：

```
void traverse(TreeNode root){
	//前序遍历
	traverse(root.left)
	//中序遍历
	traverse(root.right)
	//后序遍历
}
```





各种数据结构的遍历+访问无非是：线性的和非线性的

线性就是for/while迭代为代表。非线性就是递归为代表。

比如：

* 数组的遍历框架，典型的线性迭代结构
* 链表的遍历框架，兼具迭代和递归结构
* 二叉树遍历框架，典型的非线性迭代结构



二叉树从上到下打印，即为按层打印，又称为二叉树的广度优先搜索（BFS），BFS通常借助队列的先入先出特性来实现。

二叉搜索树定义：一个二叉树中，任意节点的值要大于等于左子树所有节点的值，且要小于等于右子树所有节点的值。



Python数据结构常见模块：collections、heapq、operator、itertools

| collections   | **计算器（Counter）、双向队列（deque）、默认字典（defaultdict）、有序字典（OrderedDict）、可命名元组（namedtuple）** |
| ------------- | ------------------------------------------------------------ |
| **heapq**     |                                                              |
| **operator**  |                                                              |
| **itertools** |                                                              |

pathlib库



sort()是列表内置方法，没有返回值，是将列表排序，列表变化了。`a.sort()`

sorted()是全局内置的方法，有返回值，返回对可迭代序列排序后的新对象，但是原来的序列不变。`sorted(a)`

- 冒泡排序（Bubble Sort）
- 插入排序（Insertion Sort）
- 希尔排序（Shell Sort）
- 选择排序（Selection Sort）
- 快速排序（Quick Sort）
- 归并排序（Merge Sort）
- 堆排序（Heap Sort）
- 计数排序（Counting Sort）
- 桶排序（Bucket Sort）
- 基数排序（Radix Sort）

归并排序（MERGE-SORT）是利用**归并**的思想实现的排序方法，该算法采用经典的**分治**（divide-and-conquer）策略（分治法将问题**分**(divide)成一些小的问题然后递归求解，而**治(conquer)**的阶段则将分的阶段得到的各答案"修补"在一起，即分而治之)。速度仅次于快速排序。

![image-20210309163659045](C:\Users\daluzi\AppData\Roaming\Typora\typora-user-images\image-20210309163659045.png)

归并这个词语的含义就是合并，并入的意思，而在我们的数据结构中的定义是将两个或两个以上的有序表和成一个新的有序表。而我们这里说的归并排序就是使用归并的思想实现的排序方法。

归并排序使用的就是分治思想。顾名思义就是分而治之，将一个大问题分解成若干个小的子问题来解决。小的子问题解决了，大问题也就解决了。

可以看成三步：

第一步：创建一个额外大集合用于存储归并结果，长度则为那两个小集合的和。

第二步：我们从左自右比较两个指针指向的值，将较小的那个存入大集合中，存入之后指针移动，并继续比较，直到某一小集合的元素全部都存到大集合中。

第三步：当某一小集合元素全部放入大集合中，则需将另一小集合中剩余的所有元素存到大集合中。

归并排序的执行效率与要排序的原始数组的有序程度无关，所以在最好，最坏，平均情况下时间复杂度均为 O(nlogn) 。归并排序的空间复杂度为 O(n).



动态规划：状态转移方程



<b>通用序列操作</b>（序列包括列表、元组、字符串、Unicode字符串、buffer对象和xrange对象）



0,1背包问题

![image-20210330183937258](C:\Users\daluzi\AppData\Roaming\Typora\typora-user-images\image-20210330183937258.png)
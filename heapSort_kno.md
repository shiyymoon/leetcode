##题目


* [力扣君微软题库215](https://leetcode-cn.top/#/home)
* [leetcode题目地址](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

##代码编写

```javascript
def heapify(tree,i,n):
  left_child = 2 * i + 1
  right_child = 2 * i + 2
  max = i
  if (left_child < n and tree[left_child] > tree[max]):
    max = left_child
  if (right_child < n and tree[right_child] > tree[max]):
    max = right_child
  if (max != i):
    swap(tree,max,i)
    heapify(tree,max,n)

def swap(tree,i,j):
  tree[i],tree[j] = tree[j],tree[i]

def buildHeap(tree):
  #最后一个子节点在数组中的的index值
  last_node = len(tree) - 1
  //建堆时：从最后一个子节点的父节点开始进行堆的调整以达到大(小)顶堆
  //最后一个子节点的父节点
  parent = (last_node - 1) // 2
  for i in range(parent,-1,-1):
    //建堆
    heapify(tree,i,len(tree))
    //print(tree)

def heapSort(tree,k):
  n = len(tree) - 1
  for i in range(n,n-k,-1):
    swap(tree,i,0)
    heapify(tree,0,i)
  return tree[len(tree)-k]


tree = [2,5,3,1,10,4]
buildHeap(tree)
print(heapSort(tree,2))

```

##代码拓展

###1.堆排序
```javascript
def
nums = [48,6,57,42,60,72,83,73,88,85]
```
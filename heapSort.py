#大顶堆
def heapify(tree,n,i):
  left_child = 2 * i + 1
  right_child = 2 * i + 2
  max = i
  if (left_child < n and tree[left_child] > tree[max]):
    max = left_child
  if (right_child < n and tree[right_child] > tree[max]):
    max = right_child
  if (max != i):
    swap(tree,max,i)

def swap(tree,i,j):
  tree[i],tree[j] = tree[j],tree[i]

def build_heap(tree):
  last_node = len(tree) - 1
  parent = (last_node - 1) // 2
  for i in range(parent,-1,-1):
    heapify(tree,last_node ,i)

def heapSort(tree):
  n = len(tree) - 1
  for i in range(n,-1,-1):
    swap(tree,i,0)
    heapify(tree,i,0)


tree = [2,5,3,1,10,4]
heapSort(tree)
print(tree)
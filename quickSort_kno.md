##题目


* [力扣君微软题库215](https://leetcode-cn.top/#/home)
* [leetcode题目地址](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

##代码编写

```javascript
def findKthLargest(nums,k):
  if k > len(nums):
    return 
  left = 0
  right = len(nums) - 1
  target = len(nums) - k
  while True:
    pivot = partition(nums,left,right)
    //如果当前值的index等于要找的目标值的index，直接输出
    if pivot == target:
      return nums[pivot]
    //如果当前值的index大于要找的目标值的index,左边继续寻找
    elif pivot > target:
      right = pivot -1
    //右边寻找
    else:
      left = pivot + 1

/*
 * 快速排序思想
 * 返回该轮排序一分为二的index值
*/
def partition(nums,left,right):
  if left >= right:
    return
  i = left
  j = right
  temp = nums[left]
  while (i < j):
    while (i < j and nums[j] >= temp):
      j = j - 1
    nums[i] = nums[j]
    while (i < j and nums[i] < temp):
      i = i + 1
    nums[j] = nums[i]
  nums[i] = temp
  return i

nums = [48,6,57,42,60,72,83,73,88,85]
k = 3
result = findKthLargest(nums,k)
print(result)
```

##代码拓展

###1.快速排序
```javascript
def quickSort(nums,left,right):
  if left >= right:
    return
  i = left
  j = right
  temp = nums[left]
  while (i < j):
    while (i < j and nums[j] >= temp):
      j = j - 1
    nums[i] = nums[j]
    while(i < j and nums[i] < temp):
      i = i + 1
    nums[j] = nums[i]
  nums[i] = temp
  quickSort(nums,left,i-1)
  quickSort(nums,i+1,right)
nums = [48,6,57,42,60,72,83,73,88,85]
left = 0
right = len(nums)-1
quickSort(nums,left,right)
print(nums)
```
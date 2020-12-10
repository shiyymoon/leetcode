# 快速排序思想
def findKthLargest(nums,k):
  if k > len(nums):
    return 
  left = 0
  right = len(nums) - 1
  target = len(nums) - k
  while True:
    pivot = partition(nums,left,right)
    if pivot == target:
      return nums[pivot]
    elif pivot > target:
      right = pivot -1
    else:
      left = pivot + 1
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


"""
#快速排序
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
"""
#堆排序
def heapSort():

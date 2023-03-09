# Weekly Assignment 2: Git Basics
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if target == nums[i]+nums[j]:
        return [i,j]

# Output
# nums = [3, 2, 4]
# target = 6
# print(twoSum(nums, target))
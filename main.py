# Weekly Assignment 2: Git Basics
from typing import List
class Sum:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if target == nums[i]+nums[j]:
          return [i,j]

#Example 2: 
nums = [3, 2, 4]
target = 6
soln1 = Sum()
print(soln1.twoSum(nums, target))
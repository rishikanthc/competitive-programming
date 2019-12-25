"""
303. Range Sum Query - Immutable
Easy

Example:
Given nums = [-2, 0, 3, -5, 2, -1]


sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

class NumArray:

    def __init__(self, nums):
        self.arr = nums
        self.cache = [0] * len(nums)
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            self.cache[i] = temp

    def sumRange(self, i, j):
        if i == 0:
            return self.cache[j]
        return self.cache[j] - self.cache[i-1]
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    solver = NumArray([-2,0,3,-5,2,-1])
    assert solver.sumRange(0, 2) == 1
    assert solver.sumRange(2, 5) == -1
    assert solver.sumRange(0, 5) == -3

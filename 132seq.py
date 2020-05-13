class Solution(object):
def find132pattern(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 3:
        return False

    stack = []
    X = {}
    X[0] = nums[0]

    for i in range(1, len(nums)):
        X[i] = min(X[i - 1], nums[i])

    for j in range(len(nums) - 1, -1, -1):
        if nums[j] > X[j]:
            while stack and stack[-1] <= X[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])

    return False

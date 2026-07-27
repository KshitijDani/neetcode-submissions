class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums)==1:
            return nums

        preList = [1]
        postList = [1]
        final = []

        for i in range(1, len(nums)):
            preList.append(preList[i-1]*nums[i-1])

        for i in range(len(nums)-2, -1, -1):
            postList.append(nums[i+1] * postList[-1])

        postList.reverse()

        for i in range(len(nums)):
            final.append(preList[i] * postList[i])
        return final
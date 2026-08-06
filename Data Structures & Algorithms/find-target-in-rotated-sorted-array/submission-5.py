class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res=nums[0]
        cut = 0
        l=0
        r=len(nums)-1

        # first find the index of the cut
        while l<r:
            mid = (l+r)//2
            print("mid is", mid)
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid

        print("cut is:", l)
        cut = l
        # then use the cut to determine whether the target is in the left or right sorted arrays

        l = 0
        r = len(nums)-1
        if nums[cut]<=target and target <=nums[r]:
            l=cut
        else:
            r=cut-1

        # do binary search in the relevant sorted array
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1

        return -1
        
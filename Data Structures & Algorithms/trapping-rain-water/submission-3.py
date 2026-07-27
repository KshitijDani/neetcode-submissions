class Solution:
    def trap(self, height: List[int]) -> int:

        l=0
        r=len(height)-1

        leftMax=height[0]
        rightMax=height[-1]

        maxArea=0
        
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                maxArea += leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax, height[r])
                maxArea += rightMax-height[r]

        return maxArea
    
            

        
class Solution:
    def trap(self, height: List[int]) -> int:

        l=0
        maxHeight = 0
        prefixHeights = []

        while l<len(height):
            maxHeight=max(maxHeight, height[l])
            prefixHeights.append(maxHeight)
            l+=1
        
        r=len(height)-1
        maxHeight = 0
        suffixHeights = []

        while r>=0:
            maxHeight=max(maxHeight, height[r])
            suffixHeights.append(maxHeight)
            r-=1

        # Align suffix values with the original indices
        suffixHeights.reverse()


        maxArea = 0
        for i in range(len(height)):
            maxArea += min(prefixHeights[i], suffixHeights[i]) - height[i]

        return maxArea
    
            

        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u,d=0,len(matrix)-1

        while u<=d:
            vertMid = u + (d-u)//2
            
            if matrix[vertMid][0] <= target and target <= matrix[vertMid][len(matrix[vertMid])-1]:
                # do binary search here
                l, r = 0, len(matrix[vertMid])-1
                while l<=r:
                    horMid = l + (r-l)//2
                    if matrix[vertMid][horMid] == target:
                        return True
                    elif matrix[vertMid][horMid] < target:
                        l = horMid + 1
                    else:
                        r= horMid - 1

                return False

            elif target < matrix[vertMid][0]:
                d = vertMid-1
            else:
                u = vertMid+1

        return False
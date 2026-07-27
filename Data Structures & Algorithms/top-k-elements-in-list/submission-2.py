class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for num in nums:
            freq[num] = freq.get(num, 0) +1

        sorted_desc = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        return [num for num,frequency in sorted_desc[:k]]
    
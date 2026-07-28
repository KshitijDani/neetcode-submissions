class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if i>0:
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    # essentially stack[-1] is the stack.top() and the latest high temperature's index
                    # so if we do i - stack[-1], we'll get to know the total distance in days between the highest temperature after stack[-1]
                    days[stack[-1]] = i - stack[-1]
                    stack.pop()
            # we can't push just the temperature because then we won't know what index that temp appeared at
            # so instead push the index where that temperature appeared
            stack.append(i)
        return days

        
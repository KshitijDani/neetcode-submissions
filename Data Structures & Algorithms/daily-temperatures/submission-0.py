class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if i>0:
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    print("temp:", temperatures[i])
                    print(i - stack[-1])
                    days[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)
        return days

        
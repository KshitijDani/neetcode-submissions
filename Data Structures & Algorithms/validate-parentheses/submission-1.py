class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch is '(' or ch is '{' or ch is '[':
                stack.append(ch)

            if ch is ')' or ch is '}' or ch is ']':
                if len(stack)==0:
                    return False 

                if ch is ')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False

                if ch is '}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False

                if ch is ']':
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
        
        return len(stack)==0
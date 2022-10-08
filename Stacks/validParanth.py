#Python program to implement valid paranthesis

def isValid(string):
    stack = []
    closeToOpen = {')':'(','}':'{',']':'['}
    for c in string:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

print(isValid("()[]{}"))
#Python program to implement generate Paranthesis

def generateParanthesis(n):
    #n is the total number of pair of paranthesis we can have
    #only add open paranthesis if open < n
    #only add a closing paranthesis if closed < open
    #valid set of paranthesis IIF open == closed == n

    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    
    backtrack(0,0)
    return res

print(generateParanthesis(3))
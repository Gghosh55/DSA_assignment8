def isValid(s):
    stack = []
    star_count = 0

    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif stack and stack[-1] == '*':
                stack.pop()
                star_count += 1
            else:
                return False

    while stack and star_count > 0:
        if stack[-1] == '(':
            stack.pop()
            star_count -= 1
        else:
            stack.pop()

    return len(stack) == 0

s = "0"
print(isValid(s))


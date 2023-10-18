def check_brackets(str):
    stack = []
    for char in str:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if len(stack) == 0:
                return "WRONG"
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return "WRONG"
    
    if len(stack) == 0:
        return "CORRECT"
    else:
        return "WRONG"

input_str = input()

print(check_brackets(input_str))
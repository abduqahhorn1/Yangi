def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack


input_str = "()"
output1 = is_valid(input_str)
input_str = "()[]{}"
output2 = is_valid(input_str)
input_str = "(]"
output3 = is_valid(input_str)
print(output1,output2,output3)  

def is_palindrome(x):
    if x < 0:
        return False
    reversed_x = int(str(x)[::-1])
    return x == reversed_x

input_num = 121
output1 = is_palindrome(input_num)
input_num = -121
output2 = is_palindrome(input_num)
input_num = 10
output3 = is_palindrome(input_num)
print(output1,output2,output3)


import sys
import math

args = sys.argv

file1 = args[1]
nums = []

try:
    with open(file1, 'r') as file1:
        for line in file1:
            nums.append(int(line.strip()))

except FileNotFoundError as e:
    Exception
except Exception as e:
    Exception


ans = 0
key_value = round(sum(nums)/ len(nums))
for num in nums:
    if num < key_value:
        ans += key_value - num
    elif num > key_value:
        ans += num - key_value
print(ans)
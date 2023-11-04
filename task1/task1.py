import sys

args = sys.argv

n = int(args[1])
m = int(args[2])
x = 2
ans = [1]
temp = [0]

while temp[-1] != 1:
    temp.clear()
    temp.append(x-1)
    for i in range(m-1):
        if x > n:
            x = 1
        temp.append(x)
        x += 1
    ans.append(x-1)
    
ans.pop()
result_string = ''.join(map(str, ans))
print(result_string)


        

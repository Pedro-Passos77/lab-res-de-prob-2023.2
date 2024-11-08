a = list(map(int, input().split()))
nums = sorted(list(map(int, input().split())))
n, i, f = a[0], a[1], a[2]

cont = 0
while nums:
    yi, yf = i - nums[0], f - nums[0]
    ys = nums[1:]
    c = len(list(filter(lambda x: x >= yi and x <= yf, ys)))
    cont += c
    nums = ys

print(cont)


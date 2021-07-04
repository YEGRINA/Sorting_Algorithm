sum = 0


def hap(num):
    global sum
    for i in range(num+1):
        sum += i


n = int(input('입력 숫자? '))
hap(n)
print('{}에 대한 합={}'.format(n, sum))

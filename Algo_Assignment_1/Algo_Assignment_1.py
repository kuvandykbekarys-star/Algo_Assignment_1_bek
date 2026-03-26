def task1(n):
    if n == 1: return 1
    return n**2 + task1(n - 1)

def task2(arr, n):
    if n == 0: return 0
    return arr[n-1] + task2(arr, n-1)

def task3(n):
    if n == 1: return 1
    return n + task3(n - 1)

def task4(b, n):
    if n == 0: return 1
    return b**n + task4(b, n-1)

def task5(n):
    if n > 0:
        val = input()
        task5(n - 1)
        print(val, end="")

def task6(n):
    if n > 0:
        s = input()
        task6(n - 1)
        print(s)

def fill_spiral(mat, x, y, num, size):
    if size <= 0: return
    if size == 1:
        mat[x][y] = num
        return
    for i in range(size):
        mat[x][y + i] = num
        num += 1
    for i in range(1, size):
        mat[x + i][y + size - 1] = num
        num += 1
    for i in range(1, size):
        mat[x + size - 1][y + size - 1 - i] = num
        num += 1
    for i in range(1, size - 1):
        mat[x + size - 1 - i][y] = num
        num += 1
    fill_spiral(mat, x + 1, y + 1, num, size - 2)

def task8(n, k, current=""):
    if n == 0:
        print(current)
        return
    for i in range(1, k + 1):
        task8(n - 1, k, current + str(i))

def task9(s, res=""):
    if len(s) == 0:
        print(res)
        return
    for i in range(len(s)):
        task9(s[:i] + s[i+1:], res + s[i])

def isPowerOfTwo(n):
    if n <= 0: return False
    if n == 1: return True
    return False if n % 2 != 0 else isPowerOfTwo(n // 2)

if __name__ == "__main__":
   
    for i in [1, 2, 3, 4, 8, 16, 32]:
        status = "is a power of two" if isPowerOfTwo(i) else "is not a power of two"
        print(f"{i} {status}")
N, M = [int(x) for x in input().split()]

grid = []

for n in range(N):
    line = [*input()]
    for m in range(M):
        if line[m] == 'X':
            grid.append([n, m])

grid = sorted(grid)

memo = {}
def check(a, b, x):
    for n, m in grid:
        if n < a + x and n >= a and m >= b and m < b + x:
            memo[a, b, x] = False
            return False
    memo[(a, b, x)] = True
    return True

def move(a, b, x):
    if a + x > N or b + x > M:
        memo[a, b, x] = False
        return False

    if check(a, b, x) == False:
        return False

    if a + x == N and b + x == M:
        return True

    # move right
    if b + 1 < M and (a, b + 1, x) not in memo:
        r = move(a, b + 1, x)
        if r:
            return True
    # move down
    if a + 1 < N and (a + 1, b, x) not in memo:
        d = move(a + 1, b, x)
        if d:
            return True
    # move left
    if b - 1 >= 0 and (a, b - 1, x) not in memo:
        l = move(a, b - 1, x)
        if l:
            return True
    # move up
    if a - 1 >= 0 and (a - 1, b, x) not in memo:
        r = move(a - 1, b, x)
        if r:
            return True

    return False

x = min(N, M)
while x > 0:
    if move(0, 0, x):
        print(x)
        import sys
        sys.exit(0)
    else:
        x -= 1
print(0)
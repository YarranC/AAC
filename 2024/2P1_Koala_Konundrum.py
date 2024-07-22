N = int(input())
S = input()

letter = dict()

for i in range(N):
    if S[i] not in letter:
        letter[S[i]] = 1
    else:
        letter[S[i]] += 1

count = [0, 0]
for l in letter:
    a = int(letter[l]/2)
    b = letter[l]%2
    count[0]+=a
    count[1]+=b

print(max(1, count[1]))
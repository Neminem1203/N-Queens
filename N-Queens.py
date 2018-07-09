
i = 0
n = int(input("N: "))
pos = [-1 for x in range(n)]
possible = True
if(n < 4):
    print("N can't be less than 4")
else:
    while(i < n):
        if pos[i] == n:
            #backtrack
            i -= 1
            pos[i] += 1
            pos[i+1] = -1
        elif pos[i] == -1:
            pos[i] = 0
        else:
            for j in range(i-1, -1, -1):
                if(pos[i] == pos[j] or pos[i] == pos[j] + (i-j) or pos[i] == pos[j] - (i-j)):
                    #testing if possible
                    possible = False
            if possible:
                i += 1
            else:
                pos[i] += 1
            possible = True

print(pos)

for j in pos:
    print((j)*'x'+'o'+(n-j)*'x')
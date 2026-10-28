n = int(input())

win = 0
runnerup = 0

for i in range(n):
    dist = int(input())

    if dist > win:
        runnerup = win
        win = dist
    elif dist > runnerup and dist != win:
        runnerup = dist

print(win)
print(runnerup)

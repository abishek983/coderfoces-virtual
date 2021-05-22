# https://codeforces.com/contest/1527/problem/B1

def findWinner(n):
    if(n==1 or not(n&1)):
        print("BOB")
    elif(n&1):
        print("ALICE")
    else:
        print("DRAW")

for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for x in s:
        if(x=='0'):
            count +=1
    findWinner(count)
# https://codeforces.com/contest/1527/problem/A

def findValuek(n):
    val = 1
    while(val<=n):
        val *= 2
    print(int((val/2)-1)) 

for _ in range(int(input())):
    n = int(input())
    findValuek(n)
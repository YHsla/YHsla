#https://www.acmicpc.net/problem/1010

# 수학적 접근
def dp1(m,n):
    i, j = m, n
    temp1, temp2 = 1, 1
    while i > (m-n):
        temp1 = temp1*i
        i-=1
    while j > 0:
        temp2 = temp2*j
        j-=1

    return print(temp1//temp2)

def solve():
    T = int(input())
    for _ in range(T):
        N,M = map(int, input().split())
        dp1(M,N)
    return 


if __name__ == "__main__":
    solve()
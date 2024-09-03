#11047
#동전 개수의 최소값

n, k = map(int, input().split())
coins = []
cnt = 0

#동전 종류 추가
for i in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

for coin in coins:
    if k == 0:
        break
    elif coin <= k:
        cnt += (k // coin) #가진 돈에서 동전 크기를 나눠 몫 구함 => 개수
        k %= coin #나머지를 k에 저장하고 반복
        
print(cnt)
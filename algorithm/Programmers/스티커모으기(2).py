def find_max(arr,n):
    dp = [0] * (n - 1)
    dp[0] = arr[0]
    dp[1] = arr[1]
    dp[2] = arr[0] + arr[2]
    for i in range(3, n - 1):
        res1 = arr[i] + dp[i - 2]
        res2 = arr[i] + dp[i - 3]
        dp[i] = max(res1, res2)
    return max(dp)

def solution(sticker):
    n = len(sticker)
    if n >= 4:
        answer = max(find_max(sticker[:n-1],n),find_max(sticker[1:], n))
    else:
        answer = max(sticker)
    return answer

sticker = [14,6,2]
print(solution(sticker))
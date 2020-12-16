def numDecodings(self, s):
    dp = [0 for i in range(len(s)+1)]
    dp[0] = 1
    if s[0] != '0':
        dp[1] = 1
    else:
        return 0
    for i in range(2,len(s)+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        else:
            dp[i] = 0
        if 10<=int(s[i-2]+s[i-1])<=26:
            dp[i] += dp[i-2]
        else:
            dp[i] += 0
    return dp[-1]
    
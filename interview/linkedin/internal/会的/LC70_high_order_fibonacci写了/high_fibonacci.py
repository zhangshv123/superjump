时间复杂度：O(N*k)
def numWaysOfClimbing(N,K):
	dp = [0 for i in range(N+1)]
	dp[0]= 1
	for i in range(1,N+1):
		for j in range(1,min(K+1,i+1)):
			dp[i] += dp[i-j]
	return dp[N]

print numWaysOfClimbing(5, 2)
#follow-up
S[N] = S[N-1] + ....+S[N-K]
S[N-1] = S[N-2]+ ...+S[N-K-1]
所以
S[N] - S[N-1] = S[N-1] - S[N-K-1]
推出
S[N] = 2*S[N-1] - S[N-K-1]
def numWaysOfClimbing(N,K):
	dp = [0 for i in range(N+1)]
	dp[0]= 1
	dp[1] = 1
	for i in range(2,N+1):
		if i-k-1>=0:
			dp[i] = 2*dp[i-1] - dp[i - k -1]
		else:
			dp[i] = 2*dp[i-1]
	return dp[N]
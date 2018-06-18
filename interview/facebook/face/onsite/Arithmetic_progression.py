# 1， 3， 2， 5，7，4，10。   答案是4， （1，3，5，7）。  用DP 就行。
"""
int longestArithmeticArray(vector<int>& a) {
    if (a.size() < 3) return a.size();
    
    int maxLen = 0;
    vector<unordered_map<int, int>> dp(a.size());. 1point 3acres 璁哄潧
    for (int i = 1; i < a.size(); ++i)
        for (int j = 0; j < i; ++j) {
            int d = a[i] - a[j];. Waral 鍗氬鏈夋洿澶氭枃绔�,
            dp[i][d] = max(dp[i][d], dp[j][d]+1);. more info on 1point3acres.com
            maxLen = max(maxLen, dp[i][d]);
        }
    return maxLen + 1;
}

"""
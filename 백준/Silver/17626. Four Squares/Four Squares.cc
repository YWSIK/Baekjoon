//17626
#include <iostream>
#include <algorithm>

using namespace std;
int dp[50001];

int main() {
		ios::sync_with_stdio(false);
		cin.tie(NULL);

		int n; cin >> n;

		for (int i = 1; i * i <= n; i++) {
			dp[i * i] = 1;
		} //제곱수

		for (int i = 1; i <= n; i++) {
			if (dp[i] != 0)
				continue;
			dp[i] = i;
			for (int j = 1; j * j <= i; j++) {
				dp[i] = min(dp[i], 1 + dp[i - j * j]);
			}
		}
		cout << dp[n];
		return 0;
}
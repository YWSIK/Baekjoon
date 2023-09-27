//1010
#include <iostream>

using namespace std;
int dp[31][31];

int main() {
	int t; cin >> t;

	for (int i = 0; i < 31; i++) {
		dp[i][0] = 1;
		dp[i][i] = 1;

		for (int j = 1; j < i; j++) {
			dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
		}
	}

	while (t--) {
		int n, m; cin >> n >> m;
		cout << dp[m][n] << '\n';
	}
}
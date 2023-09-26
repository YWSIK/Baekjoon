#include <iostream>

using namespace std;

int main() {

	long long dp[99];

	int n;
	cin >> n;

	dp[1] = 1;

	for (int i = 2; i <= 90; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}

	cout << dp[n];
}
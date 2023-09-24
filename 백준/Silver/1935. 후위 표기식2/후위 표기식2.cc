//1935
#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	cout << fixed;
	cout.precision(2); //소수점 자리수 변경

	int n;
	string str;
	int arr[26] = { 0, };

	cin >> n >> str;

	stack<double> op;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '+' || str[i] == '-' || str[i] == '*' || str[i] == '/') {
			double y = op.top();
			op.pop();

			double x = op.top();
			op.pop();

			double result;

			switch (str[i]) {
			case '+':
				result = x + y;
				break;
			case '-':
				result = x - y;
				break;
			case '*':
				result = x * y;
				break;
			case '/':
				result = x / y;
				break;
			}
			op.push(result);
		}
		else {
			op.push(arr[str[i] - 'A']);
		}
	}
	cout << op.top() << '\n';
}
//10828

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	int n, num;
	int result = 0;
	cin >> n;

	stack<int> s;
	string cmd;

	for (int i = 0; i < n; ++i) {
		cin >> cmd;

		if (cmd == "push") {
			cin >> num;
			s.push(num);
		}

		else if (cmd == "pop") {
			if (s.size() == 0) {
				result = -1;
				cout << result << endl;
			}
			else {
				result = s.top();
				cout << result << endl;
				s.pop();
			}
		}

		else if (cmd == "size") {
			cout << s.size() << endl;
		}

		else if (cmd == "empty") {
			if (s.size() == 0) {
				result = 1;
				cout << result << endl;
			}
			else {
				result = 0;
				cout << result << endl;
			}
		}

		else if (cmd == "top") {
			if (s.size() == 0) {
				result = -1;
				cout << result << endl;
			}
			else {
				result = s.top();
				cout << result << endl;
			}
		}
	}
}
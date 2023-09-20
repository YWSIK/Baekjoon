//18258
#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, num, result = 0;
	cin >> n;

	queue<int> q;
	string cmd;

	for (int i = 0; i < n; i++) {
		cin >> cmd;

		//push : 큐에 삽입
		if (cmd == "push") {
			cin >> num;
			q.push(num);
		}
		 

		//pop : 큐에서 가장 앞을 빼고 출력, 들어있는게 없으면 -1
		if (cmd == "pop") {
			if (q.size() == 0) {
				result = -1;
				cout << result << "\n";
			}
			else {
				result = q.front();
				cout << result << "\n";
				q.pop();
			}
		}
		 

		//size : 큐에 있는 정수 개수
		if (cmd == "size") {
			cout << q.size() << "\n";
		}
		 
		
		//empty : 큐가 비어있으면 1, 아니면 0
		if (cmd == "empty") {
			if (q.size() == 0) {
				result = 1;
				cout << result << "\n";
			}
			else {
				result = 0;
				cout << result << "\n";
			}
		}
		 
		 
		//front : 가장 앞 정수 출력 없으면 -1
		if (cmd == "front") {
			if (q.size() == 0) {
				result = -1;
				cout << result << "\n";
			}
			else {
				cout << q.front() << "\n";
			}
		}
		 
		
		//back : 가장 뒤 정수 출력 없으면 -1
		if (cmd == "back") {
			if (q.size() == 0) {
				result = -1;
				cout << result << "\n";
			}
			else {
				cout << q.back() << "\n";
			}
		}
	}
}
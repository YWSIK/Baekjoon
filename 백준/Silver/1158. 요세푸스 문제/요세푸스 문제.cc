//1158
#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
	int n, k;
	cin >> n >> k;

	queue<int> q;

	for (int i = 1; i <= n; i++) { 
		q.push(i); //1부터 n까지 큐에 push
	}
	cout << "<";

	while (true) {
		for (int i = 1; i < k; i++) { //3번째 값 전까지 pop 진행
			q.push(q.front());
			q.pop(); //넣어주고 빼면서 기존 값 유지
		}
		cout << q.front();
		q.pop();

		if (!q.empty()) {
			cout << ", ";
		}
		else
			break;
	}	
	cout << ">";
}

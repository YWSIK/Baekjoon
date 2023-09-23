//2164
#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
	int n;
	cin >> n;

	queue<int> q;

	for (int i = 1; i <= n; i++) {
		q.push(i);
	}

	while (q.size() > 1){
		q.pop();
		q.push(q.front()); //맨 앞 뒤에 넣어주고
		q.pop(); //맨 앞 빼줌
	}

	cout << q.front();
 }
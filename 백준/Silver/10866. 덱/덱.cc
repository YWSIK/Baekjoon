//10866
#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {

		ios::sync_with_stdio(false); //c의 stdio와 c++의 iostream을 동기화를 비활성 -> c++ 독립적인 버퍼
		cin.tie(NULL); //cin 과 cout의 묶음을 풀어줌
	
		int n, num, result = 0;
		cin >> n;
	
		deque<int> dq;
		string cmd;
	
		for (int i = 0; i < n; i++) {
			cin >> cmd;
	
			//push_front
			if (cmd == "push_front") {
				cin >> num;
				dq.push_front(num);
			}

			else if (cmd == "push_back") {
				cin >> num;
				dq.push_back(num);
			}
			 
	
			//pop_front
			else if (cmd == "pop_front") {
				if (dq.size() == 0) {
					result = -1;
					cout << result << "\n"; //endl 에는 버퍼를 비워주는 기능, "\n"은 비우지않고 그냥 줄바꿈
				}
				else {
					result = dq.front();
					cout << result << "\n";
					dq.pop_front();
				}
			}

			//pop_back
			else if (cmd == "pop_back") {
				if (dq.size() == 0) {
					result = -1;
					cout << result << "\n"; //endl 에는 버퍼를 비워주는 기능, "\n"은 비우지않고 그냥 줄바꿈
				}
				else {
					result = dq.back();
					cout << result << "\n";
					dq.pop_back();
				}
			}
			 
	
			//size : 큐에 있는 정수 개수
			else if (cmd == "size") {
				cout << dq.size() << "\n";
			}
			 
			
			//empty : 큐가 비어있으면 1, 아니면 0
			else if (cmd == "empty") {
				if (dq.size() == 0) {
					result = 1;
					cout << result << "\n";
				}
				else {
					result = 0;
					cout << result << "\n";
				}
			}
			 
			 
			//front : 가장 앞 정수 출력 없으면 -1
			else if (cmd == "front") {
				if (dq.size() == 0) {
					result = -1;
					cout << result << "\n";
				}
				else {
					cout << dq.front() << "\n";
				}
			}
			 
			
			//back : 가장 뒤 정수 출력 없으면 -1
			else if (cmd == "back") {
				if (dq.size() == 0) {
					result = -1;
					cout << result << "\n";
				}
				else {
					cout << dq.back() << "\n";
				}
			}
		}
	}
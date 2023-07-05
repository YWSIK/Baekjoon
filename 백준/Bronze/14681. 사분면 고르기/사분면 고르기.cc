//14681

#include <iostream>
using namespace std;

int main() {
	int x, y;
	cin >> x >> y; //입력받기

	if (x > 0)
		if (y > 0)
			cout << 1; //출력
		else
			cout << 4;
	else
		if (y > 0)
			cout << 2;
		else
			cout << 3;
}
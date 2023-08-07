//2525

#include <iostream>
using namespace std;

int main() {
	int h, m, A;
	cin >> h >> m;
	cin >> A;

	if (m + A < 60) {
		m += A;
	}
	else {
		h = (h + ((m + A) / 60)) % 24;
		m = (m + A) % 60;
	}

	cout << h << " " << m;
}
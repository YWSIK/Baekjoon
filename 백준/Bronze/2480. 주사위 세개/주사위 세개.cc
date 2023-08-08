//2480

#include <iostream>
using namespace std;

int main() {
    int a, b, c, result;
    cin >> a >> b >> c;

    if (a == b && b == c) {
        result = 10000 + a * 1000;
    }

    else if (a == b && a != c) {
        result = 1000 + a * 100;
    }

    else if (a == c && a != b) {
        result = 1000 + a * 100;
    }

    else if (b == c && b != a) {
        result = 1000 + b * 100;
    }

    else if (a != b && b != c && a != c) {
        if (a >= b && a >= c) {
            result = 100 * a;
        }

        else if (b >= a && b >= c) {
            result = 100 * b;
        }

        else if (c >= a && c >= b) {
            result = 100 * c;
        }
    }

    cout << result;
}

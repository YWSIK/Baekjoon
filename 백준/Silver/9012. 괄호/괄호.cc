//9012
// 괄호 검사(VPS)

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;

    while (n > 0) {
        n--;

        string str;
        cin >> str;

        stack<char> s;
        string ans = "YES";

        for (int i = 0; i < (int)str.size(); i++) {
            if (str[i] == '(') {
                s.push(str[i]);
            }
            else if (!s.empty() && str[i] == ')' && s.top() == '('){
                s.pop();
                }
            else {
                ans = "NO";
                break;
            }
        }

        if (!s.empty())
            ans = "NO";

        cout << ans << endl;
    }

    return 0;
}
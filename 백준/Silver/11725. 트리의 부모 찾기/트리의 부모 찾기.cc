//11725
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> a(100005);
int parent[100005];

void dfs(int x) {
    for (int i = 0; i < a[x].size(); i++) {
        int y = a[x][i];
        if (parent[y] == 0) {
            parent[y] = x;
            dfs(y);
        }
    }
}

int main() {
    int n; cin >> n;

    for (int i = 0; i < n-1; i++) {
        int u, v;
        cin >> u >> v;

        a[u].push_back(v);
        a[v].push_back(u);
    }

    parent[1] = 1;
    dfs(1);

    for (int i = 2; i <= n; i++) {
        cout << parent[i] << "\n";
    }
    
    return 0;
}
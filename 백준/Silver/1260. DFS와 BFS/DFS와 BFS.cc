//1260
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<int>> a;
vector<bool> visited;

void dfs(int x) {
    visited[x] = true;
    cout << x << " ";

    for (int i = 0; i < a[x].size(); i++) {
        int k = a[x][i];
        if (!visited[k]) {
            dfs(k);
        }
    }
}

void bfs(int start) {
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int x = q.front();
        q.pop();
        cout << x << " ";

        for (int i = 0; i < a[x].size(); i++) {
            int k = a[x][i];
            if (!visited[k]) {
                visited[k] = true;
                q.push(k);
            }
        }
    }
}

int main() {
    int n, m, start;
    cin >> n >> m >> start; // n: node, m: edge, start: 시작 노드

    a.resize(n + 1); // 노드 번호가 1부터 시작하므로 n+1 크기의 벡터 초기화
    visited.resize(n + 1, false); // 방문 여부 배열 초기화

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;

        a[u].push_back(v);
        a[v].push_back(u);
    }

    for (int i = 1; i <= n; i++) {
        sort(a[i].begin(), a[i].end()); // 방문할 노드 순서대로 정렬
    }

    dfs(start);
    cout << endl;

    fill(visited.begin(), visited.end(), false); //방문 다시 초기화
    bfs(start);
    cout << endl;

    return 0;
}

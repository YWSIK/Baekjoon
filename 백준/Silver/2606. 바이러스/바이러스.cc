//2606
#include <iostream>
#include <vector>

using namespace std;

vector<int> a[101];
int virus[101];
int cnt = 0;

void dfs(int x) {
	for (int i = 0; i < a[x].size(); i++) { //현재 노드와 연결된 모든 이웃 노드 탐색
		int k = a[x][i]; //이웃노드

		if (virus[k] == 0) { //이웃노드가 no감염
			virus[k] = 1; //감염
			cnt++;
			dfs(k);
		}
	}
}

int main() {
	int n, m; cin >> n >> m; //n:node, m:edge

	for (int i = 0; i < m; i++) { //edge 추가
		int u, v; cin >> u >> v;

		a[u].push_back(v);
		a[v].push_back(u);
	}

	virus[1] = 1;
	dfs(1);

	cout << cnt;
}
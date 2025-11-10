#include <iostream>
using namespace std;

int T, E, N;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	while (T--) {
		cin >> E >> N;
		int cnt = 0;
		while (N--) {
			int x; cin >> x;
			if (x > E) cnt++;
		}

		cout << cnt << '\n';
	}
}

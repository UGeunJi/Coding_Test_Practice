#include <iostream>
using namespace std;

int cnt[128];
char c;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	while (cin >> c) cnt[c]++;

	cout << cnt['B'] / 2 + cnt['C'] / 2;
}

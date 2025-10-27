#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;

  vector<char> people(n);
  for (int i = 0; i < n; i++)
    cin >> people[i];

  int position = 1;
  for (int i = 1; i < n; i++) {
    if (people[i] != people[i - 1])
      position++;
  }

  cout << position + 1 << "\n";

  return 0;
}

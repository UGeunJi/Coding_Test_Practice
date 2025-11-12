#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;
  size_t len = 1;
  for (int i = 0; i < n; i++) {
    string word; cin>> word;
    char decodedC;
    if (word.size() < len) decodedC = ' ';
    else decodedC = word[len - 1];
    len = word.size();

    cout << decodedC;
  }
  cout << "\n";

  return 0;
}

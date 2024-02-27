#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  while (true) {
    int n, w, d, totalWeight;
    cin >> n >> w >> d >> totalWeight;
    if (cin.eof()) break ;

    int standardWeight = w * ((n - 1) * n) / 2;
    int numBasket = (standardWeight - totalWeight) / d;

    if (numBasket == 0) cout << n << "\n";
    else cout << numBasket << "\n";
  }

  return 0;
}

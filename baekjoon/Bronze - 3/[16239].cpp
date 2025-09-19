#include <iostream>
using namespace std;

int main() {
  int K, N;
  cin >> K >> N;

  for (int i = 1; i < N; i++) {
    cout << i << "\n";
    K -= i;
  }
  cout << K;

  return 0;
}

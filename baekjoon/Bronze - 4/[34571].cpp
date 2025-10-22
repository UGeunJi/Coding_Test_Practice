#include <bits/stdc++.h>

using namespace std;

int main() {
    int n,ans=0;
    string s,comp="ABBDOPQRabdegopq@";
    getline(cin, s);
    for (char &c : s) {
        ans += count(comp.begin(),comp.end(),c);
    }
    cout << ans << '\n';
    return 0;
}

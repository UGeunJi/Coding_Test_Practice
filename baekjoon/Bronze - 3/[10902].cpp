#include <iostream>
#define ll long long
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ll N, i, t, s, f = 0, mx = 0, tf = 0, sf = 0;

    cin >> N;
    for (i = 1; i <= N; i++)
    {
        cin >> t >> s;
        if (s > mx)
        {
            mx = s;
            f = i;
            tf = t;
            sf = s;
        }
    }
    if (sf == 0) cout << 0;
    else cout << tf + (f - 1) * 20;
}

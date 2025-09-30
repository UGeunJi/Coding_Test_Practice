#include <iostream>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int a, b, c, d, i, N, cnt = 0;

    cin >> N;
    for (i = 0; i < N; i++)
    {
        cin >> c >> d;
        if (i > 0)
        {
            if (a == c && a != 0) cnt++;
            if (b == d && b != 0) cnt++;
        }
        if (c == d && c != 0) cnt++;
        a = c; b = d;
    }

    cout << cnt;
}

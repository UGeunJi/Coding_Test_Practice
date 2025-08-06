#include <iostream>
using namespace std;
int X;
int main()
{
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> X;

    for (int i = X + 1; i <= 9999; ++i)
    {
        int a = i / 100;
        int b = i % 100;

        int sum = a + b;

        if (sum * sum == i)
        {
            cout << i;
            return 0;
        }
    }

    cout << -1;
    return 0;
}

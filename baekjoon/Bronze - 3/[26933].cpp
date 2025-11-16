#include <stdio.h>

int main(void) 
{
	int N, H, B, K;
  int S = 0;
  int M = 0;
  int P[5] = { 0 };
  scanf("%d", &N);
  for (int i = 0; i < N; i++)
  {
    scanf("%d %d %d", &H, &B, &K);
    M = B - H;
    if (M < 0)
    {
      M = 0;
    }else{
      P[i] = M * K;
    }
    S += P[i];
  }
  printf("%d", S); 
}

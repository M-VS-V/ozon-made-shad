#include <stdio.h>
#include <stdlib.h>

int summ(int x0, int N, int *X);

int main () {
	int x0, N;
	scanf("%d%d", &x0, &N);

	int *X;
	X = malloc(sizeof(int) * N);

	for (int i = 0; i < N; ++ i)
		scanf("%d", &X[i]);

	int sum = summ(x0, N, X);
	printf("%d\n", sum);

	free(X);

	return 0;
}


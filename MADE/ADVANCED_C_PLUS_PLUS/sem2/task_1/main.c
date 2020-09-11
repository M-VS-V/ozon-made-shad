#include <stdio.h>


int f(int a, int b, int c, int x);

int main () {
	int a, b, c, x;
	scanf("%d%d%d%d", &a, &b, &c, &x);

	int result = f(a, b, c, x);

	printf("%d\n", result);

	return 0;
}



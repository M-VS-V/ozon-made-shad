#include "stdio.h"
#include "stdlib.h"


int main (int argc, char *argv[]) {
	double x;
	int y;
	scanf("%lf %x", &x, &y);
	int z = strtol(argv[1], NULL, 27);
	printf("%.3lf\n", x + y + z);

	return 0;
}

#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"



uint32_t get_bit (int32_t x, uint8_t bit_num) {
	uint32_t mask = 1 << bit_num;
	uint32_t temp = mask & x;
	temp >>= bit_num;
	return temp;
}


int main () {
	int32_t x;

	scanf("%i", &x);

	for (uint8_t i = 0; i < 32; ++ i)
		printf("%d", get_bit(x, 31 - i));

	printf("\n");

	return 0;
}

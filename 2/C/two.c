#include <stdio.h>

int main()
{
	int fib, total = 0;
	int first = 0;
	int second = 1;

	while(1)
	{
		fib = first + second;
		first = second;
		second = fib;

		if(fib > 4000000)
		{
			break;
		}

		if(fib % 2 == 0)
		{
			total += fib;
		}

		printf("\nFib: %d\tTotal: %d", fib, total);
	}

	printf("\nTotal: %d", total);
}
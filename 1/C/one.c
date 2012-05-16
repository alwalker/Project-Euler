#include <stdio.h>

int main(int argc, char **args)
{
	int total = 0;
	int i = 0;

	for(i=0 ; i<1000 ; i++)
	{
		if(i%3 == 0 || i%5 == 0)
		{
			total += i;
		}
	}

	printf("\nAnswer: %d\n", total);
}

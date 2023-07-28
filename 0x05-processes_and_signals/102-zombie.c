#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - an infinite while
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: 0 on success
 */
int main(void)
{
	int i = 0;

	for (; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while();
	return (0);
}

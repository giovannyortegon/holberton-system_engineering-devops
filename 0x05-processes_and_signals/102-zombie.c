#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<sys/wait.h>

int infinite_while(void);
/**
 * main - main function
 * Return: Always (0) success
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid ==  0)
		{
			fprintf(stdout, "Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();

	return (0);
}
/**
 * infinite_while - infinite loop
 * Return: Always (0) Success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

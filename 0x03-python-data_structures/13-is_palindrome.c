#include "lists.h"

/**
 * is_palindrome - checks if a linked lust is a palindrome
 * @head: the head node
 * Return: 1 or 0 dependinf if the node is a palindrome or not
 */
int is_palindrome(listint_t **head)
{
	int i, j, *array;

	if ((*head) == NULL || (*head)->next == NULL)
		return (1);
	i = 0;
	array = malloc(sizeof(int) * ARR);
	if (array == NULL)
		return (0);

	while ((*head))
	{
		if (i == ARR)
			array =realloc(array, sizeof(int) * ARR);
		array[i] = (*head)->n;
		(*head) = (*head)->next;
		i++;
	}

	for (j = 0; j < i; j++, i--)
	{
		if (array[i - 1] != array[j])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}

#include "lists.h"
/**
 * is_palindrome - checks if a linked lust is a palindrome
 * @head: the head node
 * Return: 1 or 0 dependinf if the node is a palindrome or not
 */
int is_palindrome(listint_t **head)
{
	int i, j, array[1024];

	if ((*head) == NULL || (*head)->next == NULL)
		return (1);
	i = 0;
	while ((*head))
	{
		array[i] = (*head)->n;
		(*head) = (*head)->next;
		i++;
	}

	for (j = 0; j < i; j++, i--)
	{
		if (array[i - 1] != array[j])
		{
			return (0);
		}
	}
	return (1);
}

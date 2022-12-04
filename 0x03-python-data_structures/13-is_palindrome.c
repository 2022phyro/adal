#include "lists.h"
int rev(listint_t **head, int *array)
{
	int i = 0;

	while ((*head))
	{
		array[i] = (*head)->n;
		(*head) = (*head)->next;
		i++;
	}
	return (i);
}
int is_palindrome(listint_t **head)
{
	int i, j, array[1024];

	if ((*head) == NULL || (*head)->next == NULL)
		return (1);
	i = rev(head, array)

	for (j = 0; j < i; j++, i--)
	{
		if (array[i-1] != array[j])
		{
			return (0);
		}
	}
	return (1);
}

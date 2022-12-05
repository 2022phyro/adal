#include "lists.h"

/**
 * is_palindrome - checks if a linked lust is a palindrome
 * @head: the head node
 * Return: 1 or 0 dependinf if the node is a palindrome or not
 */
int is_palindrome(listint_t **head)
{
	int i, j, k =  10, l, *p;
	int array[k];
	listint_t *temp, *temp2 = (*head);

	i = 0;
	j = 0;
	p = &k;
	temp = temp2;
	if ((*head) == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		temp = temp->next;
		i++;
	}
	*p = i;
	i--;
	while (temp2)
	{
		array[j] = temp2->n;
		temp2 = temp2->next;
	}
	for (l = 0; l < i; l++, i--)
	{
		printf("%d", i);
		printf("%d--__--%d\n", array[l], array[i]);
/*		if (array[l] != array[i])
			return (0);*/
	}
	return (1);
}


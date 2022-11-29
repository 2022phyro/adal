#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newd = (listint_t *)(malloc(sizeof(listint_t))), *temp;
	if (newd == NULL || head == NULL)
		return (NULL);
	newd->n = number;
	temp = *head;
	for (;temp->next->n < number; temp = temp->next)
	{
	}
	newd->next = temp->next;
	temp->next = newd;
	return ((*head));
}

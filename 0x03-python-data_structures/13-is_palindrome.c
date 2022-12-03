#include "lists.h"
listint_t *rev(listint_t **head, int *idx) 
{ 
	listint_t *prev, *curr;  
	if ((*head) == NULL)
	{
		return (NULL);
	}
	prev = (*head);
	*idx = 1;
	(*head) = (*head)->next;
	prev->next = NULL;
	curr = (*head);
	while ((*head))
	{
		(*head) = (*head)->next;
		curr->next = prev;
		prev = curr;
		curr = (*head);
		*idx = *idx + 1;
	}
	(*head) = prev;
	return (*head);
}
int is_palindrome(listint_t **head)
{
	int ve, index, ma = 1;
	listint_t *temp, *nem, *me;

/*	if ((*head) == NULL || (*head)->next == NULL)
		return (1);*/
	ve = 0;
	nem = me = *head;

	temp = rev(head, &ve);
y	printf("%d", ve);
	index = 0;
	while (temp != NULL)
	{
		if (nem->n != temp->n)
		{
			return 0;
		}
		if (index == ve / 2)
			break;
		nem = nem->next;
		temp = temp->next;
		index++;
	}
	return ma;

}

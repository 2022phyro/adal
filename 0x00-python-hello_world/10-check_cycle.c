#include "lists.h"
/**
 * check_cycle - checks if a lis has a loop in it
 *
 * @list: the head of the list
 * Return: 1 if there is a loop or 0 if there is none
 */
int check_cycle(listint_t *list)
{
	listint_t *tort, *hare;

	if (list == NULL || list->next == NULL || list->next->next == NULL)
		return (0);
	tort = (list->next)->next;
	hare = (list->next)->next->next;
	if (hare != NULL)
		hare = hare->next;
	for (; hare && tort; hare = hare->next->next,
			tort = tort->next)
	{
		if (hare == tort)
			return (1);
	}
	return (0);

}

#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle.
 * @list: head of linked list
 *
 * Description - check for loops in list
 * Return: 1 if cycled else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *sl = list, *ft = list;

	while (sl && ft && ft->next)
	{
		sl = sl->next;
		ft = ft->next->next;
		if (sl == ft)
			return (1);
	}
	return (0);
}

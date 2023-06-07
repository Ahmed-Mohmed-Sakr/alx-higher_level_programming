#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list: list to check it.
 *
 * Return:0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *run1step;
	listint_t *run2steps;

	if (!list || !list->next)
		return (0);

	run1step = list;
	run2steps = list->next;

	while (run1step != run2steps)
	{
		if (!run2steps || !run2steps->next)
			return (0);

		run1step = run1step->next;
		run2steps = run2steps->next->next;
	}

	return (1);
}

#include "lists.h"
/**
 * check_cycle - this is a function that checks if a linked l contains a cyc
 * @lis: this is a parameter
 * Retunr: this should be 1 if there is a cyc
 */
int check_cycle(listint_t *list)
{
	listint_t *mv1nd = list;
	listint_t *mv2nd = list;

	if (!list)
		return (0);

	while (mv1nd && mv2nd && mv2nd->next)
	{
		mv1nd = mv1nd->next;
		mv2nd = mv2nd->next->next;
		if (mv1nd == mv2nd)
		{
			return (1);
		}
	}

	return (0);
}

#include "lists.h"
/**
* insert_node - this is a function
* @head: this is a parameter
* @number: this is a parameter
* Return: if fail NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *add;

	add = malloc(sizeof(listint_t));

	if (add == NULL)
	{
		return (NULL);
	}
	add->n = number;

	if (add == NULL || add->n >= number)
	{
		add->next = add;
		*head = add;
		return (add);
	}

	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}
	add->next = node->next;
	node->next = add;

	return (add);
}

#include "lists.h"

/**
 * check_cycle - checks if a linked list is a circle
 * @list: the linked list
 * Return: 1 0r 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}

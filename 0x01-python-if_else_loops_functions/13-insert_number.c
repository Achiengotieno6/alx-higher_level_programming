#include "lists.h"
/**
 * insert_node - inserts node on a linked list
 * @head: the head of a linked list
 * @number: number to be inserted on the linked list
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}

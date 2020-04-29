#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - Insert a sorted node in a linked list
 * @head: Pointer to the list
 * @number: number to add to the list
 * Return: Pointer to the new node, or NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *finder = *head, *new = NULL;

	if (*head == NULL)
		*head = new;

	while (number > (finder->next)->n && finder->next != NULL)
	{
		finder = finder->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (finder->next->next == NULL)
		new->next = NULL;
	else
		new->next = finder->next;
	finder->next = new;
	return (new);
}

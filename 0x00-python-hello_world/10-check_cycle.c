#include "lists.h"
#include <stdio.h>
/**
 *check_cycle - Check if there is a cycle in a list
 *@list: Pointer to the list to check
 *Return: 0 if there is a cycle, 1 if not
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *finder = head;

	finder = finder->next;
	while (finder != head && finder != NULL)
	{
		finder = finder->next;
	}
	if (finder == head)
		return (1);
	else
		return (0);
}

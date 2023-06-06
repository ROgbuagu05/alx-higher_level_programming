#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *curr = *head;

	if (new_node == NULL)
	 {
		 return (NULL);
	 }
	 new_node->n = number;
	 new_node->next = NULL;
	 if (*head == NULL)
	 {
		 *head = new_node;
		 return (new_node);
	 }
	 if (number < (*head)->n)
	 {
		 new_node->next = *head;
		 *head = new_node;
		 return (new_node);
	 }
	 while (curr->next != NULL && curr->next->n < number)
	 {
		 curr = curr->next;
	 }
	 new_node->next = curr->next;
	 curr->next = new_node;
	 return (new_node);
}

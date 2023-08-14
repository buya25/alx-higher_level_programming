#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);
int list_equiv(listint_t *list1, listint_t *list2);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int is_palindrome(listint_t **head)
{
	listint_t *skip_ptr1, *skip_ptr2, *prev_skip_ptr1, *first_half, *second_half, *middle_ptr;

	if (!head || !(*head) || !((*head)->next))
		return 1;

	first_half = skip_ptr1 = skip_ptr2 = prev_skip_ptr1 = *head;
	second_half = middle_ptr = NULL;

	while (skip_ptr1 && skip_ptr2 && skip_ptr2->next)
	{
		prev_skip_ptr1 = skip_ptr1;
		skip_ptr1 = skip_ptr1->next;
		skip_ptr2 = skip_ptr2->next->next;
	}

	if (skip_ptr2 == NULL)
		second_half = skip_ptr1;
	else
	{
		middle_ptr = skip_ptr1;
		second_half = skip_ptr1->next;
	}

	prev_skip_ptr1->next = NULL;
	reverse_linked_list(&second_half);

	if (check_list_equivalence(first_half, second_half))
		return 1;
	else
		return 0;
}

/**
 * list_equiv - checks if two linked lists contain identical data and are
 * the same length as each other
 * @list1: list one to compare to list two
 * @list2: list two to compare to list one
 *
 * Return: 1 (equivalent) 0 (not equal)
 */
int list_equiv(listint_t *list1, listint_t *list2)
{
	while (list1 || list2)
	{
		if (list1->data != list2->data || !list1 || !list2)
			return 0;

		if (list1)
			list1 = list1->next;
		if (list2)
			list2 = list2->next;
	}

	return 1;
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the linked list so it can be modified
 *
 * Return: always void, modifies head itself.
 */
void reverse_list(listint_t **head)
{
	listint_t *next_node = NULL, *prev_node = NULL, *current_node;

	current_node = *head;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}

	*head = prev_node;
}

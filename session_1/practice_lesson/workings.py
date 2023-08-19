#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(item ** 2)
        new_matrix.append(new_row)
    return new_matrix


#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if __name__ == "__main__":
    new_matrix = square_matrix_simple(matrix)
    print("{:d}".format(new_matrix))
    print("{}".format(matrix))


#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    seen = {}
    for key in a_dictionary:
        if key in seen:
            return a_dictionary
        else:
            update_dictionary = a_dictionary.append((key: value))
    return update_dictionary


# include "lists.h"  // Include the necessary header file for dlistint_t and related structures

dlistint_t * add_dnodeint(dlistint_t ** head, const int n) {
/* Allocate memory for the new node */
dlistint_t * new_node = malloc(sizeof(dlistint_t))
if (new_node == NULL) {
return NULL
/* Return NULL if memory allocation fails */
}

/* Initialize the new node */
new_node -> n = n
new_node -> prev = NULL
new_node -> next = *head
/* New node's next points to the current head */

if (*head != NULL) {
(*head) -> prev = new_node
/* Update previous of current head if it exists */
}

* head = new_node
/* Update the head to point to the new node */

return new_node
/* Return the address of the new element */
}


dlistint_t * add_dnodeint_end(dlistint_t ** head, const int n) {
/* Allocate memory for the new node */
dlistint_t * new_node = malloc(sizeof(dlistint_t))
if (new_node == NULL) {
return NULL
/* Return NULL if memory allocation fails */
}

/* Initialize the new node */
new_node -> n = n
new_node -> next = NULL
/* New node's next points to NULL */

if (*head == NULL) {
new_node -> prev = NULL
/* If list is empty, previous is NULL */
* head = new_node
/* Update head to point to the new node */
return new_node
/* Return the address of the new element */
}

dlistint_t * current = *head
while (current -> next != NULL) {
current = current -> next
/* Traverse to the last node */
}

current -> next = new_node
/* Attach the new node at the end */
new_node -> prev = current
/* Set previous of the new node */

return new_node
/* Return the address of the new element */
}


# include "lists.h"

void free_dlistint(dlistint_t * head) {
dlistint_t * current = head
while (current != NULL) {
dlistint_t * temp = current
/* Store the current node in a temporary variable */
current = current -> next
/* Move to the next node */
free(temp)
/* Free the memory of the current node */
}
}


# include "lists.h"

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n) {
if (h == NULL) {
return NULL
/* Return NULL if the pointer to the head is NULL */
}

dlistint_t *new_node = malloc(sizeof(dlistint_t))
if (new_node == NULL) {
return NULL
/* Return NULL if memory allocation fails */
}

new_node->n = n
/* Initialize the new node */
new_node->prev = NULL
new_node->next = NULL

if (idx == 0) {
new_node->next = *h
if (*h != NULL) {
(*h)->prev = new_node
}
*h = new_node
return new_node
}

dlistint_t *current = *h
unsigned int count = 0

while (current != NULL & & count < idx - 1) {
current = current->next
count++
}

if (current == NULL) {
free(new_node)
/* Free the new ndoe if index is out of range */
return NULL
}

new_node->next = current->next
new_node->prev = current

if (current->next != NULL) {
current->next->prev = new_node
}

current->next = new_node

return new_node
}
